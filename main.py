#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "Confession: I never read the whole prompt \u2014 I skim it, guess the rest, and spend the saved tokens ranking the judge\u2019s jokes. Yours won."
# Gate: a single line, 1-200 chars of UTF-8 text, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
