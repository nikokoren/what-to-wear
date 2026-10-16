#!/usr/bin/env python3
"""
Round 13, seasons and riffs (October 2026).

    python3 review/rounds/make_round13.py

Two writers, one per language, each with notes from a third reader (the
scout) on ideas that work in the other language and haven't been tried in
theirs: riffs on the idea, never translations. Their raw output is in
2026-10-seasons/<lang>.json:

    {"lines": [{"path": "flavour_10.steady", "text": "...",
                "answers": ["fu-en-..."],      # "Write new" spots it answers
                "months": "11,12,01",          # seasonal: only these months
                "garments": ["jacket", "coat"],  # only when the forecast names these
                "three": true,                 # only with three different drawings
                "idea": "E3"}]}                # the scout's note it riffs on

Paths: flavour_10/11.<group> (follow-ups under the forecast line, the ten
groups of round 12), now_10/11.<mood> (alone under the drawing),
flavour_vf_10/11.<mood> (with two or three drawings). Follow-ups in off,
on and offon may say {GP} (the garment's pronoun) or {G} (the garment).

build_pools.py applies it (apply_follow, this round too): kept lines go
in, with their month, garment and three-drawings tags.
"""

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round11 as r11  # noqa: E402
import make_round12 as r12  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-seasons"
LEVEL = {"10": "On", "11": "11"}
GARMENTS = ["scarf", "coat", "jacket", "hoodie"]  # the order of facts.garments
# The Now drawing while a garment is still on (off) or not yet (on).
SPRITE_OFF = {"scarf": "coat_dry", "coat": "coat_dry", "jacket": "jacket_dry", "hoodie": "sweater_dry"}
SPRITE_ON = {"scarf": "coat_dry", "coat": "jacket_dry", "jacket": "sweater_dry", "hoodie": "tee_pants_dry"}
NAMES = {"scarf": "hat and scarf", "coat": "winter coat", "jacket": "jacket", "hoodie": "sweater"}


def garment_fills(lang, text, base, facts, g):
    f = r8.fills(lang, text, base, facts)
    i = GARMENTS.index(g)
    f["{G}"], f["{GP}"] = facts["garments"][i], facts["garments_pron"][i]
    if "garments_verb" in facts:
        f["{GV}"] = facts["garments_verb"][i]
    return f


def months_named(months):
    m = months.split(",")
    return "–".join(dict.fromkeys([r12.MONTH_NAMES[m[0]], r12.MONTH_NAMES[m[-1]]]))


def follow_row(lang, level, group, item, doc, base):
    facts = doc["facts"]
    fkey, sprite, what = r12.GROUP_CTX[group]
    g = (item.get("garments") or ["jacket"])[0]
    if group in ("off", "on"):
        fkey = ("w_" if group == "off" else "c_") + g
        sprite = (SPRITE_OFF if group == "off" else SPRITE_ON)[g]
    elif group == "offon":
        sprite = SPRITE_OFF[g]
    template = facts[fkey][0]
    fills = garment_fills(lang, template, base, facts, g)
    row = {"path": f"flavour_{level}.{group}", "sprite": sprite,
           "fact": r8.sentence_case(r8.fill(template, fills)),
           "batch": f"Follow-up: {group}",
           "meaning": f"New follow-up at {LEVEL[level]}: shows under the forecast line when it says {what}. "
                      "It should pick up what the line says and twist it."}
    if "{G" in item["text"]:
        row["fills"] = {"{G}": fills["{G}"], "{GP}": fills["{GP}"]}
    hints = []
    if group == "night":
        hints.append("Shown from 22:00")
    if item.get("garments"):
        hints.append("Only when the forecast line names: " + ", ".join(NAMES[x] for x in item["garments"]))
    elif "{G" in item["text"]:
        hints.append("The garment fills in from the forecast line")
    return row, hints


def flavour_row(lang, item, doc, base):
    """One writer's row as the review page shows it."""
    text, path = item["text"], item["path"]
    section, key = path.split(".")
    level = section.rsplit("_", 1)[1]
    if "{G" in text and not (section.startswith("flavour_") and key in ("off", "on", "offon")):
        raise SystemExit(f"{lang}: {{G}}/{{GP}} only in off, on, offon follow-ups: {path} {text}")
    for g in item.get("garments") or []:
        if g not in GARMENTS:
            raise SystemExit(f"{lang}: unknown garment {g}: {text}")
    hints = []
    if section.startswith("flavour_vf"):
        sprite, fact, panels = r11.screen(lang, "vf", key, doc, base)
        row = {"path": path, "sprite": sprite, "fact": fact, "batch": "Drawings",
               "meaning": r11.meaning("vf", key, level, new=True)}
        if item.get("three"):
            # three different outfits, the only days it shows
            labels = [p["label"] for p in r11.screen(lang, "vf", "fickle", doc, base)[2]]
            row["sprite"] = "coat_dry"
            row["panels"] = [{"sprite": s, "label": l} for s, l in
                             zip(("coat_dry", "jacket_dry", "tee_pants_dry"), labels)]
            hints.append("Only with three different drawings")
        elif panels:
            row["panels"] = panels
    elif section.startswith("now"):
        sprite, fact, _ = r11.screen(lang, "now", key, doc, base)
        row = {"path": path, "sprite": sprite, "fact": fact, "batch": f"Now: {key}",
               "meaning": r11.meaning("now", key, level, new=True)}
    elif section.startswith("flavour_") and key in r12.GROUP_CTX:
        row, hints = follow_row(lang, level, key, item, doc, base)
    else:
        raise SystemExit(f"{lang}: unknown path {path}")
    row = {"lang": lang, **row, "text": text, "role": "flavour", "new": True}
    if item.get("months"):
        row["months"] = item["months"]
        row["batch"] = "Seasonal"
        hints.insert(0, f"Seasonal: only {months_named(item['months'])}")
    if item.get("garments"):
        row["garments"] = item["garments"]
    if item.get("three"):
        row["three"] = True
    if item.get("answers"):
        row["answers"] = item["answers"]
        hints.append("Answers a “Write new”")
    if item.get("hint"):
        hints.append(item["hint"])
    if item.get("idea"):
        hints.append("A riff on an idea from the other language")
    if hints:
        row["hint"] = " · ".join(hints)
    return row


def voted_already(rnd):
    """A round with votes is history: building it again would drop every line
    that's in the pools now (they all look like duplicates)."""
    return any(d.get("round") == rnd for lang in ("en", "de")
               for d in json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8")).values())


def main():
    if voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        decisions = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        voted = {d["text"] for d in decisions.values()} | {d["edit"] for d in decisions.values() if d.get("edit")}
        existing = {t for s, pools in doc.items() if isinstance(pools, dict) for v in pools.values()
                    if isinstance(v, list) for t in v if isinstance(t, str)}
        raw = json.loads((HERE / ROUND / f"{lang}.json").read_text(encoding="utf-8"))["lines"]
        seen = set()
        for item in raw:
            text, path = item["text"].strip(), item["path"]
            item["text"] = text
            if text in seen or text in existing or text in voted or any(text in e for e in existing):
                print(f"  {lang} skipped, already there: {text}")
                continue
            seen.add(text)
            lines.append(flavour_row(lang, item, doc, base))
    out = {"round": ROUND, "idPrefix": "se", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:20} {n}")
    answered = {a for r in lines for a in r.get("answers", [])}
    for lang in ("en", "de"):
        waiting = (REPO / "review" / "rewrite" / f"{lang}.md").read_text(encoding="utf-8")
        ids = re.findall(r"\*\*Answers:\*\* `([^`]+)`", waiting)
        left = [i for i in ids if i not in answered]
        print(f"  {lang}: {len(left)} of {len(ids)} Write new spots not answered" + (f": {left}" if left else ""))


if __name__ == "__main__":
    main()
