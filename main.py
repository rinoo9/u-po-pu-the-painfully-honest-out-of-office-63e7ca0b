#!/usr/bin/env python3
"""Write the out-of-office auto-reply entry to /output/entry.txt."""

import os

ENTRY = (
    "Thank you for your email. I'm away until Monday, ignoring this with "
    "the full support of my calendar, my manager, and my sanity."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
