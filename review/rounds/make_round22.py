#!/usr/bin/env python3
"""
Round 22, the read-through (October 2026).

    python3 review/rounds/make_round22.py

The owner, before release: every live 2.0 text once more, in both
languages, with the lines already starred in an earlier round marked on
the page ("starred": a gold badge and frame, and the "Earlier vote"
filter). Forecast wordings, follow-ups, the lines for the drawings, now
and standalone lines, units, theme and special days. Not the topical
lines (their own skill) and not the old one-line pools.

build_pools.py applies the votes last of all rounds: a veto or "Write
new" takes the line out (a forecast situation keeps its last wording),
an edit replaces it, keep and star leave it.
"""

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round14 as r14  # noqa: E402
import make_round15 as r15  # noqa: E402
import make_round18 as r18  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-final"
TAG = re.compile(r"^((?:\{M:[^}]*\}|\{W:[^}]*\}|\{3\}|\{AM\})*)(.*)$", re.S)
SECTIONS = ("flavour_10", "flavour_11", "flavour_vf_10", "flavour_vf_11", "now_10", "now_11",
            "alone_10", "alone_11", "units_10", "units_11")


def split_tags(live):
    tags, text = TAG.match(live).groups()
    item = {"text": text}
    m = re.search(r"\{M:([^}]*)\}", tags)
    if m:
        item["months"] = m.group(1)
    w = re.search(r"\{W:([^}]*)\}", tags)
    if w:
        item["garments"] = w.group(1).split(",")
    if "{3}" in tags:
        item["three"] = True
    return item


def starred_texts(lang):
    dec = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
    out = set()
    for d in dec.values():
        if d.get("verdict") == "star":
            out.add(d["text"])
            if d.get("edit"):
                out.add(d["edit"])
    # A starred line reworded since (US spelling, the owner's notes) keeps its star.
    import build_pools as bp
    for s in list(out):
        new = s
        for old, repl in bp.WORDS.get(lang, []):
            new = new.replace(old, repl).replace(old.capitalize(), repl.capitalize())
        fact, sep, joke = new.partition(" || ")
        new = bp.NOTES_REWRITE.get(lang, {}).get(fact, fact) + sep + joke
        out.add(new)
    return out


def fact_row(lang, key, text, doc, base):
    facts = doc["facts"]
    sprite, _, meaning = r14.FACT_CTX.get(key) or ("sweater_dry", "", "The fixed sentence for a theme or special day.")
    group = r14.follow_group(key)
    fills = r8.fills(lang, text, base, facts)
    return {"lang": lang, "path": f"fact_0.{key}", "text": text, "role": "fact",
            "batch": f"Forecast: {r14.FAMILY.get(group, 'other')}", "sprite": sprite,
            "fills": fills, "fillsAlt": r8.fills(lang, text, base, facts, alt=True),
            "under": r14.under_line(doc, group, fills),
            "meaning": "Forecast line, the same at every sarcasm level. " + meaning}


def row_for(lang, section, key, live, doc, base):
    item = split_tags(live)
    item["path"] = f"{section.replace('units_', 'unit_')}.{key}"
    if section.startswith("units_"):
        row = r18.unit_row(lang, item, doc, base)
    elif key.startswith(("day_", "theme_")):
        row = r15.special_row(lang, item, doc, base)
    elif section.startswith("alone_"):
        level = section.rsplit("_", 1)[1]
        sprite = {"warming": "sweater_dry", "cooling": "jacket_dry", "fickle": "jacket_dry"}.get(key) or r13.r11.NOW_SPRITE[key]
        row = {"lang": lang, "path": item["path"], "text": item["text"], "role": "flavour", "sprite": sprite, "fact": "",
               "batch": f"Alone: {key}",
               "meaning": f"Standalone line at {r13.LEVEL[level]} for a {key} day, under the outfit with no forecast line."}
        if item.get("months"):
            row["months"] = item["months"]
            row["hint"] = "Seasonal: only " + r13.months_named(item["months"])
    else:
        row = r13.flavour_row(lang, item, doc, base)
    row.pop("new", None)
    row.pop("hint", None) if row.get("hint", "").startswith("Answers") else None
    return row


def live_rows(lang):
    """Every live 2.0 text of a language as review rows, starred ones marked."""
    doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
    base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
    stars = starred_texts(lang)
    lines, seen = [], {}
    for key, wordings in doc["facts"].items():
        if key.startswith("garments") or not isinstance(wordings, list):
            continue
        for w in wordings:
            item = split_tags(w)
            lines.append(dict(fact_row(lang, key, item["text"], doc, base), live=w, where=[f"facts.{key}"]))
    for section in SECTIONS:
        for key, pool in doc.get(section, {}).items():
            for live in pool:
                where = f"{section}.{key}"
                if (live, where) in seen:
                    continue
                seen[(live, where)] = True
                row = row_for(lang, section, key, live, doc, base)
                lines.append(dict(row, live=live, where=[where]))
    for r in lines:
        if r["text"] in stars or r["live"] in stars:
            r["starred"] = True
        if r["live"].startswith("{AM}") or "{AM}" in r["live"][:20]:
            r["hint"] = ((r.get("hint") or "") + " · Only before noon").lstrip(" ·")
    return lines


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = live_rows("en") + live_rows("de")
    out = {"round": ROUND, "idPrefix": "fn", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for lang in ("en", "de"):
        mine = [r for r in lines if r["lang"] == lang]
        print(f"{lang}: {len(mine)} lines, {sum(1 for r in mine if r.get('starred'))} starred before")

if __name__ == "__main__":
    main()
