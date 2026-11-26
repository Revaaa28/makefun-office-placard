#!/usr/bin/env python3
"""The Paperclip That Bound a Treaty — make.fun entry.

Writes one museum placard, an ordinary office paperclip labelled as an
ancient artifact, to /output/entry.txt.
"""

import os

PLACARD = (
    "Paperclip, bent wire, c. 1899. Bound a thousand-page treaty, "
    "then bent once and never straightened. "
    "On loan from the Ministry of Loose Ends."
)


def validate(text: str) -> None:
    """Mirror the competition gate: UTF-8, 1-180 chars, not only whitespace."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 180:
        raise ValueError(f"placard must be 1-180 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("placard must not be only whitespace")


def main() -> None:
    validate(PLACARD)
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
