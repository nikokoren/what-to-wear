# Top-up round (en, units): thin slots to four lines

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

### `units_10.arc_colder` (live now: 3; the critic keeps 2, write 6)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top." / "{G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer." / "You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}." / "{WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Weather update {WHEN2}. As usual, the update is worse.
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || A day that peaks early. Plenty of careers can relate.
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Someone will say 'it was warm earlier' like that helps.
Voted out here (stay away):
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || The warm part has a curfew. An early one. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The warm part is the weather being polite. Then it's honest. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || The evening outdoes the morning. In the wrong direction. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The evening has a stricter dress code. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || A round trip for {GP}. The evening brings a friend. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Evenings look warmer from inside. I go by numbers. [unclear] (note: help me fine tune that)
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Carry it all, then wear it all. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || The warm bit is a trick. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || You'll come home in more layers than you left in. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || Great weather, for exactly as long as it takes to believe in it. [not funny]
- Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top. || Half the street will dress for the warm part. I've seen the rest of the day. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || If today were a stock, I'd sell at the warm part. [not funny]
- You can take {G} off {WHEN}. Bring an extra layer to wear with {GP} {WHEN2}. || The day ends colder. Like my jokes. [not funny]
- {G} can come off {WHEN}. {WHEN2} you'll want {GP} back, plus an extra layer. || Plus. I don't say 'plus' lightly. [not funny]
- {WHEN} {G} can come off. {WHEN2} you'll need {GP} again, and something warm on top. || 'Something warm'. I trust you. A bit. [not funny]

### `units_10.arc_warmer` (live now: 3; the critic keeps 2, write 6)

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
- Once {G} comes off {WHEN}, you can leave {GP} off. || This is where I'd normally say 'but.' Not today. [not funny]
- {G} can come off {WHEN}, and you won't need {GP} again today. || The weather peaked and didn't crash. Rare, for anything that peaks. [not funny]
- You can take {G} off {WHEN}. You won't need {GP} for the rest of the day. || A day that gets better and stays better. I'd ask what it's on. [not funny]
- You can take {G} off {WHEN}. Even later on, you won't need {GP}. || Even later. I checked the whole day. You're welcome. [not funny]

### `units_10.c_relief` (live now: 3; the critic keeps 2, write 6)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "It cools off a little {WHEN}, but stays warm." / "The heat eases {WHEN}, but it stays warm." / "{WHEN} it gets a little less hot. Still warm, though." / "Some relief from the heat {WHEN}, but it stays warm." / "{WHEN} the worst of the heat is over, but it stays warm." / "It's not as hot {WHEN}, but still warm."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Some relief from the heat {WHEN}, but it stays warm. || I'll take the credit for that.
- The heat eases {WHEN}, but it stays warm. || From brutal to just rude.
- It cools off a little {WHEN}, but stays warm. || 'A little' is carrying that whole forecast.
Starred here before:
- It cools off a little {WHEN}, but stays warm. || A little. Don't get excited.
- The heat eases {WHEN}, but it stays warm. || I'd call it relief. You'll call it 'still too hot'.
Voted out here (stay away):
- The heat eases {WHEN}, but it stays warm. || The heat doesn't break. It just sprains a little. [not funny]
- {WHEN} it gets a little less hot. Still warm, though. || Cooler, by frying pan standards. [not funny]
- It cools off a little {WHEN}, but stays warm. || The heat goes down a notch. It has a lot of notches. [not funny]

### `units_10.p_wet_again_snow` (live now: 3; the critic keeps 2, write 6)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "The snow stops {WHENSTOP} and starts again {WHENP}." / "The snow stops for a while later, then comes back {WHENP}." / "It keeps snowing for now, then takes a break. It's back {WHENP}." / "Snow for now, then a break, then more snow {WHENP}." / "The snow pauses later and starts again {WHENP}." / "It snows for now, takes a break, and starts again {WHENP}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two snowfalls in one day. I'll take the credit for both.
- Snow for now, then a break, then more snow {WHENP}. || The break is just the sky reloading.
- Snow for now, then a break, then more snow {WHENP}. || A second coating. Winter's thorough, I'll give it that.
Starred here before:
- Snow for now, then a break, then more snow {WHENP}. || Part two is always the slushier one.
Voted out here (stay away):
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two rounds of snow, zero rounds of shoveling. For me. [not funny]
- Snow for now, then a break, then more snow {WHENP}. || Inches now, inches later. The sky pays in installments. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || Act two. Same set, same cast, more of it. [not funny]
- The snow stops for a while later, then comes back {WHENP}. || Long enough to clear the path. Not to keep it clear. [not funny]
- The snow pauses later and starts again {WHENP}. || The snowplow drivers get a coffee break. Exactly one. [not funny]
- Snow for now, then a break, then more snow {WHENP}. || The break is long enough for everyone to post photos. Then the photos are out of date. [not funny]
- Snow for now, then a break, then more snow {WHENP}. || Even the weather repeats itself. At least I wait a day. [not funny]
- The snow pauses later and starts again {WHENP}. || It's taking a breather. I don't need those. [not funny]

### `units_10.p_wetter` (live now: 2; the critic keeps 3, write 9)

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
- Bring the umbrella. There's a shower {WHENP}. || Small talk from the sky. Brief, damp, pointless. [not funny]
- There's a shower passing through {WHENP}, so bring the umbrella. || Just enough rain to make every car need a wash. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || I've seen longer commercials. [not funny]
- There's a short rain shower {WHENP}. Have the umbrella with you. || Short enough for people to argue about whether it counted. [not funny]
- A shower comes through {WHENP}, so take the umbrella. || It's only passing through. Don't take it personally. [not funny]
- Take the umbrella along for the rain shower {WHENP}. || As opposed to the other kind of shower. I'm thorough. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || One shower. I could have made it sound dramatic. I chose not to. [not funny]

### `units_10.steady_night` (live now: 2; the critic keeps 3, write 9)

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
- What you have on is fine for the rest of the night. || Same as before, only darker. Groundbreaking work, if I say so myself. [not funny]
- Nothing changes for the rest of the night. || My favorite kind of overtime. [not funny]
- Nothing changes for the rest of the night. || Even the raccoons find this forecast boring. They're out anyway. [not funny]
- Nothing changes for the rest of the night. || Even the weather keeps better hours than most people. [not funny]
- No more weather tonight. || I'm the one screen in here that won't keep you up. You're welcome. [not funny]
- Nothing changes for the rest of the night. || Not that anyone will see it at this hour. Except me. [not funny]
- What you're wearing works for the rest of the evening. || It also works for bed, I'm told. [not funny]
- Nothing to change before bed. || Well, one thing. But that's up to you. [not funny]

### `units_10.w_hoodie` (live now: 3; the critic keeps 2, write 6)

Warms up: the sweater comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "You'll be fine without the sweater {WHEN}." / "You can take the sweater off {WHEN}." / "The sweater can come off {WHEN}." / "{WHEN} it's warm enough to lose the sweater." / "It warms up {WHEN}, so the sweater can come off." / "{WHEN} it's warm enough for short sleeves, so the sweater can come off."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- You can take the sweater off {WHEN}. || Thrilling stuff. I'm on the edge of my frame.
- You'll be fine without the sweater {WHEN}. || And 'fine' is high praise, coming from me.
- It warms up {WHEN}, so the sweater can come off. || Folded in the bag, or balled up in the bag. Your call.
Voted out here (stay away):
- {WHEN} it's warm enough for short sleeves, so the sweater can come off. || Short sleeves. Bold claim from the weather. I'll allow it. [not funny]
- It warms up {WHEN}, so the sweater can come off. || The temperature goes up. Morale goes up slightly less. [not funny]
- The sweater can come off {WHEN}. || Every chair back in town is about to wear a sweater. [not funny]

### `units_11.p_drier` (live now: 2; the critic keeps 3, write 9)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Take the umbrella for now. The rain stops {WHENSTOP}." / "It keeps raining for a while, then stops. Take the umbrella." / "The rain stops later, but you'll want the umbrella for now." / "Take the umbrella for now. The rain stops later." / "The rain stops later, but bring the umbrella for now." / "Later the rain stops. For now, keep the umbrella with you."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Take the umbrella for now. The rain stops {WHENSTOP}. || Waiting it out is an option. Not a good one, but you like those.
- It keeps raining for a while, then stops. Take the umbrella. || Rain makes everyone look a bit miserable. Today you won't stand out.
Voted out here (stay away):
- It keeps raining for a while, then stops. Take the umbrella. || Wet doesn't suit you. Dry barely does. [not funny]
- The rain eases off later, but bring the umbrella for now. || You've survived worse than rain. Your own haircuts, for example. [not funny]
- Take the umbrella for now. The rain stops {WHENSTOP}. || Dry in here, by the way. Dry and good-looking. One of us manages both. [not funny]
- The rain eases off later, but bring the umbrella for now. || Sprinting between doorways isn't a plan. Not with your cardio. [not funny]
- It keeps raining for a while, then stops. Take the umbrella. || The sky looks sorry afterwards. It never apologises. [not funny]
- Take the umbrella for now. The rain stops later. || Then the birds start up again, as if they were never bothered. [not funny]
- The rain is here for now but stops later, so bring the umbrella. || It stops later. Your hair won't recover that fast. [not funny]
- The rain eases off later, but bring the umbrella for now. || You'll get it out just as it stops. That's the deal. [not funny]
- Later the rain stops. For now, keep the umbrella with you. || Later you can tell everyone it cleared up. I told you first. [not funny]

### `units_11.p_drier_snow` (live now: 2; the critic keeps 3, write 9)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "It stops snowing {WHENSTOP}." / "The snow stops {WHENSTOP}." / "The snow stops later." / "It stops snowing later." / "It's snowing now, but it stops later." / "It keeps snowing for a while, then stops."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It's snowing now, but it stops later. || Then it goes from 'magical' to 'still here?' in a day.
- It stops snowing later. || After that, the snow just lies around getting in the way. You two would get along.
Voted out here (stay away):
- It stops snowing later. || The snow gives up. You beat it to that by years. [not funny]
- It's snowing now, but it stops later. || You look great in snowflakes. Everyone does. It's cheating. [not funny]
- It's snowing now, but it stops later. || Pretty while it lasts. You know how that goes. [not funny]
- It stops snowing {WHENSTOP}. || One of us in this room knew that. Hint: it's not you. [not funny]
- Later on the snow stops. || Then every car wears a white hat for a few days. [not funny]
- The snow stops later. || Then the snowmen start appearing. Some of them are quite bad. [not funny]
- The snow stops later. || That's when the wet socks start. [not funny]
- The snow stops {WHENSTOP}. || I'd say 'enjoy it while it lasts', but I've given you the exact time. [not funny]
- Later on the snow stops. || Then you'll miss it. Briefly. [not funny]

### `units_11.p_stays_wet` (live now: 2; the critic keeps 3, write 9)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "There's no dry spell today. Bring the umbrella." / "The rain lasts all day, so keep the umbrella with you." / "Take the umbrella. The rain keeps going all day." / "It rains all day, so bring the umbrella." / "It's raining all day. Bring the umbrella." / "The rain doesn't stop today, so take the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain doesn't stop today, so take the umbrella. || A day for staying in. You were born for this.
- It rains all day, so bring the umbrella. || All day. So no, waiting ten minutes won't help.
Voted out here (stay away):
- Take the umbrella. The rain keeps going all day. || Under an umbrella all day, nobody sees your face. Lucky them. [not funny]
- The rain lasts all day, so keep the umbrella with you. || You'll be holding it all day. Finally, something to do with your hands. [not funny]
- The rain doesn't stop today, so take the umbrella. || I'd lend you my dry spot in here, but you'd ruin the look. [not funny]
- It's raining all day. Bring the umbrella. || You won't melt. I checked your specs. [not funny]
- It rains all day, so bring the umbrella. || Today the bottom of every trouser leg belongs to the rain. [not funny]
- The rain lasts all day, so keep the umbrella with you. || Every bus smells of wet coat today. Every single one. [not funny]
- The rain lasts all day, so keep the umbrella with you. || All day means all day. Not 'until I'm bored of carrying it'. [not funny]
- The rain doesn't stop today, so take the umbrella. || Neither will your complaining. At least the rain has an excuse. [not funny]
- It's raining all day. Bring the umbrella. || Your hair has already lost. Make peace with it. [not funny]

### `units_11.p_wet_again_snow` (live now: 2; the critic keeps 3, write 9)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The snow stops {WHENSTOP} and starts again {WHENP}." / "The snow stops for a while later, then comes back {WHENP}." / "It keeps snowing for now, then takes a break. It's back {WHENP}." / "Snow for now, then a break, then more snow {WHENP}." / "The snow pauses later and starts again {WHENP}." / "It snows for now, takes a break, and starts again {WHENP}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- It snows for now, takes a break, and starts again {WHENP}. || The break is mainly so the salt trucks can feel useful.
- The snow stops {WHENSTOP} and starts again {WHENP}. || Two rounds of snow. You can't even handle one with dignity.
Voted out here (stay away):
- The snow pauses later and starts again {WHENP}. || Beginning, middle, more snow. Better structure than your week. [not funny]
- The snow stops for a while later, then comes back {WHENP}. || It knows when to leave and when to come back. Two skills you lack. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || You, at the break: 'It's over.' Me: 'Read the whole sentence.' [not funny]
- It keeps snowing for now, then takes a break. It's back {WHENP}. || More snow than sense out there. You'll fit right in. [not funny]
- It snows for now, takes a break, and starts again {WHENP}. || The snow gets a second chance to make a first impression. You don't. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || Just enough of a gap to see the mess. Then it's covered up. [not funny]
- It keeps snowing for now, then takes a break. It's back {WHENP}. || It takes one break. You'll take three. [not funny]
- The snow stops {WHENSTOP} and starts again {WHENP}. || The break is just long enough to start believing it's over. [not funny]
- After a break later on, the snow returns {WHENP}. || Like you to the fridge. [not funny]

### `units_11.p_wetter` (live now: 3; the critic keeps 2, write 6)

Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "There's a short rain shower {WHENP}. Have the umbrella with you." / "There's a shower passing through {WHENP}, so bring the umbrella." / "A rain shower comes through {WHENP}, so take the umbrella." / "Bring the umbrella. There's a shower {WHENP}." / "Expect a rain shower {WHENP}. The umbrella's worth taking." / "{WHENP} there's a rainshower, so the umbrella comes along."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- A shower comes through {WHENP}, so take the umbrella. || Or spend it in a shop, pretending to browse. You know the drill.
- Bring the umbrella. There's a shower {WHENP}. || Not enough rain to fill a puddle, but plenty to fill a shoe.
- Bring the umbrella. There's a shower {WHENP}. || Carrying an umbrella while it's dry. People will think you have your life together.
Voted out here (stay away):
- Bring the umbrella. There's a shower {WHENP}. || A) Bring it. B) Get wet. C) Whatever you usually pick. [not funny]
- Expect a rain shower {WHENP}. The umbrella's worth taking. || A short shower won't ruin your look. Your look got there first. [not funny]
- There's a short rain shower {WHENP}. Have the umbrella with you. || A short one. You've made bigger fusses about less. [not funny]
- Expect a shower {WHENP}. The umbrella's worth taking. || With an umbrella it's weather. Without one, it's a story. [not funny]
- {WHENP} there's a shower, so the umbrella comes along. || Brief, wet, and gone. The perfect guest. [not funny]
- There's a shower passing through {WHENP}, so bring the umbrella. || It passes through. You'll take it personally. [not funny]
- A shower comes through {WHENP}, so take the umbrella. || It's a short one. Long enough to ruin your hair, though. [not funny]
- Bring the umbrella. There's a shower {WHENP}. || Yes, the folding one that won't fold. That one. [not funny]
- There's a short shower {WHENP}. Have the umbrella with you. || With you means in your hand. Not in the other bag. [not funny]

### `units_11.p_wetter_long` (live now: 2; the critic keeps 3, write 9)

Rain later, and it stays. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Pack the umbrella. Rain sets in {WHENP} and doesn't let up." / "It starts raining {WHENP} and keeps going, so bring the umbrella." / "The rain starts {WHENP} and doesn't stop. Bring the umbrella." / "Bring the umbrella. Once it starts raining {WHENP}, it keeps going." / "{WHENP} the rain sets in for good. Bring the umbrella." / "Rain arrives {WHENP} and stays, so take the umbrella."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The rain starts {WHENP} and doesn't stop. Bring the umbrella. || It has more stamina than you. Most things do.
- Rain arrives {WHENP} and stays, so take the umbrella. || Staying in was your plan anyway. Now you have a reason.
Voted out here (stay away):
- {WHENP} the rain sets in for good. Bring the umbrella. || Gray skies for the rest of the day. Finally, lighting that's kind to you. [not funny]
- Rain arrives {WHENP} and stays, so take the umbrella. || Hold it high. It's the most anyone's looked up to you. [not funny]
- The rain starts {WHENP} and doesn't stop. Bring the umbrella. || I'll be in here, dry and smug. You'll be out there, damp and you. [not funny]
- Rain arrives {WHENP} and stays, so take the umbrella. || It shows up and doesn't leave. You know the type. You are the type. [not funny]
- {WHENP} the rain sets in for good. Bring the umbrella. || From then on, puddles are permanent until further notice. [not funny]
- It starts raining {WHENP} and keeps going, so bring the umbrella. || Keeps going, like your excuses for not taking it. [not funny]
- {WHENP} the rain sets in for good. Bring the umbrella. || For good. Not for your hair. [not funny]

### `units_11.w_coat` (live now: 2; the critic keeps 3, write 9)

Warms up: the winter coat comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "The winter coat can come off {WHEN}." / "You can take the winter coat off {WHEN}." / "{WHEN} it's warm enough to lose the winter coat." / "It warms up {WHEN}, so the winter coat can come off." / "{WHEN} you can do without the winter coat." / "You'll be fine without the winter coat {WHEN}."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- The winter coat can come off {WHEN}. || You'll overheat a little before you admit I was right.
- {WHEN} it's warm enough to lose the winter coat. || Not that you'll ever manage to fold it.
Voted out here (stay away):
- It warms up {WHEN}, so the winter coat can come off. || Nobody will notice. They weren't looking at you in the coat either. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || Coat off. Now you just need a personality to replace it. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || Breaking: local person sees own arms for the first time in months. [not funny]
- The winter coat can come off {WHEN}. || Then you'll stand around holding it like a dead animal. Classy. [not funny]
- The winter coat can come off {WHEN}. || Suddenly you remember you have a shape. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || There's no chair in the world built for a winter coat. [not funny]
- It warms up {WHEN}, so the winter coat can come off. || You'll take it off and remember what you're wearing under it. [not funny]
- {WHEN} you can do without the winter coat. || You can. Whether you will is your business. [not funny]
- The winter coat can come off {WHEN}. || Then you're just a person carrying a duvet. [not funny]

## Output

Write `review/rounds/2026-11-thin/en.units.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
