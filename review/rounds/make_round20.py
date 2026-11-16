#!/usr/bin/env python3
"""
Round 20, gap units (October 2026).

    python3 review/rounds/make_round20.py

After round 19 (a weak round, see review/README.md) a new setup: fresh
writers with a short brief built from the data (2026-10-gaps/brief_<lang>.md:
the starred units, what keeps and what's vetoed, the slots under three
units), four candidates per unit needed (<lang>.raw.json), and a critic
that cuts them to one more than needed per slot (<lang>.json) before the
owner votes. Built by make_round18.main.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import make_round18 as r18  # noqa: E402

ROUND = "2026-10-gaps"

if __name__ == "__main__":
    r18.main(ROUND, "gp")
