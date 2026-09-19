# What to Wear

Source for the [What to Wear](https://trmnl.com/recipes/182853) TRMNL recipe:
your device reads the local forecast and tells you what to put on, with 30+
hand-drawn outfits and seasonal themes.

This repo holds the artwork the plugin loads at render time, the Liquid
markup, and — since the v1.3 refactor — all of the phrasing.

## Layout

```
*.png, *.jpg          outfit sprites, loaded by the markup at render time
lang/<code>.json      everything the plugin says, one file per language
src/shared.liquid     the markup. Paste into TRMNL's shared markup box
src/views/            the four view templates
src/shared.transitional.liquid
                      generated; only needed during the rollout
config/               form fields and polling URLs, for reference
tools/                validation and render tests
docs/                 how to translate, how to roll out
```

## Changing the words

Edit `lang/<code>.json`. Nothing else. Then:

```bash
python3 tools/validate_lang.py
```

New language? See [docs/TRANSLATING.md](docs/TRANSLATING.md) for the process
and the three voices, and [docs/SCENARIOS.md](docs/SCENARIOS.md) for what
each scenario key means. It is one file
and a PR.

## Changing the logic

Edit `src/shared.liquid`, then regenerate the transitional build and run the
tests:

```bash
pip install python-liquid
python3 tools/build_transitional.py
python3 tools/render_test.py
```

`render_test.py` renders every scenario in every language and compares the
output against the pre-refactor markup, so a logic change that quietly alters
what people read fails the build.

## Deploying

Markup goes into the TRMNL plugin editor by hand; this repo is the source of
truth, not a deploy target. The one path that needs care is the text
extraction rollout — see [docs/MIGRATION.md](docs/MIGRATION.md).

TRMNL caps shared markup at 100 KB. Before the refactor this file was 100,158
bytes, which is what prompted it. It is now 33 KB.

## A note for anyone who forked

Forking takes a full copy at fork time and receives no later updates, so none
of this reaches you and nothing breaks. You also will not get new artwork,
new languages or fixes. Re-installing (rather than forking) is how you get
back on the update path.
