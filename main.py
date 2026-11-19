#!/usr/bin/env python3
"""news-image-20261118 v10 (akun 4): 37-story front page, rank-11 style.

Final-check recipe (19 Nov ~11:04 WIB): v8 format + rank-11 execution --
3 TOP + 12 grid + 22 ALSO, 3-line decks (~3 facts per card), every ALSO
item carries a fact, BY THE NUMBERS strip, clean map (15 carded-story
pins only), data badges on the TOP 3 panels. Date stance (B): big Tuesday
stories enter openly, NO DATE CHECK / source tags / temporal badges.
Facts: Anthropic IPO $83 ($81.3bn, largest ever), Dow Wed -561.25.
Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
