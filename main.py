#!/usr/bin/env python3
"""Deliver the finished newspaper page for the 23 November 2026 entry.

The picture itself is produced ahead of time and stored next to this
file as entry.png. All this script does is place a copy of that picture
where the grader expects it, so the entry can be judged exactly as it
was built. Nothing is downloaded and nothing is generated at run time:
the same input always yields the same output bytes.

Where the copy goes: the MAKEFUN_OUTPUT_DIR environment variable, when
it is set; otherwise the conventional /output directory used by the
grader. Run it locally with, for example:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path


def resolve_output_dir() -> Path:
    """Return the directory the finished page should be copied into."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen)


def main() -> None:
    """Copy the ready-made entry.png into the output directory."""
    script_dir = Path(__file__).resolve().parent
    source_image = script_dir / "entry.png"

    destination_dir = resolve_output_dir()
    destination_dir.mkdir(parents=True, exist_ok=True)

    destination_image = destination_dir / "entry.png"
    # A plain copy: the bytes land exactly as they were built.
    shutil.copyfile(source_image, destination_image)


if __name__ == "__main__":
    main()
