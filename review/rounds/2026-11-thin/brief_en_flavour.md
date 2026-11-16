# Top-up round (en, flavour): thin slots to four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in this language from scratch; never translate.

These slots have fewer than four live lines, and they are the ones that actually show on screen. Each heading says how many the critic will keep for the owner's vote and how many candidates to write (three times that). At most one candidate per slot may be out of the box (a different angle or form, still clear and on voice); mark it `"wild": true`.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening": the owner's own proofreading pass. Then `docs/CRITIC.md`: the critic cuts by it, so write so nothing on it applies.
- Read `review/rounds/2026-10-en-tight/changes.md`: every before and after of that pass.
- Read `review/examples/en.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
- Read `docs/PROOFREAD_EN.md`: the proofreader checks every line by it.
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

### `flavour_10.ice` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: freezing rain: icy roads and pavements. Never undercut the advice.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Walk like you're carrying a very full cup of coffee. Graceful is optional. Upright isn't.
- If you're late, blame the ice. It's the one excuse I'll back.
- Small steps today. Trust me, even though I haven't taken steps in years.
Voted out here (stay away):
- Move like me today: slowly, and not at all if possible. [not funny]
- Every railing in town is suddenly very popular. [not funny]
- Black ice is invisible. I can't see outside either, so assume it's everywhere. [not funny]
- Today the whole town is a free ice rink, minus the handrails and the fun. [not funny]
- The sidewalks may be glazed like a donut. All of the slip, none of the sugar. [not funny]
- Freezing rain looks harmless from in here. That's the trouble with in here. [not funny]
- The fastest way anywhere today is slowly. [not funny]
- Hold on to the umbrella. Hold on to the railing more. [robotic, not funny]

### `flavour_10.on` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: a layer is needed later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- That's your one reminder. I don't do push notifications.
- {W:coat,jacket,hoodie}Shame. It was just getting comfortable.
- {W:jacket,hoodie}It'll come out of the bag looking slept in. Still works.
Starred here before:
- Shame. It was just getting comfortable.
- You'll forget {GP}. Then you'll remember this moment.
- Later you'll pull {GP} on and say 'ah, that's better'. Out loud. You're welcome.
Voted out here (stay away):
- Pack it now, feel smug later. I'll feel smugger. [not funny]
- Today's understudy: {GP}. The big scene is later. [not funny]
- Being right later costs one layer now. Bargain. [not funny]
- Now: fine. Later: less fine. Me: fine throughout. [not funny]
- Sounds silly right now. That's exactly how it gets you. [not funny]
- First outing for {G} since spring. Brace yourself for the pockets. [not funny]
- Later you'll be the only one with {GP}. You'll mention it. Often. [not funny]

### `flavour_10.pants` (live now: 2; the critic keeps 3, write 9)

Follow-up under a forecast sentence: long pants on a shorts morning: a cold front later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- The warmth's lying to you. I'm not.
- Yes, a coat. Warm now doesn't mean warm later.
Starred here before:
- The sun's lying to you. I'm not.
- Yes, a coat. Yes, I can see the sun too. Just do it.
Voted out here (stay away):
- I've seen the afternoon. You haven't. [not funny]
- You'll feel overdressed at first. Then very well informed. [not funny]
- It's warm now. Emphasis on now. [not funny]
- A cold front's coming. They don't call ahead. I do. [not funny]
- Nothing says 'cold front coming' like a lovely morning. [not funny]
- The warm morning is a free sample. The full product is chilly. [not funny]
- I wouldn't suggest a coat on a morning like this for fun. I don't have fun. [not funny]
- Today's weather is a bait and switch. I don't do bait. [not funny]
- Long pants: the most boring good decision of the day. [not funny]
- A party up front, business later. The day's a reverse mullet. [not funny]
- A coat on a shorts morning. Odd now, smug later. [robotic, unclear]

### `flavour_10.shorts` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: go out in shorts on a cold morning: shorts weather later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your knees will have opinions at first. Ignore them.
- Brave call. Correct, but brave.
- Fortune favors the bare-kneed.
Voted out here (stay away):
- Trust me. I've never had cold legs. [not funny]
- Warm on top, shorts below. You'll look like you couldn't decide. [not funny]
- Shorts: the long game. [not funny]
- Commit to shorts now. The afternoon will back you up. [not funny]
- Goosebumps are temporary. Being right lasts all day. [not funny]
- It's the morning that's wrong, not the shorts. [not funny]
- The morning will say no. The day will say yes. I side with the day. [not funny]
- Every cold morning has one person in shorts. Today that's the right person. [not funny]
- Not shorts weather yet. Shorts weather soon. I deal in soon. [not funny]

### `flavour_10.storm` (live now: 2; the critic keeps 3, write 9)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- If the power goes out, I'll still be here, showing this.
- I'll stay in for this one. Then again, I always do.
Voted out here (stay away):
- All that flashing. Some of us manage fine without a backlight. [not funny]
- A thunderstorm: all noise, plenty of water, terrible manners. [not funny]
- All that thunder. I've never raised my voice in my life. [not funny]
- Thunder is just the sky being loud about something I already told you. [not funny]
- Thunder gets a ten for volume today. Two for subtlety. [not funny]
- Lightning goes for tall things. I'm small, flat and indoors. Feeling great. [not funny]
- Dear thunder, we heard you the first time. [not funny]
- Counting between flash and bang: the only math everyone does for fun. [not funny]
- Hair, umbrella, dignity: a storm takes them in that order. [not funny]
- Film it from inside. The thunder sounds just as good. [not funny]
- When it thunders, swap the umbrella for a roof. [not funny]
- Don't unplug me. I'm on battery and I'm not scared. [not funny, unclear] (note: unplug me from what?)

### `flavour_10.theme_force` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Star Wars Day, 4 May. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- These are the clothes you're looking for.
- I have a bad feeling about this. Kidding. It's fine.
- Wrong about the weather, I have never been.
Voted out here (stay away):
- Happy Star Wars Day. R2-D2 got a whole movie career. I got this room. [not funny]
- Star Wars Day. Every planet in that galaxy has exactly one weather. Must be nice. [not funny]
- Do or do not. There is no 'I'll check again in an hour.' [not funny]
- Star Wars Day. My only Jedi skill: knowing what you should wear. [not funny] (note: speak like yoda for may the 4th)
- May the fourth be with you. I sense no disturbance in the forecast. [not funny]

### `flavour_10.theme_ny` (live now: 3; the critic keeps 2, write 6)

THEME DAY: New Year's Day. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- I don't do New Year's resolutions. I was perfect last year too.
- New Year's outlook: scattered hangovers across the country.
- Twelve new months of me being right. You're welcome.
Starred here before:
- Every gym is full of New Year's resolutions today. Give it a week.
Voted out here (stay away):
- Happy New Year. 'New year, new me' posts outnumber the actual new people. [not funny]
- Happy New Year. Somewhere a calendar is going up that will stay on January until June. [not funny]

### `flavour_11.pants` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: long pants on a shorts morning: a cold front later.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Sure, check another app. It'll say the same thing.
- You'll want to argue now. Your legs will side with me later.
- Later you'll say 'where did that come from?' From right here.
Starred here before:
- Check another app if you like. It'll say the same thing, in colour.
Voted out here (stay away):
- Long pants. Your legs will thank me. You won't, but they will. [not funny]
- You want shorts. You've wanted a lot of things. [not funny]
- I'm not saying your legs are the problem. The cold front is. Mostly. [not funny]
- You'll carry the coat like a grudge. Then wear it like a hug. [not funny]

### `flavour_11.scorch` (live now: 2; the critic keeps 3, write 9)

Follow-up under a forecast sentence: dangerous heat: water and shade. Never undercut the advice.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- {AM}Do nothing at midday. Finally, a plan you're good at.
- You'll forget to drink, then wonder where the headache came from.
Voted out here (stay away):
- Not a day for proving anything. Not that you were going to. [not funny]
- Water, not heroics. You were never the heroic type. [not funny]
- Keep the bottle with you. It's the one accessory that suits you. [not funny]
- Nobody looks good red and sweaty. You'd be starting from behind anyway. [not funny]
- Today the shade is the cool kids' table. They'll let you sit there. Just today. [not funny]
- Refill the bottle before it's empty. You never do. [not funny]

### `flavour_11.storm` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- You'll still check the radar every five minutes. I'm hurt, frankly.
- You'll pretend the thunder didn't make you jump.
- The storm's getting more attention than you've had all year.
Voted out here (stay away):
- The umbrella won't save your hair. Nothing has so far. [not funny]
- The sky's moody today. You can stop competing. [not funny]
- You'll text someone 'did you hear that?' They did. Everyone did. [not funny]
- You'll call it over after one quiet minute. Optimist. [not funny]
- You'll say you love a good storm. From indoors, you do. [not funny]
- You'll count the seconds after every flash. From inside, please. [not funny]

### `flavour_11.theme_easter` (live now: 2; the critic keeps 3, write 9)

THEME DAY: Easter Sunday. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your 'Sunday best' is a clean T-shirt, isn't it?
- You're the reason the good chocolate gets hidden higher.
Voted out here (stay away):
- Happy Easter. Your painted eggs probably look like small accidents. [not funny]
- Happy Easter. A grown adult on an egg hunt. Show some dignity. Or win. [not funny]
- Easter Sunday. All those hidden eggs, and still nobody's looking for you. [not funny]
- Easter Sunday. Pastel suits nobody. It suits you even less. [not funny]
- Easter Sunday. You'll bite the ears off first. Everyone does. [not funny]
- You'll find the Easter chocolate faster than any child. [not funny]
- Happy Easter. Your diet starts again Monday. Like last Monday. [not funny]
- You'll eat a chocolate egg before breakfast and call it tradition. [not funny]

### `flavour_11.theme_ny` (live now: 2; the critic keeps 3, write 9)

THEME DAY: New Year's Day. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- You'll call this new year your year. You said that last year.
- Resolution check: still horizontal? Right on track.
Starred here before:
- You'll call this New Year your year. You said that last year.
Voted out here (stay away):
- Happy New Year. You'll write last year's date until March. [not funny]
- Happy New Year. Still you. Nobody got an upgrade. [not funny]
- New Year's Day. Everyone's sharing their year in review. Yours fits on a sticky note. [not funny]
- Happy New Year. You look like last night won. [not funny]
- Happy New Year. Fresh start. Same pajamas, probably. [not funny]

### `flavour_11.theme_spooky` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Halloween. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your Halloween costume is 'tired adult' again, isn't it?
- Try not to buy candy for trick-or-treaters and eat it by eight again this year.
- Kids will ask for candy. You'll hand out the kind you don't like.
Starred here before:
- Your Halloween costume is 'tired adult' again, isn't it.
Voted out here (stay away):
- Halloween. You'll say you're too old for it, then wear the hat.
- Halloween. You'll pretend you're not home when the doorbell rings. Same as every day. [not funny]
- Halloween. You could go without a costume. People would assume. [not funny]
- Halloween. I'm pale, flat and I stare. You're two out of three. [not funny]

### `flavour_11.theme_xmas` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Christmas, 24 to 26 December. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your relatives will ask about your plans this Christmas. At least make some up.
- The Christmas walk after lunch is the only exercise you'll get. Enjoy it.
- You'll say the Christmas cookies were for guests. There were no guests.
Voted out here (stay away):
- Merry Christmas. Act surprised. You've been rehearsing. [not funny, unclear]
- Christmas. You'll say 'just a small slice'. Twice. [not funny]
- Merry Christmas. You're wearing the new sweater, aren't you. [not funny]
- Christmas. Wear something that survives a second helping. [not funny]
- Christmas. Your Christmas sweater is ironic. Your waistband isn't. [not funny]
- Merry Christmas. I didn't get you anything. I'm a screen. What's your excuse? [not funny]
- Christmas. The tree's better dressed than you, and it's a tree. [not funny]
- Merry Christmas. You're wearing the new sweater, aren't you. [unclear]

## Output

Write `review/rounds/2026-11-thin/en.flavour.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
