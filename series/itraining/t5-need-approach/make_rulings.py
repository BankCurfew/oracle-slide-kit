#!/usr/bin/env python3
"""T2250 · writer's recorded rulings (inventory R1 bob+fasai, R2 writer 0b09530/689239f; highest R wins) as a parity map →
rulings.json. Keys are inventory lines (matched by prefix, unique on their slide); values = build text (list = 1 → n, None = out).
Parity runs --order (the 10 question splits renumber the slides)."""
import json, os, re, sys
INV = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/repos/github.com/BankCurfew/Writer-Oracle/output/t2250-inventory/T2250-T5-need-approach-inventory.md')
body = re.split(r'^## Parity checklist', open(INV, encoding='utf-8').read(), maxsplit=1, flags=re.M)[1]
lines, cur = {}, None
for l in body.splitlines():
    m = re.match(r'^### S(\d+)', l)
    if m: cur = f'S{int(m.group(1)):02d}'; lines[cur] = []
    elif cur and l.startswith('- '): lines[cur].append(l[2:].strip())
R = {}
def rule(sl, start, new, exact=False):
    m = [x for x in lines[sl] if (x == start if exact else x.startswith(start))]
    assert len(m) == 1, (sl, start, m)
    R.setdefault(sl, {})[m[0]] = new
# layout-only / series
rule('S01', 'Need Approach (', 'Need Approach')                       # ✦ decorative note, not text
rule('S01', 'กด →', 'แตะ · ปัด · หรือกด → เพื่อเริ่ม')                # F7 = T1/T4 ruling
# R2 S2 (689239f): T.1-T.4 subtitles = T4 shipped map; T.6 card added after T.5
rule('S02', 'ขายเพราะเชื่อ', 'ขายเพราะเชื่อในคุณค่าการวางแผน')
rule('S02', 'จุดขาย AIA', 'คำมั่นสัญญา จุดขาย AIA รับมือความเสี่ยง')
rule('S02', 'อ่านคน', 'อ่านคน เปิดใจ สร้างปัญหา นำเสนอ ปิด')
rule('S02', 'เข้าเร็ว', 'ทางเข้าที่เร็วขึ้น ใช้สินค้าเป็น "ประตู" ทำนัด')
rule('S02', 'แผนครอบคลุม', ['แผนครอบคลุมทั้งชีวิต', 'T.6', 'Workshop ปิดการขาย', 'ฝึกปิดการขายแบบลงมือทำ'])
# R2 S3 (F6)
rule('S03', 'ใช้เวลา 2-3', 'ใช้เวลา 2-3 นัดหมาย: นัดแรกเก็บข้อมูล → นัดสองวิเคราะห์+เสนอแผน (ปิดได้ถ้าลูกค้าพร้อม) → นัดสามปิด (ถ้าจำเป็น)')
rule('S04', 'iCheck', 'iKnow + สินค้าเปิด')                               # R2 F4
rule('S05', '"ค่าเรียน', '"ค่าเรียนมหาวิทยาลัยใช้เงินไม่น้อย ถ้าเตรียมตั้งแต่วันนี้จะสบายกว่ามาก ขอนัดคุยสั้นๆ ครับ"')  # R2 F2
# R1 videos
rule('S07', 'คน 4 ชนชั้น', 'ฐานะ 4 ระดับ', exact=True)
rule('S07', 'Story 1: คน', 'Story 1: ฐานะ 4 ระดับ')
rule('S07', 'แผนคุ้มครองรายได้', ['แผนคุ้มครองรายได้ ดูคลิปด้วยกัน (ภาษาอังกฤษ ประมาณ 8 นาที)',
      'Dr Sanjay Tolani แบ่งคนเป็น 4 ระดับ แล้วชี้ว่าถ้าคนหารายได้หยุดทำงาน ครอบครัวอาจตกไปถึงระดับที่ต้องพึ่งญาติ เล่าด้วยแนวคิดแทนการเริ่มจากตัวแบบประกัน',
      '1 ร่ำรวย · 2 สบาย · 3 ชักหน้าไม่ถึงหลัง · 4 ต้องพึ่งญาติ'])
rule('S07', '💬 พอดูจบ', '💬 พอดูจบ คุณคิดว่าลูกค้าส่วนใหญ่ของคุณอยู่ระดับไหน?')
rule('S07', '💬 ยกมือ', '💬 ยกมือ 1-4 แล้วอภิปราย "เป้าหมายคือไม่ให้ครอบครัวของลูกค้าตกไปถึงระดับที่ 4"')
rule('S08', '2,156,000', '2,157,000'); rule('S08', '9,434,000', '9,399,000')      # R1 Editor + fasai
rule('S09', 'Circle of Life', '28,000 วัน', exact=True)
rule('S09', 'ดูคลิป', ['ดูคลิปด้วยกัน (ภาษาอังกฤษ ประมาณ 12 นาที)',
      'Dr Sanjay Tolani เล่าแนวคิด "28,000 วัน" มองการวางแผนการเงินตลอดทั้งชีวิต แล้วต่อด้วยเรื่องคุ้มครองรายได้'])
rule('S09', '💬 พอดูจบ', '💬 พอดูจบ ลูกค้าของคุณอยู่ช่วงไหนของชีวิต?')
# R2 S10/S11 (F2/F3)
rule('S10', 'เกณฑ์ที่ดี', 'หลักคิดทั่วไป', exact=True)
rule('S10', '💬 คำนวณ', '💬 คำนวณแบบเผื่อไว้ (ใช้รายได้แทนรายจ่าย): 50,000 x 6 = 300,000 บาท (มีกี่คนที่มีครบ?)')
rule('S11', '50,000 (1', '50,000 (1 เท่าของเงินเดือน)')
rule('S11', '300,000 (6', '300,000 (6 เท่าของเงินเดือน)')
rule('S11', '⚠️ ต่ำ', '⚠️ ถึงขั้นต่ำ ยังไม่ถึงเป้า 20%', exact=True)
rule('S11', 'สวัสดิการบริษัท 100,000', None, exact=True)                       # R1: stray duplicate, dropped
# R1 S12 (fasai; life row superseded by the 14:07 figures)
rule('S12', 'ประกันชีวิต (Term', 'ประกันชีวิต AIA Life Protector V70 (ตัวอย่าง)')
rule('S12', '~8,000-15,000', '~31,350-68,970/ปี (ตัวอย่าง: ชาย 35 ปี ทุน 2.5-5.5 ล้าน)')
rule('S12', 'Health Happy', 'AIA Health Happy หรือ สุขภาพเดี่ยว')
rule('S12', 'งบรวมที่แนะนำ', ['งบเบี้ยประกันรวม: ~51,350-108,970/ปี (ประมาณ 4,300-9,100/เดือน)', 'เงินออมฉุกเฉิน: 5,000/เดือน แยกจากเบี้ยประกัน'])
rule('S12', '[รอยืนยัน', None)
# R2 S13/S15/S16/S17/S20
rule('S13', '⛵ใบเรือ', '⛵ใบเรือ = การลงทุนขับเคลื่อนให้ไปข้างหน้า (หุ้น กองทุน ประกันชีวิตควบการลงทุน Unit Linked)')
rule('S15', 'แสดงใบอนุญาต', 'แสดงใบอนุญาตตัวแทน (และ IC ถ้ามี) สร้างความมั่นใจ')   # R1 fasai
rule('S16', '6 ขั้นตอนมาตรฐาน', '6 ขั้นตอนการวางแผน')
rule('S16', 'จัดพอร์ตตอบทุก', 'จัดพอร์ตให้ตอบเป้าหมายที่ตั้งไว้')
rule('S17', 'กองทุน / Unit', 'กองทุน / ประกันชีวิตควบการลงทุน (Unit Linked) / หุ้น')
rule('S17', 'ฐาน: เงิน', 'ฐาน (ชั้น 1): เงินสำรองฉุกเฉิน')
rule('S17', '[รอยืนยัน', None)
rule('S20', 'เปิดใจด้วย Story', 'เปิดใจด้วย Story 1 เรื่อง (ฐานะ 4 ระดับ / กฎ 72 / 28,000 วัน / เรือใบ)')   # R1
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rulings.json')
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n_out = sum(1 for v in R.values() for x in v.values() if x is None)
n_add = sum(len(x) - 1 for v in R.values() for x in v.values() if isinstance(x, list))
print('wrote', out, sum(len(v) for v in R.values()), 'ruled lines ·', n_out, 'out ·', n_add, 'added')
