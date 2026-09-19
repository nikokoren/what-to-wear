#!/usr/bin/env python3
"""
Merges per-level drafts into lang/<code>.json.

The 2026 rewrite was produced one (language, level) at a time so each voice
could be written in one sitting rather than assembled from fragments. This
folds those drafts back into the real language files, keeping everything the
drafts do not cover (meta, ui, garments, buckets, relative) exactly as it was.

    python3 tools/assemble_lang.py <draft-dir>

A draft is <draft-dir>/<code>_<level>.json shaped as:
    {"temp": {"<key>": ["line", ...]}, "precip": {"<key>": ["line", ...]}}
"""

import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LEVELS = ["0", "10", "11"]

TEMP_KEYS = [
    "perfect",
    "arc_colder", "arc_level", "arc_warmer",
    "w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_sweatshirt", "w_water",
    "c_scarf", "c_coat", "c_jacket", "c_hoodie", "c_sweatshirt", "c_relief",
]
PRECIP_BASE = ["wetter_maybe", "wetter", "wetter_long", "drier", "stays_wet", "snow_coming"]
PRECIP_KEYS = [k + s for k in PRECIP_BASE for s in ("", "_j")]


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    draft_dir = pathlib.Path(sys.argv[1])

    codes = sorted({p.stem.split("_")[0] for p in draft_dir.glob("*_*.json")})
    if not codes:
        print(f"no drafts found in {draft_dir}", file=sys.stderr)
        return 1

    problems = []
    for code in codes:
        target = REPO / "lang" / f"{code}.json"
        doc = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}

        for level in LEVELS:
            draft_path = draft_dir / f"{code}_{level}.json"
            if not draft_path.exists():
                problems.append(f"{code}: missing draft for level {level}")
                continue
            draft = json.loads(draft_path.read_text(encoding="utf-8"))

            for kind, keys in (("temp", TEMP_KEYS), ("precip", PRECIP_KEYS)):
                section = draft.get(kind) or {}
                missing = [k for k in keys if k not in section]
                extra = [k for k in section if k not in keys]
                if missing:
                    problems.append(f"{code}/{kind}_{level}: missing keys {missing}")
                if extra:
                    problems.append(f"{code}/{kind}_{level}: unexpected keys {extra}")
                # Preserve the canonical key order rather than the draft's.
                doc[f"{kind}_{level}"] = {
                    k: [ln.strip() for ln in section[k]] for k in keys if k in section
                }

        if problems:
            continue

        # Keep the sections the drafts do not cover, and the canonical order.
        ordered = {}
        for field in ("$schema", "meta", "ui", "garments", "buckets", "relative"):
            if field in doc:
                ordered[field] = doc[field]
        for level in LEVELS:
            for kind in ("temp", "precip"):
                ordered[f"{kind}_{level}"] = doc[f"{kind}_{level}"]

        target.write_text(
            json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        total = sum(
            len(v) for s, sec in ordered.items()
            if s.startswith(("temp_", "precip_")) for v in sec.values()
        )
        print(f"wrote lang/{code}.json  ({total} lines)")

    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
