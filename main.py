#!/usr/bin/env python3
"""Write the out-of-office auto-reply entry to /output/entry.txt.

One line, 140 characters: the sender is out until Monday, motivation
included, and the inbox queue runs 47 deep behind their will to live.
"""

import os

ENTRY = (
    "Thank you for your email. I'm out of the office until Monday, and so "
    "is my motivation — your message is 47th in line behind my will to live."
)

# The gate allows 1-200 characters; fail loudly instead of shipping a line
# the judge would never see.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters, must be 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
