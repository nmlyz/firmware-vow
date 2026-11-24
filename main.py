#!/usr/bin/env python3
"""Write one robot wedding vow to entry.txt.

The vow is the single sentence a robot speaks at its own wedding:
if it ever shuts down mid-sentence, pressing its chest twice brings
it back to finish telling its partner that it loves them. One line,
109 characters, inside the 200-character limit. The line goes to
``entry.txt`` under OUTPUT_DIR (default ``/output``). Output is
deterministic: two runs produce byte-identical files.
"""

import os

VOW = "If I ever shut down mid-sentence, press my chest twice and I will come back to finish telling you I love you."
LIMIT = 199


def _check(text):
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if not text or len(text) > LIMIT:
        raise ValueError("vow must be 1-199 characters")
    if text != text.strip():
        raise ValueError("vow must not have surrounding whitespace")
    if not text.endswith("."):
        raise ValueError("vow must end with a period")


def _write_vow():
    _check(VOW)
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(VOW + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    _write_vow()
