# Writer's brief

This replaces the rulebook in [VOICE.md](VOICE.md) as the thing a writer
works from. It is short on purpose: what steers the writing is the
owner's taste, kept as examples, not adjectives.

## Who is talking

Settled by two auditions (October 2026):

- **The speaker is the TRMNL itself**, in both languages. Not a TV
  presenter, not a grandparent, not a friend ("the TRMNL is not
  moderating in a suit").
- **English:** the screen on your wall, talking about itself and a
  little too pleased with it.
- **German:** a grumbler (Grantler), in plain German with a southern
  accent at most. The TV-presenter variant lost badly.

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

### The fact line (round 2)

**Plain, full sentences** won in both languages; the timeline and the
as-few-words-as-possible styles were "robotic" across the board. The
fact line talks about the outfit on screen, then what changes, and says
why when it asks for something: "It cools down this evening, so bring a
jacket." / "Gegen Mittag kommt ein Schauer, also nimm den Schirm mit."
A steady day says the outfit works ("What you're wearing works for the
whole day"), not "no changes". Time words, not clock times. The current
templates are `facts` in `prototypes/fact-flavour/lang/`.

### What round 2 added about the flavour line

- **End on the joke.** Most notes were cuts: "remove the last
  sentence", "remove 'I'll be here, judging'", "remove 'Oder Problem'",
  "remove the Schnee at the start". Write the line, then cut everything
  after the laugh and everything before it that restates the weather.
- Kept lines with those cuts applied are the current pools in
  `prototypes/fact-flavour/lang/`, rebuilt from the votes by
  `review/rounds/build_pools.py`.

### What round 3 added (the writing round)

From 108 lines by Opus 5.5 (German +12 with 6 stars; English −11 with 1
star; Fable 5.1 could not run):

- **Evening doesn't assume going out either.** The screen may just be
  rotating through. Lines about other people going out, or with an "if",
  are fine; "where are you going?" is not.
- **Don't lean on the drawing.** "Don't reference the drawings that
  much": an English line about "this drawing" now and then, not every
  mood.
- **`mild` is the weak mood** in both languages: 1 of 6 German On lines
  survived, 1 of 3 English 11 lines. An ordinary day gives the joke
  nothing to push against.
- **English keeps, but rarely stars.** 31 keeps against 1 star: the
  screen voice is safe, not yet loved. German is close to done.

### The moods (round 4)

The flavour line is picked by the mood of the day, first match wins
(`prototypes/fact-flavour/block.liquid`). "Mild" turned out to be three
different days with nothing in common, so it was split. Shares are of
7:00 readings over two years in London, New York and Vienna; evening and
night come on top, by the clock, and steady evenings are the most common
state of all.

| Mood | The day | Share at 7:00 |
|---|---|---|
| `snow` | snow coming or falling | 2% |
| `wet` | rain coming, possible or stopping | 36% |
| `night` | steady, from 22:00 (the only mood that may mention bed) | |
| `evening` | steady, 18:00 to 22:00 (may or may not be going out) | |
| `fickle` | warms up, then cools again | 15% |
| `hot` | heat, or climbing into it | 2% |
| `cold` | winter coat or more, all day | 21% |
| `nice` | steady, pleasant, dry | 8% |
| `cooling` | ordinary dry day, a layer needed later | 2% |
| `warming` | ordinary dry day, a layer comes off later | 11% |
| `cool` | steady, cool jacket day | 3% |

Pools should be sized by share: the common moods repeat most.

### What round 4 added (the top-up)

172 lines, one writer per language, written in volume. German 3 stars,
39 keeps, 44 vetoes; English 0 stars, 42 keeps, 44 vetoes. "Not funny"
was the tag 72 times. Volume costs quality: write fewer lines and
throw more away before the owner sees them.

- **Standard German, not Austrian.** "eh", "nix", "wurscht", "Ja, eh",
  "Leut'" were all flagged as too Austrian for a German-wide audience,
  even in lines the owner liked.
- **Concrete scenes earn stars.** Every German star is something the
  reader has seen: Glühwein, the hardware store out of fans, "drei
  Flocken, und schon Schneechaos", the Hausmeister's big day, everyone
  staring at the Regenradar. Abstract quips get "not funny".
- **Generation and neighbour commentary works** ("früher war's kälter",
  the late-night washing machine), when the ending lands.
- **Warming and cooling stay hard.** The fact line already says what
  changes; few lines survived. They also draw from the `cool` pool now
  (`block.liquid`), so they're never empty.
- **English keeps but doesn't star.** 10 stars in four rounds. The
  screen voice is safe; it needs a sharper writer or a native ear.

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
