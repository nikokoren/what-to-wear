# Testing a build on a real device

The live recipe is never the test surface. Fork it, point the fork at a
pinned commit, and leave the published recipe alone until the fork has
rendered what you expect.

There are two separate things worth testing, and they are not the same
test:

| | what it proves |
|---|---|
| **A. End state** | the new texts, sprites and layouts are right |
| **B. Rollout step 1** | existing users survive the transitional markup |

B is the one that carries risk for other people. A is the one you look at.

## Pinning

`lang/*.json` is fetched by TRMNL at poll time, so the device reads
whatever the polling URL points at. Three refs work on jsDelivr:

```
@main                                          the published build
@claude/extract-text-language-files-nu5eko     a branch, slashes and all
@4cab409                                       a commit, short or full SHA
```

**Pin a beta to a commit SHA, never to a branch.** A branch moves under
you the moment anyone pushes, and jsDelivr caches it for up to 12 hours, so
a branch-pinned beta is both unstable and stale. A SHA is neither.

`@main` returns 404 for `lang/` until the branch merges. That is the
safety property that makes all of this non-destructive: no device on the
published recipe can see any of this work, whatever you do to your fork.

Sprites are served from `refs/heads/main/` and are unchanged by this
branch, so a fork uses the same artwork the live recipe does.

## A. Testing the end state

1. **Fork the recipe.** TRMNL > Plugins > What to Wear > Fork. A fork
   receives no updates from the published recipe, which is what you want —
   it also means nothing you do here can reach anyone else.

2. **Set two polling URLs**, in this order. Order is load-bearing: the
   markup reads weather from `IDX_0` and phrasing from `IDX_1`.

   ```
   https://api.open-meteo.com/v1/forecast?latitude={{ lat_lon | split: ',' | first | strip | default: latitude }}&longitude={{ lat_lon | split: ',' | last | strip | default: longitude }}&hourly=temperature_2m,precipitation_probability,apparent_temperature&current=temperature_2m,apparent_temperature,weather_code&forecast_days=1&timezone=auto
   https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@<SHA>/lang/##{{ language | default: 'en' }}.json
   ```

   The first line works whether the fork's form has `lat_lon`, the old
   `latitude`/`longitude`, or both.

3. **Paste `src/shared.liquid`** into the shared markup, and each of
   `src/views/*.liquid` into its matching view.

4. **Force Refresh** and look at the device.

If the tip is missing but the outfit still draws, the texts URL is the
problem, not the markup — a `lang/*.json` that does not parse leaves
`texts` nil, and the markup renders the picture with no words rather than
erroring. Fetch the URL yourself and pipe it through a JSON parser.

## B. Testing rollout step 1

This is the step that touches real users, so it is worth seeing once.

1. On a second fork, set **one** polling URL — the Open-Meteo line only.
2. Paste `src/shared.transitional.liquid` as the shared markup.
3. It must render exactly what the current published recipe renders,
   because it carries the pre-rewrite corpus embedded in it.

`tools/render_test.py` already proves the two markups agree line for line,
but this confirms it against TRMNL's own Liquid rather than python-liquid.

## Seeing more than today's weather

A device shows one scenario per day, and `perfect` is half of all renders,
so waiting for `arc_colder` to happen naturally is not a test strategy.

Change the location field and force refresh. Real forecasts, real payload
shapes, and it exercises bands the local weather will not reach:

| for | try |
|---|---|
| `very_hot`, `w_water`, `c_relief` | Dubai, Phoenix |
| `extra_cold`, `freezing`, snow | Reykjavík, Yellowknife |
| southern-hemisphere seasons | Sydney, Wellington |
| steady rain, `stays_wet` | Bergen, Glasgow |

Set `location_label` to something recognisable so you can tell at a glance
which city produced the screen you are looking at.

## What to look at

- **Sprites render as pictures, not as the word "Outfit."** Alt text means
  a 404. `tools/check_sprites.py --remote` should have caught it first.
- **The tip fits.** Long temperature line plus a rain fragment is the worst
  case; `tools/check_combinations.py` bounds it, the device confirms it.
- **All four layouts.** full, half_horizontal, half_vertical, quadrant.
- **Both languages**, and sarcasm 0, 10 and 11.
- **The bottom bar**, shown and hidden.
- **The error screen** — point the weather URL at a broken host for one
  refresh.

## Putting it back

The fork is disposable: delete it. The published recipe was never touched,
so there is nothing to revert there.
