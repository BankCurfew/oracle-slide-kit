#!/usr/bin/env python3
"""Inline timeline-slide.css/.js into the demo -> output/timeline-demo.html (one file, opens as a chip)."""
import pathlib
here = pathlib.Path(__file__).parent
h = (here / 'timeline-demo.html').read_text()
h = h.replace('<link rel="stylesheet" href="timeline-slide.css">', '<style>\n' + (here / 'timeline-slide.css').read_text() + '</style>')
h = h.replace('<script src="timeline-slide.js"></script>', '<script>\n' + (here / 'timeline-slide.js').read_text() + '</script>')
out = here.parent.parent / 'output' / 'timeline-demo.html'
out.parent.mkdir(exist_ok=True)
out.write_text(h)
print(out)
