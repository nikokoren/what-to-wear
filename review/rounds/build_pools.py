#!/usr/bin/env python3
"""
Rebuilds the flavour pools in prototypes/fact-flavour/lang/ from the votes:
every starred or kept line of the winning voice, with the owner's notes
applied as edits.

    python3 review/rounds/build_pools.py

Reads review/decisions/<lang>.json (written by tools/review_sync.py).
Seasonal pools (theme_*) are built from the votes like the moods; a
theme line nobody has voted on yet (the first prototype's Christmas
placeholders) stays until it is voted.

Round 8 (the re-read) comes last: every line the beta ships, voted
again, some reworded on the page. A veto takes the line out, the owner's
edit replaces it; a fact keeps at least one wording.

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
           ("2026-10-evening", "E6"), ("2026-10-evening-2", "E6"), ("2026-10-themes-winter", "E7")},
    "de": {("2026-10-voices", "G"), ("2026-10-voices-2", "Y"), ("2026-10-writing", "D1"), ("2026-10-topup", "D4"),
           ("2026-10-evening", "D6"), ("2026-10-evening-2", "D6"), ("2026-10-themes-winter", "D7")},
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
    # round 6: the owner's notes on the evening lines
    "Um kurz vor sechs kommt immer noch eine „kurze Rückfrage“.": "Typisch. Um kurz vor Feierabend kommt natürlich eine „kurze Rückfrage“.",
    "Um die Zeit bohrt garantiert noch irgendein Nachbar.": "Gleich bohrt garantiert noch irgendein Nachbar in der Wand rum.",
    "No 'quick questions' at 5:58 for me. Perks of being a wall.": "No 'quick questions' at 5:58 for me. Perks of being a screen.",
    # "In case you're on your way out" doesn't work in the evening (round 5).
    "Falls du noch weggehst: Ich bleib hier. Wie immer.": None,
    # round 7: the owner's rewrites of the theme lines ("work the day into
    # the sentence, not just: Day. Sentence."), spelling made standard
    "Neujahr. Jetzt fegt wieder keiner die Raketenreste weg.": "Neujahr. Und wieder hat niemand die Raketenreste weggemacht.",
    "Halloween. Früher war Reformationstag, da hat keiner geklingelt.": "Halloween. Früher war Reformationstag, da hatte man seine Ruhe.",
    "Krampustag. Ob du brav warst? Ich hab mitgeschrieben.": "Ob du brav warst? Der Krampus hat mitgeschrieben.",
    "Krampustag. Ich hab ihm deine Adresse nicht gegeben. Noch nicht.": "Ich hab dem Krampus deine Adresse nicht gegeben. Noch nicht.",
    "Nikolaus. In deinem Stiefel liegt bestimmt nur Streusalz.": "Der Nikolaus hat in deinem Stiefel bestimmt nur Kohle gelassen.",
    "Nikolaus. Hast du deine Stiefel rausgestellt? In deinem Alter?": "Du hast deine Schuhe für den Nikolaus rausgestellt? In deinem Alter?",
    "Neujahr. Dein Wachsgießen sah wieder aus wie eine Kartoffel.": "Beim Bleigießen wird deine Zukunft sicher wieder 'ne Kartoffel. Wie immer.",
    "Halloween. Wenn's klingelt, bist du plötzlich nicht zu Hause.": "Wenn's klingelt, bist du heute plötzlich wieder nicht zu Hause. Typisch.",
    "Weihnachten. Du sagst wieder „wir schenken uns nichts“. Sicher.": "Du sagst wieder „wir schenken uns nichts“. Nur weil du keine guten Ideen hast.",
    "You'll buy candy for trick-or-treaters and eat it by eight.": "Try not to buy candy for trick-or-treaters and eat it by eight again this year.",
}
# Round 8: typos in the owner's edits, corrected (the wording is theirs).
EDIT_FIX = {
    "Gleichträumst du wieder vom Süden. Dann fahr halt endlich hin.": "Gleich träumst du wieder vom Süden. Dann fahr halt endlich hin.",
    "Es bleibt bis zum Abend Heiß. Nimm Wasser mit und bleib im Schatten.": "Es bleibt bis zum Abend heiß. Nimm Wasser mit und bleib im Schatten.",
    "Jetzt ists noch kühl, aber {WHEN} ist es Shorts-Wetter.": "Jetzt ist's noch kühl, aber {WHEN} ist es Shorts-Wetter.",
    "Was du anhast passt für den restlichen Tag.": "Was du anhast, passt für den restlichen Tag.",
    "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and a maybe an extra layer more.":
        "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and maybe an extra layer.",
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
# Round 8: every shipped line voted again, applied after everything else.
REREAD = "2026-10-reread"
# Round 9: rewordings from the round 8 notes, applied after round 8. Each
# line says what it replaces: one line, or "*" for every wording of a fact.
REWORK = "2026-10-rework"
# Round 10: Visual Forecast's own pools (flavour_vf_10 / flavour_vf_11).
VISUAL = "2026-10-visual"
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


def apply_reread(doc, decisions):
    """Round 8, by text: a veto takes the line out, an edit replaces it."""
    votes = {}
    for d in decisions.values():
        if d.get("round") == REREAD and d.get("verdict"):
            section, key = d["path"].split("[")[0].split(".", 1)
            votes[(section, key, d["text"])] = d
    n = collections.Counter()

    def fixed(section, key, texts):
        out = []
        for t in texts:
            d = votes.get((section, key, t))
            if d and d["verdict"] == "veto":
                n["vetoed"] += 1
                continue
            if d and d.get("edit"):
                n["edited"] += 1
                t = EDIT_FIX.get(d["edit"], d["edit"])
            if t not in out:
                out.append(t)
        return out

    facts = doc["facts"]
    for key, texts in facts.items():
        if key.startswith("garments"):
            continue
        new = fixed("fact_0", key, texts)
        if not new:
            print(f"  facts.{key}: every wording vetoed; keeping {texts[0]!r} until there's a new one")
            new = texts[:1]
        facts[key] = new
    for level in ("10", "11"):
        pools = doc[f"flavour_{level}"]
        for mood in list(pools):
            pools[mood] = fixed(f"flavour_{level}", mood, pools[mood])
            if not pools[mood]:
                print(f"  flavour_{level}.{mood}: every line vetoed; this mood shows no sarcastic line")
                del pools[mood]
        topical = doc.get(f"topical_{level}")
        if topical:
            kept = []
            for t in topical:
                d = votes.get((f"topical_{level}", "topical", t["text"]))
                if d and d["verdict"] == "veto":
                    n["vetoed"] += 1
                    continue
                if d and d.get("edit"):
                    n["edited"] += 1
                    t = {**t, "text": d["edit"]}
                kept.append(t)
            doc[f"topical_{level}"] = kept
    return n


def apply_rework(doc, lang, decisions):
    """Round 9: a kept rewording replaces its original; "*" replaces a whole fact list."""
    path = REPO / "review" / "rounds" / f"{REWORK}.json"
    n = collections.Counter()
    if not path.exists():
        return n
    votes = {d["text"]: d for d in decisions.values() if d.get("round") == REWORK}
    whole = collections.defaultdict(list)
    for line in json.loads(path.read_text(encoding="utf-8"))["lines"]:
        d = votes.get(line["text"])
        if line["lang"] != lang or not d or d.get("verdict") not in ("star", "keep"):
            continue
        text = EDIT_FIX.get(d.get("edit"), d.get("edit")) or line["text"]
        section, key = line["path"].split(".", 1)
        if line.get("replaces") == "*":
            whole[key].append(text)
            continue
        pool = doc[section].setdefault(key, [])
        old = line.get("replaces")
        if old in pool and text not in pool:
            pool[pool.index(old)] = text
            n["reworded"] += 1
        elif text not in pool:
            # new, or a second take on an original another take replaced
            pool.append(text)
            n["added"] += 1
    for key, texts in whole.items():
        doc["facts"][key] = texts
        n["fact lists replaced"] += 1
    return n


def build_visual(doc, lang, decisions):
    """Round 10: per mood, the lines that work without the fact, plus new ones.

    A "needs the fact" (a veto in this round) keeps a line off Visual
    Forecast only. Warming and cooling take cool's lines too, as the words
    do. Nothing is written until the round has votes: without these pools
    the panels show the usual line.
    """
    path = REPO / "review" / "rounds" / f"{VISUAL}.json"
    votes = {}
    for d in decisions.values():
        if d.get("round") == VISUAL:
            votes[(d["path"].split("[")[0], d["text"])] = d
    if not path.exists() or not votes:
        return collections.Counter()
    lines = [l for l in json.loads(path.read_text(encoding="utf-8"))["lines"] if l["lang"] == lang]
    moods = sorted({l["path"].split(".")[1] for l in lines})
    n = collections.Counter()
    for level in ("10", "11"):
        pools = doc[f"flavour_{level}"]
        needs = {t for (p, t), d in votes.items() if p.startswith(f"flavour_{level}.") and d.get("verdict") == "veto"}
        vf = {}
        for mood in moods:
            if mood == "cool":
                continue
            base = list(pools.get(mood, []))
            if mood in ("warming", "cooling"):
                base += [t for t in pools.get("cool", []) if t not in base]
            alone = [t for t in base if t not in needs]
            n["kept off"] += len(base) - len(alone)
            new = []
            for l in lines:
                d = votes.get((l["path"], l["text"]))
                if l["path"] == f"flavour_vf_{level}.{mood}" and d and d.get("verdict") in ("star", "keep"):
                    new.append(EDIT_FIX.get(d.get("edit"), d.get("edit")) or l["text"])
            n["new"] += len(new)
            # The new lines first: they were written for the drawings.
            if new or alone:
                vf[mood] = new + [t for t in alone if t not in new]
        doc[f"flavour_vf_{level}"] = vf
    return n


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
            # A placeholder theme line counts as voted only by its own round;
            # the owner's rewordings count as voted too, or they'd come back
            # beside the line they replaced.
            voted = {d["text"] for d in decisions.values() if d.get("round") != REREAD}
            voted |= {EDIT_FIX.get(d["edit"], d["edit"]) for d in decisions.values() if d.get("edit")}
            themes = {k for k in pools[level] if k.startswith("theme_")} | {k for k in old if k.startswith("theme_")}
            for k in sorted(themes):
                keep = [t for _, t in sorted(pools[level][k])]
                keep += [t for t in old.get(k, []) if t not in voted and t not in keep]
                if keep:
                    new[k] = keep
            doc[f"flavour_{level}"] = new
            print(f"{lang} {level}: " + "  ".join(f"{m} {len(new.get(m, []))}" for m in MOODS))
        print(f"{lang} facts: {build_facts(doc, lang, decisions, round_lines)} wordings")
        reread = apply_reread(doc, decisions)
        if reread:
            print(f"{lang} re-read: {reread['vetoed']} taken out, {reread['edited']} reworded")
        rework = apply_rework(doc, lang, decisions)
        if rework:
            print(f"{lang} rework: " + ", ".join(f"{v} {k}" for k, v in rework.items()))
        visual = build_visual(doc, lang, decisions)
        if visual:
            print(f"{lang} Visual Forecast: {visual['new']} new lines, {visual['kept off']} kept off")
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
