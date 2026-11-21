"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes the poem in entry.txt to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, stdlib only, no network, deterministic.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    source = HERE / "entry.txt"
    text = source.read_text(encoding="utf-8")
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry.txt fails the gate: must be 1-280 characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.txt")


if __name__ == "__main__":
    main()
