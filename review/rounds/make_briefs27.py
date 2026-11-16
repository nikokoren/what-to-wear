#!/usr/bin/env python3
"""
Writer briefs for round 27 (November 2026): the groups still under four
lines after round 26, follow-ups left out (owner). The owner: "really
really make sure they are actually outside the box and new while still
being sarcastic. The level 11 ones had some good ones this round. On was
meh."

    python3 review/rounds/make_briefs27.py

Reads review/rounds/2026-11-thin2.cells.in.json ([lang, path, live]),
writes review/rounds/2026-11-thin2/cells.json ([lang, path, live, keep])
and one brief per language and family. Keep = shortfall + 2 (owner).
"""

import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import make_round12 as r12  # noqa: E402,F401
import make_round14 as r14  # noqa: E402
import make_round17 as r17  # noqa: E402

ROUND = "2026-11-thin2"
LAST = "2026-11-thin"
OUT = HERE / ROUND
D = {l: json.loads((REPO / "prototypes/fact-flavour/lang" / f"{l}.json").read_text()) for l in ("en", "de")}
DEC = {l: json.loads((REPO / "review/decisions" / f"{l}.json").read_text()) for l in ("en", "de")}
CELLS = [tuple(c) for c in json.loads((HERE / f"{ROUND}.cells.in.json").read_text())]
KEEP = {(l, w): 4 - n + 2 for l, w, n in CELLS}


def path_of(v):
    return (v.get("path") or "").split("[")[0].replace("unit_", "units_")


def votes(l, where, verdicts, n=15):
    out = []
    for v in DEC[l].values():
        if v.get("verdict") in verdicts and path_of(v) == where:
            out.append(v.get("edit") or v["text"])
    return list(dict.fromkeys(out))[-n:]


def last_round(l, lv, verdicts):
    return [(path_of(v), v.get("edit") or v["text"]) for v in DEC[l].values()
            if v.get("round") == LAST and v.get("level") == lv and v.get("verdict") in verdicts]


VF = {"wet": "rain comes or goes across the drawings", "cold": "cold all the way",
      "fickle": "the same outfit first and last with a change between (off and on again)",
      "cooling": "the last drawing is colder: a layer goes on", "warming": "the last drawing is warmer: a layer comes off"}
MOOD = {"nice": "nice T-shirt weather (feels 18-30 °C, sunny or light cloud)", "wet": "a wet day (rain now, coming, possible, or stopping)",
        "cooling": "it cools down later", "warming": "it warms up later", "fickle": "a changeable day: warm, then cold again"}
LEVEL = {"10": "On: sarcastic and dry, about the weather, the world, other people, or the screen itself. Never about the reader.",
         "11": "11: sarcastic and personal, about the reader. Looks and worth are fair game."}
VOICE = {"en": "English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug.",
         "de": "German, standard German, no dialect. The speaker is the screen itself: der Grantler, grumpy, dry. Native German only: the owner finds machine-sounding German the worst fault."}


def meaning(l, sec, key):
    if sec.startswith("units"):
        return ((r17.EXTRA.get(key) or r14.FACT_CTX[key])[2] +
                " UNIT: `forecast sentence || joke`, written together. Use a live forecast sentence below, unchanged or lightly varied (same placeholders, never new ones); the joke follows from it.")
    if sec.startswith("flavour_vf"):
        return "Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: " + VF.get(key, key) + ". The drawings show the change."
    return "The ONLY text on screen, under one drawing, no forecast sentence: " + MOOD.get(key, key) + ". It must work completely on its own."


def slot(l, where, n):
    sec, key = where.split(".")
    lv = sec.rsplit("_", 1)[-1]
    k = KEEP[(l, where)]
    L = [f"### `{where}` (live now: {n}; the critic keeps {k}, write {3 * k})\n", meaning(l, sec, key), "Level " + LEVEL[lv]]
    if sec.startswith("units"):
        facts = D[l]["facts"].get(key) or sorted({u.split(" || ")[0] for u in D[l][sec].get(key, [])})
        L.append("Live forecast sentences: " + " / ".join(f"\"{x}\"" for x in facts[:6]))
    live = D[l].get(sec, {}).get(key, [])
    if live:
        L.append("Live here (their ideas are taken):")
        L += [f"- {x}" for x in live]
    st = [x for x in votes(l, where, ("star",)) if x not in live]
    if st:
        L.append("Starred here before:")
        L += [f"- {x}" for x in st]
    vo = votes(l, where, ("veto", "rewrite"))
    if vo:
        L.append("Voted out here (these angles are dead; don't go near them):")
        L += [f"- {x}" for x in vo]
    L.append("")
    return L


def brief(l, fam, mine):
    L = [f"# Round 27 ({l}, {fam}): outside the box\n",
         "You write lines for a TRMNL e-ink weather screen, \"What to Wear\". " + VOICE[l] + " Write in this language from scratch; never translate.\n",
         "## What the owner wants this round\n",
         "The owner, after the last round: \"really really make sure they are actually outside the box and new while still being sarcastic. The level 11 ones had some good ones this round. On was meh.\" Every veto last round was tagged \"not funny\".\n",
         "- **Every** candidate must be out of the box, not one per slot. Out of the box means a surprising angle or form nobody on this screen has used yet: an unexpected comparison, a fake notice, a confession, a statistic the screen makes up about itself, a very specific scene, a reversal at the end. It does not mean random or absurd: it must still be clear on first read and still sarcastic.",
         "- **New**: before you keep a line, check it against every live line, starred line and voted-out line listed under its slot, and against the files below. Same idea in new words counts as a repeat.",
         "- **On (level 10) was meh.** The usual On moves are worn out: the screen being smug about living indoors, being dry, not feeling cold, being matte or gray, being right again; \"everyone checks me\"; restating the weather with a shrug. Don't use them. On is still never about the reader, so find the bite in the world, in other people's habits, in the weather's own pettiness, in the screen's strange job.",
         "- **11 worked better.** Look at what passed at 11 (listed below) for the energy: specific, confident, a little cruel, short.",
         "- Mark nothing `wild` this round; every line is.\n",
         "## Read first\n",
         "- `docs/BRIEF.md` (the voice, the levels, every lesson), above all \"Tightening\". Then `docs/CRITIC.md`.",
         f"- `docs/PROOFREAD_{l.upper()}.md`: the proofreader checks every line by it.",
         f"- `review/rounds/2026-10-{l}-tight/changes.md`: the owner's own before-and-after edits.",
         f"- `review/examples/{l}.md` (starred lines) and `review/dont/{l}.md` (vetoed lines).\n",
         "## Rules that still cost votes\n",
         "- Short: one or two short sentences. Clear on first read; never explain the joke.",
         "- No wordplay on the forecast's words, no \"like your X\" / „wie deine X“ jabs, no predicting the reader's mishaps.",
         "- Nothing the screen can't know: no clock words or seasons the slot doesn't guarantee, no assumptions about how the reader lives (car, pets, job, partner). Evening (18-22) is not bedtime.",
         "- Garment jokes must fit every garment the slot covers. A unit stays under 165 characters with the longest placeholder values.\n"]
    for lv in ("10", "11"):
        ok = last_round(l, lv, ("keep", "star"))
        if ok:
            L.append(f"## Passed last round at {'On' if lv == '10' else '11'} ({len(ok)}): the bar\n")
            L += [f"- `{p}`: {t}" for p, t in ok]
            L.append("")
    meh = last_round(l, "10", ("veto",))
    if meh:
        L.append(f"## Vetoed last round at On ({len(meh)}): \"meh\", don't write like this\n")
        L += [f"- {t}" for p, t in meh]
        L.append("")
    L.append("## Slots\n")
    for l2, w, n in mine:
        L += slot(l2, w, n)
    L += ["## Output\n",
          f"Write `review/rounds/{ROUND}/{l}.{fam}.raw.json`: `{{\"lines\": [{{\"path\": \"...\", \"text\": \"...\"}}]}}`, each slot's path exactly as in its heading. Add `\"months\"` (e.g. \"11,12,1,2\") only for a line that only fits some months. Check the file parses. Edit nothing else, don't commit."]
    return "\n".join(L) + "\n"


FAMS = {"units": lambda w: w.startswith("units_"), "drawings": lambda w: w.startswith("flavour_vf"), "alone": lambda w: w.startswith("alone")}

OUT.mkdir(exist_ok=True)
(OUT / "cells.json").write_text(json.dumps([[l, w, n, KEEP[(l, w)]] for l, w, n in CELLS]))
made = collections.Counter()
for l in ("en", "de"):
    for fam, f in FAMS.items():
        mine = [c for c in CELLS if c[0] == l and f(c[1])]
        if mine:
            (OUT / f"brief_{l}_{fam}.md").write_text(brief(l, fam, mine))
            made[f"{l} {fam}"] = sum(KEEP[(l, w)] for _, w, _ in mine)
print(dict(made), sum(made.values()))
