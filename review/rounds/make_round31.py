#!/usr/bin/env python3
"""
Round 31 (November 2026): the evening line, written in the directions the
owner picked in round 30 (make_round30.py), 60 lines by owner choice.

    python3 review/rounds/make_round31.py

Reads review/rounds/2026-11-evening31/<lang>.proofread.json (else the
critic's <lang>.json, else <lang>.written.json) and writes
review/rounds/2026-11-evening31.json for the review page. A line's tag
({P}, {T}, {D:n}) stays out of its text and goes in "evtag";
apply_evening.py puts it back in front when the line goes live.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-11-evening31"
FROM = {"en": "from 1 pm", "de": "ab 13 Uhr"}
FACT_KEY = {"rain": "tmr_rain", "snow": "tmr_snow", "colder": "tmr_colder", "warmer": "tmr_warmer",
            "drier": "tmr_drier", "steady": "tmr_steady", "any": "tmr_rain"}
SPRITE = {"rain": "jacket_rain", "snow": "coat_snow", "colder": "coat_dry", "warmer": "sweater_dry",
          "drier": "jacket_rain", "steady": "sweater_dry", "any": "jacket_rain"}
POOL = {"rain": "rain tomorrow", "snow": "snow tomorrow", "colder": "colder tomorrow", "warmer": "warmer tomorrow",
        "drier": "a wet start, dry later", "steady": "no change tomorrow", "any": "any weather"}
LEVEL = {"10": "On", "11": "11"}
DAYS = {"en": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}


def tag_hint(tag):
    if tag == "{P}":
        return "Only with tonight's drawing beside tomorrow's"
    if tag == "{T}":
        return "Only when tomorrow's sentence names a time"
    if tag.startswith("{D:"):
        days = [DAYS["en"][int(d)] for d in tag[3:-1].split(",")]
        return "Only when tomorrow is " + " or ".join(days)
    return ""


def main():
    lines = []
    for lang in ("en", "de"):
        facts = json.loads((HERE.parent.parent / "prototypes" / "panels" / "lang" / f"{lang}.json").read_text(encoding="utf-8"))["evening"]["facts"]
        src = next((HERE / ROUND / f"{lang}{s}.json" for s in (".proofread", "", ".written")
                    if (HERE / ROUND / f"{lang}{s}.json").exists()), None)
        if not src:
            continue
        for item in json.loads(src.read_text(encoding="utf-8"))["lines"]:
            _, lvk, pool = item["path"].split(".")
            lv = lvk.split("_")[1]
            fact = facts[FACT_KEY[pool]][0].replace("{DRY}", "").replace("{FROM}", FROM[lang])
            tag = item.get("evtag", "")
            hints = [h for h in (tag_hint(tag), ("Proofread from: " + item["was"]) if item.get("was") else "") if h]
            lines.append({"lang": lang, "path": f"flavour_{lv}.evening_{pool}", "text": item["text"].strip(),
                          "evtag": tag, "role": "flavour", "sprite": SPRITE[pool], "fact": fact,
                          "batch": f"Evening, {POOL[pool]}: {LEVEL[lv]}",
                          "meaning": f"Evening screen at {LEVEL[lv]}, {POOL[pool]}: the line under tomorrow's sentence.",
                          "new": True, "hint": " · ".join(hints)})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "idPrefix": "e3", "lines": lines},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        print(l, sum(1 for r in lines if r["lang"] == l))


if __name__ == "__main__":
    main()
