# Feels-like climate of the audience

Measures how often each feels-like temperature occurs where What to Wear's
devices are, so outfit bands can be placed where the days actually are.

- `stations.txt`: Meteostat station id, city, country, time zone, and the
  city's weight within its country. Country weights are the device shares
  in `docs/AUDIENCE.md` (in `build_rows.py`).
- Apparent temperature is computed from air temperature, humidity and
  wind (Australian BoM / Steadman, without sun). Open-Meteo's own value
  is the same family but not identical, so treat shares as approximate.
- Uses the three full years 2023-2025, local daytime hours 07-21 and the
  07:00 dressing hour.

```bash
sh tools/climate/fetch.sh /tmp/climate                 # ~140 MB, no key needed
python3 -I tools/climate/build_rows.py /tmp/climate tools/climate/stations.txt
python3 -I tools/climate/compare_ladders.py /tmp/climate/rows.json
```

Edit the `LADDERS` table in `compare_ladders.py` to try a candidate: it
prints each outfit's share of daytime hours, of 7 am readings and of wet
hours, and how often a day changes outfit between 08:00, the afternoon
peak and 19:00.
