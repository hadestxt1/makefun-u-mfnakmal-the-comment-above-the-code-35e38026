"""The Comment Above the Code.

Writes one fixed comment line to entry.txt in the output directory.
The line is a single line a developer might leave above fragile
production code, 149 characters, well under the 200-character gate,
and it is written exactly the same on every run: no clock, no
randomness, no network, no model calls, standard library only.

The joke: the function is load-bearing in the most literal sense.
Nobody knows what it does, the tests can only vouch for yesterday,
and the one time someone deleted it, invoicing stopped for a day.
The punchline lands on the last words, as the judge's brief asks:
the deletion is the proof the warning was real.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys


COMMENT = (
    "This function is load-bearing: nobody knows what it does, "
    "the tests only prove it worked yesterday, and deleting it "
    "once stopped invoicing for a day."
)

MAX_CHARS = 200


def check_line(line):
    """Refuse anything that would fail the gate, before writing."""
    if not line or not line.strip():
        raise ValueError("comment line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "comment line is %d chars, over %d" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("comment line must be a single line")
    return line


def output_path():
    """Where the grader expects the text: $MAKEFUN_OUTPUT_DIR, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main(argv):
    line = check_line(COMMENT)
    if len(argv) > 1:
        target = argv[1]
    else:
        target = output_path()
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        # No trailing newline: the gate counts the file's characters,
        # so the file holds exactly the comment line, nothing more.
        handle.write(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
