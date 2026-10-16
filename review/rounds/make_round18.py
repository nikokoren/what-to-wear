#!/usr/bin/env python3
"""
Round 18, units for the layer days (October 2026).

    python3 review/rounds/make_round18.py

Round 17's units, for the days a layer comes off or goes on (w_*, c_*,
arc_*, shorts_early). These can sit under two or three drawings (What to
Wear Next and the forecast both on), so the page shows them with their
drawings, and the joke has to work with or without them. Also: round 17's
gaps (English late night at On) and its "Write new" spots.

Raw output in 2026-10-layers/<lang>.json, round 17's format plus
"answers". build_pools.py applies it like round 17 (units_10 / units_11).
"""

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round14 as r14  # noqa: E402
import make_round17 as r17  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-layers"
# The drawings above a layer day's unit, now and later, as What to Wear
# Next shows them.
PANELS = {
    "w_scarf": ("bundled_dry", "coat_dry"), "w_coat": ("coat_dry", "jacket_dry"),
    "w_jacket": ("jacket_dry", "sweater_dry"), "w_hoodie": ("sweater_dry", "tee_pants_dry"),
    "w_water": ("tee_pants_dry", "heat_dry"), "c_scarf": ("coat_dry", "bundled_dry"),
    "c_coat": ("jacket_dry", "coat_dry"), "c_jacket": ("sweater_dry", "jacket_dry"),
    "c_hoodie": ("tee_pants_dry", "sweater_dry"), "c_relief": ("heat_dry", "tee_shorts_dry"),
    "arc_warmer": ("jacket_dry", "sweater_dry"), "arc_level": ("jacket_dry", "sweater_dry", "jacket_dry"),
    "arc_colder": ("jacket_dry", "sweater_dry", "coat_dry"), "shorts_early": ("tee_pants_dry", "tee_shorts_dry"),
}
LABELS = {"en": ("Now", "from noon", "from 6 pm"), "de": ("Jetzt", "ab Mittag", "ab 18 Uhr")}


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        facts = doc["facts"]
        existing = {t for lv in ("10", "11") for v in doc.get(f"units_{lv}", {}).values() for t in v}
        seen = set()
        for item in json.loads((HERE / ROUND / f"{lang}.json").read_text(encoding="utf-8"))["lines"]:
            text = item["text"].strip()
            if text in seen or text in existing:
                print(f"  {lang} skipped, already there: {text}")
                continue
            seen.add(text)
            section, key = item["path"].split(".")
            level = section.rsplit("_", 1)[1]
            sprite, _, meaning = r17.EXTRA.get(key) or r14.FACT_CTX[key]
            fact, _, joke = text.partition(" || ")
            allowed = set(re.findall(r"\{[A-Z0-9]+\}", " ".join(facts.get(key, [])))) | {"{GP}", "{G}"}
            extra = set(re.findall(r"\{[A-Z0-9]+\}", text)) - allowed
            if extra:
                raise SystemExit(f"{lang} {key}: placeholder {sorted(extra)} not allowed here: {text}")
            row = {"lang": lang, "path": item["path"], "text": text, "role": "unit", "new": True,
                   "sprite": sprite, "fills": r8.fills(lang, text, base, facts),
                   "fillsAlt": r8.fills(lang, text, base, facts, alt=True),
                   "batch": f"Unit: {key}",
                   "meaning": f"New at {r13.LEVEL[level]}: the forecast sentence and its joke as one. {meaning} "
                              "Shows under the written forecast, with or without What to Wear Next's drawings above."}
            hints = [] if joke else ["One sentence, no second line"]
            if key in PANELS:
                row["panels"] = [{"sprite": s, "label": LABELS[lang][i]} for i, s in enumerate(PANELS[key])]
                hints.append("Also shows without the drawings")
                missing = [p for p in re.findall(r"\{[A-Z0-9]+\}", facts[key][0]) if p not in fact]
                if missing:
                    hints.append("Leaves out " + ", ".join(missing))
            if item.get("months"):
                row["months"] = item["months"]
                hints.append("Seasonal: only " + r13.months_named(item["months"]))
            if item.get("answers"):
                row["answers"] = item["answers"]
                hints.append("Answers a “Write new”")
            if hints:
                row["hint"] = " · ".join(hints)
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "ly", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:24} {n}")
    answered = {a for r in lines for a in r.get("answers", [])}
    for lang in ("en", "de"):
        waiting = (REPO / "review" / "rewrite" / f"{lang}.md").read_text(encoding="utf-8")
        ids = [i for i in re.findall(r"\*\*Answers:\*\* `([^`]+)`", waiting) if i.startswith("un-")]
        left = [i for i in ids if i not in answered]
        print(f"  {lang}: {len(left)} of {len(ids)} unit Write new spots not answered" + (f": {left}" if left else ""))


if __name__ == "__main__":
    main()
