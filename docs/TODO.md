# To do

Parked work for the complete rewrite. Nothing here is started. Each item
carries enough context to pick it up cold.

## 1. Rethink the clothing system and the temperature bands

Do this first: the visual forecast below draws outfits, so it depends on
what the outfits are.

The current eight bands (see the ladder in `docs/SCENARIOS.md` and
`BAND_EDGES` in `src/shared.liquid`) may not describe real clothing
decisions well. Example: long sleeves, hoodie and the light puffy jacket
are not different enough from each other to be worth three separate
outfits, while other steps may be missing.

To decide together, from scratch:

- Which outfits exist at all, and what actually changes between
  neighbouring ones: a different decision someone makes at the door,
  not just a different drawing.
- Where the band edges sit (feels-like temperature, °C), and whether a
  hoodie and a sweatshirt should keep counting as one warmth class.
- Which layer each tip names as coming off or going in the bag. The
  `w_*` and `c_*` keys in `lang/*.json` are tied to today's garments.

Keep from today's system:

- The "Do you run cold or warm?" setting (`temp_preference`): one
  uniform shift of every reading. Chosen over editable per-band
  thresholds because the bands can never overlap or cross.
- Two-hour persistence and band-crossing times in the forecast logic
  (`tools/logic_test.py` pins both).

Touches: the sprite set (and every themed set), `BAND_EDGES`/`BAND_NAMES`,
the garment lists in `lang/*.json`, every `w_*`/`c_*` line, the docs, and
the tests.

## 2. Visual forecast: three outfits across the day

On views wide enough for it, show three columns, each one a sprite with a
time label under it, e.g. **Now · Midday · Evening**, each drawing the
outfit for that part of the day's temperature. This would sit alongside
the text tip, not replace it.

Open questions:

- **Fixed times or the moments things change?** Fixed slots are simple
  but often show three identical outfits. The forecast logic already
  finds when a band is crossed (`warm_idx`, `bring_idx`, `back_on_idx`
  in `src/shared.liquid`), so the columns could show *now* plus only the
  moments a clothing change actually happens, and collapse to one
  sprite on a steady day.
- **Which views have room.** Likely full and half horizontal. Check the
  original TRMNL in portrait, where full is only 480 px wide. Layout
  must use the framework's responsive primitives (container units,
  `md:`/`lg:`/`portrait:` prefixes), as the current views do. Verify
  with the device classes, both orientations, OG and X, before
  shipping.
- **Rain and snow per column.** Each column needs its own wet or dry
  outfit, from the hourly precipitation in that slot.
- **Labels** go in `lang/*.json` like every other word on screen.

## 3. Better writing, and a review process that isn't tedious

The tips read robotic in both languages, English most of all, and
reviewing them line by line in JSON has always been slow. Do this after
item 1: new outfits change every `w_*`/`c_*` line, so write once, not
twice. Pilot on `perfect`, which is about half of everything shown.

### Why the current lines sound generated

- **One joke, repeated.** About 9% of the 1,025 English lines give
  objects a job: the jacket's "shift ends", the rain "cleared its
  calendar", the forecast "filed nothing". That is a rule in
  `docs/VOICE.md` ("level 10: deadpan, aimed at the objects") turned
  into a template.
- **Too many lines.** "Depth follows frequency" pushed volume, and
  volume forces formula. A reader sees one line a day; three great
  lines per key beat twelve passable ones.
- **Written and judged out of context.** Each line is written and
  reviewed alone in a JSON file, never on the screen with the outfit,
  the time words filled in, and the rain line it gets paired with.
- **Rules instead of examples.** Adjectives like "warm" or "deadpan"
  steer a model far less than a handful of lines you actually like.

### How the owner can help the writer

- **A taste file:** 20 to 30 lines you love from anywhere (apps, ads,
  friends' messages), and 20 from the current corpus you dislike, each
  with one word for why. Concrete examples beat any rulebook.
- **One sentence on who is talking.** "A friend who checked the weather
  for you", not a style guide.
- **Rate, don't rewrite.** A star or a veto with a tag is faster for you
  and better signal for the next round than editing lines yourself.
- **A native read of the English.** About 50% of devices are in the US;
  a native speaker reading the starred lines once catches what neither
  of us will.

### Generating better from the start

- Write about five candidates for every line needed. You keep the best;
  the rest are thrown away, not repaired.
- Starred lines become the examples for the next round, vetoed lines and
  their tags a "don't" list. Keep both in the repo so every future
  session starts from your taste, not from zero.
- Write each line against the situation it renders in (outfit, time,
  what changes), not against a key name.
- Extend `tools/style_report.py` to flag the tics measured above
  (object-has-a-job metaphors, semicolons, ", because" explanations,
  repeated sentence skeletons).
- German is written and judged on its own, never as a translation.

### A review page, like the postcard veto site

An artifact page with a shared database (so votes persist and can be
read back):

- Each line shown **as it renders**: on a mock device screen with the
  right sprite, time words filled in, and its rain pairing where one
  applies.
- **Star / Keep / Veto**, plus tags (robotic, too long, not funny, wrong
  garment, wrong fact, unclear) and an optional note. Keyboard shortcuts.
- Filters by language, sarcasm level and key; a count per key so you
  never veto a key empty.
- Decisions remembered across rounds, so a vetoed line never returns.
- Export in the format `tools/apply_review.py` already reads (it refuses
  to overwrite a line that changed since review). Stars feed the
  examples file; notes feed the next round.

The new `wet_again` lines (written in October to fill a new scenario)
are the first candidates for this review.

## Loose ends from the October 2026 fixes

- **Check the new views in TRMNL's own editor preview** on the original
  TRMNL and the X, landscape and portrait. Local renders could not
  reproduce one bug seen in the editor (the one-letter tip column), so
  the editor may use a different framework version.
- **Sprites:** the renames in the header of `src/shared.liquid` (cold →
  freezing and so on), and a light-jacket outfit for the `cold` band.
  The three `force_*` images are the same picture at every temperature.
  `xmas_cold_dry.jpg`, `xmas_cold_rain.jpg` and `thanks_cold_rain.jpg`
  are unreachable because the markup only loads `.png`. Likely folded
  into item 1.
- **Wording:** several `c_jacket` and `c_coat` lines name a garment
  the figure may not be wearing ("A jacket over the hoodie" when the
  drawing is a t-shirt). Also folded into item 1.
- **Usage Worker** (`worker/`): deploy it and switch the second polling
  URL to start counting forecast on/off and sarcasm level. Steps are in
  `worker/README.md`.
