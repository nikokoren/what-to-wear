#!/usr/bin/env python3
"""
Round 29, the evening pilot (November 2026): the evening line by tomorrow's
weather (rain, colder, steady), after round 28's evening lines failed.

    python3 review/rounds/make_round28.py

Reads the proofreader's files (review/rounds/2026-11-evening/<lang>.proofread.json,
or the critic's <lang>.json) and writes review/rounds/2026-11-evening.json for
the review page. Paths on the page: fact_0.evening_<situation> for the
sentences, flavour_<level>.evening for the evening line. apply_evening.py
puts the kept ones into prototypes/panels/lang/<lang>.json.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-11-evening2"
FROM = {"en": "from 1 pm", "de": "ab 13 Uhr"}
SPRITE = {"tmr_steady": "sweater_dry", "tmr_warmer": "jacket_dry", "tmr_colder": "jacket_dry", "tmr_rain": "jacket_rain",
          "tmr_snow": "coat_snow", "tmr_drier": "jacket_rain", "tmr_wet": "jacket_rain", "tmr_snow_start": "coat_snow"}
MEANING = {
    "tmr_steady": "Tomorrow's outfit works all day (one drawing, 'all day').",
    "tmr_warmer": "Tomorrow warms up from the time shown; the second drawing is lighter.",
    "tmr_colder": "Tomorrow gets colder from the time shown; the second drawing is warmer.",
    "tmr_rain": "Rain starts tomorrow at the time shown.",
    "tmr_snow": "Snow starts tomorrow at the time shown.",
    "tmr_drier": "Tomorrow starts wet; the rain stops at the time shown.",
    "tmr_wet": "Tomorrow starts wet: rain likely when you head out.",
    "tmr_snow_start": "Tomorrow starts with snow.",
}
SAMPLE = {"en": "Tomorrow: rain from 1 pm, so take the umbrella.", "de": "Morgen ab 13 Uhr Regen, also nimm den Schirm mit."}
LEVEL = {"10": "On", "11": "11"}
# Each kind of tomorrow with a sentence the owner kept in round 28.
PILOT = {
    "rain": ("jacket_rain", {"en": "Tomorrow it rains from 1\u00a0pm, so take the umbrella.",
                             "de": "Denk morgen an den Schirm, ab 13\u00a0Uhr regnet's."}, "rains"),
    "colder": ("coat_dry", {"en": "Tomorrow the temperature drops from 1\u00a0pm, so pack something warm.",
                            "de": "Morgen wird's ab 13\u00a0Uhr kälter, dann brauchst du eine Schicht mehr."}, "gets colder"),
    "steady": ("sweater_dry", {"en": "Tomorrow is a one-outfit day.", "de": "Das Outfit für morgen passt den ganzen Tag."},
               "doesn't change"),
}


def main():
    lines = []
    for lang in ("en", "de"):
        src = HERE / ROUND / f"{lang}.proofread.json"
        if not src.exists():
            src = HERE / ROUND / f"{lang}.json"
        if not src.exists():
            src = HERE / ROUND / f"{lang}.json"
        if not src.exists():
            continue
        seen = set()
        for item in json.loads(src.read_text(encoding="utf-8"))["lines"]:
            text, path = item["text"].strip(), item["path"]
            if (path, text) in seen:
                continue
            seen.add((path, text))
            hints = ["Evening, 8 pm to midnight"]
            if item.get("was"):
                hints.append("Proofread from: " + item["was"])
            if path.startswith("evening.facts."):
                key = path.rsplit(".", 1)[1]
                row = {"lang": lang, "path": f"fact_0.evening_{key}", "text": text, "role": "fact",
                       "sprite": SPRITE[key], "fills": {"{FROM}": FROM[lang]},
                       "batch": "Tomorrow: " + key.replace("tmr_", "").replace("_", " "),
                       "meaning": "Evening screen, tomorrow's forecast sentence. " + MEANING[key]}
            else:
                lv, sit = path.split(".")[1].split("_")[1], path.split(".")[2]
                row = {"lang": lang, "path": f"flavour_{lv}.evening_{sit}", "text": text, "role": "flavour",
                       "sprite": PILOT[sit][0], "fact": PILOT[sit][1][lang], "batch": f"Evening {sit}: {LEVEL[lv]}",
                       "meaning": f"Evening screen at {LEVEL[lv]}, tomorrow {PILOT[sit][2]}: the line under tomorrow's sentence."}
            row["new"] = True
            row["hint"] = " · ".join(hints)
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "e2", "lines": lines}
    (HERE / f"{ROUND}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        print(l, sum(1 for r in lines if r["lang"] == l))


if __name__ == "__main__":
    main()
