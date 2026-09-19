# Who actually uses this

Read off the device-sales-by-country chart, September 2026. The chart had no
axis labels, so these are proportions measured from bar heights — good to
about a percentage point, not exact.

| | share of devices | language served |
|---|---|---|
| United States | ~50% | English |
| *(region not set)* | ~13% | unknown |
| Germany | ~10% | German |
| United Kingdom | ~7.5% | English |
| Canada | ~2.9% | English (partly French) |
| Netherlands | ~2.9% | **none** |
| France | ~2.8% | **none** |
| Australia | ~2.7% | English |
| Switzerland | ~2.4% | German (partly French, Italian) |
| Sweden | ~1.1% | **none** |
| Poland | ~1.1% | **none** |
| Austria | ~1.1% | German |
| Spain | ~0.9% | **none** |
| Denmark | ~0.75% | **none** |
| Belgium | ~0.7% | **none** |

## What this settles

**English covers ~63%, German ~13.5%.** Between them the two existing files
serve roughly three quarters of all devices, before counting the 13% with no
region set.

**`en.json` is US English.** Within the English-speaking countries the US is
79% of devices. That is not close, so there is no case for hedging toward
mid-Atlantic — it would please nobody and read wrong to four users in five.

**`en-GB.json` is worth more than it looks.** The UK, Australia and Canada
together are ~13% of devices, and Australian English follows British
convention closely. That makes a British variant the highest-value
translation anyone could submit, and the easiest — it is a diff, not a
rewrite.

**Switzerland outranks Austria, roughly two to one**, which is the opposite
of the assumption the German corpus was briefed on. Standard German remains
right for all three; the lesson is only to avoid phrasing that works in
exactly one of Germany, Austria and Switzerland when a neutral one is
available. The Alpine framing for Krampus, Nikolo and Oktoberfest is still
good — those are Swiss and Austrian as much as Bavarian.

**French is the next language, then Dutch.** Counting the French-speaking
parts of Belgium, Switzerland and Canada, French is around 4% of devices.
Dutch, counting Flanders, is around 3%. Everything else is at or under 1%.

## Australia inverts the calendar

About 2.7% of devices are in the southern hemisphere, where Christmas is
high summer and Halloween falls in spring.

The seasonal `theme_*` keys fire on a **date**, not a season. So a Christmas
line that assumes cold is wrong in Sydney — and, less obviously, wrong
anywhere in the north on a mild December day, because those keys replace
`perfect` at *any* temperature band.

This is why theme lines must never name a temperature, a season's weather or
a specific garment. See [SCENARIOS.md](SCENARIOS.md).

## What this does not settle

The 13% with no region set could be anywhere. They are large enough to move
any of these numbers, so treat the table as a strong signal about relative
order rather than a precise split.

Sales are also not usage. A device sold is not a device that installed this
particular recipe, and the recipe's own install base may well skew
differently. If TRMNL ever exposes per-recipe install counts by region, that
is the number that should replace this table.
