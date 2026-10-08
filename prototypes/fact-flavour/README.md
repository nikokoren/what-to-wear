# Fact + flavour prototype

A proposal for the text rewrite (docs/TODO.md item 3): split the tip into

- **a fact line**, built from one short template per situation
  (`facts` in `lang/*.json` here), identical at every sarcasm setting, and
- **a flavour line**, picked by the mood of the day (`flavour_10`,
  `flavour_11`), never asked to carry a fact, absent at sarcasm 0. On a
  seasonal day with nothing else to say, a `theme_<name>` pool replaces it.

The stored setting values 0 / 10 / 11 keep working: 0 is the fact line
alone, 10 and 11 add flavour at two strengths.

`block.liquid` reads only what the scenario logic in `src/shared.liquid`
already works out; `build.py` splices it in and writes `build/proto/`.
The flavour lines are placeholders for the voice audition.

Mock with nine real days (OG and X, English and German, every setting):
https://claude.ai/artifact/JQHyySwWENqkdXd2q6KToE
