#!/usr/bin/env python3
"""Content parity: every line of the writer's inventory is on its slide, in order, in the built deck.
Usage: parity.py <inventory.md> <deck.html>   (T2194; inventory format: '### Sxx' headers + '- line' items,
struck ~~lines~~ are ruled out, '**RULED (...): new text**' replaces the line)."""
import html, re, sys
from html.parser import HTMLParser

inv, deck = sys.argv[1], sys.argv[2]
def norm(s):
    # compare the words the trainee reads: blanks `____` are drawn as writing lines in the deck,
    # and "1." numbering is a badge or an <ol> counter, so both sides drop underscores and the dot after a number
    s = html.unescape(s).replace('_', ' ')
    s = re.sub(r'(?<![\d.])(\d+)\.(?=\s|$)', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()

want, cur = {}, None
body = open(inv, encoding='utf-8').read().split('## Parity checklist', 1)[1]
for line in body.splitlines():
    m = re.match(r'^### S(\d+)', line)
    if m: cur = int(m.group(1)); want[cur] = []; continue
    if cur is None or not line.startswith('- '): continue
    item = line[2:].strip()
    if item.startswith('~~'):
        r = re.search(r'\*\*RULED \([^)]*\): (.+?)\*\*', item)
        if r: want[cur].append(norm(r.group(1)))
        continue
    item = item.strip('`')
    # exercise rows written two per line ("1. ___ · 2. ___") are one row each in the deck
    parts = item.split(' · ') if '_' in item else [item]
    want[cur].extend(norm(x) for x in parts)

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
