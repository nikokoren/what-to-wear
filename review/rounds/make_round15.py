#!/usr/bin/env python3
"""
Round 15, polish (October 2026).

    python3 review/rounds/make_round15.py

After round 14: the "Write new" spots, the big-swing wordings again (soft
and short, the owner keeps the shorts suggestion), wordings that say when
the rain stops ({WHENSTOP}), storm and ice wordings that lead with the
danger, and follow-ups for the groups still under three lines. One writer
per language, raw output in 2026-10-polish/<lang>.json, round 14's format.

Only new lines go on the page. build_pools.py applies it as round 14:
apply_facts for the wordings, apply_follow for the rest.
"""

import json
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402
import make_round14 as r14  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-polish"
# New placeholders a situation may take this round: when it stops.
STOP_KEYS = ("p_drier", "p_wet_again")


DAY_CTX = {
    "theme_ghd": "Groundhog Day, 2 February", "theme_pi": "Pi Day, 14 March", "theme_easter": "Easter Sunday",
    "theme_force": "Star Wars Day, 4 May", "theme_bike": "World Bicycle Day, 3 June",
    "theme_tdf": "the Tour de France, 1 to 23 July (every steady day for three weeks)",
    "theme_okt": "Oktoberfest, 20 September to 5 October",
    "day_monday": "Monday mornings, before noon", "day_friday": "Friday afternoons, from noon",
    "day_dst_spring": "the Sunday the clocks go forward, and the Monday after",
    "day_dst_fall": "the Sunday the clocks go back, and the Monday after",
    "day_longest": "the longest day of the year", "day_shortest": "the shortest day of the year",
}


def special_row(lang, item, doc, base):
    """A theme day or special day line: on a steady day, under "works all
    day", or alone under the drawing (round 16)."""
    section, key = item["path"].split(".")
    level = section.rsplit("_", 1)[1]
    facts = doc["facts"]
    fact = r8.sentence_case(r8.fill(facts["steady"][0], r8.fills(lang, facts["steady"][0], base, facts)))
    when = DAY_CTX.get(key, key)
    row = {"lang": lang, "path": item["path"], "text": item["text"], "role": "flavour", "new": True,
           "sprite": "sweater_dry", "fact": fact, "batch": ("Theme: " if key.startswith("theme_") else "Day: ") + key.split("_", 1)[1],
           "meaning": f"New sarcastic line at {r13.LEVEL[level]}: {when}. "
                      "Shows on a day whose weather doesn't change, under \"works all day\" or alone under the drawing."}
    hints = ["Every other hour on the day"] if key.startswith("day_") else []
    if item.get("answers"):
        row["answers"] = item["answers"]
        hints.append("Answers a “Write new”")
    if hints:
        row["hint"] = " · ".join(hints)
    return row


def main(rnd=ROUND, prefix="po"):
    if r13.voted_already(rnd):
        raise SystemExit(f"{rnd} has votes; not rebuilding it")
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        decisions = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        voted = {d["text"] for d in decisions.values()} | {d["edit"] for d in decisions.values() if d.get("edit")}
        facts = doc["facts"]
        existing = {t for s, pools in doc.items() if isinstance(pools, dict) and s != "facts"
                    for v in pools.values() if isinstance(v, list) for t in v if isinstance(t, str)}
        seen = set()
        for item in json.loads((HERE / rnd / f"{lang}.json").read_text(encoding="utf-8"))["lines"]:
            text = item["text"] = item["text"].strip()
            if text in seen or text in voted or text in existing:
                print(f"  {lang} skipped, already there: {text}")
                continue
            seen.add(text)
            if item["path"].split(".")[1].startswith(("theme_", "day_")):
                lines.append(special_row(lang, item, doc, base))
                continue
            if not item["path"].startswith("fact_0."):
                lines.append(r13.flavour_row(lang, item, doc, base))
                continue
            key = item["path"].split(".", 1)[1]
            if key not in facts or key not in r14.FACT_CTX:
                raise SystemExit(f"{lang}: unknown forecast key {key}")
            if text in facts[key]:
                continue
            allowed = set(re.findall(r"\{[A-Z0-9]+\}", "".join(facts[key])))
            if key.startswith(STOP_KEYS):
                allowed |= {"{WHENSTOP}", "{WHENP}"}
            extra = set(re.findall(r"\{[A-Z0-9]+\}", text)) - allowed
            if extra:
                raise SystemExit(f"{lang} {key}: placeholder {sorted(extra)} not allowed here: {text}")
            sprite, _, meaning = r14.FACT_CTX[key]
            group = r14.follow_group(key)
            fills = r8.fills(lang, text, base, facts)
            hints = ["New wording"]
            if "{WHENSTOP}" in text:
                hints.append("Says when it stops; only shows when there's a stop time")
            if key.startswith("p_") and len(text) > 100:
                hints.append(f"Long ({len(text)} characters): after a temperature sentence it may not fit")
            if item.get("answers"):
                hints.append("Answers a “Write new”")
            lines.append({"lang": lang, "path": f"fact_0.{key}", "text": text, "role": "fact", "new": True,
                          **({"answers": item["answers"]} if item.get("answers") else {}),
                          "batch": f"Forecast: {r14.FAMILY[group]}", "sprite": sprite,
                          "fills": fills, "fillsAlt": r8.fills(lang, text, base, facts, alt=True),
                          "under": r14.under_line(doc, group, fills),
                          "meaning": "Forecast line, the same at every sarcasm level. " + meaning,
                          "hint": " · ".join(hints)})
    out = {"round": rnd, "idPrefix": prefix, "lines": lines}
    path = HERE / f"{rnd}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:26} {n}")
    answered = {a for r in lines for a in r.get("answers", [])}
    for lang in ("en", "de"):
        waiting = (REPO / "review" / "rewrite" / f"{lang}.md").read_text(encoding="utf-8")
        ids = re.findall(r"\*\*Answers:\*\* `([^`]+)`", waiting)
        left = [i for i in ids if i not in answered]
        print(f"  {lang}: {len(left)} of {len(ids)} Write new spots not answered" + (f": {left}" if left else ""))


if __name__ == "__main__":
    main()
