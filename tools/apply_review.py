#!/usr/bin/env python3
"""
Applies a reviewer's fix list to a language file.

    python3 tools/apply_review.py <fixes.json> [--dry-run]

The fix file is what an independent review pass produces:

    {"rating": {...},
     "summary": "...",
     "replacements": [
        {"path": "temp_11.w_coat[2]", "old": "<exact current line>",
         "new": "<replacement>", "why": "..."},
        {"path": "precip_11.wetter_j[6]", "old": "",
         "new": "<new line>", "why": "..."}
     ]}

An entry with a non-empty "old" must match the line currently at that index
exactly, or nothing is written. That is the point: a reviewer works from a
snapshot, and a stale fix silently overwriting a line someone else changed is
worse than a failed run. An empty "old" appends.

The language code is taken from the fix filename (en_fixes.json -> en).
"""

import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
PATH_RE = re.compile(r"^([a-z]+_\d+)\.([a-z_]+)\[(\d+)\]$")


def main():
    argv = sys.argv[1:]
    dry = "--dry-run" in argv
    argv = [a for a in argv if not a.startswith("--")]
    if len(argv) != 1:
        print(__doc__.strip())
        return 2

    fixes_path = pathlib.Path(argv[0])
    fixes = json.loads(fixes_path.read_text(encoding="utf-8"))
    code = fixes_path.stem.split("_")[0]
    target = REPO / "lang" / f"{code}.json"
    doc = json.loads(target.read_text(encoding="utf-8"))

    rating = fixes.get("rating") or {}
    if rating:
        print("reviewer ratings: " + "  ".join(f"{k}={v}" for k, v in rating.items()))

    applied, added, problems = 0, 0, []

    for entry in fixes.get("replacements", []):
        path, old, new = entry["path"], entry.get("old", ""), entry["new"]
        m = PATH_RE.match(path)
        if not m:
            problems.append(f"{path}: unparseable path")
            continue
        section, key, index = m.group(1), m.group(2), int(m.group(3))

        lines = (doc.get(section) or {}).get(key)
        if lines is None:
            problems.append(f"{path}: no such key")
            continue

        if not old:
            if new in lines:
                problems.append(f"{path}: addition duplicates an existing line")
                continue
            lines.append(new)
            added += 1
            continue

        if index >= len(lines):
            problems.append(f"{path}: index out of range (key has {len(lines)})")
            continue
        if lines[index] != old:
            problems.append(
                f"{path}: stale - the file has a different line here\n"
                f"       expected: {old!r}\n"
                f"       found:    {lines[index]!r}"
            )
            continue
        lines[index] = new
        applied += 1

    print(f"{applied} replaced, {added} added" + (", DRY RUN" if dry else ""))

    if problems:
        print(f"\n{len(problems)} entr(ies) not applied:")
        for p in problems:
            print(f"  - {p}")

    if dry:
        return 1 if problems else 0

    target.write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    total = sum(
        len(v) for s, sec in doc.items()
        if s.startswith(("temp_", "precip_")) for v in sec.values()
    )
    print(f"wrote lang/{code}.json ({total} lines)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
