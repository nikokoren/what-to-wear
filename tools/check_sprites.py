#!/usr/bin/env python3
"""Every sprite the markup can ask for must exist in the repo.

This exists because two sprite outages shipped unnoticed:

  * `okt` was whitelisted as a themed day for sixteen days a year without
    anyone drawing okt_*.png, so from 09-20 to 10-05 every device rendered
    a 404 and showed the alt text "Outfit" instead of a picture.
  * Band 1 (`extra_cold`) was added to the temperature ladder without its
    artwork, so anyone below -7 got the same broken image all winter.

Both are invisible in review and invisible in testing, because the URL is
only assembled at render time and only for some dates and temperatures.
So: drive the real markup across every theme date and every band, collect
the URLs it actually builds, and check the files on disk.

Renders through `src/shared.liquid` rather than reimplementing the slug
rules, so the check cannot drift away from what ships.

    python3 tools/check_sprites.py [--remote]

`--remote` additionally HEADs each distinct URL, which catches the case
where a file exists locally but was never pushed.
"""

import argparse
import calendar
import datetime as dt
import pathlib
import sys

from liquid import Environment, FileSystemLoader

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from render_test import (  # noqa: E402
    REPO,
    extract_sprite,
    globals_for,
    payload,
    flat,
    render,
    settings,
)

# One apparent temperature per band, from the ladder in SCENARIOS.md.
BANDS = {
    "extra_cold": -12,
    "freezing": 0,
    "cold": 7,
    "cool": 12,
    "mild": 17,
    "warm": 24,
    "hot": 30,
    "very_hot": 35,
}

# Open-Meteo weather codes: clear, rain, snow.
PRECIP = {"dry": 0, "rain": 61, "snow": 73}

# Every date the theme ladder in shared.liquid can fire on, plus one
# ordinary day as a control. Thanksgiving is the fourth Thursday.
THEME_DATES = {
    "ny": ["12-31", "01-01"],
    "ghd": ["02-02"],
    "pi": ["03-14"],
    "force": ["05-04"],
    "bike": ["06-03"],
    "tdf": ["07-01", "07-12", "07-23"],
    "okt": ["09-20", "09-28", "10-05"],
    "spooky": ["10-31"],
    "krampus": ["12-05"],
    "nikolo": ["12-06"],
    "xmas": ["12-24", "12-25"],
    "(none)": ["04-17", "08-08"],
}

YEAR = 2026
UTC_OFFSET = 3600


def thanksgiving(year):
    """Fourth Thursday in November."""
    thursdays = [
        d for d in range(1, 31)
        if dt.date(year, 11, d).weekday() == calendar.THURSDAY
    ]
    return f"11-{thursdays[3]:02d}"


def timestamp_for(md, hour=12):
    month, day = (int(x) for x in md.split("-"))
    local = dt.datetime(YEAR, month, day, hour, tzinfo=dt.timezone.utc)
    return int(local.timestamp()) - UTC_OFFSET


def dated(data, md, hour=12):
    """Move a payload onto a given date.

    The markup derives today_md from current.time when the API supplies it,
    and only falls back to trmnl.system.timestamp_utc when it does not. The
    first version of this script set the timestamp alone, so every render
    silently happened on the shared test date and no themed sprite was ever
    requested. Set both.
    """
    stamp = f"{YEAR}-{md}T{hour:02d}:00"
    data["current"]["time"] = stamp
    data["hourly"]["time"] = [f"{YEAR}-{md}T{h:02d}:00" for h in range(24)]
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--remote", action="store_true",
                    help="also check each URL resolves over the network")
    args = ap.parse_args()

    dates = dict(THEME_DATES)
    dates["thanks"] = [thanksgiving(YEAR)]

    env = Environment(loader=FileSystemLoader(str(REPO / "src")))
    missing = {}   # filename -> set of "theme date band precip" that want it
    seen = set()
    renders = 0

    for theme, mds in sorted(dates.items()):
        for md in mds:
            ts = timestamp_for(md)
            for band, temp in BANDS.items():
                for precip, code in PRECIP.items():
                    data = dated(
                        payload(temp, code, flat(temp), flat(0),
                                flat(code) if code else None),
                        md,
                    )
                    ctx = globals_for(data, None, settings(), "root")
                    ctx["trmnl"]["system"]["timestamp_utc"] = ts
                    html, _ = render(
                        env, "shared.liquid", "views/full.liquid", ctx
                    )
                    renders += 1

                    url = extract_sprite(html)
                    if not url:
                        missing.setdefault("(no src rendered)", set()).add(
                            f"{theme} {md} {band}_{precip}"
                        )
                        continue

                    name = url.rsplit("/", 1)[-1]
                    seen.add(name)
                    if not (REPO / name).exists():
                        missing.setdefault(name, set()).add(
                            f"{theme} {md} {band}_{precip}"
                        )

    print(f"{renders} renders across {sum(len(v) for v in dates.values())} "
          f"dates x {len(BANDS)} bands x {len(PRECIP)} precip states")
    print(f"{len(seen)} distinct sprites requested")

    if args.remote and not missing:
        import urllib.request
        base = ("https://raw.githubusercontent.com/nikokoren/"
                "what-to-wear/refs/heads/main/")
        for name in sorted(seen):
            req = urllib.request.Request(base + name, method="HEAD")
            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    if r.status != 200:
                        missing.setdefault(name, set()).add(
                            f"remote HTTP {r.status}"
                        )
            except Exception as exc:  # noqa: BLE001
                missing.setdefault(name, set()).add(f"remote {exc}")
        print(f"{len(seen)} sprites checked over the network")

    if missing:
        print(f"\n{len(missing)} MISSING SPRITE(S):\n")
        for name, wanters in sorted(missing.items()):
            examples = sorted(wanters)
            print(f"  {name}")
            print(f"      wanted by {len(wanters)} combination(s), e.g. "
                  f"{', '.join(examples[:3])}")
        print("\nEither draw the artwork, or narrow that theme's whitelist "
              "in src/shared.liquid.")
        return 1

    print("\nall good: every sprite the markup can build exists")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
