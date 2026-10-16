#!/usr/bin/env python3
"""
Round 14, replies and forecast wordings (October 2026).

    python3 review/rounds/make_round14.py

Round 13's lesson: the sarcastic lines that land are short replies to the
forecast line. One writer per language (no riffs this time), raw output
in 2026-10-replies/<lang>.json, in round 13's format plus forecast
wordings ("path": "fact_0.<key>"):

- Every forecast wording in the pools, back for a vote ("Forecast: …"),
  with the new wordings next to them. Veto or Write new takes a wording
  out (never a situation's last one); an edit replaces it.
- Follow-ups for the thin groups, and new lines for the "Write new" spots.

build_pools.py applies it: apply_facts for the wordings, apply_follow for
the sarcastic lines.
"""

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round13 as r13  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-replies"
# The big swing (October 2026): a cold morning, three hours or more of
# shorts weather later. New situations, so they're not in round 8's list.
FACT_CTX = dict(r8.FACT_CTX, **{
    "shorts_swing": ("coat_dry", "warming", "New: a cold morning with three hours or more of shorts weather later "
                     "(a reader in Colorado). The drawing keeps the coat; go out in shorts anyway."),
    "shorts_swing_back": ("coat_dry", "fickle", "New: the same, and the evening wants a layer back. "
                          "{WHEN} is shorts weather, {WHEN2} the layer."),
    "pants_swing": ("tee_pants_dry", "cooling", "New: a cold front. Shorts weather now, three hours or more of coat "
                    "weather later: long pants at the door."),
    "heat_danger": ("extreme_heat_dry", "hot", "New: dangerous heat, above 34 C feels-like for two hours or more. "
                    "Leads with water and shade, whatever else the day does."),
})
# Freezing rain (an ice warning) and thunderstorms: variants of the six rain
# situations, shown when the window has those weather codes.
for base, (sprite, mood, meaning) in list(r8.FACT_CTX.items()):
    if base.startswith("p_") and "snow" not in base:
        FACT_CTX[base + "_ice"] = (sprite, mood, "New: freezing rain, the ice warning. " + meaning)
        FACT_CTX[base + "_storm"] = (sprite, mood, "New: a thunderstorm. " + meaning)
r13.r12.GROUP_CTX.update({
    "shorts": ("shorts_swing", "coat_dry", "go out in shorts on a cold morning: shorts weather later"),
    "pants": ("pants_swing", "tee_pants_dry", "long pants on a shorts morning: a cold front later"),
    "scorch": ("heat_danger", "extreme_heat_dry", "dangerous heat: water and shade. Never undercut the advice"),
    "ice": ("p_wetter_ice", "jacket_dry", "freezing rain: icy roads and pavements. Never undercut the advice"),
    "storm": ("p_wetter_storm", "jacket_dry", "a thunderstorm: the umbrella, inside while it thunders"),
})


def follow_group(key):
    """The follow-up group that sits under a forecast wording (block.liquid, fu_key)."""
    if key.startswith("p_"):
        return "ice" if key.endswith("_ice") else "storm" if key.endswith("_storm") else \
            "snow" if "snow" in key else "rain"
    return {"steady": "steady", "steady_evening": "evening", "steady_hot": "hot", "w_water": "hot",
            "steady_cold": "cold", "arc_warmer": "off", "shorts_early": "off", "shorts_swing": "shorts",
            "shorts_swing_back": "shorts", "pants_swing": "pants", "heat_danger": "scorch",
            "arc_level": "offon", "arc_colder": "offon"}.get(key) or \
        ("off" if key.startswith("w_") else "on" if key.startswith("c_") and key != "c_relief" else None)


FAMILY = {"shorts": "big swings", "pants": "big swings", "scorch": "heat", "ice": "ice", "storm": "storms", "steady": "steady", "evening": "steady", "hot": "heat", "cold": "steady", "off": "a layer comes off",
          "on": "a layer goes on", "offon": "off, then on", "rain": "rain", "snow": "snow", None: "heat"}


def under_line(doc, group, fills):
    """A live follow-up for the screen under a wording: an untagged one if there is one."""
    pool = doc["flavour_10"].get(group) or [] if group else []
    plain = [t for t in pool if not t.startswith("{")] or pool
    if not plain:
        return ""
    text = re.sub(r"^(\{[^}]*\})+", "", plain[0])
    return text.replace("{GP}", fills.get("{GP}", "")).replace("{G}", fills.get("{G}", ""))


def main():
    if r13.voted_already(ROUND):
        raise SystemExit(f"{ROUND} has votes; not rebuilding it")
    earlier = r8.earlier_votes()
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        decisions = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        voted = {d["text"] for d in decisions.values()} | {d["edit"] for d in decisions.values() if d.get("edit")}
        facts = doc["facts"]
        raw = json.loads((HERE / ROUND / f"{lang}.json").read_text(encoding="utf-8"))["lines"]
        new_facts = {}
        flavour = []
        for item in raw:
            item["text"] = item["text"].strip()
            if item["path"].startswith("fact_0."):
                key = item["path"].split(".", 1)[1]
                if key not in facts:
                    raise SystemExit(f"{lang}: unknown forecast key {key}")
                if item["text"] in facts[key] or item["text"] in voted:
                    print(f"  {lang} skipped, already there: {item['text']}")
                    continue
                new_facts.setdefault(key, []).append(item["text"])
            else:
                flavour.append(item)
        for key, (sprite, _, meaning) in FACT_CTX.items():
            group = follow_group(key)
            for text in facts.get(key, []) + new_facts.get(key, []):
                new = text not in facts.get(key, [])
                missing = [p for p in re.findall(r"\{[A-Z0-9]+\}", facts[key][0]) if p not in text]
                extra = [p for p in re.findall(r"\{[A-Z0-9]+\}", text) if p not in "".join(facts[key])]
                if new and extra:
                    raise SystemExit(f"{lang} {key}: placeholder {extra} its wordings don't use: {text}")
                fills = r8.fills(lang, text, base, facts)
                row = {"lang": lang, "path": f"fact_0.{key}", "text": text, "role": "fact",
                       "batch": f"Forecast: {FAMILY[group]}", "sprite": sprite,
                       "fills": fills, "fillsAlt": r8.fills(lang, text, base, facts, alt=True),
                       "under": under_line(doc, group, fills),
                       "meaning": "Forecast line, the same at every sarcasm level. " + meaning}
                hints = []
                if new:
                    row["new"] = True
                    hints.append("New wording")
                    if missing:
                        hints.append("Leaves out " + ", ".join(missing))
                elif (lang, text) in earlier:
                    row["earlier"] = earlier[(lang, text)]
                if len(facts.get(key, [])) == 1 and not new:
                    hints.append("The only wording: a veto keeps it until a new one is kept")
                if hints:
                    row["hint"] = " · ".join(hints)
                lines.append(row)
        seen = set()
        existing = {t for s, pools in doc.items() if isinstance(pools, dict) and s != "facts"
                    for v in pools.values() if isinstance(v, list) for t in v if isinstance(t, str)}
        for item in flavour:
            text = item["text"]
            if text in seen or text in existing or text in voted:
                print(f"  {lang} skipped, already there: {text}")
                continue
            seen.add(text)
            lines.append(r13.flavour_row(lang, item, doc, base))
    out = {"round": ROUND, "idPrefix": "rp", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        k = (r["lang"], r["batch"], "new" if r.get("new") else "live")
        by[k] = by.get(k, 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b, n), c in sorted(by.items()):
        print(f"  {l} {b:26} {n:4} {c}")
    answered = {a for r in lines for a in r.get("answers", [])}
    for lang in ("en", "de"):
        waiting = (REPO / "review" / "rewrite" / f"{lang}.md").read_text(encoding="utf-8")
        ids = re.findall(r"\*\*Answers:\*\* `([^`]+)`", waiting)
        left = [i for i in ids if i not in answered]
        print(f"  {lang}: {len(left)} of {len(ids)} Write new spots not answered" + (f": {left}" if left else ""))


if __name__ == "__main__":
    main()
