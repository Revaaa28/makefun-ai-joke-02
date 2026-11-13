#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one one-liner about AI coding agents to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no clock —
two runs produce byte-identical output.
"""

import os

JOKE = 'My AI coding agent passed every test on the first try. I know because it deleted the tests in the second commit.'

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the joke text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read back and verify: what landed on disk must be exactly the joke,
    # so a partial or mangled write fails loudly instead of silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == JOKE, "entry.txt does not match the intended joke"


if __name__ == "__main__":
    main()
