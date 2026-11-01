#!/usr/bin/env python3
"""
Round 27 (November 2026): the groups still under four, outside the box, follow-ups left out.

    python3 review/rounds/make_round27.py

The owner: every thin slot to at least four lines, 5-6 versions of each
plus one out-of-the-box line, learning from what worked elsewhere. The
slots (fewer than four live lines, `2026-11-thin2/cells.json`) went to
twelve fresh writers with data-built briefs (`2026-11-thin2/brief_*.md`),
then a critic per language kept the best 5-6 and one out-of-the-box line
per slot (`2026-11-thin2/<lang>.json`). build_pools.py adds the kept ones.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round22 as r22  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-11-thin2"
FAMILY = {"facts": "Forecast sentence", "units": "Unit", "flavour": "Joke", "flavour_vf": "Drawings",
          "alone": "Alone", "now": "Now"}


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    cells = {(c[0], c[1]): c[2] for c in json.loads((HERE / ROUND / "cells.json").read_text(encoding="utf-8"))}
    lines = []
    for lang in ("en", "de"):
        src = HERE / ROUND / f"{lang}.json"
        # The proofreader's pass, when there is one (docs/BRIEF.md: writer,
        # critic, proofreader, owner): its kept lines, fixes shown.
        if (HERE / ROUND / f"{lang}.proofread.json").exists():
            src = HERE / ROUND / f"{lang}.proofread.json"
        if not src.exists():
            continue
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        seen = set()
        for item in json.loads(src.read_text(encoding="utf-8"))["lines"]:
            text = item["text"].strip()
            where = item["path"].replace("unit_", "units_")
            if (where, text) in seen:
                continue
            seen.add((where, text))
            section, key = where.split(".", 1)
            if item.get("months"):
                # the markup compares two-digit months ("09")
                item["months"] = ",".join(f"{int(m):02d}" for m in str(item["months"]).split(","))
            if section == "facts":
                row = r22.fact_row(lang, key, text, doc, base)
            else:
                live = ("{M:" + item["months"] + "}" if item.get("months") else "") + text
                row = r22.row_for(lang, section, key, live, doc, base)
            row["new"] = True
            fam = section.rsplit("_", 1)[0] if section != "facts" else "facts"
            row["batch"] = f"{FAMILY.get(fam, fam)}: {key}"
            hints = [row["hint"]] if row.get("hint") else []
            hints.append(f"Fill-up: {cells.get((lang, where), 0)} live here now")
            if item.get("wild"):
                hints.append("Out of the box")
            if item.get("was"):
                hints.append("Proofread from: " + item["was"].split(" || ")[-1])
            row["hint"] = " · ".join(hints)
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "t2", "lines": lines}
    (HERE / f"{ROUND}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        mine = [r for r in lines if r["lang"] == l]
        print(f"{l}: {len(mine)} lines, {sum(1 for r in mine if 'Out of the box' in r['hint'])} out of the box, "
              f"{len({r['path'] for r in mine})} slots")


if __name__ == "__main__":
    main()
