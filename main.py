#!/usr/bin/env python3
"""Deliver the finished front page to the grading harness.

The 45-story newspaper image is already rendered next to this file as
entry.png (drawn by generate_image.py). The harness expects the picture
at /output/entry.png, so this script checks the picture is the one we
shipped, then copies it into place and proves the copy is identical.
"""

import hashlib
import shutil
import struct
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")
SIDE_PIXELS = 1024
BYTE_LIMIT = 1024 * 1024
PNG_MARK = b"\x89PNG\r\n\x1a\n"


def describe(path):
    """Return the byte size, pixel size and digest of the shipped picture."""
    raw = path.read_bytes()
    assert raw[:8] == PNG_MARK, "entry.png does not start with a PNG signature"
    assert raw[12:16] == b"IHDR", "entry.png has no IHDR chunk where expected"
    width = struct.unpack(">I", raw[16:20])[0]
    height = struct.unpack(">I", raw[20:24])[0]
    return len(raw), width, height, hashlib.sha256(raw).hexdigest()


def main():
    size, width, height, digest = describe(PAGE)
    assert size <= BYTE_LIMIT, f"entry.png is {size} bytes, over the 1 MiB cap"
    assert width == SIDE_PIXELS and height == SIDE_PIXELS, (
        f"entry.png is {width}x{height}, expected {SIDE_PIXELS}x{SIDE_PIXELS}"
    )
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PAGE, DESTINATION)
    assert DESTINATION.stat().st_size == size, (
        f"placed file is {DESTINATION.stat().st_size} bytes, expected {size}"
    )
    assert DESTINATION.read_bytes() == PAGE.read_bytes(), (
        "the copy in /output differs from entry.png"
    )
    print(
        f"entry.png delivered: {width}x{height}, {size} bytes, "
        f"sha256 {digest[:12]}..."
    )


if __name__ == "__main__":
    main()
