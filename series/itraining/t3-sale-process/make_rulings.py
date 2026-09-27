#!/usr/bin/env python3
"""T2249 · writer's recorded rulings (inventory R1-R3, highest R wins) + layout-only fixes (F9 ✦ / ⟨split⟩ markers)
as a parity map → rulings.json. Keys are inventory lines (matched by prefix, unique on their slide); values = build text."""
import json, os, re, sys
INV = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/repos/github.com/BankCurfew/Writer-Oracle/output/t2249-inventory/T2249-T3-sales-process-inventory.md')
body = open(INV, encoding='utf-8').read().split('## Parity baseline', 1)[1]
lines, cur = {}, None
for l in body.splitlines():
    m = re.match(r'^### S(\d+)', l)
    if m: cur = f'S{int(m.group(1)):02d}'; lines[cur] = []
    elif cur and l.startswith('- '): lines[cur].append(l[2:].strip())
R = {}
def rule(sl, start, new):
    m = [x for x in lines[sl] if x.startswith(start)]
    assert len(m) == 1, (sl, start, m)
    R.setdefault(sl, {})[m[0]] = new
# layout-only (F9): decorative ✦ dropped, extractor ⟨split⟩ markers are not text
rule('S01', 'กระบวนการขาย✦', 'กระบวนการขาย')
rule('S01', 'iTRAINING T.3/6', 'iTRAINING · T.3/6')  # series cover kicker format (SERIES-TEMPLATE §1)
for sl, ls in lines.items():
    for x in ls:
        if '⟨split⟩' in x: R.setdefault(sl, {})[x] = x.replace('⟨split⟩', '').strip()
# R1
rule('S03', '"MANHA ครบ', '"MANHA ครบ เท่ากับ พร้อมปิดการขาย"')
rule('S09', 'Found', 'Found (แต่สิ่งที่เราค้นพบคือ): "แต่พอเรามาลองกางตัวเลขเงินเฟ้อดู ถึงพบว่าถ้าเริ่มช้าไปแค่ 5 ปี ต้องเก็บเงินต่อเดือนมากกว่าที่คิดไว้เยอะเลยครับพี่..."')
# R2
rule('S14', '"เข้าใจเลยครับพี่ งั้น', '"เข้าใจเลยครับพี่ งั้นถ้าผมปรับแผนให้เบาลง โดยเลือกคุ้มครองเรื่องที่สำคัญที่สุดก่อน พี่ว่าพอไหวไหมครับ?"')
rule('S16', '(เพื่อชี้ให้เห็น', '(เพื่อชี้ให้เห็นว่าสวัสดิการส่วนใหญ่เน้นค่ารักษา ส่วนรายได้ที่หายไประหว่างพักรักษาอาจชดเชยได้ไม่ครบ)')
rule('S22', 'Professional Standard', 'จากการขาย สู่การวางแผนการเงิน')
# R3 (writer 3ca751f, Editor may reword 1:1)
rule('S01', '(คลาส 2', '(คลาส 2 ชั่วโมง · Interactive Session)')
rule('S09', 'อย่าเถียง', 'อย่าเถียงลูกค้า ให้คล้อยตามก่อนแล้วค่อยดึงกลับ (Feel · Felt · Found)')
rule('S03', 'รีบหยิบ', 'รีบหยิบแบบมาเสนอตั้งแต่ 5 นาทีแรก ยัดเยียดโดยที่ลูกค้ายังไม่เห็นปัญหา มักนำไปสู่ข้อโต้แย้ง')
rule('S04', '"ห้ามสลับ', '"ห้ามสลับและห้ามข้ามขั้นตอนเด็ดขาด"')
rule('S04', 'ถ้าเขาไม่ชอบ', 'ถ้าเขาไม่ชอบและไม่เชื่อใจเรา เขาก็ยากที่จะฟังขั้นตอนต่อไป')
rule('S05', 'ถ้าลูกค้าบอก', 'ถ้าลูกค้าบอก "ขอคิดดูก่อน" มักแปลว่าเรายังตกหล่นตัวอักษรใดตัวอักษรหนึ่งไป')
rule('S20', '(การถามแบบนี้', '(การถามแบบนี้ ช่วยให้ลูกค้าเล่าปัญหาที่แท้จริงออกมา เช่น "พอดีเงินช็อต" หรือ "ต้องถามแฟน")')
rule('S23', 'อย่าแบกปัญหา', 'อย่าแบกปัญหาไว้คนเดียว เพราะคนนอกมักมองเห็นจุดบอดได้ชัดเจนกว่า')
for n, w in [('1', 'Fact'), ('2', 'Dialogue'), ('3', 'MANHA'), ('4', 'Action')]:
    rule('S25', f'{n}. {w}', w)
rule('S02', 'และ สังเกต', 'และสังเกตภาษากาย')
rule('S26', 'กติกา:', 'กติกา: จับคู่สลับกันเป็นตัวแทนและลูกค้า')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rulings.json')
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', out, sum(len(v) for v in R.values()), 'ruled lines (all 1:1)')
