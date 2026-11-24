#!/usr/bin/env python3
"""Write one houseplant out-of-office auto-reply to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), validates the line
(1-120 characters, not only whitespace, single line), writes it as
UTF-8 with no trailing newline and mode 0644, then reads the file
back to confirm what was written.
"""

import os
import stat
import sys

ENTRY = (
    "Out of office: I'm the snake plant. "
    "Two sips of water a year, four managers outlived. "
    "I'll reply when one outlasts me."
)

MAX_LENGTH = 120


def validate(text):
    """Check the entry line against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if len(text) < 1 or len(text) > MAX_LENGTH:
        raise ValueError(
            "entry length %d is outside 1-%d characters" % (len(text), MAX_LENGTH)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be encodable as UTF-8
    return text


def main():
    entry = validate(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    os.chmod(path, 0o644)

    # Read back and confirm the written file matches exactly,
    # byte for byte, with no trailing newline added.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != entry:
        raise ValueError("written file does not match the entry")
    if os.path.getsize(path) != len(entry.encode("utf-8")):
        raise ValueError("written file size does not match the entry bytes")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise ValueError("entry.txt mode is %o, expected 0644" % mode)

    print("wrote %s (%d characters)" % (path, len(entry)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
