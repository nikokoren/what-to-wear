#!/usr/bin/env python3
"""
Measures a language file against the rules in docs/VOICE.md.

The previous corpus drifted into template-filling without anyone noticing,
because "does this read well" is hard to eyeball across a thousand lines.
These are the things that went wrong last time, turned into numbers.

    python3 tools/style_report.py            # every language
    python3 tools/style_report.py de         # one language
    python3 tools/style_report.py de --fail  # non-zero exit on a red flag

Nothing here is enforced by CI. Voice is a judgement call and a writer may
have a good reason to break any single rule. The report exists so the
decision is made on purpose rather than by accident.
"""

import collections
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LEVELS = ["0", "10", "11"]
C_KEYS = ["c_scarf", "c_coat", "c_jacket", "c_hoodie", "c_sweatshirt"]

BANNED_OPENERS = {
    "en": ["It gets", "It turns", "You will"],
    "de": ["Es wird {WHEN}", "Im Tagesverlauf"],
}
BANNED_PHRASES = {
    "en": [],
    "de": ["Im Tagesverlauf", "ist nicht in Sicht", "Eine Wetteränderung"],
}

# German modal particles: the native device for dry understatement, and
# completely absent from the corpus this replaces.
PARTICLES = re.compile(
    r"\b(ja|halt|eben|schon|wohl|doch|mal|eh|einfach)\b", re.IGNORECASE
)
CONTRACTION = re.compile(r"\b\w+'(s|t|re|ll|ve|d)\b")
EXPANDED = re.compile(r"\b(will not|does not|do not|is not|are not|cannot|you will)\b")
FUTURE_DE = re.compile(r"\b(wirst|wird|werden)\b")
READER_EN = re.compile(r"\b(you|your|you're|you'll)\b", re.IGNORECASE)
READER_DE = re.compile(r"\b(du|dein|deine|deinen|deiner|dir|dich|hast|bist)\b", re.IGNORECASE)


def level_lines(doc, level):
    out = []
    for kind in ("temp", "precip"):
        for key, lines in (doc.get(f"{kind}_{level}") or {}).items():
            for ln in lines:
                out.append((f"{kind}_{level}.{key}", ln))
    return out


def strip_tokens(text):
    return re.sub(r"\{[A-Z0-9_]+\}", "", text).strip()


def report(code, doc, flags):
    print(f"\n{'=' * 64}\n{code.upper()}  ({doc.get('meta', {}).get('name', '?')})\n{'=' * 64}")
    reader_re = READER_DE if code == "de" else READER_EN

    print(f"{'lvl':>4} {'lines':>6} {'w/line':>7} {'reader':>8} {'banned':>7} ", end="")
    print(f"{'particles':>10}" if code == "de" else f"{'contract':>10}")

    prev_reader = None
    for level in LEVELS:
        lines = level_lines(doc, level)
        if not lines:
            continue
        texts = [t for _, t in lines]
        wpl = sum(len(strip_tokens(t).split()) for t in texts) / len(texts)
        reader = sum(1 for t in texts if reader_re.search(t)) / len(texts)
        banned = sum(
            1 for t in texts
            for b in BANNED_OPENERS[code] + BANNED_PHRASES[code]
            if t.startswith(b) or b in t
        )
        if code == "de":
            extra = sum(1 for t in texts if PARTICLES.search(t)) / len(texts)
        else:
            extra = sum(1 for t in texts if CONTRACTION.search(t)) / len(texts)

        print(f"{level:>4} {len(texts):6} {wpl:7.1f} {100*reader:7.0f}% {banned:7} {100*extra:9.0f}%")

        if banned:
            flags.append(f"{code}/{level}: {banned} line(s) use a banned opener or phrase")
        if code == "en" and extra < 0.25:
            flags.append(
                f"{code}/{level}: only {100*extra:.0f}% of lines use contractions "
                "- this is what made the old corpus read like a manual"
            )
        if code == "de":
            fut = sum(1 for t in texts if FUTURE_DE.search(t)) / len(texts)
            if fut > 0.20:
                flags.append(
                    f"{code}/{level}: {100*fut:.0f}% of lines use wird/wirst/werden "
                    "- German prefers present tense for the near future (old corpus: 33%)"
                )
            # Only levels 10 and 11 are supposed to be dry. VOICE.md asks
            # level 0 to use particles sparingly, because it is friendly
            # rather than wry, so a low count there is correct.
            if level in ("10", "11") and extra < 0.15:
                flags.append(
                    f"{code}/{level}: only {100*extra:.0f}% of lines use a modal particle "
                    "- these are the native device for dry German (old corpus: ~0%)"
                )
        if code == "en":
            exp = sum(1 for t in texts if EXPANDED.search(t))
            if exp > len(texts) * 0.08:
                flags.append(f"{code}/{level}: {exp} lines use 'will not'/'does not' style")
        prev_reader = reader

    # The architecture: 0 talks to you, 10 talks about the things, 11 comes
    # back to you hard. So reader-address should dip at 10 and peak at 11.
    rates = {}
    for level in LEVELS:
        texts = [t for _, t in level_lines(doc, level)]
        if texts:
            rates[level] = sum(1 for t in texts if reader_re.search(t)) / len(texts)
    if len(rates) == 3:
        print(f"\n  voice architecture: 0={100*rates['0']:.0f}%  "
              f"10={100*rates['10']:.0f}%  11={100*rates['11']:.0f}% reader-addressed")
        if not rates["10"] < rates["11"]:
            flags.append(
                f"{code}: level 10 addresses the reader as much as 11 "
                f"({100*rates['10']:.0f}% vs {100*rates['11']:.0f}%) - 10 should aim at "
                "the objects, 11 at the reader"
            )
        if rates["11"] < 0.5:
            flags.append(
                f"{code}: level 11 only addresses the reader in {100*rates['11']:.0f}% "
                "of lines; it is supposed to be about them"
            )

    # Repetition: the old corpus opened 59 of 485 German lines identically.
    print("\n  most repeated openings:")
    for level in LEVELS:
        texts = [t for _, t in level_lines(doc, level)]
        if not texts:
            continue
        opens = collections.Counter(" ".join(t.split()[:2]) for t in texts)
        worst, n = opens.most_common(1)[0]
        pct = 100 * n / len(texts)
        mark = "  <-- over 2" if n > 2 else ""
        print(f"    level {level:>2}: {n}x {worst!r} ({pct:.0f}% of level){mark}")
        if n > 4:
            flags.append(f"{code}/{level}: {n} lines open with {worst!r}")

    # The five cooling keys were one template with the noun swapped.
    print("\n  cooling keys, first three words (must not rhyme with each other):")
    for level in LEVELS:
        section = doc.get(f"temp_{level}") or {}
        heads = []
        for key in C_KEYS:
            lines = section.get(key) or []
            if lines:
                heads.append(" ".join(lines[0].split()[:3]))
        if not heads:
            continue
        distinct = len(set(heads))
        mark = "" if distinct == len(heads) else f"  <-- only {distinct}/{len(heads)} distinct"
        print(f"    level {level:>2}: {distinct}/{len(heads)} distinct{mark}")
        for key, head in zip(C_KEYS, heads):
            print(f"        {key:15} {head}...")
        if distinct < len(heads):
            flags.append(
                f"{code}/temp_{level}: the c_* keys share a sentence frame "
                f"({distinct} distinct openings across {len(heads)} keys)"
            )

    longest = max(
        ((len(strip_tokens(t).split()), t) for _, t in
         [x for lv in LEVELS for x in level_lines(doc, lv)]),
        default=(0, ""),
    )
    print(f"\n  longest line: {longest[0]} words")
    print(f"    {longest[1]}")
    if longest[0] > 20:
        flags.append(f"{code}: longest line is {longest[0]} words; wraps badly on the OG device")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fail_mode = "--fail" in sys.argv
    codes = args or [p.stem for p in sorted((REPO / "lang").glob("*.json"))]

    flags = []
    for code in codes:
        path = REPO / "lang" / f"{code}.json"
        if not path.exists():
            print(f"no such language file: {path}", file=sys.stderr)
            return 2
        report(code, json.loads(path.read_text(encoding="utf-8")), flags)

    print(f"\n{'=' * 64}")
    if flags:
        print(f"{len(flags)} thing(s) worth a second look:\n")
        for f in flags:
            print(f"  - {f}")
        return 1 if fail_mode else 0
    print("nothing flagged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
