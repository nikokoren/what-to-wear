#!/usr/bin/env python3
"""
Puts the owner's votes on the evening rounds into
prototypes/panels/lang/<lang>.json: starred and kept lines (with the
owner's edits) replace the stand-ins. Round 28 (2026-11-evening):
evening.facts.<situation>, and its evening lines become the fallback
evening.jokes_<level>.any. Round 29 (2026-11-evening2, the pilot):
evening.jokes_<level>.<rain|colder|steady>. A pool nobody kept keeps
what it had. A note asking to show a line only while it's dry right now
puts "{DRY}" in front of it (evening.liquid).

    python3 tools/review_sync.py <decisions.json>   # first, as for every round
    python3 review/rounds/apply_evening.py
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUNDS = ("2026-11-evening", "2026-11-evening2")


def main():
    for lang in ("en", "de"):
        dec = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        pools = {}
        for d in dec.values():
            if d.get("round") not in ROUNDS or d.get("verdict") not in ("star", "keep"):
                continue
            path = (d.get("path") or "").split("[")[0]
            text = (d.get("edit") or d["text"]).strip()
            if "dry right now" in (d.get("note") or "").lower():
                text = "{DRY}" + text
            level = path.split(".")[0].split("_")[-1]
            if path.startswith("fact_0.evening_"):
                where = ("facts", path.split("evening_", 1)[1])
            elif path.startswith("flavour_") and path.endswith(".evening"):
                where = ("jokes_" + level, "any")
            elif path.startswith("flavour_") and ".evening_" in path:
                where = ("jokes_" + level, path.split(".evening_", 1)[1])
            else:
                continue
            pools.setdefault(where, []).append(text)
        p = REPO / "prototypes" / "panels" / "lang" / f"{lang}.json"
        doc = json.loads(p.read_text(encoding="utf-8"))
        ev = doc["evening"]
        for (group, key), texts in sorted(pools.items()):
            texts = list(dict.fromkeys(texts))
            ev.setdefault(group, {})[key] = texts
            print(f"{lang} evening.{group}.{key}: {len(texts)}")
        if pools:
            ev.pop("_note", None)
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
