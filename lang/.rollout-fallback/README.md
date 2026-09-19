# Rollout fallback snapshot — do not edit

Frozen copy of the text libraries as they shipped **before** the 2026
rewrite. `tools/build_transitional.py` inlines these into
`src/shared.transitional.liquid`.

They exist for exactly one window: after the transitional markup reaches a
device but before the texts polling URL does. During that window the device
has no `IDX_1` to read, so it falls back to these — and a user who has not
yet received the new polling config keeps seeing exactly what they saw
yesterday, rather than a blank tip.

Once a device has the polling URL it reads `lang/<code>.json` and never
touches these again. Step 3 of the rollout deletes them from the markup
entirely.

So: never regenerate these from the live language files. Improvements to the
text belong in `lang/<code>.json`, which is where devices actually read from
once the rollout is done. Keeping this frozen is also what keeps the
transitional build under TRMNL's 100 KB markup ceiling — the rewritten
corpus is larger, and inlining it would not fit.

See docs/MIGRATION.md.
