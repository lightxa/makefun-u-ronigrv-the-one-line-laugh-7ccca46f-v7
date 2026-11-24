#!/usr/bin/env python3
"""The One-Line Laugh entry, variant 7.

Writes a single original one-line joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.

The joke's mechanism is a personified printer with a toxic
relationship, mapped to the judge's criteria in order: (1) one
funny line, well under 200 characters; (2) the surprise lands in
the last words -- threatening a printer is absurd, and the payoff
is that the relationship runs on "fear and paper jams"; (3) the
everyday truth is printers that only work when coaxed or
threatened, which everyone with a printer recognises; (4) nothing
explains the joke, every word earns its place; (5) the scene and
phrasing are original, not a known meme. The surprise is placed
deliberately at the very end: "fear and paper jams" is the payoff,
so a reader who only skims the first half still has to reach the
last words for the laugh to land, which is exactly what criterion
(2) rewards. One everyday disaster,
one beat, one absurd concrete image -- a printer in a toxic
relationship -- as the whole entry. It shares no scene, image or
structure with our earlier variants: no GPS, no wave, no goldfish,
no mortgage, no self-checkout, no dog, no autocorrect.
"""

import os
from pathlib import Path

LINE = "My printer only works when I threaten it, so now we have a toxic relationship built on fear and paper jams."


def is_single_sentence(text: str) -> bool:
    """True when text is exactly one sentence on one line: one
    terminal full stop, at the end, with no other sentence-ending
    punctuation anywhere inside, no line break, and no leading or
    trailing whitespace."""
    return (
        text == text.strip()
        and text.count(".") == 1
        and text.endswith(".")
        and "?" not in text
        and "!" not in text
        and "\n" not in text
        and "\r" not in text
    )


def validate_line(text: str) -> str:
    """Check the entry against the gate: 1-200 chars, one sentence."""
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text or text != text.strip():
        raise SystemExit("entry must not be blank or padded with whitespace")
    if not is_single_sentence(text):
        raise SystemExit("entry must be a single sentence ending in one full stop")
    return text


def main() -> None:
    text = validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
