#!/usr/bin/env python3
"""
Builds the fact + flavour prototype next to the real markup.

    python3 prototypes/fact-flavour/build.py      # -> build/proto/

Writes build/proto/shared.liquid (src/shared.liquid with block.liquid
inserted), build/proto/views/ (the real views, showing the fact line in
bold and the flavour line under it) and build/proto/lang/ (each language
file with this prototype's keys merged in). The old tip is still computed,
so the same render can show old and new side by side.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
OUT = REPO / "build" / "proto"
ANCHOR = "{%- comment %}\n============ DRESS FOR THE DOOR"

OLD_TIP = "<p>{{ today_tip }}</p>"
NEW_TIP = ("<p class=\"font--bold\">{{ fact_line }}</p>"
           "{%- if flavour_line != '' %}<p>{{ flavour_line }}</p>{%- endif %}")


def main():
    shared = (REPO / "src" / "shared.liquid").read_text(encoding="utf-8")
    if ANCHOR not in shared:
        raise SystemExit("anchor not found in src/shared.liquid")
    block = (HERE / "block.liquid").read_text(encoding="utf-8")
    (OUT / "views").mkdir(parents=True, exist_ok=True)
    (OUT / "lang").mkdir(parents=True, exist_ok=True)
    (OUT / "shared.liquid").write_text(shared.replace(ANCHOR, block + "\n\n" + ANCHOR, 1), encoding="utf-8")

    for view in (REPO / "src" / "views").glob("*.liquid"):
        src = view.read_text(encoding="utf-8")
        if OLD_TIP not in src:
            raise SystemExit(f"{view.name}: tip markup not found")
        src = src.replace(OLD_TIP, NEW_TIP).replace("today_tip != ''", "fact_line != ''")
        (OUT / "views" / view.name).write_text(src, encoding="utf-8")

    for extra in (HERE / "lang").glob("*.json"):
        base = json.loads((REPO / "lang" / extra.name).read_text(encoding="utf-8"))
        base.update(json.loads(extra.read_text(encoding="utf-8")))
        (OUT / "lang" / extra.name).write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"built {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
