#!/usr/bin/env python3
"""T2229 · writer's recorded rulings (inventory R1-R7 + F5) as a parity map → rulings.json.
Keys are inventory checklist lines (matched by prefix, must be unique on their slide); values = the build text."""
import json, os, sys
INV = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/repos/github.com/BankCurfew/Writer-Oracle/output/t2229-inventory/T2229-T4-product-approach-inventory.md')
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
rule('S01', 'กด →', 'แตะ · ปัด · หรือกด → เพื่อเริ่ม')  # F5 = T1 ruling
R['S05'] = {'Promo': 'Promotion'}  # R2, both occurrences
rule('S09', 'บทเปิด', 'บทเปิด: "ตอนนี้มีแคมเปญตรวจสุขภาพการเงินฟรีด้วย uKnow ใช้เวลาไม่กี่นาที ได้เห็นภาพความคุ้มครองของตัวเอง สนใจลองไหมครับ"')  # R6
rule('S10', 'สถิติ', 'มักต้องเจอคำปฏิเสธหลายครั้ง กว่าจะได้นัด 1 ครั้ง')  # R1
rule('S10', 'ทัศนคติ', 'ทัศนคติ: ทุก no คือทางผ่าน ทุก no ทำให้เข้าใกล้ yes ขึ้น')  # R1
rule('S14', 'ชวนทำ iCheck', 'ชวนทำ uKnow (เดิมชื่อ iCheck) ก่อนนัด')  # R6
rule('S14', '"ก่อนเจอกัน', '"ก่อนเจอกัน ลองทำ uKnow ดูไหมคะ ใช้เวลาไม่กี่นาที จะได้เห็นภาพความคุ้มครองของตัวเองก่อน แล้วเราค่อยคุยจากผลจริงค่ะ"')
rule('S15', 'ดีเลยครับ', 'ดีเลยครับ ผมช่วยดูให้ว่าที่มีครอบคลุมพอไหม ใช้ uKnow เช็คสั้นๆ ได้')
rule('S17', 'iCheck ตอน 1', 'uKnow ตอน 1'); rule('S17', 'iCheck คืออะไร', 'uKnow คืออะไร')
rule('S17', '[รอยืนยัน', ['uKnow · รู้จักความคุ้มครอง', 'เข้า iKYS → uKnow',
     'เบื้องหลังคะแนน (เต็ม 100): ความคุ้มครอง 40 · ภาษี 20 · สำรอง (หนี้และการออม) 15 · เกษียณ 15 · CRP (ประสบการณ์และความสนใจการลงทุน) 10'])  # R6 ①②③
rule('S18', 'iCheck ตอน 2', 'uKnow ตอน 2')
rule('S18', 'Score รวม', 'คะแนนรวม → ค่ารักษาจริง → ช่องว่างความคุ้มครอง → แผนเติมเต็ม')  # R7
rule('S18', 'จุดที่ลูกค้าอึ้ง', 'จุดที่ลูกค้าอึ้ง: เห็นว่าความคุ้มครองที่มีอยู่ยังไม่พอ')  # R7
rule('S18', 'แค่ 1-17%', 'ขาดอีก 96% ของที่ควรมี (ตัวอย่าง: ชาย 30 ปี รายได้ 96,700 บาท/เดือน) = เห็นช่องว่างชัดด้วยตัวเลข')  # R7
rule('S19', 'iCheck ตอน 3', 'uKnow ตอน 3')
rule('S19', 'ตัวอย่าง:', 'ตัวอย่างเดียวกัน: มีอยู่ 1.0M ต้องการ 25.3M ต้องเพิ่มอีก 24.3M')  # R7
rule('S19', 'iCheck เปลี่ยน', 'uKnow เปลี่ยน "ช่องว่าง" ให้เป็น "สิ่งที่ต้องเติม" ด้วยตัวเลข = สร้างปัญหาให้ลูกค้าเห็นเอง ไม่ต้องขู่')
rule('S19', 'ทำไมลูกค้าเชื่อ', 'ทำไมลูกค้าเชื่อตัวเลขจาก uKnow มากกว่าคำพูดของตัวแทน?')
rule('S20', 'ใช้ iCheck', 'ใช้ uKnow')
rule('S21', 'เสนอสินค้าที่ตอบ', 'เสนอสินค้าที่ตอบช่องว่างจาก uKnow เลือก 1-2 แบบที่ใช่')
rule('S21', 'เช่น เปิดด้วยสุขภาพ', 'เช่น เปิดด้วยสุขภาพ แต่ uKnow ชี้ว่าช่องว่างใหญ่สุดคือคุ้มครองชีวิต')
rule('S23', 'Need คุ้มครอง/ออม', 'Need คุ้มครอง/ออม: สุขภาพ, ชีวิต, สะสมทรัพย์, บำนาญ')  # R4 categories, bracket removed
rule('S23', 'Need ลงทุน/เกษียณ', ['Need ลงทุน/เกษียณ: เข้าผ่านมุมการเงินก่อน ต่อยอดสู่คุ้มครอง',
     'การแนะนำและขาย Unit Linked ต้องมี ใบอนุญาตตัวแทนประกันชีวิต และ ใบอนุญาตผู้แนะนำการลงทุน (IC License) จาก ก.ล.ต. และขึ้นทะเบียนเป็นตัวแทนขาย Unit Linked กับ คปภ.'])  # R4 aia/fasai
rule('S24', 'เปิดใจ+iCheck', 'เปิดใจ+uKnow→')
rule('S26', 'เปิดใจ + ทำ iCheck', 'เปิดใจ + ทำ uKnow ให้ลูกค้าเห็นช่องว่าง')
R['+S02'] = ['T.5 Need Approach', 'เริ่มจากความต้องการลูกค้า', 'T.6 Workshop ปิดการขาย', 'ฝึกปิดการขายแบบลงมือทำ']  # F4 + R6
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rulings.json')
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', out, sum(len(v) for k, v in R.items() if not k.startswith('+')), 'ruled lines +', len(R['+S02']), 'added')
