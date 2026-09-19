#!/usr/bin/env python3
"""
Validates lang/*.json so a translation PR cannot break anyone's screen.

Run locally before opening a PR:
    python3 tools/validate_lang.py

CI runs the same check on every PR that touches lang/.

What it enforces, and why:
  - every scenario key the markup can ask for exists, with >= 1 line.
    A missing key renders an empty tip on whatever day the weather
    happens to hit that scenario, which is a bug nobody sees in review.
  - placeholders are spelled correctly and only appear where they work.
    {WHEN2} outside an arc_* key never gets substituted and ships a
    literal "{WHEN2}" to a real device.
  - arc_* lines use {GARMENT} or {GARMENTA}, because those keys are the
    ones whose sentence is about a specific garment.
  - no line is empty, and none contains the '||' or ';;' delimiters that
    the transitional build still uses to inline these strings.
  - the _j (joined) precip forms carry no {WHENP}, since they attach to a
    sentence that already placed its time reference.
"""

import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LANG_DIR = REPO / "lang"

LEVELS = ["0", "10", "11"]

TEMP_KEYS = [
    "perfect",
    "arc_colder", "arc_level", "arc_warmer",
    "w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_sweatshirt", "w_water",
    "c_scarf", "c_coat", "c_jacket", "c_hoodie", "c_sweatshirt", "c_relief",
]
PRECIP_BASE = ["wetter_maybe", "wetter", "wetter_long", "drier", "stays_wet", "snow_coming"]
PRECIP_KEYS = [k + s for k in PRECIP_BASE for s in ("", "_j")]

KNOWN_TOKENS = {"{WHEN}", "{WHEN2}", "{WHENP}", "{GARMENT}", "{GARMENTA}"}
TOKEN_RE = re.compile(r"\{[A-Z0-9_]+\}")

# Keys whose lines carry no time token at all: it is already raining, so the
# sentence is about the umbrella in hand, not about when something starts.
NO_WHENP_KEYS = {"drier", "stays_wet"}

_ENGLISH = None


def load_english():
    """English is the reference every other language is diffed against."""
    global _ENGLISH
    if _ENGLISH is None:
        path = LANG_DIR / "en.json"
        try:
            _ENGLISH = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            _ENGLISH = {}
    return _ENGLISH


def check_lang(path, problems):
    name = path.name
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        problems.append(f"{name}: not valid JSON - {exc}")
        return

    def bad(msg):
        problems.append(f"{name}: {msg}")

    meta = doc.get("meta") or {}
    code = meta.get("code")
    if not code:
        bad("meta.code is required (the two-letter code, matching the filename)")
    elif f"{code}.json" != name:
        bad(f"meta.code {code!r} does not match the filename")
    if not meta.get("name"):
        bad("meta.name is required (the language's name in that language)")

    ui = doc.get("ui") or {}
    for key in ("error_current", "error_hourly", "error_short"):
        if not (ui.get(key) or "").strip():
            bad(f"ui.{key} is required")

    garments = doc.get("garments") or {}
    for case in ("n", "a"):
        vals = garments.get(case)
        if not isinstance(vals, list) or len(vals) != 5:
            bad(f"garments.{case} must be a list of exactly 5 entries "
                "(scarf, coat, jacket, hoodie, sweatshirt)")
        elif any(not str(v).strip() for v in vals):
            bad(f"garments.{case} has an empty entry")
        elif any("," in str(v) for v in vals):
            bad(f"garments.{case} must not contain commas")

    buckets = doc.get("buckets")
    if not isinstance(buckets, list) or len(buckets) != 5:
        bad("buckets must be a list of exactly 5 entries "
            "(morning, midday, afternoon, evening, night)")
    elif any("," in str(v) for v in buckets):
        bad("buckets must not contain commas")

    relative = doc.get("relative")
    if not isinstance(relative, list) or len(relative) != 3:
        bad("relative must be a list of exactly 3 entries (1h, 2h, 3h)")
    elif any("," in str(v) for v in relative):
        bad("relative must not contain commas")

    for level in LEVELS:
        for kind, keys in (("temp", TEMP_KEYS), ("precip", PRECIP_KEYS)):
            section_name = f"{kind}_{level}"
            section = doc.get(section_name)
            if not isinstance(section, dict):
                bad(f"{section_name} is missing")
                continue

            for extra in sorted(set(section) - set(keys)):
                bad(f"{section_name}.{extra} is not a scenario the markup asks for")

            for key in keys:
                lines = section.get(key)
                if not isinstance(lines, list) or not lines:
                    bad(f"{section_name}.{key} must have at least one line")
                    continue

                for i, line in enumerate(lines):
                    where = f"{section_name}.{key}[{i}]"
                    if not isinstance(line, str) or not line.strip():
                        bad(f"{where} is empty")
                        continue
                    if line != line.strip():
                        bad(f"{where} has leading or trailing whitespace")
                    for delim in ("||", ";;"):
                        if delim in line:
                            bad(f"{where} contains the reserved delimiter {delim!r}")

                    tokens = set(TOKEN_RE.findall(line))
                    for tok in sorted(tokens - KNOWN_TOKENS):
                        bad(f"{where} uses unknown placeholder {tok}")

                    if kind == "temp":
                        if "{WHENP}" in tokens:
                            bad(f"{where} uses {{WHENP}}, which only works in precip lines")
                        if "{WHEN2}" in tokens and not key.startswith("arc_"):
                            bad(f"{where} uses {{WHEN2}}, which only resolves for arc_* keys")
                        if key in ("w_water", "c_relief") and (
                            {"{GARMENT}", "{GARMENTA}"} & tokens
                        ):
                            bad(f"{where} names a garment, but this key fires when "
                                "there is no removable layer, so it renders blank")
                    else:
                        if {"{WHEN}", "{WHEN2}"} & tokens:
                            bad(f"{where} uses a temp placeholder; precip lines use {{WHENP}}")
                        if key.endswith("_j") and "{WHENP}" in tokens:
                            bad(f"{where} is a joined fragment and must not use {{WHENP}}")
                        base = key[:-2] if key.endswith("_j") else key
                        if base in NO_WHENP_KEYS and "{WHENP}" in tokens:
                            bad(f"{where} uses {{WHENP}}, but {base} fires while it is "
                                "already raining, so there is no start time to name")

                # The markup falls back to the first line carrying no time
                # token when the forecast cannot resolve one (both hinges land
                # in the same bucket, say). If every line in the key needs a
                # token, that fallback has nothing to reach for and the tip
                # renders with a hole in it.
                if kind == "temp" and any("{WHEN" in ln for ln in lines if isinstance(ln, str)):
                    if not any(
                        isinstance(ln, str) and "{WHEN" not in ln for ln in lines
                    ):
                        bad(f"{section_name}.{key} has no token-free line; "
                            "add one line that reads correctly without a time reference")

    counts = []
    for level in LEVELS:
        for kind in ("temp", "precip"):
            section = doc.get(f"{kind}_{level}") or {}
            counts.append(sum(len(v) for v in section.values() if isinstance(v, list)))
    total = sum(counts)

    # Every key existing is not the same as every key being translated. A
    # straight copy of en.json passes every check above - the keys are all
    # there, the placeholders are all valid - and then ships English
    # sentences to someone who picked another language. Catch the lines that
    # are still byte-identical to the English.
    untranslated = []
    if code and code != "en":
        english = load_english()
        if english:
            allow = set(meta.get("allow_same_as_en") or [])
            for section_name, section in doc.items():
                if not isinstance(section, dict):
                    continue
                if not (section_name.startswith(("temp_", "precip_"))
                        or section_name in ("ui", "garments")):
                    continue
                ref = english.get(section_name)
                if not isinstance(ref, dict):
                    continue
                for key, lines in section.items():
                    ref_lines = ref.get(key)
                    if isinstance(lines, str) and isinstance(ref_lines, str):
                        if lines == ref_lines and f"{section_name}.{key}" not in allow:
                            untranslated.append(f"{section_name}.{key}")
                        continue
                    if not isinstance(lines, list) or not isinstance(ref_lines, list):
                        continue
                    for i, line in enumerate(lines):
                        where = f"{section_name}.{key}[{i}]"
                        if line in ref_lines and where not in allow:
                            untranslated.append(where)

            for section_name in ("buckets", "relative"):
                mine, ref = doc.get(section_name), english.get(section_name)
                if isinstance(mine, list) and isinstance(ref, list):
                    for i, v in enumerate(mine):
                        if v in ref and f"{section_name}[{i}]" not in allow:
                            untranslated.append(f"{section_name}[{i}]")

    if untranslated:
        done = total - len([u for u in untranslated if "[" in u])
        problems.append(
            f"{name}: {len(untranslated)} string(s) still identical to English "
            f"(roughly {max(0, done)}/{total} lines translated).\n"
            "      A partly translated file renders a mix of both languages on the "
            "device.\n"
            "      First few: " + ", ".join(untranslated[:6]) + "\n"
            "      If a string is genuinely the same in this language, list it in "
            'meta.allow_same_as_en.'
        )

    suffix = "" if not untranslated else f", {len(untranslated)} untranslated"
    print(f"  {name}: {total} lines, meta.code={code!r}{suffix}")


def main():
    files = sorted(LANG_DIR.glob("*.json"))
    if not files:
        print("no language files found in lang/", file=sys.stderr)
        return 1

    problems = []
    print(f"checking {len(files)} language file(s):")
    for path in files:
        check_lang(path, problems)

    if problems:
        print(f"\n{len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("\nall language files are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
