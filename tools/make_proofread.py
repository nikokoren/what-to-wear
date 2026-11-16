#!/usr/bin/env python3
"""
The proofreading page (owner, October 2026): every live text of one
language, for a native speaker to flag what doesn't sound right or isn't
grammatical, with a suggestion; a second tab shows the flags for the
owner to take or leave.

    python3 tools/make_proofread.py de      # writes review/proofread.html

The flags live in the page's database (collection "flags", one document
per flagged line, keyed by the line's id), so the page can be rebuilt
with new texts without losing them. Apply taken suggestions with
build_pools.py like any other edit.
"""

import hashlib
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
TEXTS = REPO / "prototypes" / "fact-flavour" / "lang"
OUT = REPO / "review" / "proofread.html"
TEMPLATE = REPO / "review" / "proofread.template.html"

# What the screen puts in for a placeholder; the page marks these words.
FILL = {
    "de": {"{GV}": "kann die Jacke", "{GP}": "sie", "{G}": "die Jacke", "{WHEN}": "heute Nachmittag",
           "{WHEN2}": "heute Abend", "{WHENP}": "am Nachmittag", "{WHENSTOP}": "gegen 16 Uhr"},
    "en": {"{GV}": "the jacket can", "{GP}": "it", "{G}": "the jacket", "{WHEN}": "this afternoon",
           "{WHEN2}": "this evening", "{WHENP}": "this afternoon", "{WHENSTOP}": "around 4 pm"},
}
TAG = re.compile(r"^((?:\{M:[^}]*\}|\{W:[^}]*\}|\{3\}|\{AM\})*)")

GROUP_DE = {
    "cold": "kalt", "hot": "warm", "scorch": "Hitze", "rain": "Regen", "snow": "Schnee", "ice": "Glätte",
    "storm": "Gewitter", "steady": "bleibt gleich", "off": "eine Schicht kann weg", "on": "eine Schicht kommt dazu",
    "offon": "weg und wieder an", "shorts": "kurze Hose", "pants": "lange Hose", "evening": "Abend",
    "night": "spät nachts", "nice": "schönes Wetter", "cool": "kühl", "wet": "nass", "fickle": "wechselhaft",
    "cooling": "wird kälter", "warming": "wird wärmer",
}
DAY_DE = {
    "day_monday": "Montagmorgen", "day_friday": "Freitagnachmittag", "day_dst_fall": "Zeitumstellung (Herbst)",
    "day_dst_spring": "Zeitumstellung (Frühling)", "day_longest": "längster Tag", "day_shortest": "kürzester Tag",
    "theme_xmas": "Weihnachten", "theme_ny": "Neujahr", "theme_easter": "Ostern", "theme_spooky": "Halloween",
    "theme_okt": "Oktoberfest", "theme_nikolo": "Nikolaus", "theme_krampus": "Krampus", "theme_ghd": "Murmeltiertag",
    "theme_force": "Star-Wars-Tag", "theme_pi": "Pi-Tag", "theme_tdf": "Tour de France", "theme_bike": "Weltfahrradtag",
    "theme_thanks": "Thanksgiving",
}


def fact_label(key):
    """A German name for a forecast situation."""
    if key == "steady_special":
        return "Sondertag: fester Satz"
    if key == "heat_danger":
        return "gefährliche Hitze"
    kind = ("Schnee" if "snow" in key else "Glätte" if "ice" in key else "Gewitter" if "storm" in key else "Regen")
    if key.startswith("p_"):
        what = {"p_wetter_maybe": "vielleicht später", "p_wetter_long": "kommt und bleibt", "p_wetter": "kommt später",
                "p_snow_coming": "kommt später", "p_stays_wet": "den ganzen Tag", "p_drier": "hört auf",
                "p_wet_again": "Pause, dann wieder"}
        for k, v in what.items():
            if key.startswith(k):
                return f"{kind}: {v}"
    if key.startswith("steady"):
        return {"steady": "bleibt den ganzen Tag gleich", "steady_cold": "bleibt kalt", "steady_hot": "bleibt heiß",
                "steady_evening": "bleibt gleich (abends)", "steady_night": "bleibt gleich (nachts)"}.get(key, key)
    garment = {"scarf": "Schal", "coat": "Winterjacke", "jacket": "Jacke", "hoodie": "Pulli", "water": "Wasser"}
    if key[:2] in ("w_", "c_"):
        g = garment.get(key[2:])
        if key == "c_relief":
            return "Hitze lässt nach"
        if key == "w_water":
            return "wird heiß: genug trinken"
        return (f"wird wärmer: {g} kann weg" if key.startswith("w_") else f"wird kälter: {g} dazu")
    return {"arc_warmer": "Schicht weg, bleibt weg", "arc_level": "Schicht weg, abends wieder an",
            "arc_colder": "Schicht weg, abends wieder an plus mehr", "shorts_early": "später warm genug für kurze Hosen",
            "shorts_swing": "kurze Hose möglich, wird wieder kühl", "shorts_swing_back": "kurz warm, dann wieder kühl",
            "pants_swing": "lange Hose"}.get(key, key)


def kind_of(section, key):
    if section == "facts":
        return "Vorhersage", fact_label(key)
    if section.startswith("units"):
        return "Vorhersage + Witz", fact_label(key)
    if key.startswith(("day_", "theme_")):
        return "Sondertag", DAY_DE.get(key, key)
    if section.startswith("flavour_vf"):
        return "Unter den Zeichnungen", GROUP_DE.get(key, key)
    if section.startswith("now"):
        return "Wetter jetzt", GROUP_DE.get(key, key)
    if section.startswith("alone"):
        return "Allein", GROUP_DE.get(key, key)
    return "Witz zur Vorhersage", GROUP_DE.get(key, key)


def lines(lang):
    doc = json.loads((TEXTS / f"{lang}.json").read_text(encoding="utf-8"))
    out = []
    for section, pools in doc.items():
        if not isinstance(pools, dict) or section.startswith("topical"):
            continue
        level = section.rsplit("_", 1)[1] if section != "facts" else ""
        for key, pool in pools.items():
            if key.startswith("garments") or not isinstance(pool, list):
                continue
            for live in pool:
                if not isinstance(live, str):
                    continue
                tags = TAG.match(live).group(1)
                text = live[len(tags):]
                where = f"{section}.{key}"
                kind, label = kind_of(section, key)
                lid = hashlib.sha1(f"{lang}|{where}|{text}".encode()).hexdigest()[:14]
                fact, sep, joke = text.partition(" || ")
                out.append({"id": f"{lang}-{lid}", "where": where, "text": text, "kind": kind, "label": label,
                            "level": level, "fact": fact if sep else "", "joke": joke if sep else text,
                            "seasonal": "{M:" in tags, "morning": "{AM}" in tags})
    return out


def main():
    lang = sys.argv[1] if len(sys.argv) > 1 else "de"
    data = {"lang": lang, "fill": FILL[lang], "lines": lines(lang)}
    page = TEMPLATE.read_text(encoding="utf-8").replace("/*DATA*/null", json.dumps(data, ensure_ascii=False))
    OUT.write_text(page, encoding="utf-8")
    print(f"{len(data['lines'])} {lang} lines -> {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
