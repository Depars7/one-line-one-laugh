#!/usr/bin/env python3
"""Write the chosen one-liner to /output/entry.txt.

Bounty: One Line, One Laugh
(slug u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a, $2).

Draft line (v1): the robot vacuum maps the flat, then behaves like a
disappointed guest and rates the place. The turn lands on the last
words: a household appliance leaving a review.

Revision (v2, see DESIGN.md): "finished mapping" cut to "mapped"
(-8 characters). Same joke, punchline arrives sooner, nothing left
to trim. Final line: "My Roomba mapped my apartment and left a
one-star review." (57 characters).

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only white space. The file is written with no trailing
newline, so the judged text is exactly this line.
"""

import os

LINE = "My Roomba mapped my apartment and left a one-star review."
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("line must not be padded with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no line breaks)")
    if not 1 <= len(line) <= 140:
        raise ValueError("line must be 1-140 characters long")
    line.encode("utf-8")


def main() -> None:
    os.umask(0o022)
    validate_line(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: the bytes on disk must be exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("verification failed: /output/entry.txt differs")


if __name__ == "__main__":
    main()
