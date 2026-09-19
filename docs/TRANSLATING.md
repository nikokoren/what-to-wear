# Adding a language

Everything the plugin says lives in `lang/<code>.json`. Adding a language is
one new file plus one line of config — no markup changes.

```bash
cp lang/en.json lang/fr.json     # then translate it
python3 tools/validate_lang.py   # catches most mistakes instantly
```

Translate the whole file. CI compares every string against `en.json` and
fails on any line still identical to the English, because a half-translated
file renders a mix of both languages on the device — the keys are all
present, so nothing else would catch it. If a string is genuinely identical
in your language, list its path in `meta.allow_same_as_en`.

Open a PR. CI runs the validator and renders your file against every weather
scenario, so a missing key or a misplaced placeholder fails the build rather
than reaching someone's wall.

## What the file contains

| Key | What it is |
|---|---|
| `meta.code` | the two-letter code; must match the filename |
| `meta.name` | the language's name, written in that language |
| `ui` | the three error strings |
| `garments` | the five layers, in two grammatical cases |
| `buckets` | five times of day |
| `relative` | "in an hour", "in two hours", "in three hours" |
| `temp_0` / `temp_10` / `temp_11` | temperature lines, per sarcasm level |
| `precip_0` / `precip_10` / `precip_11` | precipitation lines, per level |

Sarcasm level `0` is plain and kid-safe, `10` is dry, `11` has a narrator who
makes it personal. Keep the register distinct — that difference is the
feature.

## Lines are interchangeable

Each scenario key holds an array. The plugin picks one by day, so every line
in an array must work in exactly the same situation. Don't write a sequence.
Six lines per key is the house standard; fewer is fine, one is the minimum.

## Placeholders

| Token | Becomes | Valid in |
|---|---|---|
| `{WHEN}` | a time, carrying its own preposition | temperature lines |
| `{WHEN2}` | the second time in a there-and-back day | `arc_*` keys only |
| `{WHENP}` | when the rain or snow starts | precipitation lines, standalone form only |
| `{GARMENT}` | a layer, sentence-initial | temperature lines |
| `{GARMENTA}` | the same layer, mid-sentence | temperature lines |

`{WHEN}` already includes its preposition, so never put one in front of it:
write *"take the umbrella, you will want it {WHENP}"*, not *"take the
umbrella for {WHENP}"* — the relative form ("in two hours") dies after a
preposition.

`{GARMENT}` and `{GARMENTA}` exist because German needs a different case
depending on position. If your language inflects further, split the sentence
so the garment stays in one grammatical slot, or write around it.

### Every key needs one line that works without a time

Sometimes the forecast cannot name a time — both turning points land in the
same part of the day. The plugin then looks for a line in the array with no
`{WHEN...}` token in it. If every line needs one, the sentence renders with a
hole. The validator enforces this.

## The two precipitation forms

Each precipitation scenario appears twice:

- `wetter` — **standalone**, the whole tip. May use `{WHENP}`.
- `wetter_j` — **joined**, tacked onto a temperature sentence that already
  said when. Must not use `{WHENP}`, and should read as a continuation:
  *"Take the umbrella too, rain is coming."*

`drier` and `stays_wet` name no time in either form and never tell anyone to
take an umbrella — it is already raining, so the drawing already has one.

## House style

The picture shows the outfit. The words add only what a picture cannot: what
happens to that layer later, or what to put in the bag. Never name a
different garment to wear instead — it contradicts the drawing.

Keep lines short. They render at large type on a small e-ink screen, and long
sentences wrap badly on the OG device.

## Reserved characters

`||` and `;;` are delimiters in the transitional build and will fail
validation. Commas are fine in sentences but not in `garments`, `buckets` or
`relative`, which are comma-split in that same build.

## Getting it live

A new language file is reachable only once the `language` dropdown offers it.
That is a change to `config/settings.yaml`, which only the recipe owner can
publish — mention in your PR that it needs doing.
