#!/usr/bin/env python3
"""
Rebuilds the flavour pools in prototypes/fact-flavour/lang/ from the votes:
every starred or kept line of the winning voice, with the owner's notes
applied as edits.

    python3 review/rounds/build_pools.py

Reads review/decisions/<lang>.json (written by tools/review_sync.py).
Seasonal pools (theme_*) are left as they are.

Round 5 (variance) adds two things: reworded flavour lines, each placed a
whole pool's length after the line it varies so the same joke never shows
two days running; and extra wordings of each fact, appended to the list
the template rotates through (the first wording stays first).
"""

import collections
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
MOODS = ["nice", "cool", "warming", "cooling", "cold", "hot", "wet", "snow", "fickle", "evening", "night"]

# The winning voice in each round, as (round, set) pairs.
WIN = {
    "en": {("2026-10-voices", "B"), ("2026-10-voices-2", "W"), ("2026-10-writing", "E2"), ("2026-10-topup", "E4"),
           ("2026-10-evening", "E6")},
    "de": {("2026-10-voices", "G"), ("2026-10-voices-2", "Y"), ("2026-10-writing", "D1"), ("2026-10-topup", "D4"),
           ("2026-10-evening", "D6")},
}
# Round 5: reworded flavour lines (set V*) and fact wordings (set F*).
VARIANTS = "2026-10-variants"
VARIANT_SETS = {"en": ("VE", "FE"), "de": ("VD", "FD")}
# The owner's notes, applied. None drops a line a cleaner version replaces.
EDIT = {
    "I don't sweat. You will. I'll be here, judging.": "I don't sweat. You will.",
    "Go outside. I'll pretend I didn't see you stay in.": None,
    "Cold out. I'm staying on the wall where it's warm.": None,
    "Rain today. I'll be on the wall, dry and smug.": None,
    "Other screens get to show paintings. I get today.": "Other screens get to show paintings. I get today's weather.",
    "Zu heiß. Und im Winter wieder jammern, dass es zu kalt ist.": "Und im Winter wieder jammern, dass es zu kalt ist.",
    "Ausgehen? Zieh was Schöneres an als das hier.": "Zieh was Schöneres an als das hier.",
    "Schon wieder so spät? Ab ins Bett. Das Wetter wartet nicht auf dich.": "Schon wieder so spät? Ab ins Bett.",
    "Um die Uhrzeit noch aufs Wetter schauen. Respekt. Oder Problem.": "Um die Uhrzeit noch aufs Wetter schauen. Respekt.",
    "Schnee. Gleich fährt keine Bahn mehr, wetten?": "Gleich fährt keine Bahn mehr, wetten?",
    "Du wirst heut wieder jeden fragen, ob ihm auch so heiß ist.": "Du wirst heut wieder alle fragen, ob ihnen auch so heiß ist.",
    "Kalt. Und du in der dünnen Jacke. Na servas.": None,
    # round 4: the owner's notes ("too Austrian", rewordings)
    "You asked for warm weather. Be specific next time.": "You asked for warm weather. Careful what you wish for.",
    "Ausziehen, anziehen. Wie beim Doktor, bloß ohne Krankschreibung.": "Ausziehen, anziehen. Wie beim Arzt, bloß ohne Krankschreibung.",
    "Ich bleib eh im Trockenen. Mein Mitleid hält sich in Grenzen.": "Mein Mitleid hält sich in Grenzen. Ich bleib im Trockenen.",
    "Du hängst eh gleich am Heizkörper wie eine Katze.": "Du hängst gleich wieder am Heizkörper wie eine Katze.",
    "Der Schneepflug kommt eh erst, wenn alles getaut ist.": "Der Schneepflug kommt wieder erst, wenn alles getaut ist.",
    "Mir kann's wurscht sein. Ich häng hier nackt an der Wand.": "Mir kann's egal sein. Ich häng hier nackt an der Wand.",
    "Bei dem Wetter muss man raus, heißt's immer. Muss man gar nix.": "Bei dem Wetter muss man raus, heißt's immer. Muss man gar nicht.",
    "Im Haus schleudert um die Zeit noch eine Waschmaschine.": "Und wieder hält jemand nachts Wäschewaschen für eine gute Idee.",
    "Ohne Haube rausgehen und dann jammern. Kenn ma schon.": None,
    "Wennst ohne Schirm gehst, brauchst nachher nicht jammern.": None,
    "Feierabend. Jetzt lass mich auch in Ruh.": None,
    # round 5: the owner's notes on the reworded lines
    "Somewhere a screen is showing a Monet. I got today.": "Somewhere a screen is showing a Monet. All you get is this.",
    "Flat, pale and cool. Built for days like this.": "Flat, pale and cool. I'm built for days like this.",
    "Today you'll fan yourself with anything flat. Not me.": "Today you'll fan yourself with anything flat. Please don't use me.",
    "Snow stays at the door. Not near me.": "Snow stays at the door. Don't bring it near me.",
    "You won't get a sad little cloud icon from me. Standards.": "You won't get a sad little cloud icon from me. I've got artistic integrity.",
    "Bei der Kälte trinkt man sogar Glühwein freiwillig.": "Bei der Kälte trinkt man sogar freiwillig Glühwein.",
    "Dieses Hin und Her macht mich ganz kirre.": "Dieses Hin und Her macht mich ganz verrückt.",
    "Gleich kommt wieder: „Aber es ist eine trockene Hitze.“": "Gleich kommt wieder: „Früher war es auch schon heiß.“",
    "Im Januar wünschen sich das alle zurück. Wetten?": "Jetzt meckern, und im Januar wünschen sich alle wieder den Sommer zurück.",
    "Gleich fragst du wieder jeden, ob dem auch so warm ist.": "Gleich fragst du wieder alle, ob ihnen auch so warm ist.",
    "Irgendwo im Haus läuft jetzt garantiert der Trockner.": "Irgendwo im Haus läuft jetzt garantiert der Trockner. Wumm, wumm, wumm.",
    "Mich betrifft das nicht. Ich häng hier ohne alles an der Wand.": "Mich betrifft das nicht. Ich häng hier nackt an der Wand.",
    # "In case you're on your way out" doesn't work in the evening (round 5).
    "Falls du noch weggehst: Ich bleib hier. Wie immer.": None,
}
# The owner's notes on fact wordings, by template. Round 5: "don't take
# anything off" on a steady cold day is "boring and redundant".
FACT_EDIT = {
    "{WHEN} {GV} weg. Heute brauchst du {GP} nicht mehr.": "{WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr.",
    "{WHEN} {GV} weg, und du brauchst {GP} heute nicht mehr.": "{WHEN} {GV} weg, und du brauchst {GP} danach nicht mehr.",
    "Erst eine Schneepause, {WHENP} schneit's wieder.": "Erstmal eine Schneepause. {WHENP} schneit es dann aber wieder.",
    "Was du anhast, reicht für den ganzen Abend.": "Was du anhast, passt für den ganzen Abend.",
    "Es bleibt den ganzen Tag so kalt, also lass alles an.": "Es bleibt den ganzen Tag so kalt.",
    "Heute wird's nicht wärmer. Lass alles an.": "Heute wird's nicht wärmer.",
    "Die Kälte bleibt den ganzen Tag, also nichts ausziehen.": "Die Kälte bleibt den ganzen Tag.",
    "It stays this cold all day, so keep everything on.": "It stays this cold all day.",
}
# Round 4 split "mild" in three. The mild lines the owner kept all talk
# about an unremarkable day, which is the steady one.
MOOD_RENAME = {"mild": "cool"}
# Lines the owner wrote in a note, added as written.
OWNER = {("de", "10", "cooling"): ["Nachher sagt wieder jeder: Ganz schön frisch geworden."]}
# Lines the owner moved to a later hour.
MOVE = {"Nothing new from me tonight. Sleep well.": "night",
        "You've looked at me a lot today. Go to bed.": "night"}


def variants_round():
    path = REPO / "review" / "rounds" / f"{VARIANTS}.json"
    if not path.exists():
        return {}
    return {(l["lang"], l["text"]): l for l in json.loads(path.read_text(encoding="utf-8"))["lines"]}


def build_facts(doc, lang, decisions, round_lines):
    """Each fact becomes a list: its first wording, then the kept variants."""
    facts = doc["facts"]
    kept = collections.defaultdict(list)
    fact_set = VARIANT_SETS[lang][1]
    for d in decisions.values():
        if (d.get("round"), d.get("batch")) == (VARIANTS, fact_set) and d.get("verdict") in ("star", "keep"):
            line = round_lines.get((lang, d["text"]))
            if line:
                kept[d["key"]].append(FACT_EDIT.get(line["template"], line["template"]))
    order = {(l["path"], l.get("template")): i for i, l in enumerate(round_lines.values())}
    for key, value in facts.items():
        if key.startswith("garments"):
            continue
        first = value[0] if isinstance(value, list) else value
        first = FACT_EDIT.get(first, first)
        inverse = {v: k for k, v in FACT_EDIT.items()}
        more = sorted(kept.get(key, []), key=lambda t: order.get((f"fact_0.{key}", inverse.get(t, t)), 0))
        facts[key] = [first] + [t for t in more if t != first]
    return sum(len(v) for k, v in facts.items() if not k.startswith("garments"))


def main():
    round_lines = variants_round()
    for lang, winners in WIN.items():
        decisions = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        pools = collections.defaultdict(lambda: collections.defaultdict(list))
        reworded = collections.defaultdict(lambda: collections.defaultdict(list))
        for d in decisions.values():
            if (d.get("round"), d.get("batch")) == (VARIANTS, VARIANT_SETS[lang][0]):
                line = round_lines.get((lang, d["text"]))
                text = EDIT.get(d["text"], d["text"])
                if line and text and d.get("verdict") in ("star", "keep"):
                    reworded[d["level"]][d["key"]].append((line["variant_of"], text))
                continue
            if (d.get("round"), d.get("batch")) not in winners or d.get("verdict") not in ("star", "keep"):
                continue
            text = EDIT.get(d["text"], d["text"])
            if text is None:
                continue
            mood = MOVE.get(d["text"], MOOD_RENAME.get(d["key"], d["key"]))
            entry = (d["verdict"] != "star", text)  # starred lines first
            if entry not in pools[d["level"]][mood]:
                pools[d["level"]][mood].append(entry)
        for (l, level, mood), texts in OWNER.items():
            if l == lang:
                pools[level][mood] += [(False, t) for t in texts if (False, t) not in pools[level][mood]]
        path = REPO / "prototypes" / "fact-flavour" / "lang" / f"{lang}.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        for level in ("10", "11"):
            old = doc[f"flavour_{level}"]
            new = {m: [t for _, t in sorted(pools[level][m])] for m in MOODS if pools[level][m]}
            # A reworded line goes in the same order as the lines it varies,
            # so it shows one full cycle after its original, never next to it.
            for m, pairs in reworded[level].items():
                base = new.get(m, [])
                pairs = [p for p in pairs if p[0] in base]
                new[m] = base + [v for _, v in sorted(pairs, key=lambda p: base.index(p[0]))]
            new.update({k: v for k, v in old.items() if k.startswith("theme_")})
            doc[f"flavour_{level}"] = new
            print(f"{lang} {level}: " + "  ".join(f"{m} {len(new.get(m, []))}" for m in MOODS))
        print(f"{lang} facts: {build_facts(doc, lang, decisions, round_lines)} wordings")
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
