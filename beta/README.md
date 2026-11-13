# Beta

The redesign as one fork: the fact line and the sarcastic line, Visual
Forecast, jokes about current events, and the new form. Everything here
is built by `python3 tools/build_beta.py`; don't edit it by hand.

**Current beta: `@21f5325`** (the commit to put in the texts URL below).

The larger-outfit layout update is in `beta/views/`. For an existing beta
fork, replace all four view templates with these files. Shared markup,
texts and form settings are unchanged by this layout update.

The latest refinement enlarges the three-outfit half-vertical view in
landscape again, at the reviewed larger scale for every weather condition.
Every outfit in a row uses the same size, with no rain or snow downscaling.
The outer columns are inset to keep the weather artwork inside the card.
If the previous larger-outfit build is already installed, only
`beta/views/half_vertical.liquid` needs replacing.

## Setting up the fork

1. **Fork the recipe.** TRMNL > Plugins > What to Wear > Fork. A fork
   gets no updates, and nothing done to it reaches anyone else.
2. **Form:** replace the fork's form fields with `beta/settings.yaml`.
3. **Polling URLs**, two lines, in this order (the markup reads the
   weather from the first and the texts from the second):

   ```
   https://api.open-meteo.com/v1/forecast?latitude={{ lat_lon | split: ',' | first | strip | default: latitude }}&longitude={{ lat_lon | split: ',' | last | strip | default: longitude }}&hourly=temperature_2m,precipitation_probability,apparent_temperature,weather_code&current=temperature_2m,apparent_temperature,weather_code&forecast_days=2&timezone=auto
   https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@21f5325/beta/lang/{{ language | default: 'en' }}.json
   ```

   No `#` anywhere: in a URL it starts a fragment, which never reaches
   the server, so `lang/##en.json` asks jsDelivr for the folder and gets
   an HTML page back.
4. **Markup:** `beta/shared.liquid` into the shared markup, and each
   `beta/views/<view>.liquid` into its view (full, half horizontal, half
   vertical, quadrant).
5. **In the fork's settings,** switch What to Wear Next? on (and
   Written forecast as you like), save, and Force Refresh.

The drawings load from `sprites/` on `main`, where they already are.

## What to try

- **The two switches,** Written forecast and What to Wear Next?, in all four
  combinations. Both on: the drawings and the forecast line. Both off,
  with sarcasm On: the outfit and a sarcastic line.
- **A saved "No" in the new on/off field** (this decides whether
  Forecast can become on/off at launch): before pasting the new form,
  set Forecast to "No" with the old form and save. Paste the new form.
  Does the Written forecast box show off? Does the screen still have no
  forecast? Save once more without touching it, and check again. If the
  box shows on, or saving turns the forecast on, Written forecast stays a
  select with "Yes"/"No" at launch.
- **Defaults:** new installs get What to Wear Next? and Sarcasm (On)
  switched on. For an existing install, after pasting: is What to Wear
  Next? still off on the screen, and Sarcasm as you had it? If TRMNL
  fills in form defaults for an existing install without a save,
  everyone would get the drawings at launch. Then open the form: the
  box shows ticked (the new default), so saving switches the drawings
  on. That is expected; only a change without a save would be a
  surprise.
- **The evening, from 8 pm:** tonight on the left, tomorrow on the
  right. It needs the new weather URL above (`forecast_days=2`): an
  existing beta fork has to paste it again, or the evening stays as it
  was. Try **When do you head out?** at 6 am and 9 am on a day that
  starts cold, and "It varies". The evening sentences and jokes are
  stand-ins until their writing round.
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
