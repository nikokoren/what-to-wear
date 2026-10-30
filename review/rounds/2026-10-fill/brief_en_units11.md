# Fill-up round (en, units11): every thin slot to at least four lines

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

### `units_11.arc_colder` (live now: 3)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top." / "{G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and maybe an extra layer." / "You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}." / "{WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and maybe an extra layer. || 'Maybe' is me being polite. Bring it.
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || You'll call it overkill. Then you'll wear it.
- {WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top. || And no, a hot drink isn't an extra layer.
Voted out here (stay away):
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || You'll bring the layer and lose {G}. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || Bring it, then wear it. Two separate skills. [not funny]

### `units_11.arc_level` (live now: 3)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{G} can come off {WHEN}, but you'll want {GP} back {WHEN2}." / "You can take {G} off {WHEN}. You'll want {GP} back {WHEN2}." / "Take {G} off {WHEN}, put {GP} back on {WHEN2}." / "{G} can come off {WHEN}. Keep {GP} handy for {WHEN2}." / "{G} won't be needed {WHEN}, but you'll want {GP} on again {WHEN2}." / "{WHEN} you can take {G} off, but you'll need {GP} again {WHEN2}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}. || Fifty-fifty {GP} goes missing in between.
- You can take {G} off {WHEN}. You'll want {GP} back {WHEN2}. || Then you'll say 'it's turned chilly' like it's news to you.
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}. || Off, on. The layer gets more exercise than you.

### `units_11.arc_warmer` (live now: 3)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{G} comes off {WHEN}. It cools a little later, but you won't need {GP} back." / "{G} can come off {WHEN}, and you won't need {GP} again today." / "{G} can come off {WHEN} and stays off." / "You can take {G} off {WHEN}. You won't need {GP} again after that." / "You can take {G} off {WHEN}. You won't need {GP} for the rest of the day." / "Once {G} comes off {WHEN}, you can leave {GP} off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {G} can come off {WHEN}, and you won't need {GP} again today. || You'll put {GP} back on later anyway, out of spite.
- You can take {G} off {WHEN}. Even later on, you won't need {GP}. || You'll still carry {GP} around all day. You're clingy like that.
- {G} comes off {WHEN}. It cools a little later, but you won't need {GP} back. || You'll want {GP} back. Wanting isn't needing.

### `units_11.c_coat` (live now: 2)

Cools to coat weather: the winter coat needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Don't leave the winter coat behind. You'll want it {WHEN}." / "Have the winter coat with you. You'll need it {WHEN}." / "It gets colder {WHEN}, bring the winter coat." / "{WHEN} it gets cold enough for the winter coat." / "Bring the winter coat. It gets colder {WHEN}." / "{WHEN} a jacket won't be enough, so bring the winter coat."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Bring the winter coat. It gets colder {WHEN}. || You'll say 'it's not that cold' right up until it is.
- Don't leave the winter coat behind. You'll want it {WHEN}. || You've done it before. We both remember.
Voted out here (stay away):
- Have the winter coat with you. You'll need it {WHEN}. || Carrying it now looks odd. Freezing later looks worse. [not funny]
- Have the winter coat with you. You'll need it {WHEN}. || With you. Not on the hook, looking at you. [not funny]
- {WHEN} it gets cold enough for the winter coat. || Cold enough for you to admit it, even. [not funny]
- You'll want the winter coat {WHEN}. || Yes, the number looks fine. The number isn't going outside. [not funny]

### `units_11.c_hoodie` (live now: 3)

Cools to sweater weather: a sweater needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} short sleeves won't be enough, so bring a sweater." / "Pack a sweater. You'll be glad to have it {WHEN}." / "It cools down {WHEN}, so bring a sweater." / "{WHEN} it gets cool enough for a sweater." / "Bring a sweater. It cools down {WHEN}." / "It gets cooler {WHEN}, so take a sweater along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Bring a sweater. It cools down {WHEN}. || Alternatively you can practice your 'I'm not cold' face for later.
- Pack a sweater. You'll be glad to have it {WHEN}. || Bringing a layer you won't need for hours. Look at you, prepared.
- It gets cooler {WHEN}, so take a sweater along. || You'll say you're fine without it. Your goosebumps will give you away.
Voted out here (stay away):
- It cools down {WHEN}, so bring a sweater. || You'll forget it. Then you'll remember this moment. [not funny]
- {WHEN} it gets cool enough for a sweater. || Pumpkin spice showed up in August. I wait for actual weather. [not funny, unclear] (note: i like the direction, but this is a bit confusing)

### `units_11.c_jacket` (live now: 3)

Cools to jacket weather: a jacket needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "A sweater alone won't do {WHEN}, so bring a jacket." / "Bring a jacket along. You'll want it {WHEN}." / "It cools down {WHEN}, so bring a jacket." / "{WHEN} it gets cool enough for a jacket." / "Bring a jacket. It cools down {WHEN}." / "It gets cooler {WHEN}, so bring a jacket along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Bring a jacket. It cools down {WHEN}. || You'll put it on later and act like it was your idea.
- Take a jacket along. You'll want it {WHEN}. || Leave it behind and you'll think of me later. Not fondly.
- It cools down {WHEN}, so bring a jacket. || Carrying a layer you don't need yet. How very grown-up.
Voted out here (stay away):
- A sweater won't do {WHEN}, so bring a jacket. || Or borrow someone's later and keep it for a year. [not funny]

### `units_11.c_relief` (live now: 2)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "It cools off a little {WHEN}, but stays warm." / "The heat eases {WHEN}, but it stays warm." / "{WHEN} it gets a little less hot. Still warm, though." / "Some relief from the heat {WHEN}, but it stays warm." / "{WHEN} the worst of the heat is over, but it stays warm." / "It's not as hot {WHEN}, but still warm."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The heat eases {WHEN}, but it stays warm. || So you can stop sticking to things. Mostly.
- The heat eases {WHEN}, but it stays warm. || Your mood might ease too. No promises.
Voted out here (stay away):
- It's not as hot {WHEN}, but still warm. || You'll say it's 'cooled right down'. It hasn't. [not funny]
- {WHEN} the worst of the heat is over, but it stays warm. || You'll still complain about the best of it. [not funny]
- {WHEN} it gets a little less hot. Still warm, though. || Less hot. Not cool. Calm down. [not funny]

### `units_11.p_drier` (live now: 1)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Take the umbrella for now. The rain stops {WHENSTOP}." / "It keeps raining for a while, then stops. Take the umbrella." / "The rain stops later, but you'll want the umbrella for now." / "Take the umbrella for now. The rain stops later." / "The rain eases off later, but bring the umbrella for now." / "Later the rain stops. For now, keep the umbrella with you."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Take the umbrella for now. The rain stops {WHENSTOP}. || Waiting it out is an option. Not a good one, but you like those.
Voted out here (stay away):
- It keeps raining for a while, then stops. Take the umbrella. || The sky looks sorry afterwards. It never apologises. [not funny]
- Take the umbrella for now. The rain stops later. || Then the birds start up again, as if they were never bothered. [not funny]
- The rain is here for now but stops later, so bring the umbrella. || It stops later. Your hair won't recover that fast. [not funny]
- The rain eases off later, but bring the umbrella for now. || You'll get it out just as it stops. That's the deal. [not funny]
- Later the rain stops. For now, keep the umbrella with you. || Later you can tell everyone it cleared up. I told you first. [not funny]

### `units_11.p_drier_snow` (live now: 2)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "It stops snowing {WHENSTOP}." / "The snow stops {WHENSTOP}." / "The snow stops later." / "It stops snowing later." / "The snow eases off later." / "It's snowing now, but it stops later."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It's snowing now, but it stops later. || Then it goes from 'magical' to 'still here?' in a day.
- It stops snowing later. || After that, the snow just lies around getting in the way. You two would get along.
Voted out here (stay away):
- Later on the snow stops. || Then every car wears a white hat for a few days. [not funny]
- The snow stops later. || Then the snowmen start appearing. Some of them are quite bad. [not funny]
- The snow stops later. || That's when the wet socks start. [not funny]
- The snow stops {WHENSTOP}. || I'd say 'enjoy it while it lasts', but I've given you the exact time. [not funny]
- Later on the snow stops. || Then you'll miss it. Briefly. [not funny]

### `units_11.p_snow_coming` (live now: 2)

Snow later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Snow moves in {WHENP}." / "There's snow on the way {WHENP}." / "It starts snowing {WHENP}." / "Snow starts {WHENP}." / "Expect snow {WHENP}." / "{WHENP} it will start to snow."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Expect snow {WHENP}. || You'll be surprised anyway.
- Snow moves in {WHENP}. || Finally, a reason to cancel the plans you were dreading.
Voted out here (stay away):
- Snow starts {WHENP}. || The first flake gets all the attention. The thousandth gets none. [not funny]
- It starts snowing {WHENP}. || You'll check out of the window every ten minutes. I'll be over here, correct. [not funny]

### `units_11.p_stays_wet` (live now: 1)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "There's no dry spell today. Bring the umbrella." / "The rain lasts all day, so keep the umbrella with you." / "Take the umbrella. The rain keeps going all day." / "It rains all day, so bring the umbrella." / "It's raining all day. Bring the umbrella." / "The rain doesn't stop today, so take the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It rains all day, so bring the umbrella. || All day. So no, waiting ten minutes won't help.
Voted out here (stay away):
- It rains all day, so bring the umbrella. || Today the bottom of every trouser leg belongs to the rain. [not funny]
- The rain lasts all day, so keep the umbrella with you. || Every bus smells of wet coat today. Every single one. [not funny]
- The rain lasts all day, so keep the umbrella with you. || All day means all day. Not 'until I'm bored of carrying it'. [not funny]
- The rain doesn't stop today, so take the umbrella. || Neither will your complaining. At least the rain has an excuse. [not funny]
- It's raining all day. Bring the umbrella. || Your hair has already lost. Make peace with it. [not funny]

### `units_11.p_stays_wet_snow` (live now: 2)

Snowing now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The snow doesn't stop today." / "It snows all day." / "It's snowing all day." / "The snow keeps coming all day." / "It won't stop snowing today." / "There's no break in the snow today."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {M:01,02,03}It snows all day. || You stopped finding it pretty about two snowfalls ago.
- There's no break in the snow today. || Not even for you.
Voted out here (stay away):
- The snow doesn't stop today. || Everything outside is the same shape now. A lump. [not funny]
- The snow keeps coming all day. || And you'll still call it 'unexpected'. [not funny]

### `units_11.p_wet_again` (live now: 0)

Raining now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The rain pauses later but picks up again {WHENP}, so don't put the umbrella away." / "It rains for now, stops for a bit, and starts again {WHENP}. Keep the umbrella." / "The rain stops for a while later, then comes back {WHENP}. Keep the umbrella with you." / "It keeps raining for now, then takes a break. It's back {WHENP}, so keep the umbrella." / "Rain for now, then a dry spell, then more rain {WHENP}. The umbrella stays with you." / "Later the rain takes a break, but it returns {WHENP}. Hang on to the umbrella."
Placeholders you may use: only those in the forecast sentence
Voted out here (stay away):
- Rain for now, a break, then more {WHENP}. Keep the umbrella. || Rain that leaves and comes back. I'd have more pride. [not funny]
- The rain pauses later but picks up again {WHENP}. Keep the umbrella. || A rainy day with a tea break. Union rules. [not funny]
- Rain for now, then a dry spell, then more rain {WHENP}. The umbrella stays with you. || Not 'stays wherever you had lunch'. [not funny]
- It rains for now, stops for a bit, and starts again {WHENP}. Keep the umbrella. || A bit. Long enough to think you've won. [not funny]
- The rain stops {WHENSTOP} and comes back {WHENP}. Keep the umbrella with you. || That dry bit is half-time. [not funny]

### `units_11.p_wet_again_snow` (live now: 1)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The snow stops {WHENSTOP} and starts again {WHENP}." / "The snow stops for a while later, then comes back {WHENP}." / "It keeps snowing for now, then takes a break. It's back {WHENP}." / "Snow for now, then a break, then more snow {WHENP}." / "The snow pauses later and starts again {WHENP}." / "It snows for now, takes a break, and starts again {WHENP}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It snows for now, takes a break, and starts again {WHENP}. || The break is mainly so the salt trucks can feel useful.
Voted out here (stay away):
- The snow pauses later and starts again {WHENP}. || Beginning, middle, more snow. Better structure than your week. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || Just enough of a gap to see the mess. Then it's covered up. [not funny]
- It keeps snowing for now, then takes a break. It's back {WHENP}. || It takes one break. You'll take three. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || The break is just long enough to start believing it's over. [not funny]
- After a break later on, the snow returns {WHENP}. || Like you to the fridge. [not funny]

### `units_11.p_wetter` (live now: 2)

Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "There's a short rain shower {WHENP}. Have the umbrella with you." / "There's a shower passing through {WHENP}, so bring the umbrella." / "A rain shower comes through {WHENP}, so take the umbrella." / "Bring the umbrella. There's a shower {WHENP}." / "Expect a rain shower {WHENP}. The umbrella's worth taking." / "{WHENP} there's a rainshower, so the umbrella comes along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- A shower comes through {WHENP}, so take the umbrella. || Or spend it in a shop, pretending to browse. You know the drill.
- Bring the umbrella. There's a shower {WHENP}. || Not enough rain to fill a puddle, but plenty to fill a shoe.
Voted out here (stay away):
- Expect a shower {WHENP}. The umbrella's worth taking. || With an umbrella it's weather. Without one, it's a story. [not funny]
- {WHENP} there's a shower, so the umbrella comes along. || Brief, wet, and gone. The perfect guest. [not funny]
- There's a shower passing through {WHENP}, so bring the umbrella. || It passes through. You'll take it personally. [not funny]
- A shower comes through {WHENP}, so take the umbrella. || It's a short one. Long enough to ruin your hair, though. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || Yes, the folding one that won't fold. That one. [not funny]
- There's a short shower {WHENP}. Have the umbrella with you. || With you means in your hand. Not in the other bag. [not funny]

### `units_11.p_wetter_long` (live now: 2)

Rain later, and it stays. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Pack the umbrella. Rain sets in {WHENP} and doesn't let up." / "It starts raining {WHENP} and keeps going, so bring the umbrella." / "The rain starts {WHENP} and doesn't stop. Bring the umbrella." / "Bring the umbrella. Once it starts raining {WHENP}, it keeps going." / "{WHENP} the rain sets in for good. Bring the umbrella." / "Rain arrives {WHENP} and stays, so take the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain starts {WHENP} and doesn't stop. Bring the umbrella. || It has more stamina than you. Most things do.
- Rain arrives {WHENP} and stays, so take the umbrella. || Staying in was your plan anyway. Now you have a reason.
Voted out here (stay away):
- {WHENP} the rain sets in for good. Bring the umbrella. || From then on, puddles are permanent until further notice. [not funny]
- It starts raining {WHENP} and keeps going, so bring the umbrella. || Keeps going, like your excuses for not taking it. [not funny]
- {WHENP} the rain sets in for good. Bring the umbrella. || For good. Not for your hair. [not funny]

### `units_11.p_wetter_maybe` (live now: 3)

Rain possible later, not likely. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "You might get some rain {WHENP}, so the umbrella could come in handy." / "Rain {WHENP} is possible but not likely. The umbrella is up to you." / "It might rain {WHENP}, so an umbrella wouldn't hurt." / "There's a chance of rain {WHENP}. An umbrella wouldn't hurt." / "Rain is possible {WHENP}, so maybe take the umbrella." / "It could rain {WHENP}. Take the umbrella to be safe."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- There's a chance of rain {WHENP}. An umbrella wouldn't hurt. || Your small umbrella exists for exactly this forecast.
- Rain is possible {WHENP}, so maybe take the umbrella. || I've done my bit. Now it's you versus the clouds.
- Rain is possible {WHENP}, so maybe take the umbrella. || Your app gives it a percentage so it can't be wrong. I give advice.
Voted out here (stay away):
- It might rain {WHENP}, so an umbrella wouldn't hurt. || The only gamble where losing just means wet shoes. [not funny]
- Rain is possible {WHENP}, so maybe take the umbrella. || Maybe. If you don't, it definitely will. [not funny]
- It could rain {WHENP}. Take the umbrella to be safe. || 'To be safe' isn't a phrase you use much, I've noticed. [not funny]
- You might get some rain {WHENP}, so the umbrella could come in handy. || So could most of what's in your bag. Allegedly. [not funny]

### `units_11.shorts_early` (live now: 3)

A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "It starts cool, but it's shorts weather {WHEN}." / "A cool start, then shorts weather {WHEN}." / "It's cool now, but {WHEN} it's warm enough for shorts." / "It's a bit cool for shorts now, but {WHEN} you'll be glad to have them." / "Shorts could be worth it today. It's cool now, but warm {WHEN}." / "{WHEN} it's warm enough for shorts, so think about putting them on now."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} it's warm enough for shorts, so think about putting some on now. || Very PE teacher of you. Still the right call.
- A cool start, then shorts weather {WHEN}. || You'll doubt me for the first hour. Then you won't admit I was right.
- It's cool now, but {WHEN} it's warm enough for shorts. || Your legs could use the daylight, frankly.
Voted out here (stay away):
- A cool start, then shorts weather {WHEN}. || Maybe go for shorts. You'll spend the first hour explaining your legs. [not funny, wrong garment]
- Shorts could be worth it today. It's cool now, but warm {WHEN}. || Could. Or go long and complain all afternoon. Your call. [not funny]
- It starts cool, but it's shorts weather {WHEN}. || The man who wore shorts all February will say he called it. [not funny]

### `units_11.w_coat` (live now: 2)

Warms up: the winter coat comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The winter coat can come off {WHEN}." / "You can take the winter coat off {WHEN}." / "{WHEN} it's warm enough to lose the winter coat." / "It warms up {WHEN}, so the winter coat can come off." / "{WHEN} you can do without the winter coat." / "You'll be fine without the winter coat {WHEN}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The winter coat can come off {WHEN}. || You'll overheat a little before you admit I was right.
- {WHEN} it's warm enough to lose the winter coat. || Not that you'll ever manage to fold it.
Voted out here (stay away):
- The winter coat can come off {WHEN}. || Suddenly you remember you have a shape. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || There's no chair in the world built for a winter coat. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || You'll take it off and remember what you're wearing under it. [not funny]
- {WHEN} you can do without the winter coat. || You can. Whether you will is your business. [not funny]
- The winter coat can come off {WHEN}. || Then you're just a person carrying a duvet. [not funny]

### `units_11.w_scarf` (live now: 2)

Warms up: hat, scarf and gloves come off, the coat stays. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "You'll be fine without the scarf {WHEN}." / "{WHEN} you won't need the scarf any more." / "It warms up {WHEN}, so the scarf can come off." / "The scarf can come off {WHEN}." / "You can take off the scarf {WHEN}." / "{WHEN} it's mild enough to lose the scarf."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It warms up {WHEN}, so the scarf can come off. || Today you're a coat rack with legs. Well done.
- The scarf can come off {WHEN}. || A very modest striptease. The coat stays on, thank goodness.
Voted out here (stay away):
- The hat, scarf and gloves can come off {WHEN}. || Three pockets, three things. You'll find two of them. [not funny]
- {WHEN} you won't need the hat, scarf and gloves any more. || You'll keep the hat on anyway. It's hiding something. [not funny]
- You can take off the hat, scarf and gloves {WHEN}. || And finally, people get to see your face again. Brace them. [not funny]
- The hat, scarf and gloves can come off {WHEN}. || Yes, all three. You can manage three. Probably. [not funny]
- It warms up {WHEN}, so the hat, scarf and gloves can come off. || Your hair's been under that hat for hours. Good luck. [not funny]

## Output

Write `review/rounds/2026-10-fill/en.units11.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
