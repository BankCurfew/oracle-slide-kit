#!/usr/bin/env python3
"""T2248 · writer's recorded rulings (inventory R1-R4 + F7, highest R wins) as a parity map → rulings.json.
Keys are inventory checklist lines (matched by prefix, must be unique on their slide); values = the build text
(list = one line becomes several, None = ruled out)."""
import json, os, sys
INV = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/repos/github.com/BankCurfew/Writer-Oracle/output/t2248-inventory/T2248-T2-sales-technique-inventory.md')
body = open(INV, encoding='utf-8').read().split('## Parity checklist', 1)[1]
lines, cur = {}, None
for l in body.splitlines():
    if l.startswith('### S'): cur = l[4:7]; lines[cur] = []
    elif cur and l.startswith('- '): lines[cur].append(l[2:].strip())
R = {}
def rule(sl, start, new):
    m = [x for x in lines[sl] if x.startswith(start)]
    assert len(m) == 1, (sl, start, m)
    R.setdefault(sl, {})[m[0]] = new
rule('S01', 'กด →', 'แตะ · ปัด · หรือกด → เพื่อเริ่ม')  # F7 = T1 ruling
rule('S02', 'เคล็ด(ไม่ลับ)', 'เคล็ด(ไม่)ลับ ประกันชีวิต + ประกันสุขภาพ')  # R4 F9
rule('S04', 'ส่วนใหญ่ซื้อ', 'ลูกค้าซื้อเพราะ "เชื่อใจคน" ไม่ใช่แค่ตัวสินค้า')  # R4 F1
rule('S12', 'สงคราม,', ['กรมธรรม์ชีวิต: ไม่จ่ายถ้าฆ่าตัวตายภายใน 1 ปีนับจากวันเริ่มคุ้มครอง หรือถูกผู้รับประโยชน์ฆ่า',
                        'สัญญาเพิ่มเติม: สงคราม · กีฬาอันตราย (PA) · โรคที่เป็นมาก่อน (สุขภาพ) · ทำร้ายตัวเองทุกกรณี'])  # R2 #8
rule('S13', 'เจ็บป่วยทั่วไป', 'เจ็บป่วยทั่วไป (สัญญาสุขภาพ)')  # R2 #7
rule('S13', 'โรคเฉพาะ', ['โรคเฉพาะ (AIA Health Happy / AIA Health Saver): ไส้เลื่อน / ต้อเนื้อ-ต้อกระจก / ทอนซิล-อดีนอยด์ / เยื่อบุโพรงมดลูกเจริญผิดที่',
                         'สัญญา CI / Care for Cancer มีระยะรอคอยของแต่ละแบบ'])  # R1 + R2 #7 new line
rule('S17', '"ผมอาจไม่ได้', '"ผมอาจไม่ได้อยู่ดูแลคุณได้ตลอด แต่ผมวางระบบและทีมไว้ ให้คุณได้รับการดูแลต่อเนื่องครับ"')  # R4 F3
rule('S19', 'ได้เงินกลับ', ['ได้เงินกลับ', 'ใช้ได้กับแบบที่มีมูลค่าเวนคืน (ตลอดชีพ / สะสมทรัพย์ / บำนาญบางแบบ) · ไม่ใช้กับ Term และสัญญาเพิ่มเติม · Unit Linked ใช้ถอนหน่วยลงทุน / หยุดพักชำระเบี้ยแทน'])  # R2 #10
rule('S20', 'Reframe', 'Reframe: ประกันชีวิต = เพื่อนแท้ยามยาก คุ้มครองตั้งแต่วันที่กรมธรรม์มีผล ไม่ต้องรอสะสม')  # R3
rule('S21', 'ชีวิต 100,000', 'ชีวิต (สัญญา 10 ปีขึ้นไป) + สุขภาพ ≤25,000 รวมกันไม่เกิน 100,000 · บำนาญ ≤200,000 และไม่เกิน 15% ของเงินได้ (รวมกองทุนเกษียณอื่นไม่เกิน 500,000)')  # R2 #3
rule('S21', 'Preferred Rate', 'แบบ Prestige (ทุน ≥10 ล้าน): Preferred Rate (สุขภาพดีเบี้ยถูกกว่า) · สุขภาพต่ำกว่ามาตรฐานไม่เกินขั้น D ไม่เพิ่มเบี้ย · UL Prestige ลด COI 10-20% (Preferred 15-30% ตามแบบและทุน) · สิทธิ์ Prestige Club โดยไม่กำหนดเบี้ยขั้นต่ำ')  # R2 #4
rule('S21', 'IRR', 'IRR ต่างกันตามแบบ คำนวณจากตารางผลประโยชน์ของแบบนั้น')  # R2 #2
rule('S22', 'ซื้อวงเงินเพิ่ม', 'ซื้อวงเงินเพิ่ม = พิจารณาสุขภาพใหม่ + นับระยะรอคอยใหม่เฉพาะส่วนที่เพิ่ม')  # R2 #11
rule('S22', 'แต่ลดวงเงิน', 'แต่ลดวงเงิน ไม่ต้องพิจารณาใหม่ คุ้มครองต่อ (PPR ลดได้ทุกงวดเบี้ย · UDR มีผลรอบปีกรมธรรม์ถัดไป)')  # R2 #11
rule('S23', 'เบี้ยมั่นคง', 'เบี้ยปรับตามพอร์ต ไม่ใช่ตามเคลมของคนเดียว')  # R2 #5
rule('S23', '"ไม่เพิ่มเบี้ย', '"เบี้ยไม่ขึ้นเพราะเคลมของเราคนเดียว"')  # R2 #5
rule('S23', '= ไม่ลงโทษ', 'แต่: สัญญาสุขภาพมาตรฐานใหม่ (ออกตั้งแต่ 20 มี.ค. 68) อาจมี Copayment 30-50% ในปีถัดไป ถ้าเคลมนอนโรงพยาบาลด้วยโรคทั่วไป (ไม่รวมการผ่าตัดใหญ่และโรคร้ายแรง) ตั้งแต่ 3 ครั้ง และอัตราเคลมเกินเกณฑ์ ทบทวนใหม่ทุกปี')  # R3
rule('S24', 'ข้อยกเว้นทั่วไป', 'ระยะรอคอยของ AIA Health Happy')  # R2 #6
rule('S24', 'มีกี่ข้อ', 'นานแค่ไหน?')
rule('S24', 'คำตอบ:', 'คำตอบ: เจ็บป่วยทั่วไป 30 วัน · 120 วันเฉพาะ 4 กลุ่ม')
rule('S24', 'Waiting 120', None)
rule('S24', 'แบบเก่า', None)
rule('S24', 'รวมริดสีดวง', None)
rule('S25', 'ส่วนลดเบี้ย', 'Vitality Bonus = เงินคืน ไม่ใช่ส่วนลดเบี้ย')  # R2 #9
rule('S25', 'แบบใหม่', '(คู่มือสมาชิก ณ 25 ก.ย. 68)')
rule('S25', 'Vitality Bonus เงินคืน', 'จ่ายเป็นเงินคืนทุกปีตามสถานะ Vitality')
rule('S25', 'ค่ารักษา+', 'ค่ารักษา+ชดเชยรายวัน สูงสุด 15% (ปีที่ไม่เคลม IPD · ถ้าเคลม สูงสุด 5%)')
rule('S25', 'โรคร้าย', 'โรคร้าย (CI) กลุ่ม AIA CI Plus สูงสุด 20% (CI ProCare สูงสุด 9%)')
rule('S25', 'ได้ตั้งแต่ปีแรก', 'นับตั้งแต่ปีกรมธรรม์แรก จ่ายเมื่อพ้น 90 วันนับจากวันครบรอบปีกรมธรรม์')  # R3
rule('S25', 'Vitality อยู่ในไทย', 'AIA Vitality เปิดตัวในไทยปี 2559 (ครบ 10 ปี)')  # R2 #1
rule('S25', 'สมาชิก', None); rule('S25', 'ความดัน', None); rule('S25', 'น้ำตาล', None)
rule('S30', 'ลูกค้าไม่ถูกทิ้ง', 'ถ้าตัวแทนไม่อยู่ มีทีมดูแลลูกค้าต่อ')  # R4 F3
rule('S30', 'ลูกค้าได้บริการ', 'ตัวแทนทุกคนใช้มาตรฐานบริการเดียวกัน')  # R4 F3
rule('S31', 'ใช้ FA Tools', 'ใช้ iKnow ใน FA Tools ให้ลูกค้าเห็นตัวเลขจริง')  # R4 = bob F5
R['+S31'] = ['iKnow ปลดล็อกเมื่อเป็น FA ขึ้นไป · ตัวแทนใหม่เริ่มจาก uKnow']  # R4 tier line (last line)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rulings.json')
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n_out = sum(1 for k, v in R.items() if not k.startswith('+') for x in v.values() if x is None)
n_add = sum(len(v) - 1 for k, v in R.items() if not k.startswith('+') for x in v.values() if isinstance(x, list) for v in [x])
print('wrote', out, sum(len(v) for k, v in R.items() if not k.startswith('+')), 'ruled lines ·', n_out, 'out ·', n_add + len(R['+S31']), 'added')
