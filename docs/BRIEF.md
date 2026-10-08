# Writer's brief

This replaces the rulebook in [VOICE.md](VOICE.md) as the thing a writer
works from. It is short on purpose: what steers the writing is the
owner's taste, kept as examples, not adjectives.

## Who is talking

Leading after the first audition, to be settled by round 2:

- **English:** the screen on your wall, talking about itself and a
  little too pleased with it.
- **German:** a grumbler, in plain German with a southern accent at
  most, or a grumbling TV weather presenter. Round 2 has both.

The tip is a fact line plus a flavour line (`prototypes/fact-flavour/`).
Only the flavour line has a voice; sarcasm Off shows the fact alone.

| Setting | The flavour line is |
|---|---|
| Off (`0`) | absent |
| On (`10`) | sarcastic, dry |
| `11` | sarcastic and personal: it's about you |

### What the first voice audition settled (October 2026)

From 160 votes and the owner's notes (`review/decisions/`):

- **On is sarcastic too.** "Not sarcastic" was the most common note on
  On lines. Friendly or merely pleasant lines get vetoed.
- **Never restate the weather.** The fact line already said it. "Cold
  out.", "Nass heute.", "Rain." in front of a joke get cut. (Exception the
  owner starred: a pure grumble like "Regen. Wieder. Natürlich.", where
  the restatement is the joke.)
- **No clothing advice in the flavour line.** Garments the fact line
  didn't name ("wear an undershirt") are wrong garment. A joke about a
  garment is fine.
- **Evening is not bedtime.** From 18:00 people check the screen before
  going out. No going home, no tea, no bed, no end-of-day before 22:00;
  after that a `night` pool may talk about bed.
- **Light regional colour, not dialect.** The Grantler won German but was
  "too Bavarian". No "Alter". No rhymes ("not a poetry slam").
- **What worked:** English, the screen talking about itself ("I'm a
  screen on a wall. Even I'd go outside today."). German, the Grantler's
  grumbling and the TV Wetterfrosch's patter ("Und schon wieder ein Tief.
  Ich kann nichts dafür.").
- **What failed everywhere:** deadpan restatement, epic narration,
  trivia, rhymes, the caring grandparent, the buddy.
- A line that's great once can wear thin daily ("good for the first cold
  day in a while"). Prefer lines that survive repetition.

## What to read before writing, in this order

1. **The facts of the key** in [SCENARIOS.md](SCENARIOS.md): when it
   fires, what the drawing shows, which tokens resolve. These are hard
   rules. A line that is funny and wrong is vetoed.
2. **`review/taste.md`**: lines the owner likes from anywhere, and lines
   from this corpus they dislike, each with one word for why.
3. **`review/examples/<lang>.md`**: lines the owner starred on the review
   page. Write lines that would sit beside them.
4. **`review/dont/<lang>.md`**: vetoed lines with their reasons. Never
   reuse one, or its sentence frame.

## How to write a round

- **One situation at a time.** Write for the screen the line appears on:
  the drawing, the time words filled in, and the rain half it is paired
  with. `python3 tools/review_export.py --keys <key>` renders those.
- **Five candidates for every line needed.** The owner keeps the best;
  the rest are thrown away, not repaired.
- **Few lines per key.** A reader sees one line a day. Three great lines
  beat twelve passable ones; `perfect` and `c_relief` earn more because
  they show most often.
- **German is written in German**, against the German examples, never
  translated from the English. Write it without the English open. No
  German line may share its joke or concept with an English one, even
  reworded; both languages get their own material. German has plenty:
  Kaiserwetter, Aprilwetter, meckern, Oma's "zieh dir was Warmes an", the
  Funktionsjacke, socks in sandals, Hitzefrei, the Regenradar, the trains
  in snow, clearing the Gehweg, Tatort, gemütlich. A starting point, not a
  checklist. Facts too: idiomatic German ("heute Abend braucht's eine Jacke"), not
  the English sentence in German words.
- **Run `python3 tools/style_report.py <lang>`** before handing over. It
  flags the habits that made the last corpus read as generated: objects
  given a job (the jacket's "shift", the rain's "calendar"), semicolons,
  ", because" explanations, and repeated sentence frames.

Hard limits that stay: no temperatures in the text, the 165-character
budget for the full tip (`tools/check_combinations.py`), and the token
rules in [TRANSLATING.md](TRANSLATING.md).

## Handing a round over

A round is a candidates file, `review/rounds/<round>.json`:

```json
{"round": "2026-11-perfect",
 "lines": [{"lang": "en", "path": "temp_10.perfect", "text": "...", "batch": "A"}]}
```

`batch` is shown on the page only as a letter. To compare two writers
blind, give each a letter and keep which is which out of the repo until
the votes are in. The full loop is in [review/README.md](../review/README.md).
