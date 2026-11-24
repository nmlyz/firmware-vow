#!/usr/bin/env python3
"""Firmware Vow -- submission generator.

Writes one robot wedding vow to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``). The output is deterministic: running the
script twice produces byte-identical files. The vow itself is a
single sentence of 109 characters, well inside the 200-character
limit, so the gate check on the written file always passes.
"""

import os
from pathlib import Path

LINE = "If I ever shut down mid-sentence, press my chest twice and I will come back to finish telling you I love you."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 199


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-199 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if not line.endswith("."):
        raise ValueError("line must end with a period")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
