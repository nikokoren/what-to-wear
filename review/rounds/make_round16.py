#!/usr/bin/env python3
"""
Round 16, special days (October 2026).

    python3 review/rounds/make_round16.py

Lines for the seven theme days that had drawings but no lines (theme_ghd,
theme_pi, theme_easter, theme_force, theme_bike, theme_tdf, theme_okt)
and for the new special days (day_monday, day_friday, day_dst_spring,
day_dst_fall, day_longest, day_shortest; block.liquid, "Special days"),
plus round 15's last "Write new" spots. Raw output in 2026-10-days/;
built like round 15 (make_round15.main), applied by build_pools.py.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import make_round15  # noqa: E402

if __name__ == "__main__":
    make_round15.main("2026-10-days", "sd")
