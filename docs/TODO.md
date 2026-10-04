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
- **Review the `wet_again` lines** (en and de, all three sarcasm levels)
  for voice; they were written to fill the new scenario.
- **Usage Worker** (`worker/`): deploy it and switch the second polling
  URL to start counting forecast on/off and sarcasm level. Steps are in
  `worker/README.md`.
