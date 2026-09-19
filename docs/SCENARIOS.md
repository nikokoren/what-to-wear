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
| 1 `extra_cold` | ≤ −7 °C | puffer, scarf, beanie, boots |
| 2 `freezing` | ≤ 3 °C | puffer, beanie, boots |
| 3 `cold` | ≤ 10 °C | light jacket, beanie, boots |
| 4 `cool` | ≤ 14 °C | hoodie, sneakers |
| 5 `mild` | ≤ 19 °C | sweatshirt, long trousers |
| 6 `warm` | ≤ 27 °C | t-shirt, shorts, cap |
| 7 `hot` | ≤ 32 °C | vest, sandals |
| 8 `very_hot` | > 32 °C | vest, bucket hat, water |

Bands 4 and 5 count as one warmth class — a hoodie and a sweatshirt are the
same thing thermally — so moving between them produces no hint at all.

A change has to be at least 2 °C *and* cross a band to say anything.

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
| `w_scarf` | 1 `extra_cold` | the scarf comes off, everything else stays |
| `w_coat` | 2 `freezing` | the puffer comes off, and is bulky to carry |
| `w_jacket` | 3 `cold` | the light jacket comes off |
| `w_hoodie` | 4 `cool` | the hoodie comes off |
| `w_sweatshirt` | 5 `mild` | the sweatshirt comes off |

Because the key fixes the garment, name it in plain prose. Don't use
`{GARMENT}` here.

The useful content is not "it gets warmer" — the reader can feel that. It is
**you will be carrying this thing.** The English lines lean hard on that:
somewhere to put it, an arm occupied, tied round the waist.

### `w_water` — it gets hotter and there is nothing left to take off

Fires from band 6 up, when it climbs further. The figure is already in a
t-shirt or vest.

Say: clothing has run out of moves. Water, shade, hydrate. Never name a
garment — there is no removable layer, so `{GARMENT}` would render empty.

### The `c_*` keys — it cools down, bring a layer

Fires when the day drops into a colder band. The key names **the layer to
bring**, which is the destination band's garment, not what is on screen:

| Key | Drops to band | Bring |
|---|---|---|
| `c_scarf` | 1 `extra_cold` | a scarf; the coat alone stops covering the neck |
| `c_coat` | 2 `freezing` | the winter coat; a light jacket will not do |
| `c_jacket` | 3 `cold` | a jacket; a hoodie will not do |
| `c_hoodie` | 4 `cool` | a hoodie |
| `c_sweatshirt` | 5 `mild` | a sweatshirt; bare arms stop being comfortable |

Frame these as **packing**, not weather reporting. The reader is about to
leave the house and the useful sentence is "take one with you", not "it will
be 9 degrees later".

Name the garment in prose. `{GARMENT}` resolves to the *current* band's
layer here, not the one being recommended, so using it would name the wrong
thing.

### `c_relief` — it cools, but stays warm

Fires when it drops from band 7 or 8 but stays at band 6 or above.

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

On the thirteen days a year that have their own artwork, the tip can
acknowledge it. The theme names match the sprite prefixes: `theme_ny`,
`theme_ghd`, `theme_pi`, `theme_force`, `theme_bike`, `theme_tdf`,
`theme_okt`, `theme_spooky`, `theme_thanks`, `theme_krampus`,
`theme_nikolo`, `theme_xmas`.

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

A language that omits these falls back to `perfect`, so they are optional.

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
| `stays_wet` | **raining now**, no let-up | all day, no gap |
| `snow_coming` | snow ahead, not snowing yet | snow `{WHENP}`; footwear, not umbrellas |

`drier` and `stays_wet` name **no time and never tell anyone to take an
umbrella.** It is already raining, so the figure in the drawing is already
holding one. Telling them to fetch it reads as a bug.

`snow_coming` is about grip, not staying dry. Boots with tread. An umbrella
is decoration in snow.

## The one-line summary

The picture says what to wear. The words say what changes, and what to put in
the bag. If a line could be swapped between two keys without anyone
noticing, it is too vague.
