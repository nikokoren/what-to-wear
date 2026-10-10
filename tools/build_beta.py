#!/usr/bin/env python3
"""
Builds beta/, everything a beta fork of the recipe needs, from one commit:

    python3 tools/build_beta.py

    beta/shared.liquid       src/shared.liquid + the fact + flavour and the
    beta/views/*.liquid      outfit-panels prototypes (prototypes/panels/build.py)
    beta/lang/<code>.json    the texts, served by the fork's second polling URL
    beta/settings.yaml       the form, config/settings.next.yaml

The language files are the base files merged with both prototypes' keys,
then made to fit TRMNL's limit of 100 KB per polled URL (the German one
is about 100.6 KB even minified):

  - minified;
  - the old forecast-text pools (temp_*, precip_*) keep every key but only
    the first line of each list. The beta never shows those lines (its
    views show the fact and the sarcastic line instead), but the shared
    logic still checks whether some of their keys exist (shorts_early,
    the "perfect" variants, wet_again) when it picks a scenario.

Before writing anything, every day shape below is rendered with the full
and with the trimmed texts, in both languages, at every sarcasm level,
with the forecast in words and as Visual Forecast. The build stops unless
the screens are identical.
"""

import calendar
import datetime as dt
import importlib.util
import json
import pathlib
import shutil
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent
BUILD = REPO / "build" / "panels"
OUT = REPO / "beta"
LIMIT = 100_000  # TRMNL: "a maximum 100 kilobyte blob of data from external resources"
OLD_POOLS = ("temp_0", "temp_10", "temp_11", "precip_0", "precip_10", "precip_11")

_spec = importlib.util.spec_from_file_location("panels_build", REPO / "prototypes" / "panels" / "build.py")
panels_build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(panels_build)


def trim(node):
    """Every key kept, every list cut to its first entry."""
    if isinstance(node, dict):
        return {k: trim(v) for k, v in node.items()}
    if isinstance(node, list):
        return node[:1]
    return node


def minified(doc):
    return json.dumps(doc, ensure_ascii=False, separators=(",", ":"))


# Day shapes: feels-like by hour, rain chance by hour, weather code by hour.
DRY = [0] * 24
CLEAR = [0] * 24
SHAPES = {
    "steady": ([16] * 24, DRY, CLEAR),
    "warming": ([9, 9, 8, 8, 8, 9, 10, 11, 12, 14, 17, 20, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16], DRY, CLEAR),
    "arc": ([2, 2, 2, 2, 2, 3, 4, 5, 7, 10, 13, 15, 16, 16, 15, 13, 10, 7, 5, 4, 3, 3, 2, 2], DRY, CLEAR),
    "cooling": ([18, 18, 18, 18, 18, 18, 18, 18, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 8, 7, 7, 7, 7], DRY, CLEAR),
    "heat": ([22, 22, 22, 22, 22, 23, 24, 25, 27, 29, 31, 33, 34, 35, 35, 34, 33, 31, 29, 27, 26, 25, 24, 23], DRY, CLEAR),
    "cold": ([-6] * 24, DRY, CLEAR),
    "rain_later": ([12] * 24, [0] * 13 + [80] * 11, [0] * 13 + [61] * 11),
    "rain_now": ([11] * 24, [90] * 12 + [0] * 12, [61] * 12 + [0] * 12),
    "wet_again": ([10] * 24, [90] * 9 + [0] * 5 + [85] * 10, [61] * 9 + [0] * 5 + [61] * 10),
    "snow": ([-1] * 24, [0] * 10 + [80] * 14, [0] * 10 + [71] * 14),
}
DATES = ("2026-06-10", "2026-12-24")
HOURS = (7, 19, 22)
OFFSET = 3600


def context(texts, date, hour, shape, lang, sarcasm, forecast):
    feels, probs, codes = SHAPES[shape]
    times = [f"{date}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{date}T{hour:02d}:30", "temperature_2m": feels[hour],
                        "apparent_temperature": feels[hour], "weather_code": codes[hour]},
            "hourly": {"time": times, "temperature_2m": feels, "apparent_temperature": feels,
                       "precipitation_probability": probs, "weather_code": codes}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "show_future_suggestions": forecast,
           "lat_lon": "48.2,16.4", "show_bottom_bar": "on", "topical_lines": "on"}
    d = dt.date.fromisoformat(date)
    ts = calendar.timegm((d.year, d.month, d.day, hour, 30, 0)) - OFFSET
    return {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                      "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
            "IDX_0": data, "IDX_1": texts}


def verify(shared, view, full, trimmed):
    page = Environment().from_string(shared + view)
    checked = 0
    seen = set()
    panels = words = errors = 0
    for lang in ("en", "de"):
        for args in ((d, h, s) for d in DATES for h in HOURS for s in SHAPES):
            for sarcasm in ("0", "10", "11"):
                for forecast in ("Yes", "visual"):
                    a = page.render(**context(full[lang], *args, lang, sarcasm, forecast))
                    b = page.render(**context(trimmed[lang], *args, lang, sarcasm, forecast))
                    if a != b:
                        raise SystemExit(f"trimmed texts change the screen: {lang} {args} sarcasm {sarcasm} {forecast}")
                    checked += 1
                    seen.add(a)
                    panels += 'class="wtw-panels"' in a
                    words += 'class="font--bold"' in a
                    errors += 'alt="Error"' in a
    # Identical is only proof if the screens are real and varied: no error
    # screens, panels on the days that change, words on most.
    if errors or len(seen) < checked // 4 or panels < checked // 10 or words < checked // 2:
        raise SystemExit(f"verification renders look wrong: {errors} errors, {len(seen)} distinct, "
                         f"{panels} with panels, {words} with words")
    return checked


def main():
    panels_build.main()
    shared = (BUILD / "shared.liquid").read_text(encoding="utf-8")
    full = {l: json.loads((BUILD / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
    trimmed = {l: {k: (trim(v) if k in OLD_POOLS else v) for k, v in doc.items()} for l, doc in full.items()}

    n = verify(shared, (BUILD / "views" / "full.liquid").read_text(encoding="utf-8"), full, trimmed)
    print(f"verified: {n} screens identical with the trimmed texts")

    if OUT.exists():
        for sub in ("views", "lang"):
            shutil.rmtree(OUT / sub, ignore_errors=True)
    (OUT / "views").mkdir(parents=True, exist_ok=True)
    (OUT / "lang").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUILD / "shared.liquid", OUT / "shared.liquid")
    for view in sorted((BUILD / "views").glob("*.liquid")):
        shutil.copyfile(view, OUT / "views" / view.name)
    for lang, doc in trimmed.items():
        text = minified(doc)
        size = len(text.encode("utf-8"))
        if size > LIMIT * 0.9:
            raise SystemExit(f"beta/lang/{lang}.json is {size} bytes, too close to TRMNL's 100 KB limit")
        (OUT / "lang" / f"{lang}.json").write_text(text, encoding="utf-8")
        print(f"beta/lang/{lang}.json: {size // 1000} KB (full, minified: {len(minified(full[lang]).encode()) // 1000} KB)")
    shutil.copyfile(REPO / "config" / "settings.next.yaml", OUT / "settings.yaml")
    markup = (OUT / "shared.liquid").stat().st_size
    if markup > LIMIT:
        raise SystemExit(f"beta/shared.liquid is {markup} bytes, over TRMNL's 100 KB markup limit")
    print(f"beta/shared.liquid: {markup // 1000} KB; built {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
