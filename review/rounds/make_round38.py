#!/usr/bin/env python3
"""
Round 38 (November 2026): variations of starred lines for the thinnest
evening pools (owner: where variety is thin, variations of starred
phrasings are fine), 20 slots by owner choice, plus English extras
(punchline options, a standalone version, clearer versions) whose
"replaces" names the live line a kept one replaces.

    python3 review/rounds/make_round38.py
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-11-evening38"
FROM = {"en": "from 1 pm", "de": "ab 13 Uhr"}
FACT_KEY = {"rain": "tmr_rain", "snow": "tmr_snow", "colder": "tmr_colder", "warmer": "tmr_warmer",
            "drier": "tmr_drier", "steady": "tmr_steady", "any": "tmr_rain"}
SPRITE = {"rain": "jacket_rain", "snow": "coat_snow", "colder": "coat_dry", "warmer": "sweater_dry",
          "drier": "jacket_rain", "steady": "sweater_dry", "any": "jacket_rain"}
POOL = {"rain": "rain tomorrow", "snow": "snow tomorrow", "colder": "colder tomorrow", "warmer": "warmer tomorrow",
        "drier": "a wet start, dry later", "steady": "no change tomorrow", "any": "any weather"}
LEVEL = {"10": "On", "11": "11"}
ANY_SHOWN = ("rain", "colder", "warmer", "steady", "snow", "drier")
DAYS = {"en": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}


def tag_hint(tag):
    if tag == "{P}":
        return "Only with tonight's drawing beside tomorrow's"
    if tag.startswith("{N}"):
        return "Only without tomorrow's sentence (written forecast off)"
    if tag == "{S}":
        return "Only when tomorrow's sentence shows (not with the written forecast off)"
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
        items = json.loads(src.read_text(encoding="utf-8"))["lines"]
        extra = HERE / ROUND / f"{lang}.extra.json"
        if extra.exists():
            items += json.loads(extra.read_text(encoding="utf-8"))["lines"]
        for n, item in enumerate(items):
            _, lvk, pool = item["path"].split(".")
            lv = lvk.split("_")[1]
            shown = pool
            if pool == "any":  # under a different kind of tomorrow each, to judge that it fits every one
                shown = ANY_SHOWN[n % len(ANY_SHOWN)]
                item = {**item, "hint": " · ".join(h for h in ("Any weather: shown here under " + POOL[shown],
                                                               item.get("hint", "")) if h)}
            fact = facts[FACT_KEY[shown]][0].replace("{DRY}", "").replace("{FROM}", FROM[lang])
            tag = item.get("evtag", "")
            hints = [h for h in (tag_hint(tag), ("Proofread from: " + item["was"]) if item.get("was") else "",
                                  item.get("hint", "")) if h]
            lines.append({"lang": lang, "path": f"flavour_{lv}.evening_{pool}", "text": item["text"].strip(),
                          "evtag": tag, "replaces": item.get("replaces", ""), "role": "flavour", "sprite": SPRITE[shown], "fact": fact,
                          "batch": f"Evening, {POOL[pool]}: {LEVEL[lv]}",
                          "meaning": f"Evening screen at {LEVEL[lv]}, {POOL[pool]}: the line under tomorrow's sentence.",
                          "new": True, "hint": " · ".join(hints)})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "idPrefix": "eb", "lines": lines},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        print(l, sum(1 for r in lines if r["lang"] == l))


if __name__ == "__main__":
    main()
