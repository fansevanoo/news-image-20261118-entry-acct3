#!/usr/bin/env python3
"""Write this entry's image to the grader's output directory.

The entry image (entry.png) is bundled in this repository. This program
simply copies it to the output directory the grader provides. It uses
only the Python standard library, needs no network, and writes the exact
same bytes on every run, so the grader's two runs always agree.
"""
import os
import shutil
import sys


def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(repo_dir, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png was not copied completely")
    # Confirm the copy is a PNG (first 8 bytes are the PNG signature).
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError("entry.png is not a PNG file")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
