# Fill-up round (en, units10): every thin slot to at least four lines

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

### `units_10.arc_colder` (live now: 0)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top." / "{G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, and maybe an extra layer." / "You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}." / "{WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top."
Placeholders you may use: only those in the forecast sentence
Voted out here (stay away):
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || On top, not instead. I know you. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || A round trip for {GP}. The evening brings a friend. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Evenings look warmer from inside. I go by numbers. [unclear] (note: help me fine tune that)
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Carry it all, then wear it all. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || The warm bit is a trick. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || You'll come home in more layers than you left in. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The day ends colder. Like my jokes. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Plus. I don't say 'plus' lightly. [not funny]
- {WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top. || 'Something warm'. I trust you. A bit. [not funny]

### `units_10.arc_level` (live now: 2)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{G} can come off {WHEN}, but you'll want {GP} back {WHEN2}." / "You can take {G} off {WHEN}. You'll want {GP} back {WHEN2}." / "Take {G} off {WHEN}, put {GP} back on {WHEN2}." / "{G} can come off {WHEN}. Keep {GP} handy for {WHEN2}." / "{G} won't be needed {WHEN}, but you'll want {GP} on again {WHEN2}." / "{WHEN} you can take {G} off, but you'll need {GP} again {WHEN2}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Take {G} off {WHEN}, put {GP} back on {WHEN2}. || Off and on again. That fixes most things, me included.
- {G} can come off {WHEN}. Keep {GP} handy for {WHEN2}. || Handy means with you. Not 'somewhere you'll remember later'.

### `units_10.arc_warmer` (live now: 3)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{G} comes off {WHEN}. It cools a little later, but you won't need {GP} back." / "{G} can come off {WHEN}, and you won't need {GP} again today." / "{G} can come off {WHEN} and stays off." / "You can take {G} off {WHEN}. You won't need {GP} again after that." / "You can take {G} off {WHEN}. You won't need {GP} for the rest of the day." / "Once {G} comes off {WHEN}, you can leave {GP} off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Once {G} comes off {WHEN}, you can leave {GP} off. || Leave {GP} off. Not 'leave {GP} somewhere'.
- {G} can come off {WHEN} and stays off. || I'm not changing my mind about this one.
- You can take {G} off {WHEN}. || After that, you're just carrying {GP} around for company.
Voted out here (stay away):
- {G} can come off {WHEN} and stays off. || You'll say 'it's got a bit chilly' later. Not chilly enough. [not funny]
- You can take {G} off {WHEN}. You won't need {GP} again after that. || I'd say goodbye, but you'll see {GP} tomorrow. [not funny]
- You can take {G} off {WHEN}. Even later on, you won't need {GP}. || Even later. I checked the whole day. You're welcome. [not funny]

### `units_10.c_coat` (live now: 3)

Cools to coat weather: the winter coat needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Don't leave the winter coat behind. You'll want it {WHEN}." / "Have the winter coat with you. You'll need it {WHEN}." / "It gets colder {WHEN}, bring the winter coat." / "{WHEN} it gets cold enough for the winter coat." / "Bring the winter coat. It gets colder {WHEN}." / "{WHEN} a jacket won't be enough, so bring the winter coat."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Bring the winter coat. It gets colder {WHEN}. || Carrying it until then counts as exercise. Barely.
- Have the winter coat with you. You'll need it {WHEN}. || Yes, the big one. The one that doesn't fit in any bag.
- {WHEN} a jacket won't be enough, so bring the winter coat. || The jacket will try. Bless it.

### `units_10.p_drier` (live now: 1)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Take the umbrella for now. The rain stops {WHENSTOP}." / "It keeps raining for a while, then stops. Take the umbrella." / "The rain stops later, but you'll want the umbrella for now." / "Take the umbrella for now. The rain stops later." / "The rain eases off later, but bring the umbrella for now." / "Later the rain stops. For now, keep the umbrella with you."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain stops {WHENSTOP}, but you'll want the umbrella before that. || That's all the good news that I have for today.
Voted out here (stay away):
- Take the umbrella for now. The rain stops {WHENSTOP}. || Then everything's wet and shiny and acts innocent. [not funny]
- The rain stops later, but you'll want the umbrella for now. || Save the outdoor bits for after. I would, if I had any. [not funny]
- The rain eases off later, but bring the umbrella for now. || Then the whole street shakes out its umbrellas at once. [not funny]
- The rain stops later, but you'll want the umbrella for now. || Then you'll have a wet umbrella and nowhere to put it. [not funny]
- Take the umbrella for now. The rain stops {WHENSTOP}. || On time, if I have anything to do with it. I don't, but still. [not funny]
- The rain stops {WHENSTOP}, but you'll want the umbrella before that. || I'll let you know when. Well, I just did. [not funny]
- Take the umbrella for now. The rain stops later. || For now. Later it's just a stick you carry around. [not funny]

### `units_10.p_drier_snow` (live now: 1)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It stops snowing {WHENSTOP}." / "The snow stops {WHENSTOP}." / "The snow stops later." / "It stops snowing later." / "The snow eases off later." / "It's snowing now, but it stops later."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It stops snowing {WHENSTOP}. || Right on time. I like a snowfall that keeps its word.
Voted out here (stay away):
- The snow stops later. || The slush doesn't. That's on its own schedule. [not funny]
- It stops snowing {WHENSTOP}. || Then it sits there looking perfect until the first footprint. [not funny]
- It's snowing now, but it stops later. || So the pretty part has a deadline. [not funny]

### `units_10.p_stays_wet` (live now: 3)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "There's no dry spell today. Bring the umbrella." / "The rain lasts all day, so keep the umbrella with you." / "Take the umbrella. The rain keeps going all day." / "It rains all day, so bring the umbrella." / "It's raining all day. Bring the umbrella." / "The rain doesn't stop today, so take the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It's raining all day. Bring the umbrella. || Good day to be a screen. Bad day to be a sock.
- Take the umbrella. The rain keeps going all day. || I'd sing about it, but I don't do sound. Lucky you.
- It rains all day, so bring the umbrella. || Lights on at noon. Somebody will call it cozy.
Voted out here (stay away):
- It's raining all day. Bring the umbrella. || Every shop doorway has a puddle of other people's umbrellas. [not funny]
- There's no dry spell today. Bring the umbrella. || Except in here. I'm the dry spell. [not funny]
- It rains all day, so bring the umbrella. || The washing stays in today. So do I, but that's normal. [unclear]

### `units_10.p_wet_again` (live now: 3)

Raining now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "The rain pauses later but picks up again {WHENP}, so don't put the umbrella away." / "It rains for now, stops for a bit, and starts again {WHENP}. Keep the umbrella." / "The rain stops for a while later, then comes back {WHENP}. Keep the umbrella with you." / "It keeps raining for now, then takes a break. It's back {WHENP}, so keep the umbrella." / "Rain for now, then a dry spell, then more rain {WHENP}. The umbrella stays with you." / "Later the rain takes a break, but it returns {WHENP}. Hang on to the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain pauses later, but it's back {WHENP}. Keep the umbrella. || Weather like this is why rooms were invented.
- The rain stops for a bit, then it's back {WHENP}. Keep the umbrella. || I saw round two coming. It's my one job.
- It rains, stops for a bit, and starts again {WHENP}. Keep the umbrella. || It's not done. It just forgot something.
Voted out here (stay away):
- Later the rain takes a break, but it's back {WHENP}. Keep the umbrella. || The puddles won't even get a chance to shrink. [not funny]
- It rains, stops, and starts again {WHENP}. Keep the umbrella. || The dry bit is when everyone runs errands at once. [not funny]
- It rains for now, stops for a bit, and starts again {WHENP}. Keep the umbrella. || The rain gets a break. The umbrella doesn't. [not funny]
- Later the rain takes a break, but it returns {WHENP}. Hang on to the umbrella. || Fold it and it rains. That's the rule. [not funny, unclear]
- The rain stops {WHENSTOP} and comes back {WHENP}. Keep the umbrella with you. || Two parts. The umbrella's in both. [not funny]

### `units_10.p_wet_again_snow` (live now: 3)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "The snow stops {WHENSTOP} and starts again {WHENP}." / "The snow stops for a while later, then comes back {WHENP}." / "It keeps snowing for now, then takes a break. It's back {WHENP}." / "Snow for now, then a break, then more snow {WHENP}." / "The snow pauses later and starts again {WHENP}." / "It snows for now, takes a break, and starts again {WHENP}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Snow for now, then a break, then more snow {WHENP}. || Part two is always the slushier one.
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two snowfalls in one day. I'll take the credit for both.
- Snow for now, then a break, then more snow {WHENP}. || A second coating. Winter's thorough, I'll give it that.
Voted out here (stay away):
- The snow stops for a while later, then comes back {WHENP}. || Long enough to clear the path. Not to keep it clear. [not funny]
- The snow pauses later and starts again {WHENP}. || It's taking a breather. I don't need those. [not funny]

### `units_10.p_wetter` (live now: 2)

Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "There's a short rain shower {WHENP}. Have the umbrella with you." / "There's a shower passing through {WHENP}, so bring the umbrella." / "A rain shower comes through {WHENP}, so take the umbrella." / "Bring the umbrella. There's a shower {WHENP}." / "Expect a rain shower {WHENP}. The umbrella's worth taking." / "{WHENP} there's a rainshower, so the umbrella comes along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- There's a short shower {WHENP}. Have the umbrella with you. || It'll be over just as you get it open.
- Bring the umbrella. There's a shower {WHENP}. || Hours of carrying for minutes of use. Still a good deal.
Voted out here (stay away):
- There's a short shower {WHENP}. Have the umbrella with you. || Short showers are the ones nobody takes an umbrella for. [not funny] (note: whe'res the sarcsm?)
- Expect a shower {WHENP}. The umbrella's worth taking. || Ten wet minutes, then everyone acts like nothing happened. [not funny]
- A shower comes through {WHENP}, so take the umbrella. || It's only passing through. Don't take it personally. [not funny]
- Take the umbrella along for the rain shower {WHENP}. || As opposed to the other kind of shower. I'm thorough. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || One shower. I could have made it sound dramatic. I chose not to. [not funny]

### `units_10.shorts_early` (live now: 3)

A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It starts cool, but it's shorts weather {WHEN}." / "A cool start, then shorts weather {WHEN}." / "It's cool now, but {WHEN} it's warm enough for shorts." / "It's a bit cool for shorts now, but {WHEN} you'll be glad to have them." / "Shorts could be worth it today. It's cool now, but warm {WHEN}." / "{WHEN} it's warm enough for shorts, so think about putting them on now."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Shorts could be worth it today. It's cool now, but warm {WHEN}. || I'd say "trust me", but I've never had cold legs.
- A cool start, then shorts weather {WHEN}. || Shorts now might be the brave call. Correct, but brave.
- It starts cool, but it's shorts weather {WHEN}. || Shorts might be worth a cold first hour. But that's easy for me to say. I don't freeze.
Starred here before:
- Shorts could be worth it today. It's cool now, but warm {WHEN}. || I’d say ‘Trust me’. but I've never had cold legs.
Voted out here (stay away):
- It starts cool, but it's shorts weather {WHEN}. || Maybe go with shorts. Your knees will have opinions for a while. [not funny]
- It's a bit cool for shorts now, but {WHEN} you'll be glad of them. || Chilly now, glad later. Like most good decisions. [not funny]

### `units_10.steady_night` (live now: 3)

Nothing changes, from 22:00: the evening wording, late. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: 
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- What you have on is fine for the rest of the night. || Including the bit on the sofa you'll call 'resting my eyes'.
- You're dressed right for the rest of the night. || So that's not what's keeping you up.
- What you're wearing works until bed. || Whenever that is. I've stopped guessing.
Voted out here (stay away):
- The weather settles down for the night. || Worth a try. [not funny]
- Nothing more from the weather tonight. || I'll tell you the rest in the morning. Assuming you're up. [not funny]
- No more weather tonight. || I'm the one screen in here that won't keep you up. You're welcome. [not funny]
- Nothing changes for the rest of the night. || Not that anyone will see it at this hour. Except me. [not funny]
- What you're wearing works for the rest of the evening. || It also works for bed, I'm told. [not funny]
- Nothing to change before bed. || Well, one thing. But that's up to you. [not funny]

### `units_10.w_coat` (live now: 3)

Warms up: the winter coat comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "The winter coat can come off {WHEN}." / "You can take the winter coat off {WHEN}." / "{WHEN} it's warm enough to lose the winter coat." / "It warms up {WHEN}, so the winter coat can come off." / "{WHEN} you can do without the winter coat." / "You'll be fine without the winter coat {WHEN}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The winter coat can come off {WHEN}. || Then you carry it. It weighs about as much as a small child.
- You can take the winter coat off {WHEN}. || Gripping weather. I can barely stay in my frame.
- {WHEN} you can do without the winter coat. || You'll miss the pockets, though.

### `units_10.w_jacket` (live now: 3)

Warms up: the jacket comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "You can take the jacket off {WHEN}." / "The jacket can come off {WHEN}." / "{WHEN} it's warm enough to lose the jacket." / "It warms up {WHEN}, so the jacket can come off." / "{WHEN} you won't need the jacket any more." / "Once it warms up {WHEN}, the jacket can come off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The jacket can come off {WHEN}. || I'd take a layer off too, but mine are glued on.
- {WHEN} you won't need the jacket any more. || Or keep it on out of loyalty and quietly cook.
- The jacket can come off {WHEN}. || I'm not forcing anything. I'm a screen, not your parent.
Voted out here (stay away):
- You can take the jacket off {WHEN}. || Check the pockets first. Your keys are in there. [not funny]
- It warms up {WHEN}, so the jacket can come off. || Peeling off a layer: the closest today gets to drama. [not funny]
- It warms up {WHEN}, so the jacket can come off. || Over one arm, then. Very catalogue model of you. [not funny]

### `units_10.w_scarf` (live now: 3)

Warms up: hat, scarf and gloves come off, the coat stays. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "You'll be fine without the scarf {WHEN}." / "{WHEN} you won't need the scarf any more." / "It warms up {WHEN}, so the scarf can come off." / "The scarf can come off {WHEN}." / "You can take off the scarf {WHEN}." / "{WHEN} it's mild enough to lose the scarf."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} it's mild enough to lose the scarf. || 'Mild'. You'll be calling it practically spring.
- You can take off the scarf {WHEN}. || The coat stays. Let's not get carried away.
- {WHEN} you won't need the scarf any more. || That's as much good news as winter is allowed to give.
Voted out here (stay away):
- You can take off the hat, scarf and gloves {WHEN}. || Finally, you can use your phone without biting a glove off. [not funny]
- The hat, scarf and gloves can come off {WHEN}. || All at once is a lot of excitement. Pace yourself. [not funny]
- {WHEN} you won't need the hat, scarf and gloves any more. || Any more today. Don't give them away. [not funny]

### `units_10.w_water` (live now: 3)

Climbs into heat. Nothing left to take off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It gets hot {WHEN}, so bring water." / "{WHEN} it gets hot. Bring water." / "It heats up {WHEN}, so take water with you." / "Take a bottle of water. The heat arrives {WHEN}." / "{WHEN} it's going to be really hot, so have water with you." / "You'll want water {WHEN}, when the heat comes in."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It gets hot {WHEN}, so bring water. || Finally, a use for the fancy bottle you bought to drink more water.
- Take a bottle of water. The heat arrives {WHEN}. || Not for me, thanks. Water and I don't get along.
- It heats up {WHEN}, so take water with you. || Somebody's about to crank the outside too high. Not me.

## Output

Write `review/rounds/2026-10-fill/en.units10.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
