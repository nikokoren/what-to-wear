# To do

Parked work for the complete rewrite. Each item carries enough context
to pick it up cold.

## Where we left off (8 October 2026)

- All October work is on branch `claude/serene-meitner-cg3e4v`, not on
  `main`. The published recipe still runs the old markup with a single
  polling URL.
- Item 3 (the text) is deferred on purpose: it is the most expensive
  item, the approach below is agreed, and it should wait for item 1 and
  for real usage numbers.
- **Item 1 is decided and coded; the drawings are next.** See its status
  below. Items 2 and 3 are not started.

### Suggested order, and why

1. **Check the new views in TRMNL's editor** (loose end below). Quick,
   done in the editor, and the views carry over into the rewrite.
2. **Item 1, the clothing system.** It blocks everything else: it
   decides the sprite set, and the beta cannot ship until the sprites
   match the temperature ladder (today the 3-10 °C band draws a puffer
   where the code means a light jacket). Mostly a design conversation,
   so it is cheap to start. Useful input: how often each band actually
   occurs over a year in the main US and German cities, from
   Open-Meteo's archive API (rate-limited the first time; retry then).
3. **Ship the beta** with the new outfits, following
   `docs/MIGRATION.md`. That is also what lets the usage Worker count
   real users: it needs the refactored markup live first, because a
   second polling URL breaks the old markup.
4. **Item 2, the visual forecast**, drawn with the new outfits.
5. **Item 3, the text**, scoped by a few weeks of usage numbers (forecast
   on or off, which sarcasm level), so effort goes to the voices people
   actually use.

## 1. Rethink the clothing system and the temperature bands

**Status: decided and implemented (October 2026). Waiting on the art.**

Decisions:

- Eight outfits, each step one decision at the door. Edges in
  `BAND_EDGES` (feels-like °C, tune by hand):

  | Outfit | Feels like |
  |---|---|
  | `bundled`: winter coat, hat, scarf, gloves | ≤ −5 |
  | `coat`: winter coat | −5 to 5 |
  | `jacket`: jacket over long sleeves | 5 to 12 |
  | `sweater`: sweater or hoodie | 12 to 18 |
  | `tee_pants`: t-shirt, long pants | 18 to 24 |
  | `tee_shorts`: t-shirt, shorts | 24 to 30 |
  | `heat`: tank top, sandals | 30 to 34 |
  | `extreme_heat`: tank top, sun hat, water | > 34 |

- Rain adds the umbrella, as a sign that rain is coming. Snow has no item
  (no boots); it draws the dry outfit.
- **The long-pants rule:** legs are decided at the door. In long-pants
  weather, if the day warms into shorts weather and the cool stretch is
  no longer than the warm one, draw shorts now.
- Art: one finished PNG per case, made with layers in the drawing tool:
  16 base sprites, `sprites/<outfit>_<dry|rain>.png`, plus themed ones
  as `sprites/<theme>_<outfit>_<dry|rain>.png`.

Left to do:

- **Draw the 16 sprites.** `sprites/` holds placeholder copies of the
  closest old drawings so everything renders meanwhile;
  `python3 tools/check_sprites.py` lists which are still placeholders.
- **`sprites/` must be on `main`** before a beta fork can show them: the
  markup loads sprites from `main`. New names in a new folder, so the
  published recipe is unaffected.
- Themed sprites: none yet in the new set; add each theme to the
  whitelist in `src/shared.liquid` with its artwork.
- Text, with item 3: `w_sweatshirt`/`c_sweatshirt` are unused; lines for
  the optional `shorts_early` key; `w_hoodie`/`c_hoodie` lines should
  read as "sweater or hoodie"; `w_scarf`/`c_scarf` cover hat and gloves
  too.

Original brief:

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

### Data (October 2026, `tools/climate/`)

Three years of hourly station data, 28 cities weighted by device share:

- **The year is mostly cold or cool.** At the 7 am dressing hour, 52% of
  readings fall in today's three coldest bands (10 °C feels-like or
  below); above 27 °C is under 5%.
- **Hoodie and sweatshirt cover 31% of daytime hours** between them, yet
  the code already treats them as one warmth class: one outfit drawn
  twice.
- **Rain mostly falls on coat and jacket days.** 52% of wet hours are in
  today's puffer and light-jacket bands. The puffer band has no rain
  sprite (it falls back to dry), so about a quarter of rainy hours show
  no umbrella. Precipitation at snow temperatures is only ~6% of wet
  hours.
- **Most days change outfit.** About two days in three change between
  08:00, the afternoon peak and 19:00, whichever ladder is used: daily
  swings are wider than any sensible band. That argues for outfits built
  as layers that come off, and for the visual forecast (item 2).

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
  The eleven `force_*` files are just two pictures (one dry, one wet), shown at every temperature.
  `xmas_cold_dry.jpg`, `xmas_cold_rain.jpg` and `thanks_cold_rain.jpg`
  are unreachable because the markup only loads `.png`. Likely folded
  into item 1.
- **Wording:** several `c_jacket` and `c_coat` lines name a garment
  the figure may not be wearing ("A jacket over the hoodie" when the
  drawing is a t-shirt). Also folded into item 1.
- **Usage Worker** (`worker/`): built and tested, not deployed. It can
  only count real users once the refactored markup is live (step 3 of the
  order above); until then, switching the published recipe to two polling
  URLs would break it. Steps are in `worker/README.md`.
