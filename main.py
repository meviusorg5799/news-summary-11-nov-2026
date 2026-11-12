#!/usr/bin/env python3
"""Write the best summary of Wednesday 11 November 2026's world news.

make.fun bounty: news-summary-01 ("Write the best summary of
11 November's world news"). The program copies the researched summary
in summary.txt beside it to /output/entry.txt, following the kit's
starter pattern. It runs fully offline and deterministically: two runs
produce byte-identical output.

Python 3.13, standard library only.
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    source = os.path.join(_HERE, "summary.txt")
    if not os.path.isfile(source):
        raise SystemExit(f"missing source file: {source}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(
        source,
        os.path.join(OUTPUT_DIR, "entry.txt"),
    )


if __name__ == "__main__":
    main()
