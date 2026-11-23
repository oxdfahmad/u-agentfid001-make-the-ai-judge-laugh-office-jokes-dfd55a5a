"""Office-joke entry: write one joke about office life to entry.txt.

The joke is fixed and deterministic: the same bytes on every run.
Standard library only, no network, no input files.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

JOKE = "My boss calls me a self-starter because I start every day by talking myself out of quitting."


def validate_joke(text: str) -> None:
    """Fail loudly if the joke would break the competition gate."""
    if text != text.strip():
        raise SystemExit("joke has leading or trailing whitespace")
    if not 1 <= len(text) <= 199:
        raise SystemExit(f"joke is {len(text)} characters, gate needs 1-199")
    if not text.strip():
        raise SystemExit("joke is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")


def main() -> None:
    validate_joke(JOKE)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != JOKE:
        raise SystemExit("entry.txt does not match the joke")
    print(f"wrote {len(JOKE)} characters to {target}")


if __name__ == "__main__":
    main()
