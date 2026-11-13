# Evening lines: requirements

What to Wear is a recipe for TRMNL, an e-ink screen people keep at home. It reads the local forecast and shows what to wear: an outfit drawing, a short plain forecast sentence, and, if the reader has turned sarcasm on, one sarcastic line. This document asks for that sarcastic line on the **evening screen**, which is new in v2.0. Several attempts at it failed; what failed and why is below.

## The evening screen

From **8 pm to midnight** the screen shows, left to right:

- **Tonight** (outlined tag): one drawing, either what the reader has on, labelled "now", or a change still coming tonight, labelled like "from 9 pm".
- **Tomorrow · Sat** (black tag): the outfit for the reader's usual time out the door (a setting; by default the coldest hour from 6 to 9 am), then the first change of tomorrow, labelled like "from 1 pm". If tomorrow doesn't change, one drawing labelled "all day".
- Under the drawings, in bold, **tomorrow's forecast sentence** (already written and approved, see below). When tonight still changes, today's sentence about it comes first.
- Under that, at sarcasm **On** or **11**, **the evening line**. This is what you write.

At midnight the screen goes back to normal: what to wear right now, through the day.

**The moment.** The reader looks at the screen in the evening, usually before bed, to see what to put on in the morning. They are not packing a bag and not heading out now (the owner, correcting an earlier brief).

## What you write

One sarcastic line, shown under tomorrow's sentence. It **must react to what tomorrow's weather is**. The screen picks the line from a pool for the kind of tomorrow:

| Pool | Tomorrow | An approved sentence it sits under |
|---|---|---|
| `rain` | rain from a time of day, or wet from the start | "Tomorrow it rains from 1 pm, so take the umbrella." / „Denk morgen an den Schirm, ab 13 Uhr regnet's.“ |
| `snow` | snow from a time of day, or snowing from the start | "Tomorrow, expect snow from 1 pm." |
| `colder` | gets colder from a time of day (any start: T-shirt to sweater, jacket to winter coat) | "Tomorrow the temperature drops from 1 pm, so pack something warm." / „Morgen wird's ab 13 Uhr kälter, dann brauchst du eine Schicht mehr.“ |
| `warmer` | warms up from a time of day (any start, up to heat) | "Tomorrow it warms up from 1 pm." |
| `drier` | wet start, dry from a time of day | "Tomorrow you'll need the umbrella at first. It's dry from 1 pm." |
| `steady` | the same outfit all day | "Tomorrow is a one-outfit day." / „Das Outfit für morgen passt den ganzen Tag.“ |
| `any` | fallback when a pool is empty | |

All approved sentences per pool are in `prototypes/panels/lang/<lang>.json` under `evening.facts` (`tmr_rain`, `tmr_wet`, `tmr_snow`, `tmr_snow_start`, `tmr_colder`, `tmr_warmer`, `tmr_drier`, `tmr_steady`). `{FROM}` there is filled with "from 1 pm" / „ab 13 Uhr“. A line in a pool must read well under **every** sentence of its pool.

**Levels.**

- **On** (`jokes_10`): sarcastic and dry, about the weather, the world, other people or the screen's own job. **Never about the reader**, never a nag or an order.
- **11** (`jokes_11`): sarcastic and personal, about the reader. Looks and worth are fair game. The owner has liked 11 best lately when it is specific, confident and a little cruel.

**Languages.** English (US spelling and words; the speaker is the TRMNL screen itself, a little too pleased with itself, dry, smug) and German (standard German, no dialect; the speaker is der Grantler, grumpy and dry). Write each language from scratch, never translate. **German must read like a native speaker wrote it**: the owner finds machine-sounding German the worst fault.

**Count.** Ideally 4 or more per pool, level and language that the owner keeps, so the hourly rotation doesn't repeat every evening. Only funny lines: the owner would rather vote on three strong lines than ten with filler.

## Hard rules

- **React to tomorrow's weather**, as heard the night before. Not "today", no present tense about weather that hasn't happened yet.
- **Don't restate the sentence above.** It already says what and when. Add a reaction, an image, a consequence.
- **Avoid "Tomorrow" as the first or last word.** The sentence above almost always starts with it.
- **No setup the screen doesn't give.** The owner vetoed „Ab dann haben wieder alle Omas recht.“ because the joke needs the reader to know grandmas always tell you to wear a scarf.
- **True to the drawings:** the figure has a simple face (dot eyes, a nose dash, a mouth line) and, from November 2026, no logo (the owner redrew the sprites). Faces are white, clothes are shades of gray.
- **Nothing the screen can't know:** no assumptions about the reader's job, partner, kids, car, commute or plans; no packing, no "lay it out tonight"; evening is not necessarily bedtime. Don't predict the reader's mishaps.
- **No wordplay** on the forecast's own words or on idioms around them ("cold feet", "rain on your parade").
- **Short:** one or two short sentences, clear on first read, never explain the joke. The sentence above and the line together stay under about 165 characters.
- **Not new means dead:** never repeat an idea from a live line or a starred line in the same language (see "Where things are"). A vetoed line is different: the veto may have been about its wording, so a topic vetoed once may come back with a clearly new take (owner, November 2026). Only a near-copy of a vetoed line is out.
- **Across languages:** never translate. The same idea in both languages is fine when each writer came to it on their own (owner, November 2026).

## Ideas that failed more than once (avoid unless you have a clearly new take)

- The screen knowing tomorrow before anyone else.
- Tonight-you against morning-you.
- The reader being useless or late in the morning.
- The forecast as an official notice, a final ruling, a rehearsal, a TV show or a sequel.
- "Tomorrow is just more of today."
- Laying out clothes or "putting out a smile" for tomorrow.
- Smug-screen moves at On: being indoors, dry, gray, always right, "everyone checks me".
- Dogs and the coming rain. Raincapes. Cold making people huddle "except with you". Pajamas. "Finally someone commits: the weather."

## What has passed (and what failed)

**Kept by the owner** (now live as the fallback or in their pool):

- On, any: "I've known about tomorrow since lunch. I sat on it until now for the drama."
- On, any: „Ich hab mich bei den Wettergöttern schon beschwert. Zu kurzfristig, hieß es.“
- On, any: „Das Gute: Man kann sich schon heute drüber ärgern. Das spart morgen Zeit.“
- 11, any: „Leg dir für morgen auch gleich ein Lächeln raus. Morgens findest du sonst wieder keins.“
- 11, rain: „Ich hab dich schon nass gesehen. Einmal reicht.“

**Vetoed as "not funny"** (33 lines). The full list with tags is in `review/decisions/<lang>.json`, rounds `2026-11-evening` and `2026-11-evening2`. A sample:

- "I know tomorrow's weather. The weather itself won't find out until morning."
- "I've seen tomorrow. You look tired in it."
- "This forecast is final. The weather can appeal in the morning."
- "Tomorrow hasn't seen you yet. Lucky tomorrow."
- „Allergiehinweis: Morgen kann Spuren von Montag enthalten.“
- „Morgen ist die Fortsetzung von heute. Fortsetzungen sind meistens schlechter.“
- „Die Hunde ahnen noch nichts.“
- „Bei Kälte rücken die Leute zusammen. Nur mit dir nicht.“

**Not yet voted:** eight English lines from the second attempt, in `review/rounds/2026-11-evening2/en.proofread.json`. The owner judged that approach not to be working, so treat them as ideas you may beat, not as a bar.

**Why the two attempts failed.**

1. The first attempt asked for one pool for every evening, in any weather and never mentioning it. With nothing to react to, ninety lines collapsed into the dead ideas above.
2. The second attempt keyed the lines to tomorrow's weather, but too many still leaned on a stock image (dogs, grandmas, huddling) or needed context the screen doesn't give.

What has worked across this project is a line that reacts to something specific on the screen with a confident twist, in very few words.

**Rounds 31 and 32** (written in the directions the owner picked in round 30, `review/rounds/make_round30.py`) brought in the lines now live, then a top-up that both critics cut to nothing (`review/rounds/2026-11-evening32/critic_<lang>.md`). The faults to avoid:

1. **Opening with a restatement.** "Warmer tomorrow.", "A one-outfit day.", „Wärmer morgen.“ in front of the joke. On screen it reads "Tomorrow it's warmer from 1 pm. Warmer tomorrow. …". Start with the reaction.
2. **One frame for a whole pool.** Four 11 lines all said "the outfit is taken care of, you're the problem", which the owner had already vetoed. The "I asked the weather…" frame is live three times; don't add a fourth.
3. **English and German telling the same joke.** Each language needs its own lines, not a translation. (Arriving at the same idea independently is fine.)
4. **German written from an English open.** „Wärmer morgen.“ is English word order. The owner finds this the worst fault.

## Where things are

- **Voice and every lesson:** `docs/BRIEF.md` (read "Tightening"), `docs/VOICE.md`, `docs/CRITIC.md`.
- **Proofreading checklists:** `docs/PROOFREAD_EN.md`, `docs/PROOFREAD_DE.md`.
- **The owner's taste:**
  - `review/examples/<lang>.md`: starred lines, by situation and level.
  - `review/dont/<lang>.md`: vetoed lines, with tags and notes.
  - `review/rounds/2026-10-<lang>-tight/changes.md`: the owner's own before-and-after edits.
- **Live lines** (don't repeat their ideas):
  - `prototypes/fact-flavour/lang/<lang>.json`: the daytime pools.
  - `prototypes/panels/lang/<lang>.json`, under `evening`: the evening texts.
- **Evening screen logic:** `prototypes/panels/evening.liquid`.

## Delivering

Put the lines into `prototypes/panels/lang/<lang>.json` under `evening.jokes_10` and `evening.jokes_11`, keyed by pool:

```json
"jokes_10": {"rain": ["…", "…"], "colder": ["…"], "any": ["…"]},
"jokes_11": {"rain": ["…"], "steady": ["…"]}
```

A tag in front of a line limits when it shows: `{P}` only with tonight's drawing beside tomorrow's; `{T}` only when tomorrow's sentence names a time; `{S}` only when tomorrow's sentence shows (the line points at it; the written forecast can be off); `{G}` only on a good day (dry, mild, unchanging); `{D:1,6}` only when tomorrow is one of those weekdays (0 Sunday … 6 Saturday).

Empty pools may be left out; the screen then uses `any`, and shows no line if `any` is empty too. Then rebuild and test:

```bash
python3 prototypes/panels/build.py
python3 prototypes/panels/test_switch.py
python3 tools/build_beta.py
```

`test_switch.py` checks the evening against whatever the pools hold, so new wording won't break it. Anything the owner hasn't approved should go to them for a vote first. The review page and the round tools (`review/rounds/make_round29.py`, `review/rounds/apply_evening.py`) take a candidates file like `review/rounds/2026-11-evening2/<lang>.json` (`{"lines": [{"path": "evening.jokes_10.rain", "text": "…"}]}`).
