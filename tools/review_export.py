#!/usr/bin/env python3
"""
Builds the review page: every line, rendered the way a device shows it.

    python3 tools/review_export.py                      # all of lang/*.json
    python3 tools/review_export.py --keys perfect,wet_again,wet_again_j
    python3 tools/review_export.py --candidates review/rounds/<round>.json
    python3 tools/review_export.py --out <dir>          # default: build/review

Writes <out>/index.html (review/page.html with the rows embedded) and
copies the sprites it uses to <out>/sprites/, ready to publish as one
artifact. Decisions live in the page's database, not in the page, so
republishing with new rows never loses a vote.

A candidates file is a round of new lines from a writer, reviewed beside
(or instead of) the shipped ones:

    {"round": "2026-11-perfect",
     "lines": [{"lang": "en", "path": "temp_10.perfect", "text": "...",
                "batch": "A"}, ...]}

"batch" is opaque on the page: it is how a blind comparison between two
writers is kept blind. Keep the batch -> writer key out of the file.

Every row carries a stable id: language plus a hash of the text. A line
that moves index keeps its decision; a line whose text changes is a new
line and is reviewed again.
"""

import argparse
import hashlib
import json
import pathlib
import re
import shutil

REPO = pathlib.Path(__file__).resolve().parent.parent
TIP_BUDGET = 165  # src/shared.liquid
PATH_RE = re.compile(r"^((temp|precip|flavour)_(\d+))\.([a-z_]+)$")
PROTO = REPO / "prototypes" / "fact-flavour" / "lang"

# Which drawing each key renders over, and which hinge fills {WHEN}. The
# key fixes the situation (docs/SCENARIOS.md), so one example per key is
# enough to judge a line against what someone actually sees.
TEMP_CTX = {
    "perfect": "sweater", "perfect_evening": "jacket", "perfect_hot": "heat",
    "perfect_cold": "coat", "shorts_early": "tee_shorts",
    "w_scarf": "bundled", "w_coat": "coat", "w_jacket": "jacket",
    "w_hoodie": "sweater", "w_sweatshirt": "sweater", "w_water": "tee_shorts",
    "c_scarf": "coat", "c_coat": "jacket", "c_jacket": "sweater",
    "c_hoodie": "tee_pants", "c_sweatshirt": "tee_pants", "c_relief": "heat",
    "arc_warmer": "jacket", "arc_level": "jacket", "arc_colder": "jacket",
}
THEME_CTX = {
    "theme_ny": "coat", "theme_xmas": "coat", "theme_krampus": "coat",
    "theme_nikolo": "coat", "theme_bike": "tee_shorts", "theme_tdf": "tee_shorts",
    "theme_pi": "jacket", "theme_force": "sweater", "theme_easter": "sweater",
    "theme_ghd": "jacket", "theme_okt": "sweater", "theme_spooky": "jacket",
    "theme_thanks": "jacket",
}
PRECIP_CTX = {
    "wetter": "jacket_rain", "wetter_maybe": "jacket_rain",
    "wetter_long": "jacket_rain", "stays_wet": "jacket_rain",
    "drier": "jacket_rain", "wet_again": "jacket_rain",
    "snow_coming": "coat_snow",
}
# What each key means, one line, shown on the page beside the line.
MEANING = {
    "perfect": "Nothing changes. About half of everything shown.",
    "perfect_evening": "Steady, from 17:00. The day is nearly done.",
    "perfect_hot": "Steady heat (heat or extreme_heat), before 17:00.",
    "perfect_cold": "Steady cold (bundled or coat), before 17:00.",
    "shorts_early": "Shorts drawn on a cool morning that turns into shorts weather.",
    "w_scarf": "Warms up: scarf, hat and gloves come off, coat stays.",
    "w_coat": "Warms up: the winter coat comes off and gets carried.",
    "w_jacket": "Warms up: the jacket comes off.",
    "w_hoodie": "Warms up: the sweater or hoodie comes off.",
    "w_sweatshirt": "Unused since the new outfits.",
    "w_water": "Climbs into heat. Nothing left to take off.",
    "c_scarf": "Cools to bundled: bring scarf, hat, gloves.",
    "c_coat": "Cools to coat weather: bring the winter coat.",
    "c_jacket": "Cools to jacket weather: bring a jacket.",
    "c_hoodie": "Cools to sweater weather: bring a sweater or hoodie.",
    "c_sweatshirt": "Unused since the new outfits.",
    "c_relief": "Heat breaks but stays warm. Relief, nothing to bring.",
    "arc_warmer": "Off {WHEN}, stays off. Don't tell them to carry it.",
    "arc_level": "Off {WHEN}, wanted back {WHEN2}. Keep hold of it.",
    "arc_colder": "Off {WHEN}, back {WHEN2} and not enough. Extra layer.",
    "wetter": "Rain starts, short spell.",
    "wetter_maybe": "Rain is possible, not likely.",
    "wetter_long": "Rain starts and stays.",
    "stays_wet": "Raining now and all day.",
    "drier": "Raining now, stops later.",
    "wet_again": "Raining now, stops, comes back.",
    "snow_coming": "Snow is coming.",
}
LEVEL_NAME = {"0": "Off", "10": "On", "11": "11"}

# Flavour lines (prototypes/fact-flavour) render under a fact line. One
# typical day per mood: the drawing and the fact keys that build its fact.
FLAVOUR_CTX = {
    "nice": ("sweater_dry", ["steady"], "A steady, pleasant day."),
    "mild": ("sweater_dry", ["c_jacket"], "An ordinary day with one change."),
    "cold": ("coat_dry", ["steady_cold"], "Steady cold."),
    "hot": ("tee_shorts_dry", ["w_water"], "Heat building."),
    "wet": ("jacket_rain", ["w_jacket", "p_wetter"], "Rain at some point: coming, possible, or stopping."),
    "snow": ("coat_snow", ["p_snow_coming"], "Snow coming or falling."),
    "fickle": ("jacket_dry", ["arc_level"], "Warms up, then cools again."),
    "evening": ("jacket_dry", ["steady_evening"], "A steady evening, from 18:00."),
}


def line_id(lang, text):
    return lang + "-" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def sentence_case(tip):
    parts = re.split(r"(?<=[.!?]) ", tip)
    return " ".join(p[:1].upper() + p[1:] for p in parts)


def fill(text, doc, garment_rank=3):
    b = doc["buckets"]
    g = garment_rank - 1
    out = (text.replace("{GARMENT}", doc["garments"]["n"][g])
               .replace("{GARMENTA}", doc["garments"]["a"][g])
               .replace("{WHEN2}", b[3])
               .replace("{WHEN}", b[1] if "{WHEN2}" in text else b[2])
               .replace("{WHENP}", b[2]))
    return re.sub(r"  +", " ", out).strip()


def flavour_context(lang, doc, key, text):
    facts = json.loads((PROTO / f"{lang}.json").read_text(encoding="utf-8"))["facts"]
    sprite, fact_keys, meaning = FLAVOUR_CTX.get(key, ("jacket_dry", ["steady"], ""))
    if key.startswith("theme_"):
        meaning = "A seasonal day with nothing else to say."
    b = doc["buckets"]
    fact = " ".join(facts[k] for k in fact_keys)
    fact = (fact.replace("{G}", facts["garments"][2]).replace("{WHEN2}", b[3])
                .replace("{WHEN}", b[1]).replace("{WHENP}", b[2]))
    return {"sprite": sprite, "fact": sentence_case(fact), "tip": text, "pair": None,
            "meaning": "Flavour line. " + meaning}


def context(lang, doc, section, key, text):
    """What the device shows for this line: drawing, full tip, pairing."""
    kind, level = section.split("_")
    if kind == "flavour":
        return flavour_context(lang, doc, key, text)
    base = key[:-2] if key.endswith("_j") else key
    if kind == "temp":
        outfit = TEMP_CTX.get(key) or THEME_CTX.get(key) or "sweater"
        tip = fill(text, doc)
        pair = None
        if not key.startswith(("perfect", "theme_")):
            wet = (doc.get(f"precip_{level}") or {}).get("wetter_j") or []
            if wet:
                pair = sentence_case(tip + " " + fill(wet[0], doc))
        return {"sprite": f"{outfit}_dry", "tip": sentence_case(tip), "pair": pair,
                "meaning": MEANING.get(key, "Seasonal day: words over the usual outfit." if key.startswith("theme_") else "")}
    sprite = PRECIP_CTX.get(base, "jacket_rain")
    if key.endswith("_j"):
        # A joined half never stands alone: show it after a real
        # temperature clause from the same level, the way it renders.
        lead = ((doc.get(f"temp_{level}") or {}).get("w_jacket") or ["The jacket comes off {WHEN}."])[0]
        tip = fill(lead, doc) + " " + fill(text, doc)
        meaning = MEANING.get(base, "") + " Joined after a temperature line."
    else:
        tip = fill(text, doc)
        meaning = MEANING.get(base, "") + " On its own, on a steady day."
    return {"sprite": sprite, "tip": sentence_case(tip), "pair": None, "meaning": meaning.strip()}


def rows_from_lang(keys):
    rows = []
    for path in sorted((REPO / "lang").glob("*.json")):
        lang = path.stem
        doc = json.loads(path.read_text(encoding="utf-8"))
        for section, block in doc.items():
            if not section.startswith(("temp_", "precip_")):
                continue
            for key, lines in block.items():
                if keys and key not in keys:
                    continue
                for i, text in enumerate(lines):
                    rows.append(row(lang, doc, section, key, text, f"{section}.{key}[{i}]", "shipped", ""))
    return rows


def rows_from_candidates(cand_path):
    data = json.loads(pathlib.Path(cand_path).read_text(encoding="utf-8"))
    docs = {}
    rows = []
    for c in data["lines"]:
        lang = c["lang"]
        if lang not in docs:
            docs[lang] = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        m = PATH_RE.match(c["path"])
        if not m:
            raise SystemExit(f"bad candidate path {c['path']!r}: want e.g. temp_10.perfect")
        section, key = m.group(1), m.group(4)
        rows.append(row(lang, docs[lang], section, key, c["text"], c["path"] + "[+]",
                        "candidate", c.get("batch", "")))
    # Interleave the batches, the same way on every build, so no writer's
    # lines arrive as a block.
    rows.sort(key=lambda r: (r["lang"], r["key"], r["level"], r["id"]))
    return rows, data.get("round", "")


def row(lang, doc, section, key, text, path, source, batch):
    level = section.split("_")[1]
    ctx = context(lang, doc, section, key, text)
    return {
        "id": line_id(lang, text), "lang": lang, "level": level,
        "levelName": LEVEL_NAME.get(level, level), "key": key, "path": path,
        "text": text, "source": source, "batch": batch,
        # A flavour line sits under its fact line; the mock fits 200 together.
        "tooLong": (len(ctx["fact"]) + 1 + len(ctx["tip"]) > 200) if ctx.get("fact")
                   else len(ctx["tip"]) > TIP_BUDGET,
        **ctx,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keys", default="")
    ap.add_argument("--candidates")
    ap.add_argument("--only-candidates", action="store_true")
    ap.add_argument("--focus", default="", help="key the page opens on")
    ap.add_argument("--out", default=str(REPO / "build" / "review"))
    a = ap.parse_args()

    keys = {k for k in a.keys.split(",") if k}
    rows, round_name = [], ""
    if not a.only_candidates:
        rows += rows_from_lang(keys)
    if a.candidates:
        cand, round_name = rows_from_candidates(a.candidates)
        rows += cand

    seen, unique = set(), []
    for r in rows:
        if r["id"] not in seen:
            seen.add(r["id"])
            unique.append(r)

    out = pathlib.Path(a.out)
    (out / "sprites").mkdir(parents=True, exist_ok=True)
    for sprite in sorted({r["sprite"] for r in unique}):
        shutil.copy(REPO / "sprites" / f"{sprite}.png", out / "sprites" / f"{sprite}.png")

    payload = json.dumps({"round": round_name, "focus": a.focus, "rows": unique}, ensure_ascii=False)
    payload = payload.replace("</", "<\\/")
    page = (REPO / "review" / "page.html").read_text(encoding="utf-8")
    (out / "index.html").write_text(page.replace("/*ROWS*/null", payload), encoding="utf-8")
    print(f"{len(unique)} lines, {len({r['sprite'] for r in unique})} sprites -> {out}/index.html")


if __name__ == "__main__":
    main()
