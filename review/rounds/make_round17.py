#!/usr/bin/env python3
"""
Round 17, units (October 2026).

    python3 review/rounds/make_round17.py

The owner, on the beta: the forecast sentence (even "works all day") and
the sarcastic line picked to go with it don't flow. From now on, with
sarcasm on, they are written and voted together as one unit:

    "What you're wearing works all day. || Unlike your phone battery."
    "One sentence that says it and makes the joke."   (no second line)

The markup shows a unit wherever its situation has some (block.liquid,
UNITS): under the written forecast, and with What to Wear Next's single
drawing. Situations without units work as before, so they arrive a few
at a time, the commonest first: the steady days.

Raw output in 2026-10-units/<lang>.json: {"lines": [{"path":
"unit_10.steady", "text": "fact || joke", "months": "11,12"}]}.
build_pools.py applies it (units_10 / units_11).
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round14 as r14  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-units"
EXTRA = {"steady_night": ("jacket_dry", "night", "Nothing changes, from 22:00: the evening wording, late.")}


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        facts = doc["facts"]
        seen = set()
        for item in json.loads((HERE / ROUND / f"{lang}.json").read_text(encoding="utf-8"))["lines"]:
            text = item["text"].strip()
            if text in seen:
                continue
            seen.add(text)
            section, key = item["path"].split(".")
            level = section.rsplit("_", 1)[1]
            sprite, _, meaning = EXTRA.get(key) or r14.FACT_CTX[key]
            fact, _, joke = text.partition(" || ")
            row = {"lang": lang, "path": item["path"], "text": text, "role": "unit", "new": True,
                   "sprite": sprite, "fills": r8.fills(lang, fact, base, facts),
                   "fillsAlt": r8.fills(lang, fact, base, facts, alt=True),
                   "batch": f"Unit: {key}",
                   "meaning": f"New at {r13.LEVEL[level]}: the forecast sentence and its joke as one. {meaning} "
                              "Shows under the written forecast, and with What to Wear Next's single drawing."}
            hints = [] if joke else ["One sentence, no second line"]
            if item.get("months"):
                row["months"] = item["months"]
                hints.append("Seasonal: only " + r13.months_named(item["months"]))
            if hints:
                row["hint"] = " · ".join(hints)
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "un", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:24} {n}")


if __name__ == "__main__":
    main()
