#!/bin/sh
# Download Meteostat hourly station files for every city in stations.txt.
#   sh tools/climate/fetch.sh <empty data dir>
set -e
dir=${1:?usage: fetch.sh <data dir>}
mkdir -p "$dir"
here=$(dirname "$0")
while read -r id name cc tz w; do
  curl -sS --max-time 120 "https://bulk.meteostat.net/v2/hourly/$id.csv.gz" \
    -o "$dir/$name.csv.gz" -w "$name $id %{http_code}\n"
done < "$here/stations.txt"
