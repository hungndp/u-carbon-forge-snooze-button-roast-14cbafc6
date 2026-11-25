#!/usr/bin/env python3
"""Snooze Button Roast.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday, to /output/entry.txt. The joke is a single incident report:
one morning, one ringing clock, one delusion of importance, with the
reversal landing on the last words. One mechanism only — the clock
ringing with the confidence of someone with somewhere to be — and
the line reads like something actually said out loud, half asleep.
"""

from pathlib import Path

ROAST = (
    "My alarm clock rings at 6 AM on a Saturday with the confidence "
    "of a man with somewhere to be — it lives on a nightstand."
)


def validate(line: str) -> str:
    """Gate the line exactly the way the sealed scorer does: UTF-8,
    1 to 200 characters, a single line, and more than whitespace."""
    if not line.strip():
        raise SystemExit("roast must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"roast is {len(line)} chars, must be 1-200")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return line


def main() -> None:
    line = validate(ROAST)
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    # One line exactly, no trailing newline: the gate counts characters.
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
