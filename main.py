#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

The text is a fixed literal, so the output is byte-identical on every run.
Python standard library only; no network access.
"""

import os

ENTRY_TEXT = (
    "There is a letter in a drawer in Lisbon that has never been sent. "
    "It begins, 'By the time you read this,' and stops there. "
    "The ink is forty years old. "
    "The address is still legible."
)


def main() -> None:
    # Fail loudly instead of ever writing an out-of-range entry.
    if not 1 <= len(ENTRY_TEXT) <= 280:
        raise ValueError(
            f"entry text is {len(ENTRY_TEXT)} characters, must be 1-280"
        )
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
