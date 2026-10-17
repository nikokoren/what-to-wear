#!/usr/bin/env python3
"""
Round 21, fresh topics (October 2026).

    python3 review/rounds/make_round21.py

The topics the owner picked from Claude's list (docs/TODO.md, "Next review
batch"), written by fresh writers from a data-built brief
(2026-10-topics/brief_<lang>.md), four candidates per line wanted
(<lang>.raw.json), cut by a critic (<lang>.json). A line goes where its
topic fits: a unit (unit_10/11.<key>), a line for the current weather
(now_10/11.<mood>) or a special day (flavour_10/11.day_eisheilige).

Plus the US English rewrites that need new words, not just spelling
(build_pools.py's WORDS does colour, grey and the rest): a kept rewrite
replaces the old line ("replaces").
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round15 as r15  # noqa: E402
import make_round18 as r18  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-topics"
REWRITES = {"en": [
    ("unit_10.p_snow_coming", "Snow starts {WHENP}. || Five centimetres and everyone forgets how to drive.",
     "Snow starts {WHENP}. || Two inches and everyone forgets how to drive."),
    ("unit_11.p_wet_again_snow",
     "It snows for now, takes a break, and starts again {WHENP}. || The break is mainly so the gritters can feel useful.",
     "It snows for now, takes a break, and starts again {WHENP}. || The break is mainly so the salt trucks can feel useful."),
]}


def row_for(lang, item, doc, base):
    section, key = item["path"].split(".")
    if section.startswith("unit_"):
        return r18.unit_row(lang, item, doc, base)
    if key.startswith(("day_", "theme_")):
        return r15.special_row(lang, item, doc, base)
    return r13.flavour_row(lang, item, doc, base)


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        for path, old, new in REWRITES.get(lang, []):
            row = row_for(lang, {"path": path, "text": new}, doc, base)
            row["replaces"] = old
            row["batch"] = "US English"
            row["hint"] = "US English rewrite of: " + old.split(" || ")[-1]
            lines.append(row)
        src = HERE / ROUND / f"{lang}.json"
        if not src.exists():
            continue
        seen = set()
        for item in json.loads(src.read_text(encoding="utf-8"))["lines"]:
            item["text"] = item["text"].strip()
            if item["text"] in seen:
                continue
            seen.add(item["text"])
            row = row_for(lang, item, doc, base)
            if item.get("topic"):
                row["batch"] = "Topic: " + item["topic"]
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "tp", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:30} {n}")


if __name__ == "__main__":
    main()
