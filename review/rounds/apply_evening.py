#!/usr/bin/env python3
"""
Puts the owner's votes on the evening rounds into
prototypes/panels/lang/<lang>.json. Every evening pool is rebuilt from
all of them, so running this again never loses a line:

  - round 28 (2026-11-evening): evening.facts.<situation>; its evening
    lines become evening.jokes_<level>.any;
  - round 29 (2026-11-evening2, the pilot): evening.jokes_<level>.<pool>;
  - round 30 (2026-11-ideas, the directions): the samples the owner kept,
    placed by PLACE below (a sample shown under rain can fit any weather);
  - round 31 (2026-11-evening31) and later: evening.jokes_<level>.<pool>,
    with the tag the round file gives the line ("{P}", "{D:1}").

Starred and kept lines go in, with the owner's edits. A note asking to
show a line only while it's dry right now puts "{DRY}" in front of it
(evening.liquid). Facts nobody kept keep what they had.

    python3 tools/review_sync.py <decisions.json>   # first, as for every round
    python3 review/rounds/apply_evening.py
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
JOKE_ROUNDS = ("2026-11-evening", "2026-11-evening2", "2026-11-ideas")
TAGGED_ROUNDS = ("2026-11-evening31", "2026-11-evening32", "2026-11-evening33", "2026-11-evening34", "2026-11-evening35", "2026-11-evening36", "2026-11-evening37")
FACT_ROUNDS = ("2026-11-evening",)
ALONE_ROUND = "2026-11-evening-alone"

# Round 30's kept samples: (level, [pools]), the tag in front.
PLACE = {
    "en": {
        "Next on this screen, probably the stocks. Also forecasting a drop.": ("10", ["colder"], ""),
        "Marvelous. Truly.": ("10", ["rain", "snow", "colder"], ""),
        "Rain on a Saturday. The weather doesn't do weekends.": ("10", ["rain"], "{D:6}"),
        "The rain told us exactly when it's coming. No repairman has ever managed that.": ("10", ["rain"], "{T}"),
        "I asked if tomorrow's cold could wait a week. It's already left the house.": ("10", ["colder"], ""),
        "I'm doing tomorrow's grumbling tonight. During the rain I'll be busy drawing umbrellas.": ("10", ["rain"], ""),
        "If this changes overnight, I'll quietly redraw it and act like it was always that way.": ("10", ["any"], ""),
    },
    "de": {
        "Auch das noch.": ("10", ["rain", "snow", "colder"], ""),
        "Die Figur da rechts ist schon für morgen angezogen. Streber.": ("10", ["any"], "{P}"),
        "Ich meckere heute schon mal vor. Morgen reicht dann ein Seufzer.": ("10", ["any"], ""),
        "Ich wollte den Regen auf nächste Woche verschieben. Der ist aber schon losgefahren.": ("10", ["rain"], ""),
        "Ändert sich das über Nacht, mal ich's heimlich um und tu so, als wär nichts gewesen.": ("10", ["any"], ""),
    },
}
# Small fixes to the owner's edits (spelling only).
FIXES = {"But it's already on it's way.": "But it's already on its way.",
         "Vielleicht fang ich an ein bisschen Hintergrund zu malen": "Vielleicht fang ich an, ein bisschen Hintergrund zu malen",
         "Schon mal überlegt so viel Zeit": "Schon mal überlegt, so viel Zeit",
         "a 5 minute voice memo": "a five-minute voice memo",
         "Mir geht’s nicht": "Mir geht's nicht",
         "Merk dir: falls ich": "Merk dir: Falls ich"}
# Tags added after a vote, by the line's original text (owner's notes).
EXTRA_TAGS = {"Samstag, und das Wetter spielt mit. Kommt selten genug vor.": "{G}"}


def round_replaces(lang):
    """(path, text) -> the live line it replaces, from the tagged rounds' files."""
    out = {}
    for rnd in TAGGED_ROUNDS:
        f = HERE / f"{rnd}.json"
        if f.exists():
            for row in json.loads(f.read_text(encoding="utf-8"))["lines"]:
                if row["lang"] == lang and row.get("replaces"):
                    out[(row["path"], row["text"])] = row["replaces"]
    return out


def round_tags(lang):
    """(path, text) -> tag, from the tagged rounds' files."""
    tags = {}
    for rnd in TAGGED_ROUNDS:
        f = HERE / f"{rnd}.json"
        if f.exists():
            for row in json.loads(f.read_text(encoding="utf-8"))["lines"]:
                if row["lang"] == lang and row.get("evtag"):
                    tags[(row["path"], row["text"])] = row["evtag"]
    return tags


def main():
    for lang in ("en", "de"):
        dec = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        tags = round_tags(lang)
        repl = round_replaces(lang)
        dropped = set()
        facts, jokes = {}, {}
        for d in dec.values():
            rnd = d.get("round")
            if d.get("verdict") not in ("star", "keep") or rnd not in FACT_ROUNDS + JOKE_ROUNDS + TAGGED_ROUNDS:
                continue
            path = (d.get("path") or "").split("[")[0]
            text = (d.get("edit") or d["text"]).strip()
            for a, b in FIXES.items():
                text = text.replace(a, b)
            if "dry right now" in (d.get("note") or "").lower():
                text = "{DRY}" + text
            if path.startswith("fact_0.evening_"):
                facts.setdefault(path.split("evening_", 1)[1], []).append(text)
                continue
            level = path.split(".")[0].split("_")[-1]
            if rnd == "2026-11-ideas":
                level, pools, tag = PLACE[lang][d["text"]]
                for pool in pools:
                    jokes.setdefault(("jokes_" + level, pool), []).append(tag + text)
            elif path.endswith(".evening"):
                jokes.setdefault(("jokes_" + level, "any"), []).append(text)
            elif ".evening_" in path:
                tag = EXTRA_TAGS.get(d["text"], "") + tags.get((path, d["text"]), "")
                if (path, d["text"]) in repl:  # a kept rewrite of a live line: the old one goes
                    dropped.add(repl[(path, d["text"])])
                jokes.setdefault(("jokes_" + level, path.split(".evening_", 1)[1]), []).append(tag + text)
        # Round "2026-11-evening-alone": every live line shown without the
        # forecast sentence. Veto = it needs the sentence: "{S}" in front.
        # Edit = a version for the screen without the sentence (owner): the
        # original stays as it is, with "{S}"; the edit joins it with "{N}"
        # and the original's other tags.
        needs_s, alone = set(), {}
        for d in dec.values():
            if d.get("round") != ALONE_ROUND:
                continue
            edit = (d.get("edit") or "").strip()
            if d.get("verdict") in ("veto", "rewrite") or (edit and edit != d["text"]):
                needs_s.add(d["text"])
            if edit and edit != d["text"] and d.get("verdict") in ("keep", "star"):
                for a, b in FIXES.items():
                    edit = edit.replace(a, b)
                alone[d["text"]] = edit
        for key in list(jokes):
            out = []
            for x in jokes[key]:
                tag, body = x[:len(x) - len(x.split("}")[-1])], x.split("}")[-1]
                out.append(("{S}" + x) if body in needs_s and "{S}" not in tag else x)
                if body in alone:
                    out.append("{N}" + tag.replace("{S}", "") + alone[body])
            jokes[key] = out
        p = REPO / "prototypes" / "panels" / "lang" / f"{lang}.json"
        doc = json.loads(p.read_text(encoding="utf-8"))
        ev = doc["evening"]
        for key, texts in sorted(facts.items()):
            ev["facts"][key] = list(dict.fromkeys(texts))
        ev["jokes_10"], ev["jokes_11"] = {}, {}
        for (group, pool), texts in sorted(jokes.items()):
            ev[group][pool] = [x for x in dict.fromkeys(texts) if x.split("}")[-1] not in dropped]
        ev.pop("_note", None)
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(lang, {g: {k: len(v) for k, v in ev[g].items()} for g in ("jokes_10", "jokes_11")})


if __name__ == "__main__":
    main()
