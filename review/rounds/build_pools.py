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

"Write new" votes (any round) come last of all: the line and the one it
would have replaced are taken out (apply_write_new).

Round 8 (the re-read) comes after the voices: every line the beta ships, voted
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
    # round 10: the owner's note
    "Schwitzen im Stehen. Ein Traum.": "Bald schwitzt du im Stehen. Ein Traum.",
}
# Round 8: typos in the owner's edits, corrected (the wording is theirs).
EDIT_FIX = {
    # Round 19 edits.
    "It starts cool, but it's shorts weather {WHEN}. || Shorts might be worth a cold first hour. Nut that’s easy for me to say. I don’t freeze.": "It starts cool, but it's shorts weather {WHEN}. || Shorts might be worth a cold first hour. But that's easy for me to say. I don't freeze.",
    # Round 18 edits.
    "Shorts could be worth it today. It's cool now, but warm {WHEN}. || I’d say ‘Trust me’. but I've never had cold legs.": "Shorts could be worth it today. It's cool now, but warm {WHEN}. || I'd say \"trust me\", but I've never had cold legs.",
    "Jetzt noch frisch, {WHEN} wird's warm genug für ne kurze Hosen. || Deine Beine haben lang keine Sonne gesehen. Man wird's merken.": "Jetzt noch frisch, {WHEN} wird's warm genug für ne kurze Hose. || Deine Beine haben lang keine Sonne gesehen. Man wird's merken.",
    "{WHEN} kann der Pulli weg. || Was drunter ist, hast du dir heute früh hoffentlich gut überlegt": "{WHEN} kann der Pulli weg. || Was drunter ist, hast du dir heute früh hoffentlich gut überlegt.",
    "{WHEN} wird's wärmer, dann kann der Pulli weg. || Ich sag’s nur. Ausziehen musst du ihn selber.": "{WHEN} wird's wärmer, dann kann der Pulli weg. || Ich sag's nur. Ausziehen musst du ihn selber.",
    "You've already started to counted the days to the weekend.": "You've already started counting the days to the weekend.",
    "You'd be good Groundhog : pop out, look around, go back in.": "You'd make a good groundhog: pop out, look around, go back in.",
    "Überleg dir ne kurze hose anzuziehen, {WHEN} wird's warm. Die warme Schicht solltest du aber trotzdem mitnehmen.": "Überleg dir, ne kurze Hose anzuziehen, {WHEN} wird's warm. Die warme Schicht solltest du aber trotzdem mitnehmen.",
    "{WHEN} wird's kalt. Überleg dir lange Hosen anzuziehen und eine warme Schicht mitzunehmen.": "{WHEN} wird's kalt. Überleg dir, lange Hosen anzuziehen und eine warme Schicht mitzunehmen.",
    'Schön. Dann musst du dir nur noch eine Ausrede ausdenken warum du schon wieder so lange wach bist.': 'Schön. Dann musst du dir nur noch eine Ausrede ausdenken, warum du schon wieder so lange wach bist.',
    "You could think about wear shorts instead. It's warm {WHEN}, but bring {G} for {WHEN2}.": "You could think about wearing shorts instead. It's warm {WHEN}, but bring {G} for {WHEN2}.",
    'You could go even to bed in it. I know you have before.': 'You could even go to bed in it. I know you have before.',
    "Ich sag's auch dreimal, wenn's sein muss. Schatten Schatten Schatten": "Ich sag's auch dreimal, wenn's sein muss. Schatten, Schatten, Schatten.",
    'Meckern kannst du später. Erst mal nen schluck Wasser trinken.': 'Meckern kannst du später. Erst mal einen Schluck Wasser trinken.',
    'Eine Sorge weniger. Aber dir fällt bestimmt was neues ein.': 'Eine Sorge weniger. Aber dir fällt bestimmt was Neues ein.',
    'Dein „Das zieht vorbei“ hat hat noch nie gestimmt.': 'Dein „Das zieht vorbei“ hat noch nie gestimmt.',
    "Lebkuchen im September. Sowas hätt's früher nicht gegeben sagst du wieder und kaufst trotzdem heimlich zwei Packungen.": "Lebkuchen im September. „So was hätt's früher nicht gegeben“, sagst du wieder und kaufst trotzdem heimlich zwei Packungen.",
    "Noch ist's kühl, aber {WHEN} kannst du in Shorts rum laufen.": "Noch ist's kühl, aber {WHEN} kannst du in Shorts rumlaufen.",
    'Aber bitte nicht Jammern, dass es dir zu kalt ist.': 'Aber bitte nicht jammern, dass es dir zu kalt ist.',
    'After a dry spell, a thunder arrives {WHENP}. Hang on to the umbrella, and head indoors when it starts.': 'After a dry spell, thunder arrives {WHENP}. Hang on to the umbrella, and head indoors when it starts.',
    'Take the umbrella along for the rainshower {WHENP}.': 'Take the umbrella along for the rain shower {WHENP}.',
    'Dann fällt das Fitnessstudio heute ja wieder aus. "Wegen dem Wetter".': "Dann fällt das Fitnessstudio heute ja wieder aus. „Wegen dem Wetter“.",
    "Gleichträumst du wieder vom Süden. Dann fahr halt endlich hin.": "Gleich träumst du wieder vom Süden. Dann fahr halt endlich hin.",
    "Es bleibt bis zum Abend Heiß. Nimm Wasser mit und bleib im Schatten.": "Es bleibt bis zum Abend heiß. Nimm Wasser mit und bleib im Schatten.",
    "Jetzt ists noch kühl, aber {WHEN} ist es Shorts-Wetter.": "Jetzt ist's noch kühl, aber {WHEN} ist es Shorts-Wetter.",
    "Was du anhast passt für den restlichen Tag.": "Was du anhast, passt für den restlichen Tag.",
    "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and a maybe an extra layer more.":
        "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and maybe an extra layer.",
    # round 10
    "Ich sag dir es schneit und du bist trotzdem überrascht. Jedes Mal.": "Ich sag dir, es schneit, und du bist trotzdem überrascht. Jedes Mal.",
    "You've seen the forecast and leave without the extra layer anyway.": "You've seen the forecast and you'll leave without the extra layer anyway.",
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
        # The whole list as it stands, not just its first wording: later
        # rounds (14 on) add and reorder wordings, and the passes after this
        # one take out what's voted out, so a second run changes nothing.
        have = [FACT_EDIT.get(t, t) for t in (value if isinstance(value, list) else [value])]
        inverse = {v: k for k, v in FACT_EDIT.items()}
        more = sorted(kept.get(key, []), key=lambda t: order.get((f"fact_0.{key}", inverse.get(t, t)), 0))
        facts[key] = list(dict.fromkeys(have + more))
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
            if d and d["verdict"] in ("veto", "rewrite"):
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
                if d and d["verdict"] in ("veto", "rewrite"):
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
    Forecast only. Nothing is written until the round has votes: without
    these pools the panels show the usual line. (Warming and cooling used
    to take cool's lines too; a cool joke under a T-shirt drawing showed
    why not. The cool lines are now lines (build_now).)
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


NOW_MOODS = ["snow", "wet", "night", "evening", "hot", "cold", "nice", "cool"]
ALONE = "2026-10-alone"
FOLLOW = "2026-10-follow"
SEASONS = "2026-10-seasons"
REPLIES = "2026-10-replies"
POLISH = "2026-10-polish"
DAYS = "2026-10-days"
UNITS = "2026-10-units"
LAYERS = "2026-10-layers"  # round 18: units for the layer days
RAIN = "2026-10-rain"  # round 19: units for rain and snow, and top-ups
# Follow-ups go by what the forecast line says (block.liquid, fu_key), not
# by the mood: round 11's day lines are renamed to the group they follow.
MOOD_TO_GROUP = {"warming": "off", "cooling": "on", "fickle": "offon", "wet": "rain", "snow": "snow",
                 "evening": "evening", "night": "night", "nice": "steady", "cool": "steady", "cold": "cold", "hot": "hot"}


def apply_alone(doc, lang, decisions):
    """Round 11: every sarcastic line sorted into where it can show (now,
    day, drawings) and voted there. Day lines then split by the owner's
    notes into follow-ups (flavour_*, under the forecast line) and
    standalone ones (alone_*). Once the round has votes, the now, day
    and drawings pools are rebuilt from it: a current line stays (in the
    pool its row names) unless vetoed, a new one goes in only if kept;
    starred lines first, the owner's edits applied. Theme pools stay."""
    path = REPO / "review" / "rounds" / f"{ALONE}.json"
    votes = {(d["path"].split("[")[0], d["text"]): d for d in decisions.values() if d.get("round") == ALONE}
    if not path.exists() or not votes:
        return collections.Counter()
    n = collections.Counter()
    pools = collections.defaultdict(lambda: collections.defaultdict(list))
    for row in json.loads(path.read_text(encoding="utf-8"))["lines"]:
        if row["lang"] != lang:
            continue
        d = votes.get((row["path"], row["text"])) or {}
        verdict = d.get("verdict", "")
        if verdict in ("veto", "rewrite") or (row.get("new") and verdict not in ("star", "keep")):
            n["out" if verdict else "new, not kept"] += 1
            continue
        text = EDIT_FIX.get(d.get("edit"), d.get("edit")) or row["text"]
        section, mood = row["path"].split(".", 1)
        # The owner's notes (round 11) sort by the forecast line: a day line
        # "fine on its own" that doesn't flow under it is a standalone line
        # (alone_*); a line that doesn't work on its own is a follow-up.
        note = (d.get("note") or "").lower().replace("’", "'")
        level = section.rsplit("_", 1)[1]
        if section.startswith("flavour_") and not section.startswith("flavour_vf") and "fine on it" in note:
            section = f"alone_{level}"
            n["standalone (owner's note)"] += 1
        elif section.startswith("now_") and "on it's own does not work" in note:
            section = f"flavour_{level}"
            n["follow-up (owner's note)"] += 1
        pools[section][mood].append((verdict != "star", text))
        n["in"] += 1
    for level in ("10", "11"):
        themes = {k: v for k, v in doc.get(f"flavour_{level}", {}).items() if k.startswith("theme_")}
        for section in (f"now_{level}", f"alone_{level}", f"flavour_{level}", f"flavour_vf_{level}"):
            new = {}
            for mood, entries in pools[section].items():
                texts = []
                for _, t in sorted(entries, key=lambda e: e[0]):
                    if t not in texts:
                        texts.append(t)
                new[mood] = texts
            if section == f"flavour_{level}":
                grouped = {}
                for mood, texts in new.items():
                    grouped.setdefault(MOOD_TO_GROUP.get(mood, mood), []).extend(t for t in texts)
                new = {k: list(dict.fromkeys(v)) for k, v in grouped.items()}
                new.update(themes)
            doc[section] = new
    return n


def apply_follow(doc, lang, decisions, rnd=None):
    """Round 12: follow-ups by what the forecast line says, new lines for the
    "Write new" spots, month tags and the three-drawings tag. Applied once
    the round has votes. New lines go in only if kept; a kept month
    question puts "{M:..}" in front of its line wherever it is; "three"
    rows get "{3}" (only with three different drawings). Round 13 (seasons
    and riffs) goes the same way, and its "garments" rows get "{W:...}"
    (only when the forecast line names one of them)."""
    rnd = rnd or FOLLOW
    path = REPO / "review" / "rounds" / f"{rnd}.json"
    votes = {(d["path"].split("[")[0], d["text"]): d for d in decisions.values() if d.get("round") == rnd}
    if not path.exists() or not votes:
        return collections.Counter()
    n = collections.Counter()
    for row in json.loads(path.read_text(encoding="utf-8"))["lines"]:
        if row["lang"] != lang or row.get("role") == "fact":
            continue
        d = votes.get((row["path"], row["text"])) or {}
        verdict = d.get("verdict", "")
        section, key = row["path"].split(".", 1)
        if row.get("ask") == "months":
            if verdict in ("star", "keep"):
                tag = "{M:" + row["months"] + "}"
                for pools in (doc.get(s2, {}) for s2 in list(doc) if s2.split("_")[0] in ("now", "alone", "flavour")):
                    for k2, texts in pools.items():
                        if isinstance(texts, list) and row["text"] in texts:
                            texts[texts.index(row["text"])] = tag + row["text"]
                            n["month tags"] += 1
            continue
        if verdict not in ("star", "keep"):
            n["new, not kept" if not verdict or verdict == "" else "out"] += 1
            continue
        text = EDIT_FIX.get(d.get("edit"), d.get("edit")) or row["text"]
        if row.get("garments"):
            text = "{W:" + ",".join(row["garments"]) + "}" + text
        if row.get("months"):
            text = "{M:" + row["months"] + "}" + text
        if row.get("three"):
            text = "{3}" + text
        note = (d.get("note") or "").lower().replace("its own", "it's own")
        if section.startswith("now_") and "on it's own" in note and "not" in note:
            # a now line the owner kept but found doesn't stand alone: it
            # follows the forecast line instead, in its mood's group
            section, key = "flavour_" + section.split("_")[1], MOOD_TO_GROUP[key]
            n["follow-up (owner's note)"] += 1
        if section.startswith("unit_"):
            # a forecast sentence and its joke, written together: texts units_10 / units_11
            section = "units_" + section.split("_")[1]
        pool = doc.setdefault(section, {}).setdefault(key, [])
        if text not in pool:
            # starred lines first
            pool.insert(0, text) if verdict == "star" else pool.append(text)
            n["in"] += 1
    return n


def build_now(doc, lang, decisions):
    """The "now" lines: picked by what the Now drawing shows, so they stand
    alone and agree with it on every screen (the outfit alone, one drawing,
    or under the forecast line and the drawings, mixed with the day's).

    Until the rework round sorts every line, each now mood takes that
    mood's lines minus the ones round 10 voted "needs the fact"; nice,
    cool, evening and night weren't asked then and take theirs whole.
    """
    needs = {(d["path"].split("[")[0], d["text"]) for d in decisions.values()
             if d.get("round") == VISUAL and d.get("verdict") == "veto"}
    n = collections.Counter()
    for level in ("10", "11"):
        pools = doc.get(f"flavour_{level}", {})
        now = {}
        for mood in NOW_MOODS:
            lines = [t for t in pools.get(mood, []) if (f"flavour_{level}.{mood}", t) not in needs]
            if lines:
                now[mood] = lines
                n["lines"] += len(lines)
        doc[f"now_{level}"] = now
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
        now = build_now(doc, lang, decisions)
        print(f"{lang} now lines: {now['lines']}")
        alone = apply_alone(doc, lang, decisions)
        if alone:
            print(f"{lang} round 11: " + ", ".join(f"{v} {k}" for k, v in alone.items()))
        follow = apply_follow(doc, lang, decisions)
        if follow:
            print(f"{lang} round 12: " + ", ".join(f"{v} {k}" for k, v in follow.items()))
        seasons = apply_follow(doc, lang, decisions, SEASONS)
        if seasons:
            print(f"{lang} round 13: " + ", ".join(f"{v} {k}" for k, v in seasons.items()))
        facts14 = apply_facts(doc, lang, decisions, REPLIES)
        if facts14:
            print(f"{lang} round 14 forecast: " + ", ".join(f"{v} {k}" for k, v in facts14.items()))
        replies = apply_follow(doc, lang, decisions, REPLIES)
        if replies:
            print(f"{lang} round 14: " + ", ".join(f"{v} {k}" for k, v in replies.items()))
        facts15 = apply_facts(doc, lang, decisions, POLISH)
        if facts15:
            print(f"{lang} round 15 forecast: " + ", ".join(f"{v} {k}" for k, v in facts15.items()))
        polish = apply_follow(doc, lang, decisions, POLISH)
        if polish:
            print(f"{lang} round 15: " + ", ".join(f"{v} {k}" for k, v in polish.items()))
        for level in ("10", "11"):
            doc[f"units_{level}"] = {}  # rebuilt from the votes every run
        units = apply_follow(doc, lang, decisions, UNITS)
        if units:
            print(f"{lang} round 17 (units): " + ", ".join(f"{v} {k}" for k, v in units.items()))
        layers = apply_follow(doc, lang, decisions, LAYERS)
        if layers:
            print(f"{lang} round 18 (units): " + ", ".join(f"{v} {k}" for k, v in layers.items()))
        rain = apply_follow(doc, lang, decisions, RAIN)
        if rain:
            print(f"{lang} round 19 (units): " + ", ".join(f"{v} {k}" for k, v in rain.items()))
        for level in ("10", "11"):
            if not doc[f"units_{level}"]:
                del doc[f"units_{level}"]
        days = apply_follow(doc, lang, decisions, DAYS)
        if days:
            print(f"{lang} round 16: " + ", ".join(f"{v} {k}" for k, v in days.items()))
        write_new = apply_write_new(doc, lang, decisions)
        if write_new:
            print(f"{lang} write new: " + ", ".join(f"{v} {k}" for k, v in write_new.items()))
        garments = apply_garments(doc, lang)
        if garments:
            print(f"{lang} garments: {garments} follow-ups point at the forecast line's garment")
        words = apply_words(doc, lang)
        if words:
            print(f"{lang} words: {words} lines reworded")
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# Words the owner wants changed in every line, now and in later rounds
# (round 17): the screen's spot in the home is "room" in English, never a
# hallway. Applied last, so lines from any round pick it up.
WORDS = {"en": [("hallway", "room")]}


def apply_words(doc, lang):
    changed = 0
    for pools in doc.values():
        if not isinstance(pools, dict):
            continue
        for pool in pools.values():
            if not isinstance(pool, list):
                continue
            for i, text in enumerate(pool):
                if not isinstance(text, str):
                    continue
                new = text
                for old, repl in WORDS.get(lang, []):
                    new = new.replace(old, repl).replace(old.capitalize(), repl.capitalize())
                if new != text:
                    pool[i] = new
                    changed += 1
    return changed


# Follow-ups that point back at the garment the forecast line names. That
# garment changes (jacket, sweater, coat, hat and scarf), so the pronoun is
# filled in ({GP}: "it"/"them", "sie"/"ihn"), and a line that only fits
# some garments says which ({W:...}; block.liquid skips it on the others).
GARMENT = {
    "en": {
        "You'll forget it. Then you'll remember this moment.": "You'll forget {GP}. Then you'll remember this moment.",
        "Leave it behind and you'll think of me later. Not fondly.": "Leave {GP} behind and you'll think of me later. Not fondly.",
        "You'll put it on later and act like it was your idea.": "You'll put {GP} on later and act like it was your idea.",
        "Don't lose it in between. Like last time.": "Don't lose {GP} in between. Like last time.",
        "Shame. It was just getting comfortable.": "{W:coat,jacket,hoodie}Shame. It was just getting comfortable.",
    },
    "de": {
        "Und dann darfst du sie wieder überm Arm spazieren tragen.": "Und dann darfst du {GP} wieder überm Arm spazieren tragen.",
        "Und dann vergisst du sie irgendwo. Wie letztes Mal.": "Und dann vergisst du {GP} irgendwo. Wie letztes Mal.",
        "Und dann hängt sie den Rest des Tages über deinem Stuhl.": "{W:coat,jacket}Und dann hängt sie den Rest des Tages über deinem Stuhl.",
        "Und dann wieder die Jacke um die Hüfte binden? Bitte nicht.": "{W:jacket}Und dann wieder die Jacke um die Hüfte binden? Bitte nicht.",
        "Bitte nicht wieder die Ärmel um den Bauch knoten.": "{W:coat,jacket,hoodie}Bitte nicht wieder die Ärmel um den Bauch knoten.",
    },
}


def apply_garments(doc, lang):
    n = 0
    for level in ("10", "11"):
        for texts in doc.get(f"flavour_{level}", {}).values():
            for i, t in enumerate(texts):
                if t in GARMENT[lang]:
                    texts[i] = GARMENT[lang][t]
                    n += 1
    return n


def apply_facts(doc, lang, decisions, rnd):
    """Round 14: every forecast wording voted again, new ones beside them. A
    veto or Write new takes a wording out (never a situation's last one), an
    edit replaces it, a kept new wording goes in after the others."""
    path = REPO / "review" / "rounds" / f"{rnd}.json"
    votes = {(d["path"].split("[")[0], d["text"]): d for d in decisions.values() if d.get("round") == rnd}
    if not path.exists() or not votes:
        return collections.Counter()
    n = collections.Counter()
    facts = doc["facts"]
    rows = json.loads(path.read_text(encoding="utf-8"))["lines"]
    # new wordings first, so a vetoed last wording can make way for one
    for row in sorted(rows, key=lambda r: not r.get("new")):
        if row["lang"] != lang or row.get("role") != "fact":
            continue
        key = row["path"].split(".", 1)[1]
        d = votes.get((row["path"], row["text"])) or {}
        verdict = d.get("verdict", "")
        text = EDIT_FIX.get(d.get("edit"), d.get("edit")) or row["text"]
        texts = facts.setdefault(key, [])
        if row.get("new"):
            if verdict in ("star", "keep") and text not in texts:
                texts.insert(0, text) if verdict == "star" else texts.append(text)
                n["new in"] += 1
            continue
        if row["text"] not in texts:
            continue
        if verdict in ("veto", "rewrite"):
            if len(texts) > 1:
                texts.remove(row["text"])
                n["out"] += 1
            else:
                print(f"  facts.{key}: its only wording is vetoed; it stays until a new one is kept")
        elif text != row["text"]:
            i = texts.index(row["text"])
            if text in texts:
                texts.pop(i)
            else:
                texts[i] = text
            n["edited"] += 1
    return n


def apply_write_new(doc, lang, decisions):
    """Every round: "Write new" takes the line out, and the line it would have
    replaced. Last, so nothing an earlier step adds brings them back. A pool
    is never emptied: its last line stays until new ones are kept, and is
    reported (review/rewrite/<lang>.md lists what's waiting)."""
    rows = {}
    for f in sorted((REPO / "review" / "rounds").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("lines"), list):
            for line in data["lines"]:
                rows[(data.get("round", ""), line.get("lang", ""), line.get("text", ""))] = line
    n = collections.Counter()
    for d in decisions.values():
        if d.get("verdict") != "rewrite" or "." not in d.get("path", ""):
            continue
        section, key = d["path"].split("[")[0].split(".", 1)
        pool = (doc.get(section) or {}).get(key)
        if not isinstance(pool, list):
            continue
        row = rows.get((d.get("round", ""), lang, d.get("text", ""))) or {}
        out = {d["text"], EDIT_FIX.get(d.get("edit"), d.get("edit")) or d["text"]}
        if row.get("replaces") and row["replaces"] != "*":
            out.add(row["replaces"])
        for t in out:
            if t in pool and len(pool) > 1:
                pool.remove(t)
                n["taken out"] += 1
            elif t in pool:
                print(f"  {section}.{key}: {t!r} stays, the last line, until new ones are kept")
                n["waiting"] += 1
    return n


if __name__ == "__main__":
    main()
