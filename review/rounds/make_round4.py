#!/usr/bin/env python3
"""
Round 4, the top-up: one writer per language fills every flavour pool,
including the three moods that replaced "mild" (warming, cooling, cool).

    python3 review/rounds/make_round4.py <english.json> <german.json>

Drops lines that repeat an already rated line. No blind comparison in
this round: the set label is just the language (E4, D4).
"""

import hashlib
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-10-topup"
MOODS = {"nice", "cool", "warming", "cooling", "cold", "hot", "wet", "snow", "fickle", "evening", "night"}
PATH_RE = re.compile(r"^flavour_(10|11)\.([a-z]+)$")
LABEL = {"en": "E4", "de": "D4"}


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2
    rated = set()
    for path in (REPO / "review" / "decisions").glob("*.json"):
        rated |= set(json.loads(path.read_text(encoding="utf-8")))
    lines, seen = [], set()
    for src in sys.argv[1:]:
        kept = dropped = 0
        for c in json.loads(pathlib.Path(src).read_text(encoding="utf-8"))["lines"]:
            lang, text = c["lang"], c["text"].strip()
            m = PATH_RE.match(c["path"])
            i = lang + "-" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]
            if lang not in LABEL or not m or m.group(2) not in MOODS or i in rated or i in seen:
                dropped += 1
                continue
            seen.add(i)
            if len(text) > 65:
                print(f"over 65 chars: {text}")
            lines.append({"lang": lang, "path": c["path"], "text": text, "batch": LABEL[lang]})
            kept += 1
        print(f"{src}: {kept} lines, {dropped} dropped")
    random.Random(ROUND).shuffle(lines)
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "lines": lines}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{ROUND}: {len(lines)} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
