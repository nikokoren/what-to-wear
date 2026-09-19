#!/usr/bin/env python3
"""
One-shot migration helper.

Reads the embedded text libraries out of the pre-refactor shared markup
(src/shared.liquid as committed in the first commit of this branch) and
writes them out as lang/<code>.json.

The point of doing this with a script rather than by hand is fidelity: the
strings that ship to devices are byte-for-byte the ones that shipped before,
so the refactor cannot quietly reword anything.

Usage:  python3 tools/extract_texts.py <path-to-old-shared.liquid>
"""

import json
import pathlib
import re
import sys

# Scenario keys that the markup can ask a temp library for.
TEMP_KEYS = [
    "perfect",
    "arc_colder", "arc_level", "arc_warmer",
    "w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_sweatshirt", "w_water",
    "c_scarf", "c_coat", "c_jacket", "c_hoodie", "c_sweatshirt", "c_relief",
]

# Precip scenarios exist in a standalone and a joined ("_j") form.
PRECIP_BASE = [
    "wetter_maybe", "wetter", "wetter_long", "drier", "stays_wet", "snow_coming",
]
PRECIP_KEYS = [k + suffix for k in PRECIP_BASE for suffix in ("", "_j")]

LEVELS = ["0", "10", "11"]
LANGS = ["en", "de"]

# Strings that live outside the capture blocks but are still translator-owned.
UI = {
    "en": {
        "error_current": "Unable to retrieve weather data. Please try again later.",
        "error_hourly": "Unable to load forecast data. Please try again later.",
        "error_short": "Could not read weather data",
    },
    "de": {
        "error_current": "Wetterdaten konnten nicht abgerufen werden. Bitte versuche es später erneut.",
        "error_hourly": "Wettervorhersage konnte nicht geladen werden. Bitte versuche es später erneut.",
        "error_short": "Wetterdaten konnten nicht gelesen werden",
    },
}

GARMENTS = {
    "en": {
        "n": ["The scarf", "The coat", "The jacket", "The hoodie", "The sweatshirt"],
        "a": ["the scarf", "the coat", "the jacket", "the hoodie", "the sweatshirt"],
    },
    "de": {
        "n": ["Der Schal", "Die Winterjacke", "Die Jacke", "Der Hoodie", "Der Pulli"],
        "a": ["den Schal", "die Winterjacke", "die Jacke", "den Hoodie", "den Pulli"],
    },
}

BUCKETS = {
    "en": ["this morning", "around midday", "this afternoon", "this evening", "tonight"],
    "de": ["heute Vormittag", "gegen Mittag", "heute Nachmittag", "heute Abend", "heute Nacht"],
}

RELATIVE = {
    "en": ["in an hour", "in two hours", "in three hours"],
    "de": ["in einer Stunde", "in zwei Stunden", "in drei Stunden"],
}

LANG_NAMES = {"en": "English", "de": "Deutsch"}

CAPTURE = re.compile(
    r"\{%-?\s*capture\s+(\w+)\s*-?%\}(.*?)\{%-?\s*endcapture\s*-?%\}",
    re.DOTALL,
)


def parse_library(blob):
    """Turn 'key::a||b;;key2::c' into {'key': ['a','b'], 'key2': ['c']}.

    Mirrors the Liquid the markup used to run: split on ';;', strip each
    entry, split once on '::', split the remainder on '||'.
    """
    out = {}
    for entry in blob.split(";;"):
        entry = entry.strip()
        if not entry:
            continue
        if "::" not in entry:
            raise ValueError(f"entry has no '::' separator: {entry[:60]!r}")
        key, _, lines = entry.partition("::")
        key = key.strip()
        if key in out:
            raise ValueError(f"duplicate key {key!r}")
        out[key] = [ln for ln in lines.split("||")]
    return out


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2

    source = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    captures = {name: body for name, body in CAPTURE.findall(source)}

    expected = {
        f"{kind}_{level}_{lang}"
        for kind in ("temp", "precip")
        for level in LEVELS
        for lang in LANGS
    }
    missing = expected - captures.keys()
    if missing:
        raise SystemExit(f"missing capture blocks: {sorted(missing)}")

    repo = pathlib.Path(__file__).resolve().parent.parent
    problems = []

    for lang in LANGS:
        doc = {
            "$schema": "../lang/schema.json",
            "meta": {
                "code": lang,
                "name": LANG_NAMES[lang],
                "schema": 1,
            },
            "ui": UI[lang],
            "garments": GARMENTS[lang],
            "buckets": BUCKETS[lang],
            "relative": RELATIVE[lang],
        }

        for level in LEVELS:
            temp = parse_library(captures[f"temp_{level}_{lang}"])
            precip = parse_library(captures[f"precip_{level}_{lang}"])

            for key in TEMP_KEYS:
                if key not in temp:
                    problems.append(f"{lang} temp_{level}: missing key {key}")
            for key in PRECIP_KEYS:
                if key not in precip:
                    problems.append(f"{lang} precip_{level}: missing key {key}")

            doc[f"temp_{level}"] = {k: temp[k] for k in TEMP_KEYS if k in temp}
            doc[f"precip_{level}"] = {k: precip[k] for k in PRECIP_KEYS if k in precip}

        target = repo / "lang" / f"{lang}.json"
        target.write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {target.relative_to(repo)}  ({target.stat().st_size:,} bytes)")

    if problems:
        print("\nGaps carried over from the original markup:")
        for p in problems:
            print(f"  - {p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
