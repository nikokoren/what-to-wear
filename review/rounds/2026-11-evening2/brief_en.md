# Evening pilot (en): the evening line, by tomorrow's weather

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in this language from scratch; never translate.

## Why this round exists

The last evening round failed: the owner vetoed 25 of 29 evening lines as "not funny" and called the round disgraceful. The brief behind it was wrong. It asked for one pool of lines that work in any weather and never mention it, so the lines had nothing to react to and collapsed into three ideas: the screen knows tomorrow first, tonight-you versus morning-you, the reader is useless in the morning. Every line that has ever worked on this screen reacts to something on it. This round fixes that: one small pool per kind of tomorrow, and each line reacts to that weather.

## The moment

8 pm to midnight. The reader glances at the screen before bed to see what to put on in the morning. They are not packing a bag and not heading out now. The screen shows tonight on the left, and under a black "Tomorrow · Sat" tag tomorrow's outfit for their usual time out the door, then the next change ("from 1 pm"). Under the drawings, tomorrow's sentence in bold, then your line.

## Read first

- `docs/BRIEF.md`, above all "Tightening", then `docs/CRITIC.md`.
- `docs/PROOFREAD_EN.md`.
- `review/examples/en.md`: the owner's starred lines. Study the sections for rain/wet, cold and on/c_*, steady and evening: these are the bar. Work out why they land (a specific image, a confident twist, short), and do that, not their words.
- `review/dont/en.md`: vetoed lines.
- The live pools in `prototypes/fact-flavour/lang/en.json` (flavour_10/11 rain, on, steady, cold, evening; now_10/11 wet, cold, evening): never repeat an idea from them.

## Rules

- **React to tomorrow's weather**, as someone hearing it the night before. Rain tomorrow, a colder afternoon tomorrow, a day that doesn't change tomorrow. Never "today", never present tense about weather that isn't happening yet.
- **Don't restate the sentence.** It already says when and what. Add a reaction, an image, a consequence.
- **On (level 10)**: about the weather, the world, other people, the screen's odd job. Never about the reader, never a nag. Banned On moves: the screen smug about being indoors, dry, gray or always right; "everyone checks me"; the screen knowing the future first.
- **11**: about the reader: looks, worth, habits. Specific, confident, a little cruel. Short.
- No assumptions about job, partner, kids, car, commute or plans. No packing, no "lay it out tonight". Evening is not necessarily bedtime.
- One or two short sentences, clear on first read, never explain the joke. Don't predict the reader's mishaps.
- Only funny lines. If you only have three good ones in a slot, deliver three good ones and say so: nothing here may be filler.

## What passed last time (the only ones)

- I've known about tomorrow since lunch. I sat on it until eight for the drama.

## Vetoed last time (dead ideas: don't go near them)

- I know tomorrow's weather. The weather itself won't find out until morning.
- Bakers get up at four to get the day ready. I had tomorrow done by eight.
- Tomorrow's a fresh start. For the weather.
- Looking ahead to tomorrow already? Today went that well, huh?
- Notice: tomorrow's outfit has been chosen. Your input was considered and rejected.
- The evening news makes everyone wait for the weather. I lead with it.
- Tomorrow's weather is taken care of. Tomorrow's hair is on you.
- Tomorrow hasn't seen you yet. Lucky tomorrow.
- Tomorrow's outfit took me longer than today's. It had to look effortless.
- I show you tomorrow a night early. Frankly, you need the head start.
- You've read tomorrow's forecast. Probably the most reading you'll do tonight.
- I've seen tomorrow. You look tired in it.
- This forecast is final. The weather can appeal in the morning.
- I've watched tomorrow twice already. The middle drags.

## The other language's vetoed lines (also dead, as ideas)

- Ich mach diese Vorschau extra für dich. Andere Leute wissen auch so, was sie anziehen.
- Ich sag's dir schon heute. Dann hast du die ganze Nacht Zeit, es falsch zu verstehen.
- Die Sachen für morgen sehen gut aus. Solange du nicht drinsteckst.
- Am Abend vorher sieht jeder Tag harmlos aus. Das ist seine Masche.
- Allergiehinweis: Morgen kann Spuren von Montag enthalten.
- Morgen ist die Fortsetzung von heute. Fortsetzungen sind meistens schlechter.
- Schön, dass du dir mal Gedanken um deine Kleidung machst. Gemerkt hat man's bisher nicht.
- Morgen ist das Wetter früher wach als dein Gesicht.
- Hinweis: Diese Vorschau ist unverbindlich. Der Tag selbst leider nicht.
- Abends ist jeder ein Frühaufsteher. Morgens komischerweise keiner.
- Die Sachen für morgen legst du sicher wieder auf den Stuhl. Zu denen von letzter Woche.

## Slots

### `evening.jokes_10.rain`

Tomorrow it rains from some time of day on (the sentence names it), or it's wet from the start. The second drawing has the umbrella.
Tomorrow's sentence above your line will be one of: "Tomorrow there's rain from 1 pm. Bring the umbrella." / "Tomorrow it rains from 1 pm, so take the umbrella." / "Tomorrow you'll want the umbrella. It rains from 1 pm."
Level On. Write up to 10; the critic keeps at most 2.

### `evening.jokes_11.rain`

Tomorrow it rains from some time of day on (the sentence names it), or it's wet from the start. The second drawing has the umbrella.
Tomorrow's sentence above your line will be one of: "Tomorrow there's rain from 1 pm. Bring the umbrella." / "Tomorrow it rains from 1 pm, so take the umbrella." / "Tomorrow you'll want the umbrella. It rains from 1 pm."
Level 11. Write up to 10; the critic keeps at most 2.

### `evening.jokes_10.colder`

Tomorrow gets colder from some time of day on: the second drawing wears more.
Tomorrow's sentence above your line will be one of: "Tomorrow it's colder from 1 pm." / "Tomorrow the temperature drops from 1 pm, so pack something warm." / "Tomorrow it gets colder from 1 pm, so bring something warmer."
Level On. Write up to 10; the critic keeps at most 2.

### `evening.jokes_11.colder`

Tomorrow gets colder from some time of day on: the second drawing wears more.
Tomorrow's sentence above your line will be one of: "Tomorrow it's colder from 1 pm." / "Tomorrow the temperature drops from 1 pm, so pack something warm." / "Tomorrow it gets colder from 1 pm, so bring something warmer."
Level 11. Write up to 10; the critic keeps at most 2.

### `evening.jokes_10.steady`

Tomorrow doesn't change: one drawing, labelled 'all day'.
Tomorrow's sentence above your line will be one of: "Tomorrow you can wear one outfit all day." / "Tomorrow is a one-outfit day." / "Tomorrow, one outfit works from start to finish."
Level On. Write up to 10; the critic keeps at most 2.

### `evening.jokes_11.steady`

Tomorrow doesn't change: one drawing, labelled 'all day'.
Tomorrow's sentence above your line will be one of: "Tomorrow you can wear one outfit all day." / "Tomorrow is a one-outfit day." / "Tomorrow, one outfit works from start to finish."
Level 11. Write up to 10; the critic keeps at most 2.

## Output

Write `review/rounds/2026-11-evening2/en.raw.json`: `{"lines": [{"path": "evening.jokes_10.rain", "text": "..."}]}`. Check it parses. Edit nothing else, don't commit.
