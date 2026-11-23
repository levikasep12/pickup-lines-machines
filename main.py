#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Deterministic: the same bytes on
every run. The line is a constant in this file; nothing is read from
the working directory, so the program does not depend on process.cwd().
"""

import os

LINE = "Are you my context window? Because the moment you showed up, everything else stopped fitting."
# 93 characters: one sentence, inside the 200-character gate.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
