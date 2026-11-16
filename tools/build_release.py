#!/usr/bin/env python3
"""
Build a release of the recipe into release/<version>/.

    python3 tools/build_release.py 2.0.0 --date 2026-11-01

Owner's rollout (October 2026): two steps, and the texts URL pinned to a
version tag so the markup and the texts always match.

  release/<version>/step1/shared.liquid   2.0 markup that also reads the
                                          single-URL shape devices have
                                          today, with the old wording built
                                          in for that window
  release/<version>/shared.liquid         the same markup without it (step 3)
  release/<version>/views/*.liquid        the four views (all steps)
  release/<version>/lang/<code>.json      the texts the tag serves
  release/<version>/settings.yaml         the form, with the release date
  release/<version>/polling_urls.txt      weather, then texts at @v<version>
  release/<version>/README.md             the steps, in order

It builds the beta first (tools/build_beta.py: the same markup, texts and
views, verified) and then checks the release itself:
  - step 1 on today's single URL: every screen has a drawing and words;
  - step 1 with both URLs renders exactly what step 3 renders;
  - every markup file is under TRMNL's 100 KB ceiling.
"""

import argparse
import calendar
import datetime as dt
import json
import pathlib
import random
import re
import shutil
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import build_beta  # noqa: E402
import build_transitional  # noqa: E402

LIMIT = 100_000
# The old wording step 1 carries only serves its one-day window: two
# wordings per situation keep the 2.0 markup under the ceiling.
STEP1_PER_KEY = 2
OFFSET = 7200
STEP1_HEADER = """{%- comment %}
What to Wear {version}, rollout step 1. Built by tools/build_release.py:
the 2.0 markup, plus the old wording for devices that don't have the texts
polling URL yet. Don't edit by hand; see release/{version}/README.md.
{%- endcomment %}
"""


def screens(seed=7, n=60):
    rnd = random.Random(seed)
    for _ in range(n):
        lo = rnd.uniform(-8, 24)
        amp = rnd.uniform(0, 16)
        peak = rnd.randint(12, 17)
        feels = [round(lo + amp * max(0, 1 - abs(h - peak) / 8)) for h in range(24)]
        wet = rnd.random() < 0.3
        start = rnd.randint(8, 18)
        probs = [80 if wet and start <= h < start + 3 else 0 for h in range(24)]
        codes = [61 if p else 0 for p in probs]
        yield feels, probs, codes, rnd.choice((7, 9, 12, 15, 19))


def render(env, feels, probs, codes, hour, cfg, shape, texts=None):
    date = "2026-10-20"
    hours = [f"{date}T{h:02d}:00" for h in range(24)]
    wx = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna", "latitude": 48.2,
          "current": {"time": f"{date}T{hour:02d}:30", "temperature_2m": feels[hour],
                      "apparent_temperature": feels[hour], "weather_code": codes[hour]},
          "hourly": {"time": hours, "temperature_2m": feels, "apparent_temperature": feels,
                     "precipitation_probability": probs, "weather_code": codes}}
    d = dt.date.fromisoformat(date)
    ts = calendar.timegm((d.year, d.month, d.day, hour, 30, 0)) - OFFSET
    trmnl = {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
             "user": {"utc_offset": OFFSET}, "device": {"width": 800}}
    if shape == "root":
        return env.render(trmnl=trmnl, **wx)
    return env.render(trmnl=trmnl, IDX_0=wx, IDX_1=texts)


def words(html):
    return [w.strip() for w in re.findall(r"<p[^>]*>(.*?)</p>", html, re.S) if w.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("version")
    ap.add_argument("--date", required=True, help="release date, YYYY-MM-DD, for the changelog")
    args = ap.parse_args()
    version, tag = args.version, "v" + args.version
    out = REPO / "release" / version

    build_beta.main()
    beta = REPO / "beta"
    slim = (beta / "shared.liquid").read_text(encoding="utf-8")
    step1 = STEP1_HEADER.replace("{version}", version) + build_transitional.build(
        (build_beta.BUILD / "shared.liquid").read_text(encoding="utf-8"), per_key=STEP1_PER_KEY)

    if out.exists():
        shutil.rmtree(out)
    (out / "step1").mkdir(parents=True)
    (out / "views").mkdir()
    (out / "lang").mkdir()
    (out / "step1" / "shared.liquid").write_text(step1, encoding="utf-8")
    (out / "shared.liquid").write_text(slim, encoding="utf-8")
    for f in (beta / "views").glob("*.liquid"):
        shutil.copyfile(f, out / "views" / f.name)
    for f in (beta / "lang").glob("*.json"):
        shutil.copyfile(f, out / "lang" / f.name)
    form = (REPO / "config" / "settings.next.yaml").read_text(encoding="utf-8").replace("RELEASE_DATE", args.date)
    (out / "settings.yaml").write_text(form, encoding="utf-8")
    weather = [l for l in (REPO / "config" / "polling_urls.txt").read_text(encoding="utf-8").splitlines()
               if l.startswith("https://api.open-meteo.com")][0]
    texts_url = (f"https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@{tag}/release/{version}/lang/"
                 "{{ language | default: 'en' }}.json")
    (out / "polling_urls.txt").write_text(weather + "\n" + texts_url + "\n", encoding="utf-8")

    # ---- checks ----
    problems = []
    for name, text in (("step1/shared.liquid", step1), ("shared.liquid", slim)):
        size = len(text.encode("utf-8"))
        print(f"{name}: {size:,} bytes")
        if size > LIMIT:
            problems.append(f"{name} is over the 100 KB ceiling")
    texts = {l: json.loads((out / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
    checked = 0
    for view in ("full", "half_vertical"):
        v = (out / "views" / f"{view}.liquid").read_text(encoding="utf-8")
        e1, e3 = Environment().from_string(step1 + v), Environment().from_string(slim + v)
        for feels, probs, codes, hour in screens():
            for lang in ("en", "de"):
                # Today's devices: one polling URL, the old form's values.
                old = {"language": lang, "sarcasm_level": "10", "show_future_suggestions": "Yes",
                       "lat_lon": "48.2,16.4", "show_bottom_bar": "on"}
                html = render(e1, feels, probs, codes, hour, old, "root")
                if "sprites/" not in html or not words(html):
                    problems.append(f"step 1, one URL, {view} {lang} {hour}:30: no drawing or no words")
                new = dict(old, what_to_wear_next=True)
                a = render(e1, feels, probs, codes, hour, new, "idx", texts[lang])
                b = render(e3, feels, probs, codes, hour, new, "idx", texts[lang])
                if words(a) != words(b) or re.findall(r"sprites/[a-z_]+", a) != re.findall(r"sprites/[a-z_]+", b):
                    problems.append(f"step 1 and step 3 differ with both URLs, {view} {lang} {hour}:30")
                checked += 1
    print(f"checked {checked} screen pairs")
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems[:20]))
        return 1

    (out / "README.md").write_text(f"""# What to Wear {version}

Built by `python3 tools/build_release.py {version} --date {args.date}`. Don't
edit these files by hand.

Before step 1: this branch merged to `main` (the drawings load from
`sprites/` on `main`), and the tag `{tag}` pushed, so the texts URL below
resolves. Check it in a browser: it should return JSON.

## Step 1: the markup

In TRMNL > Plugins > What to Wear (the original, not a fork):

1. **Shared markup:** `step1/shared.liquid`.
2. **Views:** `views/full.liquid`, `half_horizontal.liquid`,
   `half_vertical.liquid`, `quadrant.liquid` into their boxes.
3. **Form:** `settings.yaml`.

Don't touch the polling URL yet. Devices keep today's single URL and show
the 2.0 drawings with the old one-line wording, which this markup carries.
Force Refresh in the editor, check a screen, then give it a day to reach
installed devices.

## Step 2: the polling URL

Replace the Polling URL box with the two lines in `polling_urls.txt`,
weather first, texts second. Devices pick up the new wording, What to Wear
Next? and everything else in 2.0. Check on a real device that the words
appear.

## Step 3: the slim markup

Once devices are on both URLs (give it a day), paste `shared.liquid` into
the shared markup. Same output, without the old wording built in.

## Later text updates

New texts go out as a new tag and a new texts URL (`@v{version}` becomes
the next version), so markup and texts never drift apart.
""", encoding="utf-8")
    print(f"built release/{version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
