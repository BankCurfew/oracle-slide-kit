#!/usr/bin/env python3
"""Content parity: every line of the writer's inventory is on its slide, in order, in the built deck.
Usage: parity.py <inventory.md> <deck.html> [--rulings rulings.json] [--order]   (T2194;
--rulings (T2229): {"S17": {"<inventory line>": "<new line>" | ["<new>", ...] | null}} applies the writer's recorded rulings
(null = ruled out); "+S02": ["<added line>", ...] appends lines to a slide. --order: deck slides were split/renumbered, so every
line is checked in order across the whole deck instead of on its own slide number. inventory format: '### Sxx' headers + '- line' items,
struck ~~lines~~ are ruled out, '**RULED (...): new text**' replaces the line)."""
import html, re, sys
from html.parser import HTMLParser

import json
args = sys.argv[1:]
order = '--order' in args
rul = json.load(open(args[args.index('--rulings') + 1], encoding='utf-8')) if '--rulings' in args else {}
inv, deck = args[0], args[1]
def norm(s):
    # compare the words the trainee reads: blanks `____` are drawn as writing lines in the deck,
    # and "1." numbering is a badge or an <ol> counter, so both sides drop underscores and the dot after a number
    s = html.unescape(s).replace('_', ' ')
    s = re.sub(r'(?<![\d.])(\d+)\.(?=\s|$)', r'\1', s)
    s = re.sub(r'\s*→\s*', '→', s)  # flow chevrons are their own element in the deck
    return re.sub(r'\s+', ' ', s).strip()

want, cur = {}, None
body = open(inv, encoding='utf-8').read().split('## Parity checklist', 1)[1]
for line in body.splitlines():
    if line.startswith('## '): cur = None; continue  # a later '## R..' section is notes, not slide lines (T2229)
    m = re.match(r'^### S(\d+)', line)
    if m: cur = int(m.group(1)); want[cur] = []; continue
    if cur is None or not line.startswith('- '): continue
    item = line[2:].strip()
    if item.startswith('~~'):
        r = re.search(r'\*\*RULED \([^)]*\): (.+?)\*\*', item)
        if r: want[cur].append(norm(r.group(1)))
        continue
    item = item.strip('`')
    item = re.sub(r'\s*\[รอยืนยัน[^\]]*\]\s*⚠️ PLACEHOLDER$', '', item).strip() if f'S{cur:02d}' not in rul or item not in rul[f'S{cur:02d}'] else item
    r = rul.get(f'S{cur:02d}', {})
    if item in r:
        new = r[item]
        want[cur].extend(norm(x) for x in ([] if new is None else [new] if isinstance(new, str) else new))
        continue
    # exercise rows written two per line ("1. ___ · 2. ___") are one row each in the deck
    parts = item.split(' · ') if '_' in item else [item]
    want[cur].extend(norm(x) for x in parts)

for k, v in rul.items():
    if k.startswith('+S'): want.setdefault(int(k[2:]), []).extend(norm(x) for x in v)

class P(HTMLParser):
    def __init__(s): super().__init__(); s.slides = []; s.depth = 0; s.skip = 0
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == 'section' and 'slide' in (a.get('class') or ''): s.slides.append(''); s.depth = 1; return
        if s.depth: s.depth += 1
        if t in ('script', 'style'): s.skip += 1
        if t == 'br' and s.depth: s.slides[-1] += ' '
        if t == 'ol' and s.depth: s.ol = 0
        if t == 'li' and s.depth and hasattr(s, 'ol'): s.ol += 1; s.slides[-1] += f' {s.ol} '
    def handle_endtag(s, t):
        if t in ('script', 'style'): s.skip -= 1
        if s.depth: s.depth -= 1
    def handle_data(s, d):
        if s.depth and not s.skip: s.slides[-1] += d + ' '
p = P(); p.feed(open(deck, encoding='utf-8').read())
got = [norm(x) for x in p.slides]

total = ok = 0; miss = []
if order:  # the whole deck is one text; lines must appear in inventory order
    want = {0: [l for n, ls in sorted(want.items()) for l in ls]}; got = [' '.join(got)]
for n, lines in sorted(want.items()):
    text = got[n - 1] if n - 1 < len(got) else ''
    pos = 0
    for l in lines:
        total += 1
        k = text.find(l, pos)
        if k < 0:
            k2 = text.find(l)
            miss.append(f'S{n:02d} {"OUT OF ORDER" if k2 >= 0 else "MISSING"}: {l}')
            continue
        ok += 1; pos = k + len(l)
print(f'parity {ok}/{total} lines [inventory {inv.split("/")[-1]} vs {deck.split("/")[-1]}, {len(got)} slides]')
for m in miss: print('  ' + m)
sys.exit(0 if ok == total else 1)
