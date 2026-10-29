#!/usr/bin/env python3
"""
Round 23: the English read-through, and the German rewrites (October 2026).

    python3 review/rounds/make_round23.py

English: every live English text, as round 22 did for German (built from
today's texts: US spelling, the scarf, the storms), starred lines marked.
build_pools.py applies it like round 22: a veto takes a line out, an edit
replaces it.

German: new lines for the slots the German read-through emptied or thinned
(the 54 lines voted out outside the forecast wordings, Eisheilige at On),
written by a fresh writer from a data-built brief (2026-10-final2/brief_de.md)
and cut by a critic (de.json). build_pools.py adds the kept ones.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round21 as r21  # noqa: E402
import make_round22 as r22  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-final2"


def add_level_notes(lines):
    """The level check (owner, before the German reread): each flag a note under its line."""
    flags = HERE / ROUND / "level_flags.json"
    if not flags.exists():
        return
    label = {"too_personal_for_10": "Level check: a personal jab, belongs at 11?",
             "too_mild_for_11": "Level check: not about you, fits On better?",
             "not_sarcastic": "Level check: not sarcastic",
             "too_harsh": "Level check: goes after looks or worth",
             "both_levels": "Level check: the same joke at On and 11"}
    by = {}
    for f in json.loads(flags.read_text(encoding="utf-8")):
        by.setdefault((f["lang"], f["where"].replace("unit_", "units_")), []).append(f)
    for r in lines:
        where = r["where"][0] if r.get("where") else r["path"].replace("unit_", "units_")
        for f in by.get((r["lang"], where), []):
            joke = f["text"].split(" || ")[-1].lstrip("| ").strip()
            if joke and joke in r["text"]:
                r["hint"] = ((r.get("hint") or "") + " · " + label[f["flag"]] + " (" + f["why"] + ")").lstrip(" ·")
                r["batch"] = "Level check"


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = r22.live_rows("en") + r22.live_rows("de")

    doc = json.loads((r8.PROTO / "de.json").read_text(encoding="utf-8"))
    base = json.loads((REPO / "lang" / "de.json").read_text(encoding="utf-8"))
    src = HERE / ROUND / "de.json"
    new = []
    if src.exists():
        for item in json.loads(src.read_text(encoding="utf-8"))["lines"]:
            item["text"] = item["text"].strip()
            row = r21.row_for("de", item, doc, base)
            row["new"] = True
            row["batch"] = "New: " + item["path"].split(".", 1)[1]
            new.append(row)
    add_level_notes(lines + new)
    out = {"round": ROUND, "idPrefix": "f2", "lines": lines + new}
    (HERE / f"{ROUND}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        mine = [r for r in lines if r["lang"] == l]
        print(f"{l}: {len(mine)} lines to read, {sum(1 for r in mine if r.get('starred'))} starred before, "
              f"{sum(1 for r in mine if r.get('batch') == 'Level check')} with a level-check note")
    print(f"de: {len(new)} new lines, {sum(1 for r in new if r.get('batch') == 'Level check')} with a level-check note")


if __name__ == "__main__":
    main()
