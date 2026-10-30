# Fill-up round (en, flavour10): every thin slot to at least four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in this language from scratch; never translate.

The owner reviewed every live line. These slots have fewer than four lines. For EACH slot write **9 candidates in the slot's established style plus 3 out-of-the-box ones** (a genuinely different angle or form the slot has never tried, still clear and on voice). A critic keeps the best 5-6 plus one out-of-the-box line per slot for the owner's vote, and the owner will cut some.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson).
- Read `review/examples/en.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
- Skim `review/dont/en.md`: vetoed lines with tags and notes. Never go near those.

## Rules that cost the most votes

- Sarcasm with bite; never merely pleasant, never a restatement of the weather. Clear on first read, short (one or two short sentences).
- No wordplay on the forecast's words, no "like your X" / „wie deine X“ jabs, no predicting the reader's mishaps, never explain the joke.
- Nothing the screen can't know; no assumptions about how the reader lives. Evening (18-22) is not bedtime.
- Garment jokes must fit every garment the slot covers. Storms: no "get inside" lectures. The extra-cold layer is just the scarf.
- Each joke sits at one level: On is not about the reader; 11 is.
- The room, never the hallway (en). Keep the device's spot in the home vague (de).
- No line may repeat another candidate's idea, or a live line's.

## Slots

### `flavour_10.day_dst_fall` (live now: 1)

SPECIAL DAY: the Sunday the clocks go back, and the Monday after. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- An extra hour this weekend. I'd ask what you did with it, but I know.
Voted out here (stay away):
- Clocks back. An hour you didn't earn. Don't spend it all at once. [not funny]
- The clocks went back. An extra hour, and I spent it refreshing. [not funny]
- Clocks went back. If you're early for everything today, that's why. [not funny]

### `flavour_10.day_dst_spring` (live now: 0)

SPECIAL DAY: the Sunday the clocks go forward, and the Monday after. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- One hour less this weekend. Don't look at me, I didn't take it. [not funny]
- The clocks went forward. I'd say 'feel refreshed', but I don't lie. [not funny]
- Clocks forward, an hour gone. I didn't notice. I don't sleep. [not funny]
- Clocks forward. Lighter evenings soon. You paid for them in sleep. [not funny]

### `flavour_10.day_friday` (live now: 3)

SPECIAL DAY: Friday afternoons, from noon. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- No weekends for me, but no Mondays either. Fair trade.
- My weekend plans: be right, the whole time.
- Weekend plans? The outfit's ready. That's my part done.
Voted out here (stay away):
- Friday afternoon. The slowest hours of the week, and I see every one. [not funny]
- Friday afternoon. Whatever happens tonight, I wasn't there. [not funny]
- Friday afternoon. Everyone slows down. I'm e-ink, I was already slow. [not funny]

### `flavour_10.day_longest` (live now: 1)

SPECIAL DAY: the longest day of the year. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- I look my best in daylight. There's loads of that today.
Voted out here (stay away):
- Longest day of the year. From tomorrow, it's all downhill. Enjoy. [not funny]
- Longest day of the year, and your outfit lasts all of it. Value. [not funny]

### `flavour_10.day_monday` (live now: 2)

SPECIAL DAY: Monday mornings, before noon. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Monday morning. At least one of us is fully charged.
- I don't do weekends, so I don't get what the fuss is about.
Voted out here (stay away):
- Monday. I look exactly as good as I did on Friday. [not funny]
- Monday. I've never had the Sunday-night dread. Sounds awful. [not funny]
- Monday. The weekend went by in about four minutes, didn't it. [not funny]
- Monday morning. I'm the only thing in the house not annoyed about it. [not funny]

### `flavour_10.day_shortest` (live now: 0)

SPECIAL DAY: the shortest day of the year. Shows on a dry, steady day under the fixed sentence "What you're wearing works for the rest of the day." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Shortest day of the year. Turn a light on later. I can't glow. [not funny]
- Shortest day of the year. Blink and you'll miss it. I don't blink. [not funny]
- Shortest day of the year. It improves from tomorrow. You're welcome. [not funny]

### `flavour_10.evening` (live now: 3)

Follow-up under a forecast sentence: 18:00 to 22:00: what you're wearing works for the rest of the evening.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Whatever the evening brings, your outfit won't be the problem.
- {M:11,12,01}And there's plenty of it. It's been dark since about four.
- That leaves the evening free for losing your remote. Again.
Starred here before:
- And there's plenty of it. It's been dark since about four.
Voted out here (stay away):
- Off somewhere? I'll hold the wall down. [not funny]
- Today's to-dos are tomorrow's now. My only to-do: be right. [not funny]
- I've looked this good all day without a mirror. [unclear, not funny]
- Your to-do list carried over again. Mine's blank. Screen life. [not funny]
- Going out is overrated, says the screen that never has. [not funny]
- Same outfit, new lighting. Evenings are generous like that. [not funny]
- The leftovers in your fridge, less so. [not funny]
- Also fine for a Christmas party. The dancing's out of my hands. [not funny, unclear]
- It works for going out, too. In theory. [not funny]
- The weather's sorted for the evening. The washing-up isn't. [not funny]
- The weather's the easy part of tonight. [not funny]
- Of everything tonight, the weather is the easy bit. [not funny]
- My plans for tonight: this wall. It's a great wall. [not funny] (note: Mine is on a wall, but other's might be standing on a desk or shelf.)
- Somewhere a neighbour just picked up a drill. For the rest of the evening. [not funny]
- The trains are another story. [not funny]

### `flavour_10.ice` (live now: 3)

Follow-up under a forecast sentence: freezing rain: icy roads and pavements. Never undercut the advice.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Walk like you're carrying a very full cup of coffee. Graceful is optional. Upright isn't.
- If you're late, blame the ice. It's the one excuse I'll back.
- Small steps today. Trust me, even though I haven't taken steps in years.
Voted out here (stay away):
- Move like me today: slowly, and not at all if possible. [not funny]
- Hold on to the umbrella. Hold on to the railing more. [robotic, not funny]

### `flavour_10.night` (live now: 2)

Follow-up under a forecast sentence: from 22:00: the same line, late.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- It also works for bed, I'm told.
- Not that anyone will see it at this time of day. Except me.
Starred here before:
- I'm the one screen that won't keep you up. You're welcome.
Voted out here (stay away):
- I look just as good in the dark. You can't tell. [not funny, unclear]
- I'll hold this picture all night on no power. Your move. [not funny]
- That's all from me tonight. Sleep well. [not funny]
- Late. I'm on battery, you're on coffee. Let's both rest. [not funny]
- I've never lain awake at night. I've never lain down. [not funny]
- At this hour, I'm the only one here still making sense. [not funny]
- And 'the rest of the evening' should be about five minutes now. [not funny]
- Still showing this at three in the morning. Hopefully to nobody. [not funny]
- Tomorrow's forecast will be ready before you are. As always. [not funny]
- Your phone probably said bedtime an hour ago. Listen to one of us. [not funny, unclear]
- Good. One less thing to lie awake thinking about. [not funny]
- Somewhere a neighbour's washing machine is just starting its spin. [not funny]
- You'll see the fridge light a few more times before bed, I'm guessing. [not funny]

### `flavour_10.offon` (live now: 3)

Follow-up under a forecast sentence: a layer comes off, then back on in the evening.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Off and on again. That fixes most things, me included.
- Two outfit changes in one day. Very pop star of you.
- I'll redraw you both times. No extra charge.

### `flavour_10.pants` (live now: 2)

Follow-up under a forecast sentence: long pants on a shorts morning: a cold front later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Yes, a coat. Yes, I can see the sun too. Just do it.
- The sun's lying to you. I'm not.
Voted out here (stay away):
- I've seen the afternoon. You haven't. [not funny]
- You'll feel overdressed at first. Then very well informed. [not funny]
- A coat on a shorts morning. Odd now, smug later. [robotic, unclear]

### `flavour_10.scorch` (live now: 2)

Follow-up under a forecast sentence: dangerous heat: water and shade. Never undercut the advice.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- For once, staying in with me is the sensible choice.
- I'll handle the forecast. You handle refilling that bottle.
Voted out here (stay away):
- The coolest spot in the house is the floor. I won't tell anyone. [not funny]
- I don't do the midday sun either. Look how well I've turned out. [not funny]
- Plenty of water today. Not the sip-and-forget kind. [not funny]
- I'm staying in the shade too. I recommend the company. [not funny]
- You and the houseplants both need watering today. I don't. [not funny]

### `flavour_10.shorts` (live now: 2)

Follow-up under a forecast sentence: go out in shorts on a cold morning: shorts weather later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your knees will have opinions this morning. Ignore them.
- Brave call. Correct, but brave.
Voted out here (stay away):
- Trust me. I've never had cold legs. [not funny]
- Warm on top, shorts below. You'll look like you couldn't decide. [not funny]

### `flavour_10.storm` (live now: 2)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- If the power goes out, I'll still be here, showing this.
- I'll stay in for this one. Then again, I always do.
Voted out here (stay away):
- All that flashing. Some of us manage fine without a backlight. [not funny]
- Film it from inside. The thunder sounds just as good. [not funny]
- When it thunders, swap the umbrella for a roof. [not funny]
- Don't unplug me. I'm on battery and I'm not scared. [not funny, unclear] (note: unplug me from what?)

### `flavour_10.theme_bike` (live now: 0)

THEME DAY: World Bicycle Day, 3 June. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- World Bicycle Day. The forecast's the same at any speed. [not funny]
- World Bicycle Day. The outfit works on a bike too. [not funny]
- World Bicycle Day. No pedals, no wheels and no complaints. That's me. [not funny]
- World Bicycle Day. I've never cycled. Never had a flat tyre, either. [not funny]

### `flavour_10.theme_easter` (live now: 2)

THEME DAY: Easter Sunday. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Happy Easter. Unlike the eggs, the forecast isn't hidden.
- Happy Easter. One egg will turn up in July. There's always one.
Voted out here (stay away):
- The Easter bunny and I both work today. Only one of us hops. [not funny]
- Happy Easter. I'm the only screen in here with no chocolate on it. [not funny]

### `flavour_10.theme_force` (live now: 2)

THEME DAY: Star Wars Day, 4 May. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- These are the clothes you're looking for.
- I have a bad feeling about this. Kidding. It's fine.
Voted out here (stay away):
- Star Wars Day. My only Jedi skill: knowing what you should wear. [not funny] (note: speak like yoda for may the 4th)
- May the fourth be with you. I sense no disturbance in the forecast. [not funny]

### `flavour_10.theme_ghd` (live now: 2)

THEME DAY: Groundhog Day, 2 February. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Today a rodent does my job, and gets a crowd. Pathetic.
- I'll be here long after the groundhog's in bed.
Voted out here (stay away):
- Groundhog Day. Nobody has ever asked the groundhog about umbrellas. [not funny]
- Over and over? Amateur. I've done it for years. Happy Groundhog Day. [not funny]

### `flavour_10.theme_ny` (live now: 2)

THEME DAY: New Year's Day. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- I don't do New Year's resolutions. I was perfect last year too.
- Every gym is full of New Year's resolutions today. Give it a week.

### `flavour_10.theme_okt` (live now: 2)

THEME DAY: Oktoberfest, 20 September to 5 October. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Someone has to stay sober and do the forecast.
- So would a dirndl, apparently.
Voted out here (stay away):
- Oktoberfest. Somewhere there's a pretzel bigger than me. I'm fine. [not funny]
- Oktoberfest. The forecast stays steady. Everyone else, less so. [not funny]
- Oktoberfest. One full stein weighs more than I do. Think about that. [not funny]
- It's Oktoberfest. I don't do the chicken dance. I don't do any dance. [not funny]

### `flavour_10.theme_pi` (live now: 2)

THEME DAY: Pi Day, 14 March. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- I'm a rectangle, so I'll be sitting this one out.
- Today's forecast: exactly one outfit. No decimals.
Voted out here (stay away):
- Pi Day. I could show you the digits, but I'd run out of screen. [not funny]
- Happy Pi Day. I've done the maths for today. You can have the pie. [not funny]

### `flavour_10.theme_spooky` (live now: 3)

THEME DAY: Halloween. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Everyone's dressing up for Halloween. I'm going as a screen again.
- Pale, staring, never blinking. I've been dressed for Halloween all year.
- That ghosting on my screen? It's for Halloween.

### `flavour_10.theme_tdf` (live now: 1)

THEME DAY: the Tour de France, 1 to 23 July (every steady day for three weeks). Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- The Tour riders get a rest day. I don't. Not that I'm complaining.
Voted out here (stay away):
- It's Tour de France time. Lycra is optional for the rest of us. [not funny]
- Tour de France riders eat about six dinners a day. Don't get ideas. [too long]
- Tour de France. Every rider has a team car. You have me. [not funny]
- Two hundred kilometres for the Tour riders today. One outfit for you. [wrong fact] (note: we cant make sure that this is actually true.)
- The Tour riders change jerseys more often than you'll change today. [not funny]

### `flavour_10.theme_thanks` (live now: 2)

THEME DAY: Thanksgiving. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- This Thanksgiving, I'm thankful I don't have to eat anything.
- After Thanksgiving dinner, I'll be the only one not napping.
Voted out here (stay away):
- Thanksgiving. I won't bring up politics. I'm a weather screen. [robotic, not funny] (note: i like the direction. but the joke doesnt land)

### `flavour_10.theme_xmas` (live now: 2)

THEME DAY: Christmas, 24 to 26 December. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Of all the Christmas decorations, I'm the only one that knows the forecast.
- Merry Christmas. Unlike the tree, I'll still be up in February.
Voted out here (stay away):
- Merry Christmas. The weather's not the point today. [robotic]
- Christmas Day. Staying in counts as a plan. [robotic]
- Unlike the Christmas tree, I'll still be up in February. [not funny, unclear]

## Output

Write `review/rounds/2026-10-fill/en.flavour10.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
