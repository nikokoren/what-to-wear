#!/usr/bin/env python3
"""
Checks that the weather logic in src/shared.liquid decides what it claims to.

render_test.py proves every scenario renders cleanly in every language. It
does not check that the RIGHT scenario fires. Each case below is a weather
shape that once produced the wrong advice, pinned to the advice it should
produce now.

It also checks the one thing no rendered output can show: that every field
the markup reads is actually requested by the polling URL. The hourly
weather_code went missing that way - the fixtures carried it, the real URL
did not, so snow forecasts were dead in production while every test passed.

Usage:  python3 tools/logic_test.py
"""

import calendar
import copy
import datetime as dt
import json
import pathlib
import re
import sys
from urllib.parse import parse_qs, urlsplit

from liquid import Environment

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_sprites import easter  # noqa: E402
from render_test import REPO, assert_engine, payload as fixture_payload  # noqa: E402

SHARED = (REPO / "src" / "shared.liquid").read_text(encoding="utf-8")
LANGS = {c: json.loads((REPO / "lang" / f"{c}.json").read_text(encoding="utf-8"))
         for c in ("en", "de")}

FIELDS = ["scenario", "precip_scenario", "band", "sprite_slug", "active_theme",
          "when_temp", "when_temp2", "when_precip", "today_tip"]
PROBE = "<P>" + "^".join("{{ %s }}" % f for f in FIELDS) + "</P>"


def utc(y, m, d, hh, mi=0):
    return calendar.timegm(dt.datetime(y, m, d, hh, mi).timetuple())


def run(env, cur, temps, probs, hour, codes=None, date="2026-10-07",
        offset=7200, ts=None, lang="en", texts=None, current_extra=None,
        preference=None, device={"width": 800}):
    """Render one payload and return the markup's own decisions."""
    codes = codes or [0] * 24
    hours = [f"{date}T{h:02d}:00" for h in range(24)]
    current = {"time": f"{date}T{hour:02d}:30", "temperature_2m": cur,
               "apparent_temperature": cur, "weather_code": codes[hour]}
    current.update(current_extra or {})
    data = {
        "utc_offset_seconds": offset,
        "current": current,
        "hourly": {"time": hours, "temperature_2m": temps,
                   "apparent_temperature": temps,
                   "precipitation_probability": probs, "weather_code": codes},
    }
    if ts is None:
        y, m, d = (int(x) for x in date.split("-"))
        ts = utc(y, m, d, hour, 30) - offset
    cfg = {"language": lang, "sarcasm_level": "10", "show_future_suggestions": "yes",
           "lat_lon": "48.2,16.4"}
    if preference is not None:
        cfg["temp_preference"] = preference
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg},
                     "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": 0}, "device": device},
           "IDX_0": data, "IDX_1": texts or LANGS[lang]}
    out = env.from_string(SHARED + PROBE).render(**ctx)
    values = out.split("<P>", 1)[1].split("</P>", 1)[0].split("^")
    return dict(zip(FIELDS, values))


def polling_fields():
    """The hourly= and current= lists of the weather polling URL."""
    for line in (REPO / "config" / "polling_urls.txt").read_text().splitlines():
        if line.startswith("https://api.open-meteo.com/"):
            # Liquid in the query string is fine for parse_qs; only the
            # field lists matter here.
            q = parse_qs(urlsplit(line).query)
            return (set(q["hourly"][0].split(",")), set(q["current"][0].split(",")))
    raise SystemExit("no Open-Meteo line in config/polling_urls.txt")


def main():
    assert_engine()
    env = Environment()
    failures = []

    def expect(label, got, **want):
        for key, value in want.items():
            if got[key] != value:
                failures.append(f"{label}: {key} = {got[key]!r}, expected {value!r}"
                                f"\n      tip: {got['today_tip']!r}")

    # ---- the polling URL feeds everything the markup reads ----
    hourly_req, current_req = polling_fields()
    used_hourly = set(re.findall(r"\bh\.([a-z_0-9]+)", SHARED)) - {"time"}
    used_current = set(re.findall(r"\bcw\.([a-z_0-9]+)", SHARED)) - {"time"}
    for f in sorted(used_hourly - hourly_req):
        failures.append(f"markup reads hourly.{f}, the polling URL never asks for it")
    for f in sorted(used_current - current_req):
        failures.append(f"markup reads current.{f}, the polling URL never asks for it")
    fx = fixture_payload(10, 0, [10] * 24, [0] * 24)
    for f in sorted(set(fx["hourly"]) - hourly_req - {"time"}):
        failures.append(f"render_test fixtures carry hourly.{f}, which the real URL "
                        "does not request - the tests see data devices never get")
    for f in sorted(set(fx["current"]) - current_req - {"time"}):
        failures.append(f"render_test fixtures carry current.{f}, which the real URL "
                        "does not request")

    # ---- snow ahead is about boots, not umbrellas ----
    got = run(env, 1, [1] * 24, [0] * 12 + [80] * 12, 8, codes=[0] * 12 + [73] * 12)
    expect("snow later", got, precip_scenario="snow_coming", when_precip="around midday")

    # ---- a one-hour dip at sunrise does not outrank the day ----
    day = [6, 6, 5.5, 5.5, 5.2, 5.0, 4.0, 2.5, 3.5, 6, 8, 10, 12, 14, 15.5, 16,
           15.5, 14, 12.5, 11, 10, 8, 7.5, 7]
    got = run(env, 5.0, day, [0] * 24, 5)
    expect("one-hour sunrise dip", got, scenario="arc_level",
           when_temp="around midday", when_temp2="tonight")

    # ...but a dip that holds for two hours is real, and it comes first
    held = list(day)
    held[7], held[8] = 2.5, 2.0
    got = run(env, 5.0, held, [0] * 24, 5)
    expect("two-hour sunrise dip", got, scenario="c_coat", when_temp="in two hours")

    # ---- the time named is when the band is crossed, not the trough ----
    cooling = [12] * 8 + [18, 17, 15.5, 14, 12.5, 11, 10.2, 9.5, 9, 8.5, 8, 7, 6.5, 6, 6, 6]
    got = run(env, 18, cooling, [0] * 24, 8)
    expect("cooling crosses at 15:00", got, scenario="c_jacket", when_temp="this afternoon")

    warming = [8] * 9 + [8, 9, 11, 13, 15, 17, 18, 19, 19, 19.5, 20, 20, 20, 20, 20]
    got = run(env, 8, warming, [0] * 24, 8)
    expect("warming crosses at 11:00", got, scenario="w_jacket", when_temp="around midday")

    # ---- raining now: clears, never stops, or stops and comes back ----
    wet = [61] * 24
    got = run(env, 12, [12] * 24, [90] * 10 + [5] * 8 + [80] * 6, 8,
              codes=[61] * 10 + [0] * 8 + [61] * 6)
    expect("rain, dry break, rain", got, precip_scenario="wet_again",
           when_precip="this evening")
    got = run(env, 12, [12] * 24, [90] * 24, 8, codes=wet)
    expect("rain all day", got, precip_scenario="stays_wet")
    got = run(env, 12, [12] * 24, [90] * 10 + [5] * 14, 8, codes=[61] * 10 + [0] * 14)
    expect("rain that clears", got, precip_scenario="drier")
    # a single 30% blip after the break is not "it comes back"
    got = run(env, 12, [12] * 24, [90] * 10 + [5] * 8 + [30] + [5] * 5, 8,
              codes=[61] * 10 + [0] * 14)
    expect("rain, break, blip", got, precip_scenario="drier")
    # a language without wet_again says the true half
    bare = copy.deepcopy(LANGS["en"])
    for lvl in ("0", "10", "11"):
        bare[f"precip_{lvl}"].pop("wet_again")
        bare[f"precip_{lvl}"].pop("wet_again_j")
    got = run(env, 12, [12] * 24, [90] * 10 + [5] * 8 + [80] * 6, 8,
              codes=[61] * 10 + [0] * 8 + [61] * 6, texts=bare)
    expect("wet_again missing from language", got, precip_scenario="drier")

    # ---- the picture dresses for the next hour ----
    got = run(env, 12, [12] * 24, [0] * 9 + [90] * 15, 8)
    expect("rain from the next hour", got, sprite_slug="cool_rain",
           precip_scenario="wetter_long", when_precip="in an hour")
    got = run(env, 12, [12] * 24, [0] * 9 + [40] * 15, 8)
    expect("40% next hour", got, sprite_slug="cool_dry")

    # ---- band edges are inclusive: 3.0 is still freezing ----
    got = run(env, 3.0, [3.0] * 24, [0] * 24, 8)
    expect("exactly on an edge", got, band="freezing")

    # ---- a missing feels-like reading falls back to the air ----
    got = run(env, 24, [24] * 24, [0] * 24, 8,
              current_extra={"apparent_temperature": None})
    expect("no apparent temperature", got, band="warm")

    # ---- the calendar is the forecast location's, not UTC ----
    ny = -5 * 3600
    got = run(env, 12, [12] * 24, [0] * 24, 20, date="2026-11-25", offset=ny)
    expect("Wed before Thanksgiving, 20:30 New York", got, active_theme="")
    got = run(env, 12, [12] * 24, [0] * 24, 19, date="2026-11-26", offset=ny)
    expect("Thanksgiving, 19:30 New York", got, active_theme="thanks")
    got = run(env, 12, [12] * 24, [0] * 24, 7, date="2026-11-26", offset=ny)
    expect("Thanksgiving, 07:30 New York", got, active_theme="thanks")

    # ---- Easter, checked against an independent computus ----
    for year in range(2024, 2036):
        md = easter(year)
        got = run(env, 16, [16] * 24, [0] * 24, 10, date=f"{year}-{md}")
        expect(f"Easter {year}-{md}", got, active_theme="easter", sprite_slug="easter_mild_dry")
    got = run(env, 16, [16] * 24, [0] * 24, 10, date="2026-04-06")
    expect("Easter Monday", got, active_theme="")
    # no theme_easter line yet: falls through to the evening variant
    got = run(env, 16, [16] * 24, [0] * 24, 18, date="2026-04-05")
    expect("Easter evening, no themed line", got, scenario="perfect_evening")

    # ---- "Do you run cold or warm?" shifts the reading, not the ladder ----
    got = run(env, 21, [21] * 24, [0] * 24, 10)
    expect("21C, average", got, band="warm")
    got = run(env, 21, [21] * 24, [0] * 24, 10, preference="-4")
    expect("21C, always cold", got, band="mild")
    got = run(env, 17, [17] * 24, [0] * 24, 10, preference="4")
    expect("17C, always hot", got, band="warm")
    got = run(env, 21, [21] * 24, [0] * 24, 10, preference="3")
    expect("unlisted preference is ignored", got, band="warm")
    # the forecast is shifted too, so the hint agrees with the picture:
    # 12 -> 16 is hoodie weather all day for most, jacket-then-hoodie
    # for someone who is always cold
    rising = [12] * 11 + [13, 14, 15, 16] + [16] * 9
    got = run(env, 12, rising, [0] * 24, 10)
    expect("12 to 16, average", got, scenario="perfect", band="cool")
    got = run(env, 12, rising, [0] * 24, 10, preference="-4")
    expect("12 to 16, always cold", got, scenario="w_jacket", band="cold",
           when_temp="around midday")

    # ---- sentences start capitalised after ? and ! too ----
    texts = copy.deepcopy(LANGS["de"])
    texts["temp_10"]["c_jacket"] = ["Kalt? {WHEN} wird es kälter! ja."]
    got = run(env, 18, cooling, [0] * 24, 8, lang="de", texts=texts)
    expect("German time phrase after a question", got,
           today_tip="Kalt? Heute Nachmittag wird es kälter! Ja.")

    if failures:
        print(f"{len(failures)} FAILURE(S):\n")
        for f in failures:
            print(f"  {f}")
        return 1
    print("all good: polling URL covers the markup, and every pinned weather "
          "shape gets the advice it should")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
