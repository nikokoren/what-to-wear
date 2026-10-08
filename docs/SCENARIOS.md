# What each scenario key means

A translator working from the English lines alone has to reverse-engineer
when each key fires. This is that information written down, so the lines you
write are *about* the right thing rather than a paraphrase of the English.

Everything below is derived from `src/shared.liquid`. Temperatures are
apparent ("feels like") temperature in Celsius, and the forecast window runs
from now until 21:00 local, or three hours out, whichever is later.

## The outfit on screen

The sprite is chosen by temperature band. The words never contradict it and
never propose a different outfit — they say what happens to the layer the
drawing already shows, or what to put in the bag.

| Band | Feels like | What the drawing shows |
|---|---|---|
| 1 `bundled` | ≤ −5 °C | winter coat, hat, scarf, gloves |
| 2 `coat` | ≤ 5 °C | winter coat |
| 3 `jacket` | ≤ 12 °C | jacket over long sleeves |
| 4 `sweater` | ≤ 18 °C | sweater or hoodie |
| 5 `tee_pants` | ≤ 24 °C | t-shirt, long pants |
| 6 `tee_shorts` | ≤ 30 °C | t-shirt, shorts |
| 7 `heat` | ≤ 34 °C | tank top, sandals |
| 8 `extreme_heat` | > 34 °C | tank top, sun hat, water |

Each step is one decision at the door. Rain adds the umbrella, as a sign
that rain is coming rather than a garment. Snow is the dry outfit with snow
falling, drawn for `bundled` and `coat`, the only outfits snow falls on.

Bands 5 and 6 have the same top layer. Moving between them is a question of
legs, which are decided once at the door (the long-pants rule below), so it
produces no hint at all.

**The long-pants rule.** Every other layer comes off, but someone told
"long pants" on a morning that turns into shorts weather is stuck in them
all afternoon. So when it is long-pants weather now and the day warms into
shorts weather (held for two hours), the drawing switches to shorts if the
cool stretch before it is no longer than the warm stretch. Better a bit
cool for a while than sweating all afternoon. A shorts day that only
arrives late keeps the long pants.

A change has to be at least 2 °C *and* cross a band to say anything, and
it has to **hold for two consecutive hours**, the same rule rain has always
had. A single cold hour at sunrise is not a story.

The rain or snow half of the picture looks one hour ahead: dry now but at
least 50% in the next hour draws the wet outfit, so someone leaving in ten
minutes sees the umbrella rather than only reading about it.

### When a line says "this afternoon"

`{WHEN}` and `{WHEN2}` are the hour the band is **crossed**, not the hour of
the peak or the low. A jacket needed from 15:00 says "this afternoon", even
if the coldest hour of the window is 21:00.

The edges above are the defaults. The optional **"Do you run cold or
warm?"** setting shifts every reading by up to ±4 °C before it meets the
ladder, so someone who is always cold gets a sweatshirt where the default
gives a t-shirt. It is one uniform shift rather than seven editable
thresholds, which is what makes it safe: adding the same number to every
reading cannot reorder the edges, so overlapping bands are not
representable and there is nothing to validate. Differences survive it
untouched, so the 2 °C rule and every arc comparison behave identically.

None of this changes what you write. No line may name a temperature
anyway, so a shifted ladder is invisible in the text — it only changes
which scenario fires and which outfit is drawn.

## Temperature keys

### `perfect`, and its four variants

Nothing worth mentioning happens. No band change, or too small to matter.

**This is about half of everything the plugin ever says.** Measured over a
year of real weather it fires on 53% of renders, against 0.1% for
`arc_colder`. Depth here is worth more than depth anywhere else in the file.

Because it fires across the whole temperature range and the whole day, the
markup refines it into whichever of these the day actually is. Each falls
back to plain `perfect` when a language has not written it, so a translation
can ship with just the one key and add the rest later.

| Key | Fires when | Say |
|---|---|---|
| `perfect_evening` | from 17:00 | the day is nearly done, not "you're set for the day" |
| `perfect_hot` | band 7-8, before 17:00 | steady heat. Water and shade, because clothing has nothing left to offer |
| `perfect_cold` | band 1-2, before 17:00 | steady cold. What is on screen is the right answer, all day |
| `perfect` | everything else | the outfit holds, nothing to carry, nothing to decide |
| `theme_<name>` | a seasonal day, any time | see below |

Two of those exist because the plain key was getting them wrong. It skews
late — the forecast window shrinks as the day ends, so a steady evening is
the commonest state of all, and lines like "one outfit covers the whole day"
were rendering at 20:00. And at the top of the scale it said "nothing changes
today" during a heatwave, which is true and useless.

`perfect` also renders on its own when there is no forecast window left.

### The `w_*` keys — it warms up, a layer comes off

Fires when the day gets warmer and crosses up out of the current band. The
key names **the layer in the drawing right now**, so the garment is fixed:

| Key | Fires in band | The sentence is about |
|---|---|---|
| `w_scarf` | 1 `bundled` | the scarf (and hat, gloves) come off, the coat stays |
| `w_coat` | 2 `coat` | the winter coat comes off, and is bulky to carry |
| `w_jacket` | 3 `jacket` | the jacket comes off |
| `w_hoodie` | 4 `sweater` | the sweater or hoodie comes off |

`w_sweatshirt` is no longer used: the sweater band covers it.

Because the key fixes the garment, name it in plain prose. Don't use
`{GARMENT}` here.

The useful content is not "it gets warmer" — the reader can feel that. It is
**you will be carrying this thing.** The English lines lean hard on that:
somewhere to put it, an arm occupied, tied round the waist.

### `w_water` — it gets hotter and there is nothing left to take off

Fires from band 5 up, when it climbs into heat (band 7 or 8). The figure is
already in a t-shirt or tank top.

Say: clothing has run out of moves. Water, shade, hydrate. Never name a
garment — there is no removable layer, so `{GARMENT}` would render empty.

### The `c_*` keys — it cools down, bring a layer

Fires when the day drops into a colder band. The key names **the layer to
bring**, which is the destination band's garment, not what is on screen:

| Key | Drops to band | Bring |
|---|---|---|
| `c_scarf` | 1 `bundled` | a scarf, hat and gloves; the coat alone stops being enough |
| `c_coat` | 2 `coat` | the winter coat; a jacket will not do |
| `c_jacket` | 3 `jacket` | a jacket; a sweater will not do |
| `c_hoodie` | 4 `sweater` | a sweater or hoodie; bare arms stop being comfortable |

`c_sweatshirt` is no longer used.

### `shorts_early` — shorts now, though it starts cool (optional)

Fires when the long-pants rule draws shorts in long-pants weather and nothing
else changes. `{WHEN}` is when shorts weather starts. Say: a cool start, worth
it, because long pants would be wrong for most of the day. A language without
it reads the day as steady, which is still true of the drawing.

Frame these as **packing**, not weather reporting. The reader is about to
leave the house and the useful sentence is "take one with you", not "it will
be 9 degrees later".

Name the garment in prose. `{GARMENT}` resolves to the *current* band's
layer here, not the one being recommended, so using it would name the wrong
thing.

### `c_relief` — it cools, but stays warm

Fires when it drops from band 7 or 8 but stays at band 5 or above.

**Far more common than it looks: 26% of renders across a summer, and 32% in
US cities.** It is the second-busiest key in the file after `perfect`, and
it deserves the depth that implies.

Say: the worst of the heat passes, nothing to bring, the outfit is unchanged.
The tone is relief without a recommendation.

It is tempting to write these vaguely because no garment can be named — above
band 6 there is no removable layer. But the key only ever fires when the
current band is hot or very hot, so the line can always talk about the heat
itself. That is the specific thing it has to work with, and vagueness here is
a choice rather than a constraint.

Do not say "nothing to bring" or "put the bag down": this key joins to
precipitation fragments, and "nothing to carry" followed by "take the
umbrella" is a self-contradiction that shipped once already. Scope every
claim to layers.

### The `arc_*` keys — it warms, then cools again

These are the subtle ones, and the three differ only in **where the day
ends** relative to right now. All three describe a layer coming off partway
through the day. What changes is whether it goes back on, and whether it is
enough when it does.

The peak comes before the trough, so the shape is: now → warmer → colder.

| Key | Ends | The story |
|---|---|---|
| `arc_warmer` | warmer than now | comes off `{WHEN}` and **stays off**. There is a dip later but not enough to want it back. Do not tell the reader to carry it. |
| `arc_level` | same as now | comes off `{WHEN}`, wanted again `{WHEN2}`. **Keep hold of it** — the day ends where it started. |
| `arc_colder` | colder than now | comes off `{WHEN}`, back on `{WHEN2}`, **and is not enough by then**. Take an extra layer on top. |

Getting these wrong is the one mistake with a real cost: `arc_warmer` telling
someone to carry a coat they will not need, or `arc_colder` failing to warn
them the evening is colder than the morning they dressed for.

These are the only three keys where `{GARMENT}` / `{GARMENTA}` earn their
place, because the garment genuinely varies across bands 1–5. They are still
optional — see [TRANSLATING.md](TRANSLATING.md).

`{WHEN2}` only resolves in these three keys. It is the second turning point,
always a time of day rather than "in two hours".

### `theme_<name>` — a seasonal day

On the seasonal days, the tip can acknowledge the occasion. The theme names
match the sprite prefixes: `theme_ny`,
`theme_ghd`, `theme_pi`, `theme_easter`, `theme_force`, `theme_bike`, `theme_tdf`,
`theme_okt`, `theme_spooky`, `theme_thanks`, `theme_krampus`,
`theme_nikolo`, `theme_xmas`.

No theme has artwork in the new outfit set yet, so every theme gets its
themed *words* over the ordinary outfit, which is the intended fallback and
not a bug. Easter fires on Easter Sunday (computed). A theme is only whitelisted for a
themed sprite once every band of it exists; `tools/check_sprites.py`
enforces that, after `okt` spent sixteen days a year pointing at a PNG
nobody had drawn.

**A theme line only ever replaces `perfect`.** If the day has real advice to
give — a layer coming off, rain arriving — that advice wins and the theme
stays in the picture only. A joke about Christmas is never worth someone
getting cold.

**Never name a temperature, a season's weather, or a specific garment.**
These keys replace `perfect` at *any* band, so the same line renders on a
mild Christmas and a freezing one. And about 2.7% of devices are in the
southern hemisphere, where Christmas is high summer — the themes fire on a
date, not a season.

> ✗ `Steady cold all day. The good coat has one job and today's it.`
> ✓ `Nothing about the weather changes today. The day has enough going on.`

Keep them weather-shaped rather than pure greeting: the plugin is still a
weather plugin on Christmas Day. `Merry Christmas!` is not a tip.

A language that omits these falls back to the evening, hot or cold variant
the day would otherwise get, then to `perfect`, so they are optional.

## Precipitation keys

Each appears twice. The bare key is the **whole tip**, used when the
temperature is doing nothing worth mentioning. The `_j` key is a **fragment
joined onto a temperature sentence** that has already named a time, so it
must not carry `{WHENP}` and should read as a continuation.

| Key | Fires when | Say |
|---|---|---|
| `wetter_maybe` | rain likely but under 60% at peak | it might; the umbrella is cheap insurance |
| `wetter` | rain is coming, short | take the umbrella, it arrives `{WHENP}` |
| `wetter_long` | rain for 4+ consecutive hours | it settles in; the umbrella earns its keep |
| `drier` | **raining now**, stopping later | it clears; the umbrella gets a rest |
| `stays_wet` | **raining now**, no dry break of 2+ hours in the window | all day, no gap |
| `wet_again` | **raining now**, a dry break, then rain again `{WHENP}` | it stops for a while; don't leave the umbrella anywhere |
| `snow_coming` | snow ahead, not snowing yet | snow `{WHENP}`; footwear, not umbrellas |

`drier`, `stays_wet` and `wet_again` **never tell anyone to take an
umbrella**, and only `wet_again` (standalone form) names a time — when the
rain comes back. It is already raining, so the figure in the drawing is already
holding one. Telling them to fetch it reads as a bug.

`wet_again` is optional. A language without it gets `drier` — the true half
of the story — rather than no rain line at all.

`snow_coming` is about grip, not staying dry. Boots with tread. An umbrella
is decoration in snow.

## The one-line summary

The picture says what to wear. The words say what changes, and what to put in
the bag. If a line could be swapped between two keys without anyone
noticing, it is too vague.
