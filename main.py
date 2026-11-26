#!/usr/bin/env python3
"""The Paperclip That Bound a Treaty — make.fun entry.

Writes one museum placard, an ordinary office paperclip labelled as an
ancient artifact, to /output/entry.txt.
"""

import os
import re

PLACARD = (
    "Paperclip, bent wire, c. 1899. Bound a thousand-page treaty, "
    "then bent once and never straightened. "
    "On loan from the Ministry of Loose Ends."
)


def validate(text: str) -> None:
    """Mirror the competition gate: UTF-8, 1-180 chars, not only whitespace.

    Also check the placard's museum-label structure: a single line with an
    object/material header, an approximate date, at least one full
    sentence, and a provenance segment, ending with a period.
    """
    text.encode("utf-8")
    if not 1 <= len(text) <= 180:
        raise ValueError(f"placard must be 1-180 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("placard must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("placard must be exactly one line")
    # Header is "Object, material, date": the material is the second
    # comma-separated segment and must be present and non-empty.
    header = text.split(".", 1)[0]
    segments = [segment.strip() for segment in header.split(",")]
    if len(segments) < 2 or not segments[1]:
        raise ValueError("placard must contain a material segment")
    if not re.search(r"c\. \d{4}\b", text):
        raise ValueError("placard must contain a 'c. YYYY' approximate date")
    sentences = [s.strip() for s in re.findall(r"[^.!?]+[.!?]", text)]
    if not sentences:
        raise ValueError("placard must contain at least one full sentence")
    if not any(sentence.startswith("On loan from ") for sentence in sentences):
        raise ValueError("placard must contain a provenance segment "
                         "beginning with 'On loan from'")
    if not text.endswith("."):
        raise ValueError("placard must end with a period")


def main() -> None:
    validate(PLACARD)
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(PLACARD)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != PLACARD.encode("utf-8"):
        raise ValueError("written output does not match the validated placard")


if __name__ == "__main__":
    main()
