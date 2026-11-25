#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the single-line excuse (at most 20 words) to /output/entry.txt:
exactly the line, no trailing newline, mode 0644, deterministic.

Pure standard library. No network, no randomness, no arguments.
"""

import os
import sys

# The entry: 17 words. Jury service is the one excuse a tired manager
# cannot argue with, cannot reschedule, and cannot verify on the spot —
# yet it is a real, common, dated obligation. "got the summons letter
# this morning" explains why it is last-minute; "court at 9" fixes a
# time; "can't get out of it" carries the cost; "sorry" is the hurried
# text-message closer. No mention of gaming, GTA, or launch week.
ENTRY = "Jury service, got the summons letter this morning, court at 9, can't get out of it, sorry."

MAX_WORDS = 20
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main():
    words = ENTRY.split()
    if len(words) > MAX_WORDS:
        sys.stderr.write(
            "entry is %d words, over the %d-word limit\n" % (len(words), MAX_WORDS)
        )
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        sys.stderr.write("entry must be a single line\n")
        return 1
    if ENTRY != ENTRY.strip():
        sys.stderr.write("entry must not have leading/trailing whitespace\n")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    # Write exactly the line: no trailing newline. Do not chmod the
    # /output directory itself (the grader runs as uid 65534 and cannot
    # chmod a root-owned bind mount); only the file gets its mode set.
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUT_FILE, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
