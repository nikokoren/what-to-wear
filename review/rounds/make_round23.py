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


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = r22.live_rows("en")
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
    out = {"round": ROUND, "idPrefix": "f2", "lines": lines + new}
    (HERE / f"{ROUND}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"en: {len(lines)} lines to read, {sum(1 for r in lines if r.get('starred'))} starred before")
    print(f"de: {len(new)} new lines")


if __name__ == "__main__":
    main()
