#!/usr/bin/env python3
"""Every figure in the deck, drawn from real structures and published numbers.

`python figures.py` makes them all and `python figures.py cover hook` makes some. The figures live in one module
per part of the talk, in slide order (fig_opening.py to fig_close.py), and share the canvas, marks and scenes in
draw.py and the atoms in structures.py. Each figure is laid out in slide pixels at the size of the box it fills, so
its text matches the slide text. Molecules on surfaces are illustrative arrangements, not simulation snapshots.
"""
import sys

import fig_close
import fig_examples
import fig_opening
import fig_pairs
import fig_terms

PARTS = (fig_opening, fig_terms, fig_pairs, fig_examples, fig_close)
FIGURES = {make.__name__: make for part in PARTS for make in part.FIGURES}

if __name__ == '__main__':
    for name in sys.argv[1:] or list(FIGURES):
        print(FIGURES[name]())
