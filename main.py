#!/usr/bin/env python3
"""Write the out-of-office auto-reply entry to /output/entry.txt."""

import os

ENTRY = (
    "Thank you for your email \u2014 I'm on holiday and not reading this, "
    "because the inbox will still be here when I return; I'll reply properly "
    "once I've recovered from coming back to it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
