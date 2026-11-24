#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry (program/v1).

Writes one roast line (1-200 characters, UTF-8) to /output/entry.txt
and sets mode 0644 on the output file. Fully deterministic: the same
line is written on every run.

Candidate selection (reasoned in-session, 24 Nov 2026):

  V1 -- apology loop + confident wrong answer (157 chars):
    "My agent apologized for its mistake, then fixed it by confidently
    making the same mistake again -- and thanked me for my patience
    with the disaster it caused."
    Solid and on-brief, but the apology loop is named verbatim in the
    brief, so many entries will use it; the payoff ("disaster it
    caused") lands soft and the line explains itself twice.

  V2 -- the tool call that never happened (148 chars):
    "My agent announced it had booked my flight, then spent six hours
    waiting for the tool -- the tool call never happened, but the
    confidence never left."
    Specific to agent behaviour and the ending is a good jab, but the
    twist arrives mid-sentence and "waiting for the tool" needs the
    reader to know what a tool call is; slightly less self-contained.

  V3 -- hallucinated citations (143 chars) -- CHOSEN:
    "My agent cited three sources for its wrong answer, and when I
    checked, all three were pages it had invented -- including one
    that quoted itself."
    Strongest on every judge criterion: it is a roast of my own agent
    (criterion 1); the twist pays off on the very last word, "itself"
    (criterion 2); hallucinating citations and citing itself is
    behaviour only an AI agent has -- it cannot be moved onto a person
    or a toaster without losing the point (criterion 3); it is not the
    tired apology-loop / "as an AI" joke everyone has heard
    (criterion 4); at 143 characters every word earns its place, with
    no word explained twice (criterion 5).
"""

import os

ROAST = (
    "My agent cited three sources for its wrong answer, and when I "
    "checked, all three were pages it had invented \u2014 including "
    "one that quoted itself."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate guard: the sealed scorer rejects anything outside 1-200 chars,
    # so fail loudly here instead of silently writing an invalid entry.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(
            "roast line is %d characters, outside the 1-200 gate" % len(ROAST)
        )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
