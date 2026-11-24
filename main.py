#!/usr/bin/env python3
"""THE WORLD — 23 November 2026. Entry for news-image-20261123.

The program copies the newspaper image beside this file to the
output directory. It uses only the Python standard library, needs
no network, and writes the same bytes on every run.

Run locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
In the grader it writes to /output/entry.png.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    if not SOURCE.is_file():
        print("entry.png is missing beside main.py in",
              HERE, file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # A plain copy: the bytes written are exactly the bytes shipped,
    # so two runs always write the same bytes.
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
