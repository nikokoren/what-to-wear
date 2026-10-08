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
    assert_engine,
    extract_sprite,
    globals_for,
    payload,
    flat,
    render,
    settings,
)

# One apparent temperature per outfit, from BAND_EDGES in src/shared.liquid.
BANDS = {
    "bundled": -10,
    "coat": 0,
    "jacket": 8,
    "sweater": 15,
    "tee_pants": 21,
    "tee_shorts": 27,
    "heat": 32,
    "extreme_heat": 37,
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


def easter(year):
    """Easter Sunday, anonymous Gregorian computus - the same arithmetic as
    the markup, written independently so the two can be checked against
    each other (tools/logic_test.py does)."""
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, day = divmod(h + l - 7 * m + 114, 31)
    return f"{month:02d}-{day + 1:02d}"


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
    assert_engine()

    dates = dict(THEME_DATES)
    dates["thanks"] = [thanksgiving(YEAR)]
    dates["easter"] = [easter(YEAR)]

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

                    # repo-relative path: sprites/<slug>.png, or 404.png
                    name = url.split("/refs/heads/main/", 1)[1]
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
                "what-to-wear/refs/heads/main/")  # + sprites/<slug>.png
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

    # Drawing progress: a new sprite still byte-identical to an old
    # root-level drawing is a placeholder copied in to keep the set
    # rendering until the real artwork lands.
    import hashlib
    digest = lambda f: hashlib.md5(f.read_bytes()).hexdigest()
    legacy = {digest(f): f.name for f in REPO.glob("*.png")}
    placeholders = [
        (f.name, legacy[digest(f)])
        for f in sorted((REPO / "sprites").glob("*.png"))
        if digest(f) in legacy
    ]
    if placeholders:
        print(f"\n{len(placeholders)} sprite(s) still a placeholder copy of old art:")
        for new, old in placeholders:
            print(f"  sprites/{new:24} (copy of {old})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
