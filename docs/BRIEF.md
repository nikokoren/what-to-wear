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
| `wet` | rain coming, possible or stopping | 40% |
| `night` | steady, from 22:00 (the only mood that may mention bed) | |
| `evening` | steady, 18:00 to 22:00 (may or may not be going out) | |
| `fickle` | warms up, then cools enough to want the layer back | 11% |
| `hot` | heat, or climbing into it | 3% |
| `cold` | winter coat or more, all day | 20% |
| `nice` | steady, pleasant, dry | 6% |
| `cooling` | ordinary dry day, a layer needed later | 2% |
| `warming` | ordinary dry day, a layer comes off later (and stays off) | 14% |
| `cool` | steady, cool jacket day | 2% |

A day that warms up and only cools a little (the evening still warmer
than the morning, `arc_warmer`) is not `fickle`: its fact says the layer
"can come off and stay off", and the owner limited "Erst zu warm, dann
zu kalt" to days that cool down again (October 2026). Lines in the
`fickle` pool may assume the layer goes back on. Shares re-measured
then, on 2023 and 2024.

Pools should be sized by share: the common moods repeat most.

### Variance (round 5)

The owner's goal: repeats rare enough that nobody notices, closer to
Carrot Weather than to one line per mood. A line seen within the last
month counts as a repeat; `tools/climate/repeat_report.py` measures it.
Facts get several wordings each (small swaps are enough: "You're dressed
right for the whole day" next to "What you're wearing works for the
whole day"), and flavour lines get reworded twins placed a cycle apart.
Twins only stretch a pool; new jokes are what move the number.

### What round 5 added (variants)

- **Rewording a joke usually breaks it.** A third of the English twins
  and a fifth of the German ones were vetoed, nearly all "not funny":
  the original's exact wording was the joke ("I can hold this picture
  all night without power. Try that." beat "Your move."). Fact lines
  reword well; flavour lines need new material.
- **Evening: general observations, not the reader's plans.** "In case
  you're on your way out" doesn't work. Write about the end of a day in
  general: looking back on
  it, grumbling about it, about work, about the commute. Never assume
  where the reader is or what they did: they may have been home all day.
- **A steady cold day just says it stays cold.** "Keep everything on"
  after it is "boring and redundant"; the drawing shows the outfit.
- **Terse fact fragments read as robotic** ("Bis dahin Schirm.", "Kalt
  bis zum Abend, da bleibt alles an."). Full sentences.
- **No regional words the owner doesn't know**, northern ones included
  ("kirre").

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

### What round 6 added (evenings)

9 kept of 21. The German Feierabend scenes worked: the S-Bahn cancelled
on time, everyone in traffic calling it Feierabend, the "kurze
Rückfrage" just before six, the neighbour's drill.

- **An idea isn't a joke.** Five notes said "I like the idea, but it
  isn't funny": the line stated the observation and stopped. It needs
  a punch line, a turn at the end.
- **Don't rework a flat idea twice.** Second takes on the five
  liked-but-flat ideas: 1 kept of 10. If the first version of an idea
  doesn't land, drop the idea.
- **Work lines need their evening.** "Ignorierte Mails gehen nicht weg"
  read as "a random sentence about emails from your weather app". The
  kept ones carry their context: Feierabend, the Stau, the S-Bahn.
- **The TRMNL is a screen, not a wall.** "Perks of being a wall" was
  corrected to "a screen".

### What round 8 added (the re-read)

Every line the beta ships, voted again by the owner after seeing the
first ones on a device: 98 vetoed, 58 reworded on the page (round 8
facts 155 kept, 40 starred, 4 vetoed; sarcastic lines 245 kept, 58
starred, 69 vetoed, nearly all "not funny").

- **Don't assume a wall.** The screen may stand on a desk, a shelf or
  the fridge. "On a wall", "I can't leave the wall": out. "In here",
  "indoors", "my frame" work wherever it is.
- **Theme lines: the day in the sentence.** Not "Christmas. Joke." but a
  sentence the day belongs to: "Der Nikolaus hat in deinem Stiefel
  bestimmt nur Kohle gelassen", "Ich hab dem Krampus deine Adresse nicht
  gegeben. Noch nicht."
- **A fact must agree with the drawing.** While it rains the drawing
  has the umbrella, so "the rain is taking a break" reads as a lie. Say
  the order: rain for now, a break later, back this afternoon.
- **Hedge a guess about the reader.** The owner's edits added
  "vermutlich", "sicher", "lieber": "Irgendein Depp läuft vermutlich
  trotzdem in kurzen Hosen rum". The screen doesn't know; it guesses.
- **When two rounds vote the same line, the later vote stands.**

### What round 11 added (the lines on their own)

Every sarcastic line shown where it can appear (now lines alone under
their drawing, day lines under the forecast line). 350 lines, 41 "Write
new".

- **Two kinds of sarcastic line** (owner, October 2026). Under the
  forecast line, a line has to **build on it**: the ones that worked pick
  up what it said and twist it ("Taking that layer off might be the
  highlight of your day", "You'll put it on later and act like it was
  your idea", "Fifty-fifty that layer goes missing by tonight"). A line
  that is "fine on its own" reads as disconnected there ("sarcasm and
  forecast aren't flowing together"), and one that answers the forecast
  makes no sense without it ("You'll read all this, then do what you
  were going to anyway"). So: **follow-ups** only under the forecast
  line, written per situation; **standalone lines** everywhere else (the
  outfit alone, the drawings).
- **Seasonal lines.** Some only work at the start of the season ("every
  year everyone's surprised it's cold" is wrong in February; the boots
  still in the basement only at the first snow). A line can carry the
  months it shows in.
- **Twins are fine.** The owner kept both wordings of most round 5 twins.
- **Say what it means.** "Unclear" came with questions: what's "refresh
  on a schedule", "weather doesn't dress", "a neutral palette"? Plain
  images over clever ones.

### What rounds 12 and 13 added (follow-ups, seasons, riffs)

Round 12: 104 follow-ups and answers. Round 13: 157 lines from two
writers riffing on a scout's notes about the other language. English 0
stars, 31 keeps, 50 out; German 5 stars, 22 keeps, 49 out.

- **The follow-ups that land are short and answer the forecast line.**
  All five German stars of round 13 sit under "what you're wearing works
  all day" or "the layer comes off": „Da hätt ich heute auch frei nehmen
  können.“, „Dann kann ja nur noch alles andere schiefgehen.“, „Ob's dir
  steht, ist eine andere Frage.“, „Zumindest bis zum ersten
  Kaffeefleck.“, „Wohin damit, ist dann dein Problem. Ich sag nur das
  Wetter an.“ The owner's edits cut lines to their sharpest half and
  make them about "you" ("I'll know" → "I know you").
- **Scenes from elsewhere don't follow.** A follow-up that opens a new
  scene ("Somewhere a neighbour just picked up a drill", the pool's chip
  stand, the commute) reads as disconnected, however good the scene.
  English "somewhere, someone…" observations went out almost to a line.
- **Riffs travel badly.** Most ideas carried over from the other language
  were vetoed; the seasonal ones held up best (asparagus prices, the
  Brenner jam, Christmas trees on the pavement, "dark since four",
  browsing flights in January).
- **Don't time a line on something the screen can't know.** "You'll
  enjoy it right up to the first sneeze" is wrong once the sneeze has
  happened, and the screen can't tell. Cut that kind of line.
- **Don't assume where the reader is or what they're doing.** „Also Tür
  zu“ implies the door is open right now; the screen may sit on a desk.
  Nor that the TRMNL shows only this recipe: other frames showing the
  grandchildren could be this one.
- **The garment changes** (jacket, sweater, winter coat, hat and scarf):
  follow-ups to a layer coming off or going on say `{GP}`/`{G}` or list
  the garments they fit.

### What round 14 added (replies, forecast wordings, weather outliers)

622 lines: every forecast wording again with new ones, follow-ups, and
the new situations (big swings, cold fronts, dangerous heat, ice,
storms). A much better round: 200 stars, 329 keeps.

- **Suggest, don't command, on the big swings.** The owner's edits soften
  the shorts and long-pants advice ("think about wearing shorts",
  "maybe wear long pants", „Überleg dir …“, „eventuell“). Those lines
  were also too long and too complex: one idea, short.
- **The Now drawing is the weather right now.** The suggestion (shorts on
  a cold morning, long pants before a cold front) is the forecast line's,
  never the drawing's.
- **Storm and ice wordings lead with the danger.** "Bring the umbrella,
  then get inside when it hits: why the umbrella?" The ice warning is
  about the ice, not the umbrella; the thunder part must not be tacked
  on. Hedge what's uncertain ("may be icy").
- **"Until tonight" implies a change tonight.** A steady day's wording
  says all day.
- **Short replies keep winning** under the forecast line: „Wenigstens das
  Wetter ist heute mal unkompliziert.“, "No layer to carry today. Both
  hands free for snacks.", "That's your one reminder. I don't do push
  notifications."

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
