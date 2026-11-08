#!/usr/bin/env python3
"""
Puts the owner's votes on round 28 (the evening) into
prototypes/panels/lang/<lang>.json: starred and kept lines (with the
owner's edits) replace the stand-ins in evening.facts.<situation> and
evening.jokes_<level>. A pool nobody kept keeps its stand-ins.

    python3 tools/review_sync.py <decisions.json>   # first, as for every round
    python3 review/rounds/apply_evening.py
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-11-evening"


def main():
    for lang in ("en", "de"):
        dec = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        pools = {}
        for d in dec.values():
            if d.get("round") != ROUND or d.get("verdict") not in ("star", "keep"):
                continue
            path = (d.get("path") or "").split("[")[0]
            text = (d.get("edit") or d["text"]).strip()
            if path.startswith("fact_0.evening_"):
                where = ("facts", path.split("evening_", 1)[1])
            elif path.startswith("flavour_") and path.endswith(".evening"):
                where = (None, "jokes_" + path.split(".")[0].split("_")[1])
            else:
                continue
            pools.setdefault(where, []).append(text)
        p = REPO / "prototypes" / "panels" / "lang" / f"{lang}.json"
        doc = json.loads(p.read_text(encoding="utf-8"))
        ev = doc["evening"]
        for (group, key), texts in sorted(pools.items(), key=lambda kv: (kv[0][0] or "", kv[0][1])):
            texts = list(dict.fromkeys(texts))
            if group:
                ev[group][key] = texts
            else:
                ev[key] = texts
            print(f"{lang} {group or 'evening'}.{key}: {len(texts)}")
        if pools:
            ev.pop("_note", None)
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
