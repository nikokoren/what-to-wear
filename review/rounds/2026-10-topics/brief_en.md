# Fresh topics, en

You write sarcastic lines for a TRMNL e-ink weather screen ("What to Wear"). Two kinds:
- **units**: a forecast sentence and its joke, written together: `forecast sentence || joke`. Path `unit_10.<key>` (sarcasm On, mild) or `unit_11.<key>` (sharper).
- **now lines**: one sarcastic line about the weather right now, shown alone under the drawing. Path `now_10.<mood>` or `now_11.<mood>`.

Voice: the TRMNL screen itself, a little too pleased with itself; dry, short. US English (color, gray, sidewalk, inches).

## What the owner keeps
1. **The screen's own stake**: it is a screen, indoors, it only does forecasts, and it has opinions about that. The owner's own edits keep pulling jokes there ("…but I'm not the one dealing with the consequences.", „Wenn's warm ist, glaubst du mir sowas nie.“).
2. **Truths everyone recognizes**, with **bite**: sarcasm, not gentle observation. Round 20's "Then every car wears a white hat for a few days" got the owner's note "where's the sarcasm?".
3. **Clear on first read.** Round 20's German notes: "what is that supposed to mean?", "joke does not make sense", "no flow".

## What the owner vetoes, nearly always
- Wordplay on a word of the forecast sentence. "Like your X" / „wie deine X“ jabs. Predicting the reader's mishaps or behavior.
- Explaining the joke. Mentioning drawings. Anything the screen can't know (what the reader did, where they are, what's in their bag). Assuming the TRMNL shows only this recipe.
- English: the screen's spot is "room", never hallway. German: keep it open („drinnen“, „hier drin“).

## Rules
- Units: the forecast part comes from that key's live wordings (one is listed below; you may shorten it) and keeps its placeholders: {WHEN}/{WHEN2} times, {WHENP} when rain or snow starts, {WHENSTOP} when it stops, {G}/{GV}/{GP} the garment. Steady days say "all day", never "until tonight".
- Short: a now line under about 90 characters, a unit under about 120.
- Seasonal lines carry "months": "11,12,01".

## The topics (8 candidates per topic, each a different idea; mix units and now lines where the topic allows)

- **feels like**: The recipe dresses you by the feels-like temperature, not the thermometer: 9° that feels like 4°. Nobody believes the number until they're outside. Good homes: steady_cold, c_* units; now cold/cool. Give each line "topic": "feels like".
- **the weather app**: The phone's weather app as the screen's rival: two forecasts, one of them on the wall. Good homes: p_wetter_maybe, steady units; now cool/wet. Give each line "topic": "the weather app".
- **weather small talk**: The only topic strangers share. The screen is the one thing that does it professionally. Good homes: steady units; now cool/nice. Give each line "topic": "weather small talk".
- **weather lore**: Red sky at night, April showers. The screen quoting, doubting or out-doing folk wisdom. 'April showers' only in April (months 04). Good homes: p_* units; now wet. Give each line "topic": "weather lore".
- **early dark**: Dark by half past four, November to January (months 11,12,01). The screen knows the date. Good homes: steady_evening units; now evening. Give each line "topic": "early dark".
- **the one person in shorts in February**: Everyone knows one. Never the reader. Winter months. Good homes: shorts_early, w_* units; now cold. Give each line "topic": "the one person in shorts in February".
- **'too hot', two days after 'when's summer coming'**: The complaint swap. Good homes: steady_hot, w_water units; now hot. Give each line "topic": "'too hot', two days after 'when's summer coming'".
- **pumpkin spice**: Arrives early, September and October only (months 09,10). Good homes: steady, c_* units; now cool. Give each line "topic": "pumpkin spice".

## Unit keys and one live wording each

- `steady`: Nothing changes all day. About half of all screens; also Visual Forecast's "works all day". e.g. "This outfit works all day."
- `steady_evening`: Nothing changes, from 17:00. e.g. "What you're wearing works for the rest of the evening."
- `steady_night`: Nothing changes, from 22:00: the evening wording, late. e.g. "What you're wearing works for the rest of the evening."
- `steady_cold`: Steady cold (coat or more), before 17:00. e.g. "It's this cold the whole day."
- `steady_hot`: Steady heat, before 17:00. e.g. "It's hot the whole day, so drink plenty of water and find shade."
- `w_jacket`: Warms up: the jacket comes off. e.g. "You can take the jacket off {WHEN}."
- `w_hoodie`: Warms up: the sweater comes off. e.g. "You'll be fine without the sweater {WHEN}."
- `c_jacket`: Cools to jacket weather: a jacket needed later. e.g. "A sweater won't do {WHEN}, so bring a jacket."
- `c_hoodie`: Cools to sweater weather: a sweater needed later. e.g. "{WHEN} short sleeves won't be enough, so bring a sweater."
- `w_scarf`: Warms up: hat, scarf and gloves come off, the coat stays. e.g. "You'll be fine without the hat, scarf and gloves {WHEN}."
- `w_coat`: Warms up: the winter coat comes off. e.g. "The winter coat can come off {WHEN}."
- `w_water`: Climbs into heat. Nothing left to take off. e.g. "It gets hot {WHEN}, so bring water."
- `c_scarf`: Cools to bundled: hat, scarf and gloves needed later. e.g. "The cold sets in {WHEN}, so pack a hat, scarf and gloves."
- `c_coat`: Cools to coat weather: the winter coat needed later. e.g. "Don't leave the winter coat behind. You'll want it {WHEN}."
- `c_relief`: The heat breaks, but it stays warm. Nothing to bring. e.g. "It cools off a little {WHEN}, but stays warm."
- `arc_warmer`: The jacket comes off and stays off: the evening is still warmer than now. e.g. "{G} comes off {WHEN}. It cools a little later, but you won't need {GP} back."
- `arc_level`: The jacket comes off, and is wanted back in the evening. e.g. "{G} can come off {WHEN}, but you'll want {GP} back {WHEN2}."
- `arc_colder`: The jacket comes off; the evening is colder than now: jacket back, plus a layer. e.g. "Take {G} off {WHEN}, then put {GP} back on {WHEN2} with an extra layer on top."
- `shorts_early`: A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. e.g. "It starts cool, but it's shorts weather {WHEN}."
- `p_wetter`: Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. e.g. "There's a short shower {WHENP}. Have the umbrella with you."
- `p_wetter_long`: Rain later, and it stays. Shown alone; after a change, it follows that sentence. e.g. "Pack the umbrella. Rain sets in {WHENP} and doesn't let up."
- `p_wetter_maybe`: Rain possible later, not likely. Shown alone; after a change, it follows that sentence. e.g. "You might get some rain {WHENP}, so the umbrella could come in handy."
- `p_stays_wet`: Raining now and all day. e.g. "There's no dry spell today. Bring the umbrella."
- `p_drier`: Raining now, stops later. e.g. "Take the umbrella for now. The rain stops {WHENSTOP}."
- `p_wet_again`: Raining now, stops, comes back. e.g. "The rain pauses later but picks up again {WHENP}, so don't put the umbrella away."
- `p_snow_coming`: Snow later. e.g. "Snow moves in {WHENP}."
- `p_stays_wet_snow`: Snowing now and all day. e.g. "The snow doesn't stop today."
- `p_drier_snow`: Snowing now, stops later. e.g. "It stops snowing {WHENSTOP}."
- `p_wet_again_snow`: Snowing now, stops, comes back. e.g. "The snow stops {WHENSTOP} and starts again {WHENP}."

## Now moods

- `nice`: T-shirt weather (18–30 °C feels-like) under a clear or partly cloudy sky
- `cool`: sweater or jacket weather, or any grey/overcast day that isn't cold
- `cold`: winter coat weather or colder
- `hot`: hot (above 30 °C feels-like)
- `wet`: raining right now
- `snow`: snowing right now
- `evening`: 18:00–22:00, dry
- `night`: after 22:00, dry

## Lines the owner starred recently (study the tone)

- What you're wearing works for the rest of the evening.
- The snow stops later.
- The winter coat can come off {WHEN}.
- Taking that layer off might be the highlight of your day.
- You'll overheat a little before you admit I was right.
- You'll call it 'fresh' to sound like an outdoors person.
- It's hot all day. Bring water and stay in the shade.
- It snows all day.
- {WHEN} it gets cool enough for a sweater.
- It starts snowing {WHENP}.
- You won't get a sad little cloud icon from me. I've got artistic integrity.
- You'll search 'ice cream near me' later. Twice.
- {WHEN} it's mild enough to lose the hat, scarf and gloves.
- The sweater can come off {WHEN}.
- On days like this you barely look at me. Fair enough.
- Remember wishing for summer? This is what you get.
- Expect snow {WHENP}.
- You'll call it 'crisp' like you go hiking or something.
- Same jacket, same route. You wild thing.
- It stays this cold all day.
- Perfect weather to talk about going for a run.
- A good day for pretending you'll go for a run.
- It stops snowing later.
- You've looked at me a lot today. Go to bed.
- You'll still check your phone. As if it knows something I don't.
- What you're wearing works for the whole day.
- You'll double-check on your phone. As if it knows better.
- You can take {G} off {WHEN}. You'll want {GP} back {WHEN2}.
- {G} can come off {WHEN}, but you'll want {GP} back {WHEN2}.
- No break from the heat today. Water and shade help.
- You can take the jacket off {WHEN}.
- Today a rodent does my job, and gets a crowd. Pathetic.
- The heat lasts all day: drink water and find shade. || Somebody cranked the outside too high. Wasn't me.
- This outfit is fine all day. || 'Fine' is the highest praise I give.
- It's hot all day. Bring water and stay in the shade. || Remember wishing for summer? This is what you get.
- What you have on is right for the whole day. || Don't let it go to your head.
- What you have on lasts the whole day. || Unlike your phone battery.
- Nothing to add or take off all day. || My shortest forecast, and my favourite.
- No break from the heat today. Drink water, find shade. || And somehow you'll still burn the back of your neck.
- You can wear this for the rest of the evening. || You were going to anyway.
- It stays hot all day. Water and shade, please. || You'll say 'I'm not built for this' at least once. You're right.
- You're dressed right for the rest of the evening. || Plenty of evening left for not answering that message.
- Nothing changes tonight. || You'll scroll in bed for an hour and call it winding down.
- It's cold all day. || My only weakness is the cold. Kidding, I don't have one.
- You're dressed right for the rest of the evening. || That leaves the evening free for losing the remote.
- It's this cold the whole day. || You'll walk twice as fast. Still not cardio.
- You'll be comfortable in this for the rest of the evening. || You'll probably spend half of it choosing what to watch.
- The heat lasts all day. Stay in the shade and drink water. || You'll find shade, then complain it's the wrong shade.
- It doesn't get any warmer today. || No use checking again in an hour, I won't change my mind.
- It doesn't get any warmer today. || Staring at me longer won't change that.
- No warming up today. || You'll see your breath and pretend you're a dragon. Don't deny it.
- It's cold all day. || You'll come home and hug the radiator like it's family.
- Hot all day, so water and shade. || You'll probably end up loitering in the freezer aisle. Again.
- What you have on works for the whole day. || You've worn worse for longer.
- It's hot all day, so drink water and find shade. || Finally, a use for the fancy bottle you bought to drink more water.
- It stays this cold the whole day. || I'm staying in here where it's warm.
- It stays cold all day. || Perfect for browsing flights somewhere warm and booking nothing. Again.
- No layer to carry today. That means you have both hands free for snacks.
- What you're wearing works for the rest of the evening. || You'll read all this, then do what you were going to anyway.
- Hot all day: drink water and look for shade. || You'll search 'ice cream near me' later. Twice.

## Output

Write `review/rounds/2026-10-topics/en.raw.json`: `{"lines": [{"path": "now_10.cold", "text": "…", "topic": "feels like"}, {"path": "unit_10.steady_cold", "text": "fact || joke", "topic": "feels like", "months": "11,12"}]}`. Check it parses. Don't edit any other file, don't commit.
