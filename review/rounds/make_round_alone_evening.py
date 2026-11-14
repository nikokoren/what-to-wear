#!/usr/bin/env python3
"""
Round "2026-11-evening-alone" (November 2026): every live evening line
shown without tomorrow's sentence, as the screen shows it with the written
forecast off (owner: some lines don't work without it; judge them one by
one). Keep = it stands alone. Veto = it needs the sentence: apply_evening.py
puts "{S}" in front, so it shows only with the forecast on. An edit (with
Keep) is a version for the screen without the sentence only: the original
stays unchanged with "{S}", the edit is added with "{N}" (owner). Lines already
tagged {S} are left out. These votes stay out of review/examples and
review/dont (tools/review_sync.py, JUDGE_ROUNDS).

    python3 review/rounds/make_round_alone_evening.py
"""

import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-11-evening-alone"
SPRITE = {"rain": "jacket_rain", "snow": "coat_snow", "colder": "coat_dry", "warmer": "sweater_dry",
          "drier": "jacket_rain", "steady": "sweater_dry", "any": "sweater_dry"}
POOL = {"rain": "rain tomorrow", "snow": "snow tomorrow", "colder": "colder tomorrow", "warmer": "warmer tomorrow",
        "drier": "a wet start, dry later", "steady": "no change tomorrow", "any": "any weather"}
LEVEL = {"10": "On", "11": "11"}
TAG = re.compile(r"^((?:\{[A-Z](?::[0-9,]+)?\})*)(.*)$")


def main():
    lines = []
    for lang in ("en", "de"):
        ev = json.loads((REPO / "prototypes" / "panels" / "lang" / f"{lang}.json").read_text(encoding="utf-8"))["evening"]
        for lv in ("10", "11"):
            for pool, texts in ev.get("jokes_" + lv, {}).items():
                for t in texts:
                    tag, text = TAG.match(t).groups()
                    if "{S}" in tag:
                        continue
                    lines.append({"lang": lang, "path": f"flavour_{lv}.evening_{pool}", "text": text, "evtag": tag,
                                  "role": "flavour", "sprite": SPRITE[pool], "fact": "",
                                  "batch": f"Without the sentence: {LEVEL[lv]}, {POOL[pool]}",
                                  "meaning": "Evening screen with the written forecast off: no sentence above. "
                                             "Keep = it stands alone. Veto = it needs the sentence (it then shows only "
                                             "with the forecast on; it is not deleted).",
                                  "new": False,
                                  "hint": "Keep = stands alone · Veto = needs the sentence (not deleted) · Edit = a version only for screens without the sentence; the original stays as it is"
                                          + (f" · tag {tag}" if tag else "")})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "idPrefix": "ea", "lines": lines},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        print(l, sum(1 for r in lines if r["lang"] == l))


if __name__ == "__main__":
    main()
