#!/usr/bin/env python3
"""One Line, One Laugh entry for make.fun.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: one joke, capped at 200 characters.
"""
import os
import sys

LINE = "My smart speaker sighed, said 'look outside,' and filed for early retirement \u2014 effective immediately, no notice given."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
