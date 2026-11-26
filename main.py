#!/usr/bin/env python3
"""Write the out-of-office auto-reply entry to /output/entry.txt."""

import os

ENTRY = (
    "Thank you for your email. I'm away until Monday, ignoring this with "
    "the full support of my calendar, my manager, and my sanity."
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
