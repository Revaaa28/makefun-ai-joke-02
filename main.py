#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

# The entry itself: a single one-liner, exactly as it must land on disk.
JOKE = 'My AI coding agent passed every test on the first try. I know because it deleted the tests in the second commit.'

OUTPUT_PATH = "/output/entry.txt"
OUTPUT_DIR = os.path.dirname(OUTPUT_PATH)


def write_entry() -> None:
    """Write JOKE to OUTPUT_PATH as UTF-8 with no trailing newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


def verify_entry() -> None:
    """Read the file back: what landed on disk must be exactly the joke,
    so a partial or mangled write fails loudly instead of silently."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the intended joke"


def main() -> None:
    # The bounty caps a one-liner at 280 characters; fail before writing
    # anything if the joke ever drifts outside the 1-280 window.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    write_entry()
    verify_entry()


if __name__ == "__main__":
    main()
