#!/usr/bin/env python3
"""
Round 3, the writing round: two writers fill every flavour pool from the
same brief, cold, without seeing each other's lines.

    python3 review/rounds/make_round3.py <writer-1.json> <writer-2.json>

Each input is {"lines": [{"lang", "path": "flavour_<level>.<mood>", "text"}]}.
The writers get a blind set label per language; which writer is which
goes into 2026-10-writing.key.json. Don't open the key, or the inputs,
until the votes are in.

Lines that repeat an already rated line, or each other, are dropped:
a rated line would only come back with its old vote.
"""

import hashlib
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-10-writing"
WRITERS = ["Fable 5.1", "Opus 5.5"]
MOODS = {"nice", "mild", "cold", "hot", "wet", "snow", "fickle", "evening", "night"}
PATH_RE = re.compile(r"^flavour_(10|11)\.([a-z]+)$")
MAX_CHARS = 65


def line_id(lang, text):
    return lang + "-" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2
    rated = set()
    for path in (REPO / "review" / "decisions").glob("*.json"):
        rated |= set(json.loads(path.read_text(encoding="utf-8")))

    rng = random.Random(ROUND)
    labels = {"en": ["E1", "E2"], "de": ["D1", "D2"]}
    for lang in labels:
        rng.shuffle(labels[lang])

    lines, key, seen, report = [], {}, set(), []
    for n, (writer, src) in enumerate(zip(WRITERS, sys.argv[1:])):
        data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
        kept = dropped = 0
        for c in data["lines"]:
            lang, path, text = c["lang"], c["path"], c["text"].strip()
            m = PATH_RE.match(path)
            if lang not in labels or not m or m.group(2) not in MOODS:
                report.append(f"{writer}: bad entry {c!r}")
                dropped += 1
                continue
            i = line_id(lang, text)
            if i in rated or i in seen:
                dropped += 1
                continue
            seen.add(i)
            if len(text) > MAX_CHARS:
                report.append(f"{writer}: {len(text)} chars: {text}")
            label = labels[lang][n]
            key[label] = {"lang": lang, "writer": writer}
            lines.append({"lang": lang, "path": path, "text": text, "batch": label})
            kept += 1
        report.append(f"{writer}: {kept} lines, {dropped} dropped")

    rng.shuffle(lines)
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "lines": lines}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (HERE / f"{ROUND}.key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # Counts only: printing names next to labels would unblind the round.
    print("\n".join(r for r in report if "lines," in r or "bad entry" in r or "chars" in r))
    print(f"{ROUND}: {len(lines)} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
