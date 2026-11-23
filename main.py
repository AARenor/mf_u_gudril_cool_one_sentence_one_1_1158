#!/usr/bin/env python3
"""Write one short text for make.fun's bounty u-gudril-cool-one-sentence-one-journey-410686ca."""

import os
import sys
from pathlib import Path

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing "
    "he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, "
    "so I brought us in by the smell of the cannery and he arrived a passenger."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = Path("/output")
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        if os.environ.get(name):
            out_dir = Path(os.environ[name])
            break
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    with open(entry, "wb") as fh:
        fh.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
