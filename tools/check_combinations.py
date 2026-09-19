#!/usr/bin/env python3
"""
Checks every temperature + precipitation sentence PAIR that can render.

Most of the time the tip is one sentence. But when the day has both a
temperature hinge and rain coming, the markup joins a temp line to a precip
"_j" fragment with a single space:

    today_tip = temp_clause + " " + precip_clause

Each half is written and reviewed on its own, so the pair is the one thing
nobody looks at. This enumerates all of them and flags the mechanical
failures: a combined tip too long for the screen, the same word landing
twice, two imperatives stacked, or both halves opening identically.

    python3 tools/check_combinations.py           # all languages
    python3 tools/check_combinations.py de --show 20

It cannot judge whether a pair reads naturally. That needs a human, or at
least a fresh reader - see docs/TRANSLATING.md.
"""

import itertools
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LEVELS = ["0", "10", "11"]

# 'perfect' is excluded: when the temperature does nothing the markup uses
# the standalone precip form as the whole tip, never the joined one.
TEMP_KEYS = [
    "arc_colder", "arc_level", "arc_warmer",
    "w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_sweatshirt", "w_water",
    "c_scarf", "c_coat", "c_jacket", "c_hoodie", "c_sweatshirt", "c_relief",
]
PRECIP_BASE = ["wetter_maybe", "wetter", "wetter_long", "drier", "stays_wet", "snow_coming"]

# Roughly what fits at title--large on the small device before the layout
# starts eating the sprite. Deliberately generous; the point is to catch the
# pairs that are obviously too long, not to police every word.
MAX_WORDS = 30

# Must match TIP_BUDGET in src/shared.liquid. The markup picks whichever of a
# scenario's interchangeable precipitation lines fits the room the temperature
# line left, so a pair only overflows when NO alternative fits.
TIP_BUDGET = 165

STOPWORDS = {
    "en": {
        "the", "a", "an", "and", "or", "but", "so", "it", "its", "is", "are",
        "was", "be", "been", "to", "of", "in", "on", "at", "by", "for", "with",
        "you", "your", "youll", "youre", "that", "this", "there", "then",
        "not", "no", "all", "day", "today", "will", "wont", "have", "has",
        "get", "gets", "from", "out", "up", "off", "back", "more", "one",
        "what", "when", "them", "they", "as", "if", "do", "does", "doesnt",
        "can", "cant", "just", "still", "own", "about", "like", "before",
    },
    "de": {
        "der", "die", "das", "den", "dem", "des", "ein", "eine", "einen",
        "einem", "eines", "und", "oder", "aber", "doch", "es", "ist", "sind",
        "war", "sein", "zu", "von", "in", "an", "auf", "bei", "für", "mit",
        "du", "dein", "deine", "deinen", "deiner", "dir", "dich", "das",
        "nicht", "kein", "keine", "alle", "tag", "heute", "wird", "hat",
        "hast", "aus", "ab", "auch", "noch", "schon", "halt", "eben", "mal",
        "wohl", "ja", "dann", "denn", "sich", "man", "was", "wenn", "wie",
        "so", "nur", "mehr", "sie", "er", "im", "am", "zum", "zur", "dabei",
    },
}

# The clumsiest join in practice: both halves tacking on an "as well".
ALSO = {
    "en": re.compile(r"\b(too|also|as well|plus|either)\b", re.I),
    "de": re.compile(r"\b(auch|außerdem|ebenfalls|dazu|zudem)\b", re.I),
}

IMPERATIVE = {
    "en": re.compile(r"\b(take|bring|pack|put|grab|carry|keep|wear|slip|add|drink)\b", re.I),
    "de": re.compile(r"\b(nimm|pack|bring|schnapp|trag|behalt|zieh|trink|hol|leg)\b", re.I),
}

WORD = re.compile(r"[A-Za-zÄÖÜäöüß']+")


def content_words(text, code):
    return {
        w.lower().replace("'", "")
        for w in WORD.findall(text)
        if len(w) > 3 and w.lower().replace("'", "") not in STOPWORDS[code]
    }


def main():
    argv = sys.argv[1:]
    show = 10
    if "--show" in argv:
        i = argv.index("--show")
        show = int(argv[i + 1])
        del argv[i:i + 2]
    args = [a for a in argv if not a.startswith("--")]
    codes = args or [p.stem for p in sorted((REPO / "lang").glob("*.json"))]

    grand_total = 0
    all_findings = []

    for code in codes:
        doc = json.loads((REPO / "lang" / f"{code}.json").read_text(encoding="utf-8"))
        findings = {"long": [], "echo": [], "double_also": [],
                    "double_imperative": [], "same_open": []}
        total = 0

        for level in LEVELS:
            temp = doc.get(f"temp_{level}") or {}
            precip = doc.get(f"precip_{level}") or {}
            for tkey, pbase in itertools.product(TEMP_KEYS, PRECIP_BASE):
                tlines = temp.get(tkey) or []
                plines = precip.get(pbase + "_j") or []
                for tline, pline in itertools.product(tlines, plines):
                    total += 1
                    combined = f"{tline} {pline}"
                    plain = re.sub(r"\{[A-Z0-9_]+\}", "", combined)
                    words = len(plain.split())
                    where = f"{code}/{level} {tkey} + {pbase}_j"

                    if words > MAX_WORDS:
                        findings["long"].append((words, where, combined))

                    shared = content_words(tline, code) & content_words(pline, code)
                    if shared:
                        findings["echo"].append((sorted(shared), where, combined))

                    if ALSO[code].search(tline) and ALSO[code].search(pline):
                        findings["double_also"].append((where, combined))

                    if IMPERATIVE[code].search(tline) and IMPERATIVE[code].search(pline):
                        findings["double_imperative"].append((where, combined))

                    t0 = tline.split()[0].lower().strip(".,")
                    p0 = pline.split()[0].lower().strip(".,")
                    if t0 == p0 and len(t0) > 2:
                        findings["same_open"].append((where, combined))

        # Which scenario pairs can never fit, whatever the markup picks?
        unfittable = []
        for level in LEVELS:
            temp = doc.get(f"temp_{level}") or {}
            precip = doc.get(f"precip_{level}") or {}
            for tkey, pbase in itertools.product(TEMP_KEYS, PRECIP_BASE):
                tlines = temp.get(tkey) or []
                plines = precip.get(pbase + "_j") or []
                if not tlines or not plines:
                    continue
                longest_temp = max(len(t) for t in tlines)
                shortest_precip = min(len(p) for p in plines)
                over = longest_temp + 1 + shortest_precip - TIP_BUDGET
                if over > 0:
                    unfittable.append((over, f"{level} {tkey} + {pbase}_j",
                                       longest_temp, shortest_precip))
        unfittable.sort(reverse=True)
        print(f"  {len(unfittable):6,}          scenario pairs where no alternative fits "
              f"{TIP_BUDGET} chars")
        for over, where, lt, sp in unfittable[:show]:
            print(f"          over by {over:3}  {where}  "
                  f"(longest temp {lt}ch + shortest precip {sp}ch)")
        if len(unfittable) > show:
            print(f"          ... and {len(unfittable) - show:,} more")

        grand_total += total
        print(f"\n{'=' * 70}\n{code.upper()}: {total:,} renderable pairs\n{'=' * 70}")
        labels = {
            "long": f"longer than {MAX_WORDS} words",
            "echo": "a content word appears in both halves",
            "double_also": "both halves tack on an 'as well'",
            "double_imperative": "an instruction in both halves",
            "same_open": "both halves open with the same word",
        }
        for kind, label in labels.items():
            hits = findings[kind]
            pct = 100 * len(hits) / total if total else 0
            print(f"  {len(hits):6,} ({pct:4.1f}%)  {label}")
            for item in hits[:show]:
                if kind == "long":
                    w, where, text = item
                    print(f"          [{w}w] {where}")
                    print(f"                {text}")
                elif kind == "echo":
                    shared, where, text = item
                    print(f"          {shared} {where}")
                    print(f"                {text}")
                else:
                    where, text = item
                    print(f"          {where}")
                    print(f"                {text}")
            if len(hits) > show:
                print(f"          ... and {len(hits) - show:,} more")
        all_findings.append((code, total, findings))

    print(f"\n{'=' * 70}")
    print(f"{grand_total:,} pairs checked across {len(codes)} language(s)")
    worst = sum(len(f["long"]) for _, _, f in all_findings)
    return 1 if worst else 0


if __name__ == "__main__":
    raise SystemExit(main())
