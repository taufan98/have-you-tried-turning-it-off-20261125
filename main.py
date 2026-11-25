#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun bounty entry.

Writes one funny single line to /output/entry.txt: the line a hopeless
tech support agent gives a desperate customer. The twist is on the
classic itself — the agent took his own advice, turned his own computer
off, and it has stayed off ever since. Cheerful, useless, and the
customer is never the butt of the joke.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? "
    "I did it to my own computer this morning \u2014 "
    "it's been off ever since, and honestly, "
    "it's the best it's ever worked."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
