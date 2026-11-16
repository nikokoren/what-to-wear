# Top-up round (en, units): thin slots to four lines

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

### `units_10.arc_colder` (live now: 1; the critic keeps 5, write 15)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top." / "{G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}." / "{WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Weather update {WHEN2}. As usual, the update is worse.
Voted out here (stay away):
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || On top, not instead. I know you. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || On TV they'd call this 'changeable'. I call it showing off. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || The warm part has a curfew. An early one. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The warm part is the weather being polite. Then it's honest. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || The evening outdoes the morning. In the wrong direction. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The evening has a stricter dress code. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || A round trip for {GP}. The evening brings a friend. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Evenings look warmer from inside. I go by numbers. [unclear] (note: help me fine tune that)
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Carry it all, then wear it all. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || The warm bit is a trick. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || You'll come home in more layers than you left in. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The day ends colder. Like my jokes. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Plus. I don't say 'plus' lightly. [not funny]
- {WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top. || 'Something warm'. I trust you. A bit. [not funny]

### `units_10.arc_level` (live now: 1; the critic keeps 5, write 15)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{G} can come off {WHEN}, but you'll want {GP} back {WHEN2}." / "You can take {G} off {WHEN}. You'll want {GP} back {WHEN2}." / "Take {G} off {WHEN}, put {GP} back on {WHEN2}." / "{G} can come off {WHEN}. Keep {GP} handy, you'll want {GP} back {WHEN2}." / "{G} won't be needed {WHEN}, but you'll want {GP} on again {WHEN2}." / "{WHEN} you can take {G} off, but you'll need {GP} again {WHEN2}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Take {G} off {WHEN}, put {GP} back on {WHEN2}. || Off and on again. That fixes most things, me included.
Voted out here (stay away):
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}. || The weather can't commit. I can. I've held this picture for hours. [not funny]
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}. || The warm part is the intermission. The second act is colder. [not funny]
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}. || The weather's version of a nap: warm for a bit, then grumpy. [not funny]
- {WHEN} you can take {G} off, but you'll need {GP} again {WHEN2}. || Warm for a while. Don't get attached. I didn't. [not funny]

### `units_10.arc_warmer` (live now: 3; the critic keeps 3, write 9)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{G} comes off {WHEN}. It cools a little later, but you won't need {GP} back." / "{G} can come off {WHEN}, and you won't need {GP} again today." / "{G} can come off {WHEN} and stays off." / "You can take {G} off {WHEN}. You won't need {GP} again after that." / "You can take {G} off {WHEN}. You won't need {GP} for the rest of the day." / "Once {G} comes off {WHEN}, you can leave {GP} off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {G} can come off {WHEN} and stays off. || I'm not changing my mind about this one.
- You can take {G} off {WHEN}. || After that, you're just carrying {GP} around for company.
- {G} can come off {WHEN} and stays off. || That's it. That's the forecast.
Starred here before:
- Once {G} comes off {WHEN}, you can leave {GP} off. || Leave {GP} off. Not 'leave {GP} somewhere'.
Voted out here (stay away):
- {G} can come off {WHEN} and stays off. || Warm, and staying warm. The weather finally read my forecast. [not funny]
- {G} comes off {WHEN}. It cools a little later, but you won't need {GP} back. || The evening tries to look dramatic. It doesn't have the numbers. [not funny]
- {G} can come off {WHEN} and stays off. || You'll say 'it's got a bit chilly' later. Not chilly enough. [not funny]
- You can take {G} off {WHEN}. You won't need {GP} again after that. || I'd say goodbye, but you'll see {GP} tomorrow. [not funny]
- You can take {G} off {WHEN}. Even later on, you won't need {GP}. || Even later. I checked the whole day. You're welcome. [not funny]

### `units_10.c_relief` (live now: 2; the critic keeps 4, write 12)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It cools off a little {WHEN}, but stays warm." / "The heat eases {WHEN}, but it stays warm." / "{WHEN} it gets a little less hot. Still warm, though." / "Some relief from the heat {WHEN}, but it stays warm." / "{WHEN} the worst of the heat is over, but it stays warm." / "It's not as hot {WHEN}, but still warm."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Some relief from the heat {WHEN}, but it stays warm. || I'll take the credit for that.
- It cools off a little {WHEN}, but stays warm. || 'A little' is carrying that whole forecast.
Starred here before:
- It cools off a little {WHEN}, but stays warm. || A little. Don't get excited.
- The heat eases {WHEN}, but it stays warm. || I'd call it relief. You'll call it 'still too hot'.

### `units_10.p_drier` (live now: 3; the critic keeps 3, write 9)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Take the umbrella for now. The rain stops {WHENSTOP}." / "It keeps raining for a while, then stops. Take the umbrella." / "The rain stops later, but you'll want the umbrella for now." / "Take the umbrella for now. The rain stops later." / "The rain stops later, but bring the umbrella for now." / "Later the rain stops. For now, keep the umbrella with you."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain stops {WHENSTOP}, but you'll want the umbrella before that. || That's all the good news that I have for today.
- Take the umbrella for now. The rain stops {WHENSTOP}. || I can't stop the rain. I can only tell you when it gets bored.
- It keeps raining for a while, then stops. Take the umbrella. || 'A while.' I'd be more precise, but the rain isn't.
Voted out here (stay away):
- The rain stops later, but you'll want the umbrella for now. || I've seen how this ends. It's dry. Sorry, spoilers. [not funny]
- The rain eases off later, but bring the umbrella for now. || The sky runs out eventually. It's not as well stocked as it acts. [not funny]
- The rain stops later, but you'll want the umbrella for now. || The worst part comes first. The weather's one good habit. [not funny]
- Take the umbrella for now. The rain stops {WHENSTOP}. || Then everything's wet and shiny and acts innocent. [not funny]
- The rain stops later, but you'll want the umbrella for now. || Save the outdoor bits for after. I would, if I had any. [not funny]
- The rain eases off later, but bring the umbrella for now. || Then the whole street shakes out its umbrellas at once. [not funny]
- The rain stops later, but you'll want the umbrella for now. || Then you'll have a wet umbrella and nowhere to put it. [not funny]
- Take the umbrella for now. The rain stops {WHENSTOP}. || On time, if I have anything to do with it. I don't, but still. [not funny]
- The rain stops {WHENSTOP}, but you'll want the umbrella before that. || I'll let you know when. Well, I just did. [not funny]
- Take the umbrella for now. The rain stops later. || For now. Later it's just a stick you carry around. [not funny]

### `units_10.p_drier_snow` (live now: 3; the critic keeps 3, write 9)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It stops snowing {WHENSTOP}." / "The snow stops {WHENSTOP}." / "The snow stops later." / "It stops snowing later." / "It's snowing now, but it stops later." / "It keeps snowing for a while, then stops."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The snow stops later. || The kids won't take the news well.
- The snow stops later. || Every snowplow driver just exhaled.
- It stops snowing {WHENSTOP}. || Note the time. I'll be smug about it afterwards.
Starred here before:
- It stops snowing {WHENSTOP}. || Right on time. I like a snowfall that keeps its word.
Voted out here (stay away):
- The snow stops later. || The slush doesn't. That's on its own schedule. [not funny]
- It stops snowing later. || Snow does the fun part, then leaves the shoveling to everyone else. [not funny]
- It stops snowing later. || Snow knows when to leave. Rare in a guest. [not funny]
- It stops snowing {WHENSTOP}. || Then it sits there looking perfect until the first footprint. [not funny]
- It's snowing now, but it stops later. || So the pretty part has a deadline. [not funny]

### `units_10.p_wet_again_snow` (live now: 2; the critic keeps 4, write 12)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "The snow stops {WHENSTOP} and starts again {WHENP}." / "The snow stops for a while later, then comes back {WHENP}." / "It keeps snowing for now, then takes a break. It's back {WHENP}." / "Snow for now, then a break, then more snow {WHENP}." / "The snow pauses later and starts again {WHENP}." / "It snows for now, takes a break, and starts again {WHENP}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two snowfalls in one day. I'll take the credit for both.
- Snow for now, then a break, then more snow {WHENP}. || A second coating. Winter's thorough, I'll give it that.
Starred here before:
- Snow for now, then a break, then more snow {WHENP}. || Part two is always the slushier one.
Voted out here (stay away):
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two rounds of snow, zero rounds of shoveling. For me. [not funny]
- Snow for now, then a break, then more snow {WHENP}. || Inches now, inches later. The sky pays in installments. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || Act two. Same set, same cast, more of it. [not funny]
- The snow stops for a while later, then comes back {WHENP}. || Long enough to clear the path. Not to keep it clear. [not funny]
- The snow pauses later and starts again {WHENP}. || It's taking a breather. I don't need those. [not funny]

### `units_10.p_wetter` (live now: 2; the critic keeps 4, write 12)

Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "There's a short rain shower {WHENP}. Have the umbrella with you." / "There's a shower passing through {WHENP}, so bring the umbrella." / "A rain shower comes through {WHENP}, so take the umbrella." / "Bring the umbrella. There's a shower {WHENP}." / "Expect a rain shower {WHENP}. The umbrella's worth taking." / "{WHENP} there's a rainshower, so the umbrella comes along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- There's a short shower {WHENP}. Have the umbrella with you. || It'll be over just as you get it open.
- Bring the umbrella. There's a shower {WHENP}. || Hours of carrying for minutes of use. Still a good deal.
Voted out here (stay away):
- There's a short rain shower {WHENP}. Have the umbrella with you. || Clear, rain, clear. I've drawn more exciting days. Not many. [not funny]
- There's a short rain shower {WHENP}. Have the umbrella with you. || Short is the worst kind. Too long to ignore, too short to complain about properly. [not funny]
- There's a shower passing through {WHENP}, so bring the umbrella. || The rest of the day stays dry. The rain just wanted a cameo. [not funny]
- A rain shower comes through {WHENP}, so take the umbrella. || One shower, just to prove the sky still can. [not funny]
- There's a short shower {WHENP}. Have the umbrella with you. || Short showers are the ones nobody takes an umbrella for. [not funny] (note: whe'res the sarcsm?)
- Expect a shower {WHENP}. The umbrella's worth taking. || Ten wet minutes, then everyone acts like nothing happened. [not funny]
- A shower comes through {WHENP}, so take the umbrella. || It's only passing through. Don't take it personally. [not funny]
- Take the umbrella along for the rain shower {WHENP}. || As opposed to the other kind of shower. I'm thorough. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || One shower. I could have made it sound dramatic. I chose not to. [not funny]

### `units_10.steady_night` (live now: 2; the critic keeps 4, write 12)

Nothing changes, from 22:00: the evening wording, late. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: 
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- What you're wearing works until bed. || Whenever that is. I've stopped guessing.
- You're dressed right for the rest of the night. || End of broadcast. Please enjoy this still image until morning.
Starred here before:
- You're dressed right for the rest of the night. || So that's not what's keeping you up.
- What you have on is fine for the rest of the night. || Including the bit on the sofa you'll call 'resting my eyes'.
Voted out here (stay away):
- Nothing changes for the rest of the night. || I could show anything now and get away with it. I won't. Probably. [not funny]
- What you're wearing works until bed. || The night shift is me and the fridge. The fridge hums. I don't. [not funny]
- The weather settles down for the night. || Worth a try. [not funny]
- Nothing more from the weather tonight. || I'll tell you the rest in the morning. Assuming you're up. [not funny]
- No more weather tonight. || I'm the one screen in here that won't keep you up. You're welcome. [not funny]
- Nothing changes for the rest of the night. || Not that anyone will see it at this hour. Except me. [not funny]
- What you're wearing works for the rest of the evening. || It also works for bed, I'm told. [not funny]
- Nothing to change before bed. || Well, one thing. But that's up to you. [not funny]

### `units_10.w_hoodie` (live now: 3; the critic keeps 3, write 9)

Warms up: the sweater comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "You'll be fine without the sweater {WHEN}." / "You can take the sweater off {WHEN}." / "The sweater can come off {WHEN}." / "{WHEN} it's warm enough to lose the sweater." / "It warms up {WHEN}, so the sweater can come off." / "{WHEN} it's warm enough for short sleeves, so the sweater can come off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- You can take the sweater off {WHEN}. || Thrilling stuff. I'm on the edge of my frame.
- You'll be fine without the sweater {WHEN}. || And 'fine' is high praise, coming from me.
- It warms up {WHEN}, so the sweater can come off. || Folded in the bag, or balled up in the bag. Your call.

### `units_10.w_water` (live now: 2; the critic keeps 4, write 12)

Climbs into heat. Nothing left to take off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It gets hot {WHEN}, so bring water." / "{WHEN} it gets hot. Bring water." / "It heats up {WHEN}, so take water with you." / "Take a bottle of water. The heat arrives {WHEN}." / "{WHEN} it's going to be really hot, so have water with you." / "You'll want water {WHEN}, when the heat comes in."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Take a bottle of water. The heat arrives {WHEN}. || Not for me, thanks. Water and I don't get along.
- It heats up {WHEN}, so take water with you. || Somebody's about to crank the outside too high. Not me.
Starred here before:
- It gets hot {WHEN}, so bring water. || Finally, a use for the fancy bottle you bought to drink more water.
Voted out here (stay away):
- Take a bottle of water. The heat arrives {WHEN}. || The heat arrives on time. Nothing else ever does. [not funny]
- It gets hot {WHEN}, so bring water. || Ice cubes everywhere are bracing themselves. [not funny]
- {WHEN} it gets hot. Bring water. || The only forecast where everyone agrees with me and nobody's happy. [not funny]

## Output

Write `review/rounds/2026-10-onfill/en.units.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
