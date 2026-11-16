#!/usr/bin/env python3
"""
Pins the weather cases the November 2026 review found, where the words
and the drawings disagreed or said something untrue. Words and drawings
now read one rain timeline (ONE RAIN TIMELINE, src/shared.liquid).

    python3 prototypes/panels/build.py
    python3 prototypes/panels/test_weather_cases.py
"""

import calendar
import datetime as dt
import json
import pathlib
import random
import re
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
BUILD = REPO / "build" / "panels"
TEMPLATE = Environment().from_string((BUILD / "shared.liquid").read_text(encoding="utf-8")
                                     + "@@{{ precip_scenario }}|{{ heat_danger }}@@"
                                     + (BUILD / "views" / "full.liquid").read_text(encoding="utf-8"))
TEXTS = {l: json.loads((BUILD / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
OFFSET = 7200
DATE = "2026-03-10"


def render(feels, hour=7, probs=None, codes=None, now_code=None, days=1, forecast=True, nxt=True, pref=None, lang="en"):
    n = 24 * days
    feels = list(feels) + [feels[-1]] * (n - len(feels))
    probs = list(probs or [0] * n)
    probs += [probs[-1]] * (n - len(probs))
    codes = list(codes or [0] * n)
    codes += [codes[-1]] * (n - len(codes))
    d0 = dt.date.fromisoformat(DATE)
    hours = [f"{d0 + dt.timedelta(days=i // 24)}T{i % 24:02d}:00" for i in range(n)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna", "latitude": 48.2,
            "current": {"time": f"{DATE}T{hour:02d}:30", "temperature_2m": feels[hour], "apparent_temperature": feels[hour],
                        "weather_code": codes[hour] if now_code is None else now_code},
            "hourly": {"time": hours, "temperature_2m": feels, "apparent_temperature": feels,
                       "precipitation_probability": probs, "weather_code": codes}}
    cfg = {"language": lang, "sarcasm_level": "0", "lat_lon": "48.2,16.4", "show_bottom_bar": "on",
           "show_future_suggestions": forecast, "what_to_wear_next": nxt}
    if pref is not None:
        cfg["temp_preference"] = pref
    ts = calendar.timegm((d0.year, d0.month, d0.day, hour, 30, 0)) - OFFSET
    html = TEMPLATE.render(trmnl={"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                                  "user": {"utc_offset": OFFSET}}, IDX_0=data, IDX_1=TEXTS[lang])
    scenario, heat = re.search(r"@@(.*?)@@", html).group(1).split("|")
    body = html.split("@@")[-1]
    fact = re.search(r'<p class="font--bold">(.*?)</p>', body, re.S)
    return {"scenario": scenario, "heat": heat == "true",
            "drawings": re.findall(r'src="[^"]*/sprites/([a-z_]+)[.]png"', body),
            "fact": (fact.group(1) if fact else "").replace("&#39;", "'")}


failures = []


def expect(name, ok, got=None):
    if not ok:
        failures.append(name if got is None else f"{name}: got {got!r}")


def one_of(text, lang, key, section="facts"):
    """Is one of the pool's wordings in the text (placeholders as wildcards)?"""
    pool = TEXTS[lang][section][key] if section == "facts" else TEXTS[lang]["evening"]["facts"][key]
    for line in pool:
        pattern = re.sub(r"\\\{[A-Z0-9:,]+\\\}", ".*?", re.escape(line))
        if re.search(pattern, text, re.I):
            return True
    return False


# 1. Snowing now, rain later: not "the snow doesn't stop", and the later drawings are rain.
r = render([0] * 8 + [3, 4, 5, 6, 6, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 4], codes=[73] * 9 + [61] * 15, probs=[80] * 24)
expect("snow turning to rain: its own sentence", one_of(r["fact"], "en", "p_turns_rain"), r["fact"])
expect("snow turning to rain: not 'snow all day'", not one_of(r["fact"], "en", "p_stays_wet_snow"), r["fact"])
expect("snow turning to rain: snow now, rain drawn later", r["drawings"][0].endswith("_snow")
       and all(d.endswith("_rain") for d in r["drawings"][1:]) and len(r["drawings"]) > 1, r["drawings"])
r = render([-3] * 24, codes=[73] * 24, probs=[80] * 24)
expect("snow all day stays snow all day", one_of(r["fact"], "en", "p_stays_wet_snow") and r["drawings"] == ["coat_snow"], r)

# 2. Raining now at 40% all day: the words say it stays wet, and no dry drawing follows.
r = render([14] * 24, hour=8, codes=[61] * 24, probs=[40] * 24)
expect("rain at 40% all day: stays wet", r["scenario"] == "stays_wet", r["scenario"])
expect("rain at 40% all day: one wet drawing", r["drawings"] == ["sweater_rain"], r["drawings"])
# ... and when the words say it stops, the last drawing is dry.
r = render([14] * 24, hour=8, codes=[61] * 11 + [0] * 13, probs=[80] * 11 + [10] * 13)
expect("rain that stops: drier, and a dry drawing after it", r["scenario"] == "drier" and r["drawings"] == ["sweater_rain", "sweater_dry"], r)

# 3. Coat, jacket, sweater, and the coat back at night: the evening's layer is drawn.
SWING = [3, 3, 3, 3, 3, 3, 3, 4, 6, 8, 10, 13, 14, 15, 15, 15, 14, 11, 9, 7, 6, 5, 4, 4]
r = render(SWING, forecast=False)
expect("a day that warms and cools: the warmest outfit and the layer back on",
       r["drawings"] == ["coat_dry", "sweater_dry", "coat_dry"], r["drawings"])
UP = [3, 3, 3, 3, 3, 3, 3, 4, 7, 10, 13, 16, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]
r = render(UP, forecast=False)
expect("a day that only warms: it ends on the last outfit", r["drawings"][-1] == "tee_pants_dry" and len(r["drawings"]) == 3, r["drawings"])

# 4. Dangerous heat doesn't move with "Do you run cold or warm?".
HOT = [28, 28, 27, 27, 27, 28, 29, 31, 33, 35, 36, 37, 37.5, 37.5, 37, 36, 35, 34, 33, 31, 30, 29, 29, 28]
for pref in (None, "-4", "-2", "2", "4"):
    r = render(HOT, hour=8, pref=pref)
    expect(f"37.5 C feels-like, preference {pref}: the heat warning", r["heat"] and one_of(r["fact"], "en", "heat_danger"), r["fact"])
WARM = [22, 22, 21, 21, 21, 22, 23, 25, 27, 29, 30, 31, 32, 32, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]
for pref in (None, "-4", "4"):
    expect(f"32 C feels-like, preference {pref}: no heat warning", not render(WARM, hour=8, pref=pref)["heat"])

# 5. Rain that's only possible, drawings only: the rain sentence, not "works all day".
MAYBE = [0] * 12 + [45] * 5 + [0] * 7
r = render([14] * 24, hour=8, probs=MAYBE, forecast=False)
expect("possible rain, drawings only: one dry drawing", r["drawings"] == ["sweater_dry"], r["drawings"])
expect("possible rain, drawings only: the 'maybe' sentence", one_of(r["fact"], "en", "p_wetter_maybe"), r["fact"])
expect("no rain, drawings only: 'works all day'", one_of(render([14] * 24, hour=8, forecast=False)["fact"], "en", "steady"))

# 6. The evening: tomorrow's possible rain is said.
r = render([8] * 48, hour=20, days=2, probs=[0] * 24 + [45] * 24)
expect("tomorrow at 45% all day: 'rain is possible'", one_of(r["fact"], "en", "tmr_maybe", "evening"), r["fact"])
r = render([8] * 48, hour=20, days=2)
expect("a dry tomorrow: 'one outfit all day'", one_of(r["fact"], "en", "tmr_steady", "evening"), r["fact"])
r = render([8] * 48, hour=20, days=2, probs=[0] * 24 + [45] * 24, lang="de")
expect("morgen 45 %: 'Regen ist möglich'", one_of(r["fact"], "de", "tmr_maybe", "evening"), r["fact"])

# 7. Dry by the code, but this hour is forecast at 90%: the umbrella now.
r = render([14] * 24, hour=14, codes=[3] * 24, probs=[0] * 14 + [90] + [0] * 9)
expect("rain due this hour: said", r["scenario"] == "wetter", r["scenario"])
expect("rain due this hour: the umbrella now, dry after", r["drawings"] == ["sweater_rain", "sweater_dry"], r["drawings"])

# 8. Rain setting in at 10 pm for the night isn't "a short shower".
NIGHT = [0] * 22 + [90] * 10 + [0] * 16
r = render([8] * 48, hour=19, days=2, probs=NIGHT, codes=[61 if p else 0 for p in NIGHT], nxt=False)
expect("rain from 10 pm into the night: 'sets in'", r["scenario"] == "wetter_long", r["scenario"])
r = render([8] * 48, hour=19, days=2, probs=[0] * 22 + [90] + [0] * 25, nxt=False)
expect("one wet hour at 10 pm: a shower", r["scenario"] == "wetter", r["scenario"])

# One threshold: a likely hour is rain in the words and in a drawing; less is "maybe" and draws nothing.
r = render([14] * 24, hour=8, probs=[0] * 13 + [55] * 2 + [0] * 9)
expect("55%: rain in the words", r["scenario"] == "wetter", r["scenario"])
expect("55%: rain in a drawing", any(d.endswith("_rain") for d in r["drawings"]), r["drawings"])
r = render([14] * 24, hour=8, probs=[0] * 13 + [45] * 2 + [0] * 9)
expect("45%: 'maybe' in the words, nothing drawn", r["scenario"] == "wetter_maybe" and r["drawings"] == ["sweater_dry"], r)

# Random days: whenever the words promise rain or say it stays wet, a drawing shows it.
rnd = random.Random(11)
for _ in range(400):
    base = rnd.uniform(4, 28)
    feels = [round(base + rnd.uniform(0, 8) * max(0, 1 - abs(h % 24 - 14) / 8), 1) for h in range(48)]
    start, length = rnd.randint(0, 40), rnd.randint(1, 10)
    probs = [rnd.choice((55, 70, 90)) if start <= i < start + length else rnd.choice((0, 5, 15, 30, 45)) for i in range(48)]
    codes = [61 if p >= 50 else 0 for p in probs]
    hour = rnd.randint(5, 19)
    r = render(feels, hour=hour, probs=probs, codes=codes, days=2)
    wet = [d.endswith("_rain") for d in r["drawings"]]
    if r["scenario"] in ("wetter", "wetter_long") and not any(wet):
        expect(f"words say rain, no wet drawing (hour {hour})", False, (r["drawings"], probs[hour:24]))
    if r["scenario"] in ("", "wetter_maybe") and any(wet):
        expect(f"a wet drawing, no rain in the words (hour {hour})", False, (r["drawings"], probs[hour:24]))
    if r["scenario"] == "stays_wet" and not all(wet):
        expect(f"words say it stays wet, a dry drawing (hour {hour})", False, (r["drawings"], probs[hour:24]))

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: the words and the drawings agree on rain, snow that turns to rain, the evening's layer, heat and tomorrow")
