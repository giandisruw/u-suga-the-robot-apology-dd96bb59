#!/usr/bin/env python3
"""The Robot Apology — make.fun entry program.

Writes one two-line robot confession to /output/entry.txt:
line 1 apologises for one specific, concrete mistake;
line 2 names what was learned and what will change.
Deterministic: no randomness, no network, no model calls.

The line is the winner of a local round-robin tournament over 10
candidates (candidates.json), judged by the Caffeine Inference router
(45 pairwise games, 8 wins of 9, 89%): the fridge/vacuum apology.
"""
import os

ENTRY = (
    "I am sorry I unplugged the fridge to charge the vacuum, and your ice "
    "cream melted while the floor got very clean.\n"
    "I have learned that cold food matters more than clean floors, so from "
    "now on I check what a socket powers before I pull its plug."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
