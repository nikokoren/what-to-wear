#!/usr/bin/env python3
"""
Merges a partial key set into a language file.

    python3 tools/merge_keys.py <partial.json> [--dry-run]

Unlike tools/assemble_lang.py, which expects a complete level, this replaces
only the keys present in the partial file and leaves everything else alone.
That is what a "write the new keys and deepen the busy ones" pass produces.

The partial is named <code>_<level>_add.json and shaped as:
    {"temp": {"<key>": ["line", ...]}, "precip": {"<key>": ["line", ...]}}
"""

import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not argv:
        print(__doc__.strip())
        return 2

    touched = {}
    for arg in argv:
        path = pathlib.Path(arg)
        code, level = path.stem.split("_")[0], path.stem.split("_")[1]
        partial = json.loads(path.read_text(encoding="utf-8"))
        target = REPO / "lang" / f"{code}.json"
        doc = touched.get(code) or json.loads(target.read_text(encoding="utf-8"))
        touched[code] = doc

        for kind in ("temp", "precip"):
            section = f"{kind}_{level}"
            doc.setdefault(section, {})
            for key, lines in (partial.get(kind) or {}).items():
                if not isinstance(lines, list) or not lines:
                    print(f"  skip {section}.{key}: not a non-empty list", file=sys.stderr)
                    continue
                before = len(doc[section].get(key, []))
                doc[section][key] = [ln.strip() for ln in lines]
                print(f"  {section}.{key}: {before} -> {len(lines)}")

    if dry:
        print("DRY RUN, nothing written")
        return 0

    for code, doc in touched.items():
        target = REPO / "lang" / f"{code}.json"
        target.write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        total = sum(len(v) for s, sec in doc.items()
                    if s.startswith(("temp_", "precip_")) for v in sec.values())
        print(f"wrote lang/{code}.json ({total} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
