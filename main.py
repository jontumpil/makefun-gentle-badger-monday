"""Monday Morning Punchlines — entry by @jontumpil.

The punchline is assembled from three fragments and written to
/output/entry.txt for the sealed scorer.
"""

import os
import sys

FRAGMENTS = [
    "Monday morning is an audit: ",
    "weekend-you made the promises, ",
    "and Monday-you has to produce the receipts.",
]


def punchline():
    return "".join(FRAGMENTS)


def emit(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError as exc:
        print(f"cannot write entry: {exc}", file=sys.stderr)
        raise
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    emit(punchline())
