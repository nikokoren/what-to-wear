# Beta

The redesign as one fork: the fact line and the sarcastic line, Visual
Forecast, jokes about current events, and the new form. Everything here
is built by `python3 tools/build_beta.py`; don't edit it by hand.

**Current beta: `@5bd87a0`** (the commit to put in the texts URL below).

## Setting up the fork

1. **Fork the recipe.** TRMNL > Plugins > What to Wear > Fork. A fork
   gets no updates, and nothing done to it reaches anyone else.
2. **Form:** replace the fork's form fields with `beta/settings.yaml`.
3. **Polling URLs**, two lines, in this order (the markup reads the
   weather from the first and the texts from the second):

   ```
   https://api.open-meteo.com/v1/forecast?latitude={{ lat_lon | split: ',' | first | strip | default: latitude }}&longitude={{ lat_lon | split: ',' | last | strip | default: longitude }}&hourly=temperature_2m,precipitation_probability,apparent_temperature,weather_code&current=temperature_2m,apparent_temperature,weather_code&forecast_days=1&timezone=auto
   https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@5bd87a0/beta/lang/{{ language | default: 'en' }}.json
   ```

   No `#` anywhere: in a URL it starts a fragment, which never reaches
   the server, so `lang/##en.json` asks jsDelivr for the folder and gets
   an HTML page back.
4. **Markup:** `beta/shared.liquid` into the shared markup, and each
   `beta/views/<view>.liquid` into its view (full, half horizontal, half
   vertical, quadrant).
5. **In the fork's settings,** switch What to Wear Next? on (and
   Forecast as you like), save, and Force Refresh.

The drawings load from `sprites/` on `main`, where they already are.

## What to try

- **The two switches,** Forecast and What to Wear Next?, in all four
  combinations. Both on: the drawings and the forecast line. Both off,
  with sarcasm On: the outfit and a sarcastic line.
- **A saved "No" in the new on/off field** (this decides whether
  Forecast can become on/off at launch): before pasting the new form,
  set Forecast to "No" with the old form and save. Paste the new form.
  Does the Forecast box show off? Does the screen still have no
  forecast? Save once more without touching it, and check again. If the
  box shows on, or saving turns the forecast on, Forecast stays a
  select with "Yes"/"No" at launch.
- **Defaults:** after pasting, are What to Wear Next? off and Sarcasm
  as you had it? If TRMNL fills in defaults for an existing install,
  the new Sarcasm default (Off) would switch sarcasm off for everyone
  at launch.
- **Jokes about current events** are parked: the beta has none.
- **Sarcasm** Off, On and 11, **both languages**, **all four views**,
  landscape and portrait, OG and X.
- **Other weather:** change the location (Dubai for heat, Reykjavík for
  snow, Sydney for the other season, Bergen for rain) and Force Refresh.

## The texts are trimmed

TRMNL takes at most 100 KB from each polled URL, and the German texts
with everything merged in come to about 100.6 KB even minified. The
beta's files keep every key of the old forecast-text pools (`temp_*`,
`precip_*`) but only the first line of each: the beta never shows those
lines, and the logic only checks whether some of their keys exist. The
build renders 720 day shapes with the full and the trimmed texts and
stops unless they are identical; a year of real days in London, Vienna
and New York (6,588 screens) matched too.

## A new beta

Run `python3 tools/build_beta.py`, commit and push, and put the new
commit in the texts URL (and here). jsDelivr keeps each commit's files
forever, so a new commit is fetched fresh. Paste the markup again if it
changed.
