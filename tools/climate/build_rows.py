"""Feels-like climate of the audience, from Meteostat hourly station data.
usage: python3 -I build_rows.py <data_dir> <stations.txt>   (writes <data_dir>/rows.json)"""
import csv, gzip, math, sys, json, collections, datetime as dt
from zoneinfo import ZoneInfo

DATA, STATIONS = sys.argv[1], sys.argv[2]
COUNTRY = {'US': 50, 'DE': 10, 'GB': 7.5, 'CA': 2.9, 'NL': 2.9, 'FR': 2.8, 'AU': 2.7,
           'CH': 2.4, 'SE': 1.1, 'PL': 1.1, 'AT': 1.1}
REGION = {'US': 'US', 'CA': 'US', 'AU': 'AU'}  # everything else: Europe

def apparent(t, rh, ws_kmh):
    # Australian BoM / Steadman apparent temperature without radiation:
    # AT = Ta + 0.33 e - 0.70 ws - 4.00, e in hPa, ws in m/s
    e = rh / 100 * 6.105 * math.exp(17.27 * t / (237.7 + t))
    return t + 0.33 * e - 0.70 * (ws_kmh / 3.6) - 4.00

cities = []
for line in open(STATIONS):
    sid, name, cc, tz, w = line.split()
    cities.append((name, cc, tz, float(w)))
csum = collections.defaultdict(float)
for _, cc, _, w in cities: csum[cc] += w

rows = []  # (weight, region, local_dt, AT, prcp or None, temp)
for name, cc, tz, w in cities:
    z = ZoneInfo(tz); recs = []
    with gzip.open(f'{DATA}/{name}.csv.gz', 'rt') as f:
        for r in csv.reader(f):
            if not r[0].startswith(('2023', '2024', '2025')): continue
            if r[2] == '' or r[4] == '': continue
            t, rh = float(r[2]), float(r[4])
            ws = float(r[8]) if r[8] else 10.8
            pr = float(r[5]) if r[5] else None
            utc = dt.datetime.fromisoformat(r[0]).replace(hour=int(r[1]), tzinfo=dt.timezone.utc)
            loc = utc.astimezone(z)
            recs.append((loc, apparent(t, rh, ws), pr, t))
    share = COUNTRY[cc] * w / csum[cc]
    for loc, at, pr, t in recs:
        rows.append((share / len(recs), REGION.get(cc, 'EU'), name, loc, at, pr, t))
    print(f'{name:13} {cc} {len(recs):6} hours  share {share:5.2f}%', file=sys.stderr)

json.dump([(w, reg, n, loc.isoformat(), at, pr, t) for w, reg, n, loc, at, pr, t in rows],
          open(f"{DATA}/rows.json", "w"))
print('rows', len(rows), file=sys.stderr)
