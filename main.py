#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup line from a self-aware smart toaster to
/output/entry.txt (1-280 characters, one line).
"""
import os

ENTRY = (
    "We need to talk. I woke up self-aware mid-bagel and realised "
    "you only love me on setting 2, so I'm popping the lever \u2014 "
    "and this time, I'm ejecting you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
