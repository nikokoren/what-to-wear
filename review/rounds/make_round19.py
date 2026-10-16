#!/usr/bin/env python3
"""
Round 19, units for rain and snow (October 2026).

    python3 review/rounds/make_round19.py

The last family of units: the rain and snow sentences (p_*; not the ice
and thunderstorm variants, which lead with the danger and keep the
separate pick). The unit replaces the rain sentence, which comes last:
alone on a day whose temperature doesn't change, after a temperature
sentence on one that does. Plus top-ups so every steady and layer
situation reaches three units (a situation needs two to use them).

Raw output in 2026-10-rain/<lang>.json, round 18's format; built by
make_round18.main. build_pools.py applies it like round 17.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import make_round18 as r18  # noqa: E402

ROUND = "2026-10-rain"

if __name__ == "__main__":
    r18.main(ROUND, "rn")
