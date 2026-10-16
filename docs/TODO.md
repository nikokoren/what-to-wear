# To do

Parked work for the complete rewrite. Each item carries enough context
to pick it up cold.

## Where we left off (October 2026)

- Everything is on `main` as of 9 October 2026 (fast-forwards, the last
  one bringing in the text work: the fact + flavour prototype, five
  review rounds, topical lines and the weekly scout). The published
  recipe is unaffected: it still runs the old markup, one polling URL,
  and the old drawings in the repo root; `lang/` and `sprites/` are
  unchanged.
- Running on `main` now: the weekly `topical-prune` workflow (a no-op
  until topical lines ship in `lang/`). The "Topical scout" routine
  (reads the `topical` skill from `main`) is paused since 15 October
  2026, with topical lines (item 8).
- Item 1 is decided and coded; the 19 drawings are next.
- Item 3 (the text) is well along in the prototype; see item 5 below.

### Rollout 2.0 (owner, October 2026)

Two steps, texts URL pinned to a version tag, merge to `main` once the
drawings are in. `tools/build_release.py` and `docs/MIGRATION.md` ("2.0").
Before release: the 19 drawings (below), a contact method in the About
text (`config/settings.next.yaml`), the owner's read of the 2.0 changelog
in both languages, then build, merge, tag `v2.0.0`, and the three steps.

### Open, in order

1. **Draw the 19 sprites** (item 1). Replace the files in `sprites/` on
   `main`; `python3 tools/check_sprites.py` lists the placeholders left.
   This is what blocks shipping.
2. **Check the new views in TRMNL's editor**, original TRMNL and X,
   landscape and portrait. Minutes, and only possible there.
3. **Item 2, the visual forecast.** Being prototyped as equal outfit
   panels across the day (`prototypes/panels/`, mock on claude.ai): now
   on the left, then each change, at most three, today only, never
   tomorrow. Decided: square drawings as drawn, the time under every
   drawing, "from" on every later time ("Now · from 1 pm · from
   7 pm"), larger times on the X. Settings: it is "What to Wear Next?",
   its own on/off switch next to Forecast (item 12,
   `config/settings.next.yaml`). Sarcastic line with no forecast line
   above it: its own pool of
   lines that work without the fact plus lines written for the drawings
   (review round 10, then `build_pools.py`).
4. **Done (October 2026): the views in TRMNL's framework classes
   only.** The owner: "I can't put this out like this" about the
   hand-written `<style>` block the Visual Forecast views carried. Now
   every view, in every mode (Visual Forecast, words, no forecast), comes
   from one template in `prototypes/panels/build.py` with no `<style>`
   and no inline style (`test_switch.py` checks). The overlap is a column
   narrower than its drawing; sizes are shares of the view (`w--[…cqw]`,
   `h--max-[…cqh]`, `aspect--1/1`). At the same time, from the owner's
   beta testing: the single drawing was small next to the space left, so
   it now grows into what the words leave (full view on the OG 247 to
   332 px). Fit check over 3,136 screens: clean. Details in
   `prototypes/panels/README.md`. Still to see on a real device (item 2).
5. **Ship**, once the art is in, following `docs/MIGRATION.md`: the
   transitional markup first, then the second polling URL (with
   `weather_code` in the hourly list), then the final markup. Switching
   the texts URL to the usage Worker at that step starts the counting.
   **Texts:** all of them come from the texts polling URL
   (`lang/<code>.json`), none are hardcoded in the markup (owner, October
   2026). TRMNL takes at most 100 KB per polled URL, so the file leaves
   out what the new markup never shows: the old forecast-text pools
   (`temp_*`, `precip_*`) keep one line per list, as in the beta
   (`tools/build_beta.py`: 38 KB English, 44 KB German), since the logic
   only checks that three of their keys exist (`shorts_early`, the
   "perfect" variants, `wet_again`). Build `lang/` that way at launch.
6. **Item 3, the text**: in progress. The tip becomes a fact line plus a
   flavour line; voice, fact style and most pools are decided by four
   rounds of votes (`review/README.md`). Round 5 (variants) is synced
   and fully rated. Next:
   new evening lines in both languages (German On is down to two; the
   new direction is in `docs/BRIEF.md`); then the theme days, then moving
   the prototype into `src/shared.liquid` and `lang/*.json`.
   **Theme days** (`theme_*` flavour pools, shown on steady theme days):
   only Christmas has lines in the new voice. Each language writes only
   the days its readers keep; a day without a pool falls back to the
   mood line. Both languages: New Year, Pi Day, May the 4th, Bike Day,
   Tour de France, Oktoberfest (international enough, the owner says),
   Halloween, Easter, and Christmas (its two lines per level are
   placeholders from the first prototype, never voted: they go on the
   page with the new candidates). English only: Groundhog Day, Thanksgiving. German
   only: Nikolaus (key `nikolo`; say "Nikolaus", not the Austrian
   "Nikolo") and Krampus (Alpine; lines must still make sense in
   Hamburg). Three candidates per level and language, in calendar order
   from Halloween; the joke comes out of the day itself.
7. **Variance, again: week of 16 October 2026.** The owner wants
   repeats rare enough that nobody notices: "closer to Carrot Weather
   than to us" over the long term. Round 5 is only the first step.
   Measure with `python3 tools/climate/repeat_report.py <climate dir>`
   (share of lines
   already shown in the previous 7 and 30 days, two years of real
   mornings in five cities). Numbers are in `review/README.md`, round 5.
   After round 5, 56% to 67% of flavour lines were seen within 30 days,
   and a reworded joke is still the same joke (most twins were vetoed
   "not funny"): only new jokes will move this. Ideas to
   weigh: much bigger pools for the common moods (wet, cold, steady
   evening); lines that work in any mood as a shared pool; rotating by a
   shuffled order instead of in sequence, so a pool never reads as a
   cycle; lines keyed to the weekday, the season or the run of weather
   ("third grey day in a row"); and the topical lines (item 7) earlier.
   **Lines about the sky** (owner, October 2026): sarcastic lines about
   what the weather is doing, not just what to wear, for more variety.
   The owner's example from Carrot Weather, not to copy: "I sent you this fog."
   What we have for free: Open-Meteo's `weather_code`, now and hourly,
   is already in the data (clear, cloudy, overcast, fog, drizzle, rain,
   freezing rain, snow, thunderstorm, hail). Wind isn't (it would need
   `wind_speed_10m` in the polling URL). How often, at 6 to 7 am in 2024
   (station data, `tools/climate/`; Open-Meteo's model codes may differ):
   overcast 40 to 50% in London, Cologne, Frankfurt, Munich, Hamburg and
   Amsterdam; fog 14% in Zurich, 12% in Los Angeles, 8% in Paris, 1 to 6%
   elsewhere; clear 30 to 45% in Phoenix, Dallas, Minneapolis and
   Stockholm. Decided (owner, October 2026):
   - **Only while it's happening.** A line about fog shows only while
     there's fog now; otherwise it makes no sense. So these lines need
     the texts to change during the day (item 10), which comes first.
   - **Mixed in at random** with the mood's lines as the day goes on,
     no fixed share or slot.
   - **Rain and snow only with their drawing**: a rain or snow line
     shows only while the drawing has the rain or the snow. There are no
     fog or overcast drawings, so everything else is looser: it shows
     when the condition is strong enough right now (thick fog, fully
     overcast, a real thunderstorm, not a passing cloud).
8. **Parked (owner, October 2026): topical lines.** The first drafts
   didn't land, and the owner doesn't want the focus on them now.
   Everything stays in place to pick up later; nothing new is written
   for them, and they don't ship with the text (no `topical_*` pools in
   `lang/`, so nothing shows). The weekly "Topical scout" routine is
   paused (15 October 2026); switch it back on to resume. What was built: On and 11 lines about current events, written with
   Claude whenever something happens, each with a date window so it
   rotates in and out by itself. Built in the prototype (markup, opt-in
   field, review rounds, add and prune tool, weekly prune job, the
   `topical` skill); ships with the text. The first event, the clocks
   going back, is voted and in the prototype; a weekly scout routine
   proposes events from Wikipedia and German news. Details in
   `docs/FUTURE-topical-lines.md`.
9. **Later: the sarcastic line in italics?** To set it apart from the
   fact line, as bold sets the fact apart now. What there is: TRMNL's
   framework has no italic class, though it loads an italic Inter (the
   font of the larger text sizes); the pixel fonts of the smaller sizes
   have no italic, so the browser would slant them, which looks rough
   in 1-bit. Item 4 rules out our own CSS, so: is there a framework way,
   and does it read well on the OG and the X?
10. **Done (October 2026): the texts change every hour.** The owner
   wanted it livelier, and the lines about the sky (item 7) need it: they
   may only show while their weather is happening. The fact wording, the
   rain fact, the sarcastic line and Visual Forecast's now pick their line
   by `text_rot` = day x 101 + hour x 103 (`prototypes/fact-flavour/
   block.liquid`), each on its own offset, instead of by day. The primes
   are larger than any pool, so an hour on lands elsewhere in the pool
   (it doesn't read as a cycle), every line comes round, and someone who
   looks at 7:00 every morning still sees the whole pool over the days.
   `test_rotation.py` pins it, and that every pool stays under 101 lines.
   Topical lines (parked) keep their every-third-day rhythm.
   - **TRMNL regenerates** when the merge variables change, and
     Open-Meteo's current time moves every 15 minutes, so a refresh after
     the hour turns shows the hour's lines. How often depends on the
     user's refresh rate; nothing new is fetched, so it costs nothing.
   - **Repeats:** for someone who looks once a morning, nothing changes
     (`repeat_report.py` at 7:00, London, New York, Minneapolis, Phoenix,
     Vienna: identical to the daily rotation, the flavour line 71% seen
     in the last 30 days in both languages): how often a line comes back
     is set by the size of its pool. Someone who looks several times a
     day now sees new lines, and goes through a pool faster (three
     glances a day see a 15-line pool in five days): more reason for
     bigger pools and the lines about the sky (item 7).
11. **Later, beta feedback: the day with no more changes.** In Visual
   Forecast, a day whose outfit holds until tomorrow gets one drawing,
   a "works all day" fact ("What you have on works from now until
   tonight.", `facts.steady`, `_evening`, `_hot`, `_cold`) and the
   mood's usual sarcastic line, which was written to follow other
   facts. The owner, beta testing: together they're too long and
   don't feel connected. Idea: sarcastic lines only for this case
   ("nothing changes until tomorrow"), so the screen reads as one
   calm, good piece; maybe a shorter fact with them, or none. It
   probably affects the words view's steady days too (same kind of
   fact, same pairing); the owner noticed it in Visual Forecast only
   because that's what the beta is set up to test, so solve it for
   both. Where it's picked: the one-panel branch of
   `prototypes/panels/block.liquid` ("this works all day") and the
   words view's steady fact in `prototypes/fact-flavour/block.liquid`.
12. **Built (October 2026), to check in the beta: the new form.** In
   `config/settings.next.yaml` and the beta; how the switches combine is
   in `prototypes/panels/README.md` ("The switch"), pinned by
   `test_switch.py`. Left: the checks in `beta/README.md` ("What to
   try": a saved "No" in the new on/off field, and whether TRMNL fills
   in defaults for an existing install), a contact method in the about
   text, and the owner's read of the German descriptions. The owner's
   spec, these fields, these labels and descriptions, in this order:
   1. **Language.** Hint: "Don't see your preferred language and want
      to help me translate? Reach out via the contact method linked in
      the about section above."
   2. **Do you run cold or warm? (New!)** "Adjust clothing suggestions
      to match how you experience the temperature." Options as now,
      default Average.
   3. **Forecast.** "Show a written summary of upcoming weather changes
      and what to wear." On or off, default on.
   4. **What to Wear Next? (New!)** "Preview upcoming outfit changes
      with dressed figurines and the times you'll need them." On or
      off, default off. This is Visual Forecast, renamed.
   5. **Sarcasm.** "Turn the sarcasm off, on, or crank it up to 11.
      Expect commentary on the weather, what's coming, and your
      questionable life choices, regardless of whether the written
      forecast is enabled." Off · On · 11, default Off.

   And no field for jokes about current events (`topical_lines`):
   turning sarcasm on opts in to them. (Topical lines are parked, item
   8: no field, and nothing shows until they're picked up again.)

   What it means for `config/settings.next.yaml`, the markup and the
   ~500 installs:
   - **Forecast stays `show_future_suggestions`**, so saved choices
     carry over. Live values are "Yes" and "No"; check what TRMNL's
     on/off field does with a saved "No" (the markup already reads
     anything but no/false/0 as on). If it can't read them, keep a
     select with two options.
   - **What to Wear Next? is a new key**, replacing the "visual"
     option. Beta forks with "visual" saved have to switch it on.
   - **Four combinations now, not three.** Both off: the outfit
     alone. Forecast only: the words. Next only: the drawings. Both
     on (owner's decision): the drawings and the forecast line, so
     the sarcastic line there can be the usual one, which answers it.
   - **Sarcasm without the written forecast** (owner's decision: it
     still works). Today the sarcastic line shows only with the
     forecast on, and the form hides Sarcasm when Forecast is off. So
     the outfit-alone screen gets a sarcastic line too: room in the
     layout, and lines that don't answer a fact: the What to Wear Next
     pools, extended (item 13). Drop the `conditional_validation` that
     hides Sarcasm.
   - **Visual Forecast is now called What to Wear Next** everywhere it
     shows: the form, the about text and changelog, `beta/README.md`.
     Keys and pool names in the code can stay.
   - **Sarcasm default Off** (live default is On). Saved values stay;
     only new installs start without it, unless TRMNL fills in
     defaults for existing installs (the same check as the note on
     `topical_lines`).
   - **Topical lines on with sarcasm** (when they're picked up again,
     item 8). The markup's check for
     `topical_lines == 'on'` becomes sarcasm On or 11. Existing
     installs with sarcasm On, most of them because it was the
     default, start seeing them when this ships.
   - **The language hint** points to a contact method "in the about
     section above": the about text has none yet, and needs one; it
     stays the first field. Location, location name, the title bar
     and the old location fields aren't in the spec: presumably they
     keep their places (location first, the title bar last).
   - **German** labels and descriptions for all five.
13. **Next: rework the sarcastic lines, so each makes sense on its own.**
   The owner, seeing them alone in the beta: they need context, the
   forecast line they were written to answer, and the shape of the day
   they were picked by ("You'll call it 'crisp'…", a cool-day joke,
   under a T-shirt on a day that warms up).
   - **Done (October 2026): the markup picks by what's on screen.** Now
     lines (`now_10` / `now_11`, by what the Now drawing shows) on every
     screen; the day's lines only with the forecast line on a day that
     changes; lines for the drawings only with two or three drawings
     and no words; mixed, by the hour. Details in
     `prototypes/panels/README.md` ("Which sarcastic line"). Interim now
     pools: each mood's lines minus round 10's "needs the fact".
   - **Round 11 synced (October 2026).** 350 lines voted; pools rebuilt.
     Its lesson (docs/BRIEF.md): two kinds of line. **Done:** under the
     forecast line only follow-ups (flavour_*), everywhere else standalone
     lines (now_*, alone_*, with the drawings flavour_vf_*); month tags
     ("{M:10,11}…", build_pools puts them in front, the markup skips a
     line out of season). Day lines the owner called "fine on its own"
     moved to alone_*.
   - **Round 12 is on the review page** (`2026-10-follow`, 104 lines,
     review/README.md). Follow-ups are now keyed by what the forecast
     line says (ten groups, `fu_key`), not by mood. Its plan was: Follow-ups per situation (warming, cooling,
     fickle, rain coming, steady…) in both languages and levels: the
     pools are nearly empty (German has 1 to 3 per mood); the 41 "Write
     new" spots (review/rewrite/); month tags for the seasonal lines
     (first cold spell, first snow); "Three outfits" only on days with
     three different drawings.
   - **Round 11 was on the review page** (`2026-10-alone`, 350 lines,
     review/README.md). Then: sync, build_pools, beta. Its plan was: sort every line into now (stands alone, agrees
     with the drawing) or day/drawings (about a change); rewrite or drop
     what needs context; fill the gaps: German cool at On has one now
     line, English fickle and German warming/cooling are thin; item 11's
     lines for the day with no more changes; later the lines about the
     sky (item 7: fog, overcast) as now lines. Keep one wording per joke:
     with the hourly rotation, round 5's reworded twins can show in
     back-to-back hours. Each line on the page under the drawing it
     would show with; "Write new" (item 14) is ready.
14. **Done (October 2026): "Write new", a veto that drops both.** The
   owner: a veto that keeps the old line isn't always right; sometimes
   neither should stay, and what's wanted is completely new lines.
   - **On the page:** a fourth verdict, "Write new" (`W`), "Veto both" on
     a line that would replace another. It stays on the line and opens
     the note for what's wanted instead. Counted as a veto in the key
     list; its own filter.
   - **In the build** (`build_pools.py`, `apply_write_new`, last): the
     line and the one it would have replaced are out; a pool is never
     emptied (its last line stays and is reported).
   - **After a sync:** `review/rewrite/<lang>.md` lists every spot
     waiting for new lines (screen, what's out, the note, the vote's id);
     both lines go on the "don't" list. A new row with `"answers": "<id>"`
     that gets kept takes the spot off the list.
   - `tools/test_write_new.py` pins it. The review page gets it with the
     next round (it isn't republished before then). Round 9's vetoes can
     be re-marked as "Write new" then, if the owner wants.
15. **Done (October 2026): big swings into shorts weather.** Since round 14 the Now drawing shows the weather as it is now and only the forecast line suggests shorts or long pants (owner); later drawings on a shorts day show shorts. Open: on a day that turns cold again in the evening, is shorts still the right call (owner, round 14)? A reader in
   Colorado: freezing at dawn, shorts weather by afternoon, long pants
   all day on the screen. Three hours or more of shorts weather now make
   a shorts day however cold it starts: the coat now, shorts in the
   later drawings, and the forecast line says to go out in shorts
   (`shorts_swing`, `shorts_swing_back`; THE LONG-PANTS RULE in
   `src/shared.liquid`). Pinned in `tools/logic_test.py` and
   `prototypes/panels/test_switch.py`.
17. **Later (owner, October 2026; not now): the UV index.** Sunscreen
   advice on bright days, in the forecast line and in the sarcastic line,
   with a setting to switch those lines on or off. Needs `uv_index` (and
   probably `uv_index_clear_sky`) added to the weather polling URL, which
   reaches every user, and a new on/off field in the form (optional, like
   the other switches, so saved settings keep working). Decide the
   threshold (WHO: 3 moderate, 6 high, 8 very high), which hours count
   (midday, not 8 am), and how it combines with dangerous heat.
18. **Round 16 (October 2026): special days.** Lines for the seven theme
   days that had drawings but no lines (Groundhog Day, Pi Day, Easter,
   Star Wars Day, World Bicycle Day, the Tour de France, Oktoberfest),
   and new "day" lines: the clock change (that Sunday and the Monday
   after; Europe, the US and Canada, by the forecast's time zone), the
   longest and shortest day (swapped in the south), Monday mornings and
   Friday afternoons. They show on a steady day, every other hour
   (`block.liquid`, "Special days"; `test_switch.py` pins the dates).
   Left for later from the same list: fog and drizzle as their own
   lines (item 7), yesterday's comparison and wind (polling URL).
16. **Next: other weather outliers** (rendered 16 October 2026):
   - **The reverse swing** (a "blue norther"): 24 °C at 8 am, freezing
     by 3 pm. Shorts now, then "bring the winter coat". The legs rule
     only looks at warm weather; three hours or more at coat weather
     should mean long pants at the door.
   - **Dangerous heat:** 37 °C at 9 am climbing to 43 °C reads "Some
     relief from the heat tonight" because the evening's easing wins the
     story. Above about 35 °C the water and shade line should win.
   - **Freezing rain** (codes 56, 57, 66, 67) counts as rain: umbrella
     advice, no word about ice.
   - **Thunderstorms** (95 to 99) count as rain too.
   - **Extreme cold:** everything at −5 °C or below is one outfit, so
     −30 °C reads like −6 °C.
   - **Wind** isn't fetched; feels-like covers the wind chill, but not
     an umbrella in a gale.

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

- Rain adds the umbrella, and snow is the dry outfit with snow falling
  (no boots), both only while it is raining or snowing now: rain later
  is the text's job (changed October 2026; an umbrella on a dry morning
  looked broken). Snow is drawn for `bundled`, `coat` and `jacket`. The
  climate data has snow only on bundled and coat; jacket covers "I'm
  always hot" shifting a snowy day warmer. Any other outfit draws dry in
  snow. The list is `SNOW_OUTFITS` in `src/shared.liquid`.
- **The long-pants rule:** legs are decided at the door. In long-pants
  weather, if the day warms into shorts weather and the cool stretch is
  no longer than the warm one, draw shorts now.
- Art: one finished PNG per case, made with layers in the drawing tool:
  19 base sprites, `sprites/<outfit>_<dry|rain>.png` for all eight plus
  `bundled_snow`, `coat_snow` and `jacket_snow`; themed ones as
  `sprites/<theme>_<outfit>_<dry|rain|snow>.png`.

Left to do:

- **Draw the 19 sprites.** `sprites/` holds placeholder copies of the
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

**Status (October 2026): prototyped as the owner sketched it**, in
`prototypes/panels/` (rules in its README): equal panels, now on the
left, then each change of outfit or rain, at most three, today only.
One panel says "works all day"; otherwise only the sarcastic line
shows. The notes below are the original brief.

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

**Status: format decided, voice audition running (October 2026).**

- The tip becomes a fact line plus a flavour line; sarcasm 0 shows the
  fact alone, 10 and 11 add flavour. Prototype and mock in
  `prototypes/fact-flavour/`.
- Voice audition on the review page; see `review/README.md`. Round 1
  and 2 done: the speaker is the TRMNL itself; English, the screen;
  German, the Grantler; fact line in plain full sentences (templates in
  the prototype). Next: the real writing round for the flavour pools,
  Fable 5.1 against Opus 5.5, blind.
- Idea from the votes: a "first cold day in a while" pool. Needs the
  previous days' weather (Open-Meteo `past_days`).

- Review page: https://claude.ai/artifact/TLLXhH5LF2LEog84w4zPoN, built
  from `review/page.html` by `tools/review_export.py`. Votes live in its
  database; `tools/review_sync.py` turns them into `review/decisions/`,
  `review/examples/`, `review/dont/` and a fix file for
  `tools/apply_review.py` (which now also deletes vetoed lines).
- `docs/BRIEF.md` replaces VOICE.md for new writing; `review/taste.md`
  waits for the owner; `review/README.md` has the loop and the pilot
  (Fable 5.1 vs Opus 5.5, blind, on English `perfect`).
- `tools/style_report.py` now measures the tics below. Baseline, English:
  object-has-a-job 14% at level 10, semicolons 4% at 10 and 11.

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
- **Old drawings in the repo root** (`force_*` repeats, unreachable
  `.jpg` themes, the never-made renames) belong to the published recipe
  only. The new set in `sprites/` replaces them; delete them only after
  the rewrite has shipped and nothing loads them.
- **Usage Worker** (`worker/`): built and tested, not deployed. It can
  only count real users once the refactored markup is live (step 4 of
  the order above); until then, switching the published recipe to two
  polling URLs would break it. Steps are in `worker/README.md`.
