# Top-up round (en, flavour): thin slots to four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in this language from scratch; never translate.

These slots have fewer than four live lines. Each heading says how many the critic will keep for the owner's vote and how many candidates to write (three times that). At most one candidate per slot may be out of the box (a different angle or form, still clear and on voice); mark it `"wild": true`.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening": the owner's own proofreading pass. Then `docs/CRITIC.md`: the critic cuts by it, so write so nothing on it applies.
- Read `review/rounds/2026-10-en-tight/changes.md`: every before and after of that pass.
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

### `flavour_10.cold` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: it stays this cold all day.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- All day. I checked twice, out of pure spite.
- Somewhere, someone in shorts didn't read this.
- If the sun shows up today, it's purely decorative.
Starred here before:
- You'll say 'it's freezing' twenty times today.
Voted out here (stay away):
- Batteries hate the cold. So do you. Dress warm.
- Scarf up to the nose today. [not funny]
- Cold. Dress like it. [not funny, unclear, wrong fact] (note: Not funny, not sarcastic, repeating the first line about the weather)
- Wind makes cold feel colder. Cover the bits that stick out. [not funny]
- I counted the layers twice. Correct both times. [unclear, not funny]
- I don't feel the cold. You do. That's the difference between us. [not funny]
- Cold slows everything down. I had a head start. [not funny, unclear]
- I'll be on the wall. The warm side. [not funny]
- I'd soften it, but I only do accurate. [not funny, unclear]
- Your phone will claim it's dead at thirty percent. Drama queen. [not funny, unclear]
- The cold can't touch me. Nothing can. I'm on a wall. [not funny]
- Today's drawing is mostly coat. I'm very proud of the coat. [not funny]
- Today I'm showing mostly coat. Proud of that coat. [not funny]
- I'd say it in a warmer colour, but I only have grey. [not funny]
- Someone will say 'at least it's a dry cold'. All day. [not funny]

### `flavour_10.evening` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: 18:00 to 22:00: what you're wearing works for the rest of the evening.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Whatever the evening brings, your outfit won't be the problem.
- No changes tonight. I checked. It's what I do instead of TV.
- Breaking news: nothing. More at eleven.
Starred here before:
- And there's plenty of it. It's been dark since about four.
- That leaves the evening free for losing your remote. Again.
Voted out here (stay away):
- Today's to-dos are tomorrow's now. My only to-do: be right. [not funny]
- I've looked this good all day without a mirror. [unclear, not funny]
- Your to-do list carried over again. Mine's blank. Screen life. [not funny]
- Going out is overrated, says the screen that never has. [not funny]
- A steady evening. Which makes me the most interesting thing in the room again. [not funny]
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

### `flavour_10.hot` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: heat: stays hot, gets hot later, or eases a little; water and shade.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- I'd come along, but I only work in range of your WiFi.
- You'll cross the road for a strip of shade the width of a lamppost.
- Not for me, thanks. Water and I don't get along.
Starred here before:
- I'll sit this one out in your nice shady hallway.
- Thin, pale and cool. I was made for this.
- Somebody cranked the outside too high. Wasn't me.
- Finally, a use for the fancy bottle you bought to drink more water.
- No sweat here. One of the perks of being a screen.
Voted out here (stay away):
- Melting is for candles and lesser screens. [not funny]
- I give off no heat. Just charm. [not funny]
- Somewhere, a weather presenter is saying 'scorcher'. I'd never. [unclear, not funny]
- Today rewards staying very still. At last, my sport. [unclear]
- Stay in the shade. It's where all the cool screens hang out. [not funny]
- Water and shade are on you. Staying cool is my thing. [not funny]
- I stay cool to the touch. A seatbelt buckle can't say that. [not funny]
- Every patch of shade out there will soon have someone guarding it. [not funny, robotic, unclear] (note: not flowing well with the forecast.)
- Iced coffee isn't water. I checked the spelling. [not funny]

### `flavour_10.ice` (live now: 3; the critic keeps 3, write 9)

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
- Hold on to the umbrella. Hold on to the railing more. [robotic, not funny]

### `flavour_10.night` (live now: 1; the critic keeps 5, write 15)

Follow-up under a forecast sentence: from 22:00: the same line, late.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Not that anyone will see it at this time of day. Except me.
Starred here before:
- I'm the one screen that won't keep you up. You're welcome.
- It also works for bed, I'm told.
Voted out here (stay away):
- That's all from me tonight. Sleep well. [not funny]
- Late. I'm on battery, you're on coffee. Let's both rest. [not funny]
- I've never lain awake at night. I've never lain down. [not funny]
- At this hour, I'm the only one here still making sense. [not funny]
- Overnight update: there won't be one. [not funny]
- Nothing changes overnight. My favorite kind of night: uneventful and correct.
- Quiet night ahead. Even the weather's turned in. [not funny]
- Everything stays put until morning. Including me. Especially me.
- And 'the rest of the evening' should be about five minutes now. [not funny]
- Still showing this at three in the morning. Hopefully to nobody. [not funny]
- Tomorrow's forecast will be ready before you are. As always. [not funny]
- Your phone probably said bedtime an hour ago. Listen to one of us. [not funny, unclear]
- Good. One less thing to lie awake thinking about. [not funny]
- Somewhere a neighbour's washing machine is just starting its spin. [not funny]
- You'll see the fridge light a few more times before bed, I'm guessing. [not funny]

### `flavour_10.offon` (live now: 2; the critic keeps 4, write 12)

Follow-up under a forecast sentence: a layer comes off, then back on in the evening.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Off and on again. That fixes most things, me included.
- I'll redraw you both times. No extra charge.
Starred here before:
- Two outfit changes in one day. Very pop star of you.
Voted out here (stay away):
- I predicted both halves. Most forecasts only manage one.
- The warmth is a loan. It's due back this evening.
- Layer status today: on, off, on. I'll keep the minutes.

### `flavour_10.on` (live now: 3; the critic keeps 3, write 9)

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
- Sounds silly right now. That's exactly how it gets you. [not funny]
- First outing for {G} since spring. Brace yourself for the pockets. [not funny]
- Later you'll be the only one with {GP}. You'll mention it. Often. [not funny]

### `flavour_10.pants` (live now: 2; the critic keeps 4, write 12)

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
- A coat on a shorts morning. Odd now, smug later. [robotic, unclear]

### `flavour_10.rain` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: a rain line: shower later, rain all day, rain stopping, or rain now.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Rain or not, my humor stays bone dry.
- Then you can be smug at everyone sheltering in doorways. I love the feeling.
- Open it outside, please. I don't need the bad luck.
Starred here before:
- Open it outside, please. You can't afford the bad luck.
- Bring it back, too. I'm keeping count.
Voted out here (stay away):
- Forecast delivered. What happens to the umbrella next is on you. [not funny, unclear]
- That's my rain forecast. The umbrella's forecast is less certain. [not funny, robotic, unclear]
- I'd hold it for you, but I'm not that kind of screen. [unclear, not funny] (note: what kind of screen holds stuff?)
- You own at least four. Any one of them will do. [not funny]
- You'll keep it closed through the whole shower. 'It's only spitting.' [not funny]
- The one with the bent spoke still counts. Just about. [not funny]
- You'll judge the rain by other people's umbrellas. [not funny]
- You'll try to open it with one hand, like in films. It won't. [not funny]
- And afterwards you'll open it to dry and trip over it. [not funny]
- My most-read sentence all week. Also my most ignored. [not funny]
- Summer, as advertised. [robotic] (note: not flowing well with the forecast.)
- That was in bold. For me, that's shouting. [not funny]

### `flavour_10.scorch` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: dangerous heat: water and shade. Never undercut the advice.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- For once, staying in with me is the sensible choice.
- I'll handle the forecast. You handle refilling that bottle.
- I'd say it nicer, but it's too hot for nice.
Voted out here (stay away):
- The coolest spot in the house is the floor. I won't tell anyone. [not funny]
- Today the smartest thing outside is a lizard under a rock. Be the lizard. [not funny]
- Heat like this isn't a challenge. Nobody's handing out medals. [not funny]
- Today the shade is worth more than the view. [not funny]
- I don't do the midday sun either. Look how well I've turned out. [not funny]
- Plenty of water today. Not the sip-and-forget kind. [not funny]
- I'm staying in the shade too. I recommend the company. [not funny]
- You and the houseplants both need watering today. I don't. [not funny]

### `flavour_10.shorts` (live now: 2; the critic keeps 4, write 12)

Follow-up under a forecast sentence: go out in shorts on a cold morning: shorts weather later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Your knees will have opinions at first. Ignore them.
- Brave call. Correct, but brave.
Voted out here (stay away):
- Trust me. I've never had cold legs. [not funny]
- Warm on top, shorts below. You'll look like you couldn't decide. [not funny]
- Shorts: the long game. [not funny]
- Commit to shorts now. The afternoon will back you up. [not funny]
- Goosebumps are temporary. Being right lasts all day. [not funny]
- It's the morning that's wrong, not the shorts. [not funny]

### `flavour_10.snow` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: a snow line: snow later, all day, or stopping.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Everyone will act shocked anyway. I'm used to it.
- Somewhere, a school is already drafting the snow-day email.
- I've never once slipped on ice. Never left the house, either.
Voted out here (stay away):
- Snow is basically e-ink for the outdoors. I approve. [not funny]
- Snow falls at about my refresh speed. Elegantly. [not funny]
- Everything goes quiet in snow. I was quiet first. [not funny]
- Snow gets more photos than I do. I'm not bitter. [not funny, unclear]
- Grown adults go giddy over snow. I remain composed. [not funny, unclear]
- I've only heard about snow. Tell me everything later. [not funny]
- You'll say it won't settle. You say that every time. [not funny]
- Snow on schedule. I'd take a bow if I had a waist. [unclear]
- Pretty through the window. Less pretty inside your shoe. [not funny]
- Cue the bread-and-milk panic. Nobody's ever explained the milk. [not funny]
- Everyone will be nine for an hour, then ninety on the ice. [not funny, unclear]

### `flavour_10.steady` (live now: 3; the critic keeps 3, write 9)

Follow-up under a forecast sentence: what you're wearing works all day.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- No layer to carry today. Both hands free for snacks. Excellent!
- The one forecast I could do in my sleep.
- Unlike your phone battery.
Starred here before:
- Same look all day, no updates. You'd make a decent e-ink screen.
- No layer to carry today. Both hands free for snacks.
Voted out here (stay away):
- One outfit, all day, no plot twists. Restful, isn't it? [not funny]
- Nothing to update. I'll just stand here being right. [not funny, unclear, robotic] (note: forecast and sarcasm arent working together.)
- Get dressed once and you're done. I do the same, permanently. [not funny]
- In spring, that practically makes me a miracle worker. [not funny]

### `flavour_10.storm` (live now: 2; the critic keeps 4, write 12)

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
- Film it from inside. The thunder sounds just as good. [not funny]
- When it thunders, swap the umbrella for a roof. [not funny]
- Don't unplug me. I'm on battery and I'm not scared. [not funny, unclear] (note: unplug me from what?)

## Output

Write `review/rounds/2026-10-onfill/en.flavour.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
