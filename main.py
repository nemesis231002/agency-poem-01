# Agency poem entry for make.fun's agency-poem-01.
# Writes one fixed poem about agency to /output/entry.txt.
# The poem is about the agency that passes between a person and an
# agent: delegation that lets an unbearable task proceed, and the
# speaker's power to take it back with a single word, "Wait".
# Deterministic: no network, no randomness, no time or environment input.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Cancel my mother's phone, I type.
The pear beside my laptop has gone soft
where my thumb keeps finding it.
The agent takes the number,
finds the form I closed three times,
fills the little boxes.
A blue dot moves along the screen.
For once, something happens
without my having to keep wanting it.
Then: Save voicemail before closing?
Wait, I type, and the blue dot stops.
I wash the pear juice from my hands
before I press her voice."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
