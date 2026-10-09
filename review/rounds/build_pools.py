#!/usr/bin/env python3
"""
Rebuilds the flavour pools in prototypes/fact-flavour/lang/ from the votes:
every starred or kept line of the winning voice, with the owner's notes
applied as edits.

    python3 review/rounds/build_pools.py

Reads review/decisions/<lang>.json (written by tools/review_sync.py).
Seasonal pools (theme_*) are left as they are.
"""

import collections
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
MOODS = ["nice", "cool", "warming", "cooling", "cold", "hot", "wet", "snow", "fickle", "evening", "night"]

# The winning voice in each round, as (round, set) pairs.
WIN = {
    "en": {("2026-10-voices", "B"), ("2026-10-voices-2", "W"), ("2026-10-writing", "E2")},
    "de": {("2026-10-voices", "G"), ("2026-10-voices-2", "Y"), ("2026-10-writing", "D1")},
}
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
    "Ohne Haube rausgehen und dann jammern. Kenn ma schon.": None,
    "Wennst ohne Schirm gehst, brauchst nachher nicht jammern.": None,
    "Feierabend. Jetzt lass mich auch in Ruh.": None,
}
# Round 4 split "mild" in three. The mild lines the owner kept all talk
# about an unremarkable day, which is the steady one.
MOOD_RENAME = {"mild": "cool"}
# Lines the owner moved to a later hour.
MOVE = {"Nothing new from me tonight. Sleep well.": "night",
        "You've looked at me a lot today. Go to bed.": "night"}


def main():
    for lang, winners in WIN.items():
        decisions = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        pools = collections.defaultdict(lambda: collections.defaultdict(list))
        for d in decisions.values():
            if (d.get("round"), d.get("batch")) not in winners or d.get("verdict") not in ("star", "keep"):
                continue
            text = EDIT.get(d["text"], d["text"])
            if text is None:
                continue
            mood = MOVE.get(d["text"], MOOD_RENAME.get(d["key"], d["key"]))
            entry = (d["verdict"] != "star", text)  # starred lines first
            if entry not in pools[d["level"]][mood]:
                pools[d["level"]][mood].append(entry)
        path = REPO / "prototypes" / "fact-flavour" / "lang" / f"{lang}.json"
        doc = json.loads(path.read_text(encoding="utf-8"))
        for level in ("10", "11"):
            old = doc[f"flavour_{level}"]
            new = {m: [t for _, t in sorted(pools[level][m])] for m in MOODS if pools[level][m]}
            new.update({k: v for k, v in old.items() if k.startswith("theme_")})
            doc[f"flavour_{level}"] = new
            print(f"{lang} {level}: " + "  ".join(f"{m} {len(new.get(m, []))}" for m in MOODS))
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
