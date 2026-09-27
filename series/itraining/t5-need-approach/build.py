#!/usr/bin/env python3
"""T2250 · iTraining T5/6 Need Approach builder (fe, on the T2194/T2229 series template).
Text source = Writer-Oracle output/t2250-inventory/T2250-T5-need-approach-inventory.md (22 source slides / 317 lines after R2),
verbatim, with the recorded rulings applied (highest R wins). rulings.json = make_rulings.py; parity runs --order because
the 10 question splits renumber the slides.
Layout = Designer-Oracle output/t2250-t5-need-approach/ART-DIRECTION.md (1d71519 + 0141fa6): 32 slides = 22 + 10 split
question slides (Q3 Q5 Q7 Q8 Q9 Q10 Q12 Q13 Q14 Q17), Q10's answer on the next tap, the two videos as tap-to-play facades
(no iframe until ▶), S8 bars, S13 inline-SVG sailboat lit part by part, S17 pyramid built base-first.
Rulings: R1 (bob + fasai) + R2 (writer 0b09530/689239f), highest R wins; parity 317.
"""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.join(HERE, '..')
BG_DIR = os.path.join(SERIES, 't1-mindset', 'img')  # series backgrounds, shared with T1-T4
OUT = os.path.join(HERE, '..', '..', '..', 'output', 'itraining-t5-need-approach.html')

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def bg(name):
    return "url('data:image/webp;base64," + b64(os.path.join(BG_DIR, f'bg-{name}.webp')) + "')"

def poster(name):
    return 'data:image/webp;base64,' + b64(os.path.join(HERE, 'img', f'poster-{name}.webp'))

def pending(flag):
    return f'<div class="pend" data-pending="{flag}" hidden></div>'

# ---------- writer R2 (0b09530 + 689239f): F4 iKnow; F5 S17 placeholder removed ----------
S4_TOOL = 'iKnow + สินค้าเปิด'

# ---------- builders ----------
def qs(question, prompt, answer=None, bg_name=None):
    """split question slide (R1 hero): 💬 question = hero, 💬 instruction under it; answer (Q10) reveals on tap"""
    cls = f'slide img q" data-bg="{bg_name}' if bg_name else 'slide dots q'
    ans = f'\n  <div class="card qa stp"><div class="cd">{answer}</div></div>' if answer else ''
    pr = f'\n  <div class="prompt rv">{prompt}</div>' if prompt else ''
    return f'''<section class="{cls} qsplit">
  <div class="kick rv">คำถามฝึกคิด</div>
  <h2 class="qtext rv"><span class="qe">💬</span> {question}</h2>{pr}{ans}
</section>'''

def table(head, rows, cls=''):
    th = ''.join(f'<th scope="col">{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="tb {cls} rv"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def rowcards(head, rows, cls=''):
    """390 form of a table: one card per row, first cell as the tag (screen only; the table carries the text for parity)"""
    out = []
    for r in rows:
        rest = ''.join(f'<div class="rc-v"><span class="rc-k">{h}</span>{c}</div>' for h, c in zip(head[1:], r[1:]))
        out.append(f'<div class="rc"><div class="rc-t">{r[0]}</div>{rest}</div>')
    return f'<div class="rcards {cls}" aria-hidden="true">' + ''.join(out) + '</div>'

def video(n, title, vid, length_line, summary, extra=''):
    return f'''<div class="vwrap rv"><div class="vid">
    <button class="vfacade" type="button" data-vid="{vid}" aria-label="เล่นวิดีโอ {title}">
      <img src="{poster(n)}" alt="{title}" width="480" height="270"><span class="play" aria-hidden="true">▶</span>
    </button>
    <div class="vcap">{title}</div>
  </div><div class="vtxt">
  <div class="cd">{length_line}</div>
  <div class="cd dim">{summary}</div>{extra}
  <a class="ytlink" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">▶ เปิดใน YouTube</a></div></div>'''

SLIDES = []
S = SLIDES.append

# S1 · cover
S('''<section class="slide img cover" data-bg="cover">
  <div class="tag0 rv">NEED DISCOVERY</div>
  <div class="kick rv">iTRAINING · T.5/6</div>
  <h1 class="rv"><span class="aurora">Need Approach</span></h1>
  <div class="bar rv"></div>
  <div class="lead rv">ระบุความต้องการ เสนอเมื่อมั่นใจ</div>
  <div class="hint rv">แตะ · ปัด · หรือกด → เพื่อเริ่ม</div>
</section>''')

# S2 · series map, T.5 lit, T.6 added (F6 / bob T4 F4)
smap = [('T.1', 'Mindset', ['ขายเพราะเชื่อในคุณค่าการวางแผน'], ''), ('T.2', 'เทคนิคการขาย', ['คำมั่นสัญญา จุดขาย AIA รับมือความเสี่ยง'], ''),
        ('T.3', 'กระบวนการขาย', ['อ่านคน เปิดใจ สร้างปัญหา นำเสนอ ปิด'], ''), ('T.4', 'Product Approach', ['ทางเข้าที่เร็วขึ้น ใช้สินค้าเป็น "ประตู" ทำนัด'], ''),
        ('T.5', 'Need Approach', ['เข้าลึก 2-3 นัด', 'แผนครอบคลุมทั้งชีวิต'], 'now'), ('T.6', 'Workshop ปิดการขาย', ['ฝึกปิดการขายแบบลงมือทำ'], '')]
li = ''.join(f'<li class="{c}"><b>{n}</b><b>{t}</b>' + ''.join(f'<span>{d}</span>' for d in ds) + '</li>' for n, t, ds, c in smap)
S(f'''<section class="slide dots">
  <div class="kick rv">เชื่อม T.1-4 สู่ความลึกใหม่</div>
  <h2 class="rv">T.5 อยู่ตรงไหน</h2>
  <ol class="smap rv">{li}</ol>
</section>''')

# S3 · concept + the 2-3 appointment flow (R2 F6: matches S18, pill 3 dashed)
S('''<section class="slide dots ans">
  <div class="kick rv">Need Approach</div>
  <h2 class="rv">Need Approach คืออะไร</h2>
  <div class="intro rv">เริ่มจากการค้นหาความต้องการที่แท้จริงก่อน</div>
  <div class="foot rv">ระบุความต้องการก่อน เสนอเมื่อมั่นใจเท่านั้น</div>
  <div class="apf rv"><span class="apl">ใช้เวลา 2-3 นัดหมาย:</span><ul class="flow"><li style="--k:0"><span>นัดแรกเก็บข้อมูล</span><i>→</i></li><li style="--k:1"><span>นัดสองวิเคราะห์+เสนอแผน (ปิดได้ถ้าลูกค้าพร้อม)</span><i>→</i></li><li style="--k:2" class="opt"><span>นัดสามปิด (ถ้าจำเป็น)</span></li></ul></div>
  <div class="sub rv">ต่างจาก Product Approach (T.4) ที่ปิดภายใน 1-2 นัด</div>
</section>''')
S(qs('ถ้าลูกค้ายังไม่รู้ตัวว่าต้องการอะไร คุณจะเริ่มยังไง?', None))

# S4 · compare table (neither side recommended); R2 F4 tool = iKnow
t4 = [('เริ่มจาก', 'สินค้าที่ตรงกับข้อมูลที่มี', 'ความต้องการที่ยังไม่รู้ตัว'), ('จำนวนนัด', '1-2 นัด', '2-3 นัด'),
      ('ความลึก', 'ตอบ Need เฉพาะจุด', 'ครอบคลุมทั้งชีวิต'), ('เหมาะกับ', 'ลูกค้าที่ Need ชัดแล้ว', 'ลูกค้าที่ยังไม่เคยวางแผน')]
tool = S4_TOOL
t4b = t4 + [('เครื่องมือ', tool, 'Story + Financial Planning + อัตราส่วนการเงิน')]
S(f'''<section class="slide dots cmp4 scroll">
  <div class="kick rv">💬 ยกมือ เปรียบเทียบ Product vs Need Approach</div>
  <h2 class="rv">Product vs Need Approach</h2>
  {table(['', 'Product Approach (T.4)', 'Need Approach (T.5)'], t4b, 'cmp')}
  {rowcards(['', 'Product Approach (T.4)', 'Need Approach (T.5)'], t4b, 'cmp')}
  <div class="foot rv center">ไม่มีอันไหนดีกว่า<br>เลือกใช้ตามลูกค้าที่อยู่ตรงหน้า</div>
</section>''')

# S5 · 4 life topics + scripts (listen bg)
tp = [('🎯', 'วางแผนเกษียณ', '"ผมช่วยลูกค้าหลายท่านวางแผนให้เกษียณแล้วไม่ต้องเป็นภาระลูก ขอเวลา 30 นาทีเล่าให้ฟังครับ"'),
      ('🎓', 'วางแผนการศึกษาบุตร', '"ค่าเรียนมหาวิทยาลัยใช้เงินไม่น้อย ถ้าเตรียมตั้งแต่วันนี้จะสบายกว่ามาก ขอนัดคุยสั้นๆ ครับ"'),
      ('💰', 'วางแผนการเงินแบบองค์รวม', '"ผมเป็นที่ปรึกษาด้านการเงิน ช่วยดูภาพรวมให้ทั้งออม ลงทุน คุ้มครอง ภาษี ขอ 30 นาทีครับ"'),
      ('🛡️', 'คุ้มครองรายได้', '"ถ้าวันหนึ่งต้องหยุดทำงาน ครอบครัวจะเป็นยังไง ผมช่วยวางแผนตรงนี้ได้ครับ"')]
cs = ''.join(f'<div class="card spot" style="--ci:{k}"><div class="em">{e}</div><div class="ct">{t}</div><div class="bub me">{s}</div></div>' for k, (e, t, s) in enumerate(tp))
S(f'''<section class="slide img ans" data-bg="listen">
  <div class="kick rv">การนัดหมาย · Need Approach</div>
  <h2 class="rv">ใช้ "หัวข้อชีวิต" นำ ไม่ใช่สินค้านำ</h2>
  <div class="grid c2 topics rv">{cs}</div>
</section>''')
S(qs('Topic ไหนเหมาะกับลูกค้าวัย 30 ที่เพิ่งมีลูก?', '💬 เลือก 1 Topic บอกเหตุผล'))

# S6 · STORYTELLING opener (white)
S('''<section class="slide part ed">
  <div class="bigS rv">S</div>
  <div class="kick rv">STORYTELLING</div>
  <div class="skew rv"></div>
  <div class="intro rv">เปิดใจด้วย Story · เครื่องมือทรงพลัง ให้ลูกค้าเห็นภาพชีวิตตัวเองก่อนพูดเรื่องเงิน</div>
</section>''')

# S7 · Story 1 video (R1)
S(f'''<section class="slide dots vs-s">
  <div class="kick rv">Story 1</div>
  <h2 class="rv">Story 1: ฐานะ 4 ระดับ</h2>
  {video('s7', 'Story 1: ฐานะ 4 ระดับ', 'N_w9WRKTzzM', 'แผนคุ้มครองรายได้ ดูคลิปด้วยกัน (ภาษาอังกฤษ ประมาณ 8 นาที)',
         'Dr Sanjay Tolani แบ่งคนเป็น 4 ระดับ แล้วชี้ว่าถ้าคนหารายได้หยุดทำงาน ครอบครัวอาจตกไปถึงระดับที่ต้องพึ่งญาติ เล่าด้วยแนวคิดแทนการเริ่มจากตัวแบบประกัน',
         '\n  <div class="levels">1 ร่ำรวย · 2 สบาย · 3 ชักหน้าไม่ถึงหลัง · 4 ต้องพึ่งญาติ</div>')}
</section>''')
S(qs('พอดูจบ คุณคิดว่าลูกค้าส่วนใหญ่ของคุณอยู่ระดับไหน?', '💬 ยกมือ 1-4 แล้วอภิปราย "เป้าหมายคือไม่ให้ครอบครัวของลูกค้าตกไปถึงระดับที่ 4"'))

# S8 · Story 2 rule of 72 (R1: 61 = 2,157,000 / 9,399,000); bars scaled to the value
r72 = [(35, 1000000, 1000000), (41, 1194000, 1677000), (47, 1426000, 2813000), (53, 1702000, 4717000),
       (59, 2033000, 7911000), (61, 2157000, 9399000)]
mx = max(b for _, _, b in r72)
tr = ''.join(f'<tr style="--k:{k}"><td>{a}</td><td><span class="bar-a" style="--w:{x / mx:.3f}"></span>{x:,}</td>'
             f'<td><span class="bar-b" style="--w:{y / mx:.3f}"></span>{y:,}</td></tr>' for k, (a, x, y) in enumerate(r72))
S(f'''<section class="slide dots r72">
  <div class="kick rv">Story 2</div>
  <h2 class="rv">Story 2: กฎ 72</h2>
  <table class="tb t72 rv"><thead><tr><th scope="col">อายุ</th><th scope="col">คน A (ผลตอบแทน 3%)</th><th scope="col">คน B (ผลตอบแทน 9%)</th></tr></thead><tbody>{tr}</tbody></table>
  <div class="foot rv">72 ÷ ผลตอบแทน = จำนวนปีที่เงินเพิ่มเป็น 2 เท่า · ต่างกัน 4 เท่า+ จากแค่ 3% vs 9% ยิ่งเวลายาว ยิ่งห่าง</div>
</section>''')
S(qs('คน A ต้องทำยังไงถ้าอยากมีเท่าคน B ตอนอายุ 61?', '💬 ช่วยกันตอบ (เพิ่มเงินลงทุน / เริ่มเร็วกว่า / หาผลตอบแทนดีกว่า)'))

# S9 · Story 3 video (R1: 28,000 วัน)
S(f'''<section class="slide dots vs-s">
  <div class="kick rv">Story 3</div>
  <h2 class="rv">Story 3: 28,000 วัน</h2>
  {video('s9', 'Story 3: 28,000 วัน', 'asnuSg9pJ3w', 'ดูคลิปด้วยกัน (ภาษาอังกฤษ ประมาณ 12 นาที)',
         'Dr Sanjay Tolani เล่าแนวคิด "28,000 วัน" มองการวางแผนการเงินตลอดทั้งชีวิต แล้วต่อด้วยเรื่องคุ้มครองรายได้')}
</section>''')
S(qs('พอดูจบ ลูกค้าของคุณอยู่ช่วงไหนของชีวิต?', '💬 ยกมือ แล้ววิเคราะห์ว่าช่วงนั้นต้องวางแผนอะไร'))

# S10 · financial ratios (R2: a rule of thumb, not a standard)
t10 = [('เงินสำรองฉุกเฉิน', '3-6 เดือนของรายจ่าย', 'พอดูแลตัวเองถ้าขาดรายได้'), ('ความคุ้มครองชีวิต', '5-10 เท่าของรายได้ต่อปี', 'ครอบครัวอยู่ได้ถ้าเราจากไป'),
       ('สัดส่วนหนี้ต่อรายได้', 'ไม่เกิน 40%', 'ไม่เป็นทาสหนี้'), ('อัตราการออม', 'อย่างน้อย 10-20% ของรายได้', 'มีอนาคตทางการเงิน'),
       ('ค่ารักษาพยาบาลสำรอง', 'วงเงินคุ้มครองสุขภาพ ≥ 1-5 ล้าน', 'ป่วยแล้วไม่กินทุน')]
S(f'''<section class="slide dots scroll">
  <div class="kick rv">เครื่องมือชี้ปัญหา สำหรับนักวางแผนการเงิน</div>
  <h2 class="rv">อัตราส่วนทางการเงิน</h2>
  {table(['อัตราส่วน', 'หลักคิดทั่วไป', 'ความหมาย'], t10, 'rat')}
  {rowcards(['อัตราส่วน', 'หลักคิดทั่วไป', 'ความหมาย'], t10, 'rat')}
  <div class="foot rv">เป้า: อยู่ได้ถ้าขาดรายได้</div>
</section>''')
S(qs('ลูกค้ารายได้ 50,000/เดือน ควรมีเงินสำรองฉุกเฉินเท่าไหร่?', None, answer='💬 คำนวณแบบเผื่อไว้ (ใช้รายได้แทนรายจ่าย): 50,000 x 6 = 300,000 บาท (มีกี่คนที่มีครบ?)'))

# S11 · case คุณเอ analysis (stray last line dropped per designer/writer R1)
def chip(v):
    c = 'red' if v.startswith('🔴') else 'sal'
    return f'<span class="vchip {c}">{v}</span>'
t11 = [('เงินสำรองฉุกเฉิน', '50,000 (1 เท่าของเงินเดือน)', '300,000 (6 เท่าของเงินเดือน)', chip('⚠️ ขาด 250,000')),
       ('ความคุ้มครองชีวิต', '500,000', '3,000,000-6,000,000', chip('🔴 ขาดมาก (ภรรยาแบกบ้าน 5M คนเดียว)')),
       ('ประกันสุขภาพ', 'สวัสดิการ 100,000', '1,000,000-5,000,000', chip('⚠️ ไม่พอ')),
       ('อัตราการออม', '5,000/เดือน (10%)', '10,000/เดือน (20%)', chip('⚠️ ถึงขั้นต่ำ ยังไม่ถึงเป้า 20%')),
       ('หนี้ต่อรายได้', '20,000/เดือน (40%) กู้บ้าน 5M', 'ไม่เกิน 40%', chip('⚠️ เต็มเพดาน'))]
h11 = ['รายการ', 'สถานะปัจจุบัน', 'เกณฑ์ที่ควรมี', 'ผลวิเคราะห์']
S(f'''<section class="slide dots case11 scroll">
  <div class="kick rv">ตัวอย่าง: คุณเอ</div>
  <div class="prof rv"><b>👤 คุณเอ · อายุ 35 ปี</b><span class="chip">พนักงานเงินเดือน 50,000/เดือน</span><span class="chip">เพิ่งแต่งงาน วางแผนมีลูกใน 2 ปี</span><span class="chip">กู้บ้าน 5M ร่วมภรรยา ผ่อน 20,000/เดือน</span><span class="chip">สวัสดิการบริษัท: ค่ารักษาพยาบาล 100,000 บาท</span></div>
  {table(h11, t11, 'c11')}
  {rowcards(h11, t11, 'c11')}
  <div class="take rv">"หนี้เต็มเพดาน 40% + คุ้มครองชีวิตขาดมาก ถ้าเกิดอะไรขึ้น ภรรยาต้องแบกภาระบ้าน 5 ล้านคนเดียว"</div>
</section>''')

# S12 · case plan (R1 fasai rows, total split in 2, placeholder removed)
t12 = [('คุ้มครองชีวิตขาด 2.5-5.5 ล้าน', 'ประกันชีวิต AIA Life Protector V70 (ตัวอย่าง)', '~31,350-68,970/ปี (ตัวอย่าง: ชาย 35 ปี ทุน 2.5-5.5 ล้าน)'),
       ('สุขภาพไม่พอ (100K → 1-5M)', 'AIA Health Happy หรือ สุขภาพเดี่ยว', '~10,000-20,000/ปี'),
       ('สำรองฉุกเฉินขาด 250,000', 'แผนออมระยะสั้น', 'ออมเพิ่ม 5,000/เดือน x 50 เดือน'),
       ('อัตราการออมต่ำ', 'สะสมทรัพย์/บำนาญ + ลดหย่อนภาษี', '~10,000-20,000/ปี')]
h12 = ['ช่องว่าง', 'แผนแนะนำ', 'เบี้ยโดยประมาณ']
S(f'''<section class="slide dots case11 scroll">
  <div class="kick rv">แผนแนะนำสำหรับคุณเอ</div>
  <h2 class="rv">จากวิเคราะห์ สู่แผนที่ตอบโจทย์</h2>
  {table(h12, t12, 'c12')}
  {rowcards(h12, t12, 'c12')}
  <div class="tot rv"><b>งบเบี้ยประกันรวม: ~51,350-108,970/ปี (ประมาณ 4,300-9,100/เดือน)</b><span>เงินออมฉุกเฉิน: 5,000/เดือน แยกจากเบี้ยประกัน</span></div>
  <div class="sub rv">(จัดลำดับความสำคัญ ไม่ต้องทำทีเดียวทุกอย่าง)</div>
</section>''')
S(qs('ถ้าคุณเอมีงบแค่ 3,000/เดือน ควรเริ่มจากอะไรก่อน?', '💬 ช่วยกันจัดลำดับความสำคัญ'))

# S13 · sailboat: each tap lights one part (sail → mast → hull → anchor) and its line
boat = '''<svg class="boat" viewBox="0 0 200 220" role="img" aria-label="เรือใบ">
  <path class="p-sail" d="M104 20 L104 130 L170 130 Z"/><path class="p-sail" d="M96 36 L96 130 L44 130 Z"/>
  <line class="p-mast" x1="100" y1="12" x2="100" y2="150"/>
  <path class="p-hull" d="M30 150 L170 150 L150 178 L50 178 Z"/>
  <path class="p-anchor" d="M100 178 L100 204 M88 196 Q100 212 112 196 M92 186 L108 186"/>
  <path class="water" d="M10 184 Q30 176 50 184 T90 184 T130 184 T170 184 T190 184"/>
</svg>'''
parts = [('l1', '⛵ใบเรือ = การลงทุนขับเคลื่อนให้ไปข้างหน้า (หุ้น กองทุน ประกันชีวิตควบการลงทุน Unit Linked)'),
         ('l2', '🏗️เสา = ประกันชีวิตค้ำจุนให้ใบเรือทำงานได้ (ถ้าเสาหัก ใบเรือตก = รายได้หาย)'),
         ('l3', '🛟ตัวเรือ = เงินออมทำให้ลอยน้ำ มั่นคง (ฝากแบงก์ สลากออมทรัพย์)'),
         ('l4', '⚓สมอ = ประกันสุขภาพกันไม่ให้ลอยไปตามกระแส (ค่ารักษาไม่กินทุน)')]
ls = ''.join(f'<li class="stp {c}">{t}</li>' for c, t in parts)
S(f'''<section class="slide dots sailb">
  <div class="kick rv">Story</div>
  <h2 class="rv">Story: เรือใบ</h2>
  <div class="intro rv">เปรียบชีวิตทางการเงินเป็นเรือใบ</div>
  <div class="sbw rv">{boat}<ul class="sbl">{ls}</ul></div>
  <div class="foot rv">"ถ้ามีแต่ใบเรือ (ลงทุน) แต่ไม่มีเสา (ประกัน) พอเจอพายุ ทุกอย่างพังหมด"</div>
</section>''')
S(qs('เรือใบของคุณ (หรือลูกค้าคุณ) ยังขาดส่วนไหน?', '💬 วิเคราะห์ตัวเอง/ลูกค้า 1 คน'))

# S14 · two levels
S('''<section class="slide dots ans lv2">
  <div class="kick rv">สร้างปัญหา · แบบ Need Approach</div>
  <h2 class="rv">2 ระดับของการสร้างปัญหา</h2>
  <div class="grid c2 rv">
    <div class="card"><div class="ct">ระดับ 1: ที่ปรึกษาทางการเงิน</div><div class="cd">ถามตรงประเด็น</div>
      <div class="thread"><div class="bub me">"พี่ได้วางแผนสำหรับเรื่องนี้แล้วหรือยังครับ?"</div><div class="bub me">"ถ้าต้องหยุดทำงาน 6 เดือน ครอบครัวจะเป็นยังไง?"</div><div class="bub me">"ค่าเรียนลูกอีก 15 ปี พี่เตรียมไว้เท่าไหร่แล้ว?"</div></div></div>
    <div class="card"><div class="ct">ระดับ 2: นักวางแผนการเงิน</div><div class="cd">ใช้ข้อมูลชี้ปัญหา</div>
      <div class="card sm"><div class="cd">ใช้อัตราส่วนทางการเงิน วิเคราะห์สถานะจริง</div></div>
      <div class="card sm"><div class="cd">เช่น: รายได้ vs รายจ่าย, เงินสำรอง, ความคุ้มครอง, สัดส่วนหนี้</div></div>
      <div class="card sm"><div class="cd">พูดคุยเพื่อเสนอ Solution (ชี้ช่องว่างจากข้อมูลจริง)</div></div></div>
  </div>
</section>''')
S(qs('ลูกค้ารายได้ 50,000/เดือน ยังไม่มีประกัน ควรมีความคุ้มครองชีวิตเท่าไหร่?', '💬 ใช้สูตร 5-10 เท่าของรายได้ต่อปี คำนวณ'))

# S15 · meeting: 3 numbered keys (R1 ใบอนุญาตตัวแทน), coach bg
S('''<section class="slide img ans" data-bg="coach">
  <div class="kick rv">เมื่อเข้าพบลูกค้า</div>
  <h2 class="rv">3 ขั้นตอนมืออาชีพ</h2>
  <div class="grid c3 rv">
    <div class="card spot" style="--ci:0"><div class="n">1</div><div class="ct">แนะนำตัว + ใบอนุญาต</div><div class="cd">แสดงใบอนุญาตตัวแทน (และ IC ถ้ามี) สร้างความมั่นใจ</div></div>
    <div class="card spot" style="--ci:1"><div class="n">2</div><div class="ct">วัตถุประสงค์ที่ชัดเจน</div><div class="bub me">"วันนี้ผมมาเพื่อทำความเข้าใจเป้าหมายของพี่ ยังไม่ได้มาเสนออะไร"</div></div>
    <div class="card spot" style="--ci:2"><div class="n">3</div><div class="ct">ชี้แจงขอบข่ายบทสนทนา</div><div class="bub me">"เราจะพูดกัน 4 เรื่อง: คุ้มครอง ออม ลงทุน ภาษี" + ยกตัวอย่าง</div></div>
  </div>
</section>''')

# S16 · 6 steps
st6 = [('เก็บข้อมูล', 'รายได้ รายจ่าย ทรัพย์สิน หนี้สิน'), ('วิเคราะห์', 'สถานะปัจจุบัน ช่องว่าง ความเสี่ยง'), ('กำหนดเป้าหมาย', 'ร่วมกับลูกค้า'),
       ('ออกแบบแผน', 'จัดพอร์ตให้ตอบเป้าหมายที่ตั้งไว้'), ('นำเสนอ', 'ลูกค้าเห็นภาพรวม เลือกแผน'), ('ทบทวนแผน', 'ปีละครั้ง ปรับตามชีวิต')]
li = ''.join(f'<li><span class="rn">{k + 1}</span><b>{t}</b><span class="dl">{d}</span></li>' for k, (t, d) in enumerate(st6))
S(f'''<section class="slide dots">
  <div class="kick rv">DATA → ANALYZE → PLAN</div>
  <h2 class="rv">Financial Planning Process <span class="sub2">6 ขั้นตอนการวางแผน</span></h2>
  <ol class="hstep six6 rv" style="--n:6">{li}</ol>
  <div class="foot rv">"กระบวนการนี้ทำให้ลูกค้ามั่นใจว่าทุกอย่างมีระบบ ไม่ได้ซื้อตามอารมณ์"</div>
</section>''')

# S17 · pyramid, built base-first (DOM order = source order top→base; CSS reverses the build delay)
tiers = [('top', '🎯', 'ยอด: ลงทุนเพื่อเติบโต', ['กองทุน / ประกันชีวิตควบการลงทุน (Unit Linked) / หุ้น']),
         ('t3', '💰', 'ชั้น 3: ออม เกษียณสบาย', ['สะสมทรัพย์ / บำนาญ', 'เป้า: เงินพอใช้หลังเกษียณ']),
         ('t2 key', '🛡️', 'ชั้น 2: คุ้มครอง ชีวิต+สุขภาพ+รายได้', ['ประกันชีวิต + สุขภาพ', '⚠️ สำคัญมาก! คุณเอมีภาระบ้าน 5M']),
         ('base key', '🏦', 'ฐาน (ชั้น 1): เงินสำรองฉุกเฉิน', ['เงินสด 3-6 เดือนของรายจ่าย'])]
py = ''.join(f'<li class="{c}" style="--i:{k}"><span class="pe">{e}</span><b>{t}</b>' + ''.join(f'<span>{d}</span>' for d in ds) + '</li>'
             for k, (c, e, t, ds) in enumerate(tiers))
S(f'''<section class="slide dots pyr-s scroll">
  <div class="kick rv">จัดพอร์ตตามลำดับความสำคัญ จากฐานขึ้นยอด</div>
  <h2 class="rv">พีระมิดการเงิน</h2>
  <ol class="pyr">{py}</ol>
  <div class="cd rv">กรณีคุณเอ: ฐานยังไม่แข็ง (สำรองแค่ 1 เดือน + คุ้มครองชีวิตไม่พอแบกบ้าน 5M) → เริ่มชั้น 1-2 ก่อน</div>
  <div class="foot rv">สร้างจากฐานก่อน อย่าสร้างยอดก่อนฐาน</div>
</section>''')
S(qs('คุณเอควรเริ่มจากชั้นไหนของพีระมิด เพราะอะไร?', '💬 ช่วยกันจัดลำดับ'))

# S18 · close over 2-3 appointments (light bg); step 3 dashed
S('''<section class="slide img ans" data-bg="light">
  <div class="kick rv">ปิดการขาย · แบบ Need Approach</div>
  <h2 class="rv">2-3 นัดหมาย ลึก ครบ มืออาชีพ</h2>
  <ol class="ap3 rv">
    <li><span class="al">นัดที่ 1</span><span class="rn">1</span><b>เก็บข้อมูล + สร้างความเข้าใจ</b><span>ฟัง เก็บข้อมูล ใช้ Story เปิดใจ</span><div class="bub me">"ผมขอเวลาไปวิเคราะห์ข้อมูลของพี่ แล้วนัดเจอกันอีกครั้ง"</div></li>
    <li><span class="al">นัดที่ 2</span><span class="rn">2</span><b>วิเคราะห์ + เสนอแผน</b><span>นำเสนอผลวิเคราะห์ + แผนเฉพาะ ถามตอบ ปรับแผน</span><span class="ok">ปิดได้เลยถ้าลูกค้าพร้อม</span></li>
    <li class="opt"><span class="al">นัดที่ 3 (ถ้าจำเป็น)</span><span class="rn">3</span><b>ปิดการขาย (ถ้าจำเป็น)</b><span>ตอบข้อสงสัย ปรับแผน ปิดด้วยการให้เลือก (แผน A หรือ B)</span></li>
  </ol>
  <div class="foot rv">Need Approach ใช้เวลามากกว่า แต่ลูกค้าได้แผนครอบคลุม + ความสัมพันธ์ระยะยาว</div>
</section>''')

# S19 · Q&A (already question-only), group bg
S('''<section class="slide img q" data-bg="group">
  <div class="kick rv">Q&amp;A</div>
  <h2 class="qtext rv">ถาม-ตอบ <span class="r">เคสจริง</span></h2>
  <div class="prompt rv">💬 ยกเคสลูกค้าจริง 1 คน → ช่วยกันเลือกว่าควรใช้ Product หรือ Need Approach → เลือก Topic/Story ที่เหมาะ</div>
  <div class="prompt rv">💬 ยกเคสคนละ 1 เรื่อง</div>
</section>''')

# S20 · workshop round (white), R1 story names
wr = ['เลือก Topic ทำนัด (เกษียณ / การศึกษาบุตร / องค์รวม / คุ้มครองรายได้)', 'เปิดใจด้วย Story 1 เรื่อง (ฐานะ 4 ระดับ / กฎ 72 / 28,000 วัน / เรือใบ)',
      'สร้างปัญหา (ถามตรงประเด็น + ใช้อัตราส่วนการเงิน)', 'แนะนำตัว + วัตถุประสงค์ + ขอบข่าย', 'เสนอแผน + จัดพอร์ตตัวอย่าง', 'ปิดการขาย (ให้เลือกแผน A หรือ B)']
li = ''.join(f'<li><span class="rn">{k + 1}</span><span>{t}</span></li>' for k, t in enumerate(wr))
S(f'''<section class="slide part notes ws">
  <div class="kick rv">🛑 WORKSHOP</div>
  <h2 class="rv">Need Approach <span class="r">1 รอบเต็ม</span></h2>
  <div class="intro rv">Role-play จับคู่</div>
  <ol class="vstep rv">{li}</ol>
</section>''')

# S21 · presentation + criteria checklist (white)
cr = ['เลือก Topic ตรงลูกค้า', 'Story เปิดใจได้', 'สร้างปัญหาจากข้อมูล', 'แผนครอบคลุม', 'ปิดมืออาชีพ']
li = ''.join(f'<li><span class="tick" aria-hidden="true"></span><span>✔️ {t}</span></li>' for t in cr)
S(f'''<section class="slide part notes ws">
  <div class="kick rv">🛑 WORKSHOP</div>
  <h2 class="rv">นำเสนอหน้าห้อง</h2>
  <div class="big5 rv">5 นาที</div>
  <div class="intro rv">ยาวกว่า T.4 เพราะลึกกว่า รับ feedback</div>
  <div class="ct rv">เกณฑ์การประเมิน</div>
  <ul class="crit rv">{li}</ul>
</section>''')

# S22 · closing quote + close (the only gold), next class T.6/6
S('''<section class="slide img quote close" data-bg="leader">
  <div class="bar gbar rv"></div>
  <div class="one rv" data-read><span class="ql">"ตัวแทนที่ดี ขายสิ่งที่ลูกค้าต้องการ</span><span class="ql gold">นักวางแผนการเงินที่ดี ช่วยลูกค้าค้นพบสิ่งที่เขาต้องการจริงๆ"</span></div>
  <div class="tag rv late2">จริงใจ · ลงมือ · อยู่ด้วยกัน •</div>
  <div class="next rv late2">🌟 คลาสถัดไป · T.6/6 Workshop ปิดการขาย</div>
</section>''')

T5CSS = '''
/* T5-only layout */
.tag0{letter-spacing:.2em;font-weight:800;color:var(--salmon)}
.sub2{display:block;font-size:var(--fs);color:var(--salmon);font-weight:800;margin-top:.2em}
/* S2 map: 6 slots, number + title + subtitles */
.smap li b+b{display:block}
/* S3 appointment flow */
.apf{display:flex;flex-direction:column;gap:.4em;width:100%}.apl{font-weight:700}
/* split question slides: one layout (measured in G1) */
.qsplit .qe{font-size:.6em;vertical-align:.25em}
.q .card.qa{max-width:900px;background:rgba(38,38,44,.85);border-color:rgba(232,153,141,.45)}
/* tables (S4 S8 S10 S11 S12): real <table> >= 681px, row cards below */
.tb{border-collapse:separate;border-spacing:0 .35em;width:100%;max-width:1200px}
.tb th{color:var(--muted);font-weight:800;text-align:left;padding:0 .7em}
.tb td{background:rgba(38,38,44,.8);padding:.45em .7em;line-height:1.4;vertical-align:top}
.tb td:first-child{border-radius:10px 0 0 10px;font-weight:800}.tb td:last-child{border-radius:0 10px 10px 0}
.tb.cmp td:first-child{color:var(--salmon)}
.rcards{display:none;flex-direction:column;gap:.5em;width:100%}
.rc{background:rgba(38,38,44,.85);border:1px solid var(--line);border-radius:14px;padding:.55em .8em;display:flex;flex-direction:column;gap:.3em}
.rc-t{font-weight:900;color:var(--salmon)}.rc-v{display:flex;flex-direction:column;line-height:1.4}.rc-k{color:var(--muted);font-weight:700}
.rcards.cmp .rc-v+.rc-v{border-top:1px solid var(--line);padding-top:.3em}
.foot.center{text-align:center;border-left:0;align-self:center}
/* S5 topics */
.topics .card{gap:.35em}.topics .em{font-size:1.6em;line-height:1}.topics .bub{max-width:100%}
/* S6 big S */
.bigS{font-size:clamp(80px,min(14vw,24vh),240px);font-weight:900;color:var(--red);line-height:.9}
/* S7/S9 video facade */
.vwrap{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(12px,2vw,32px);align-items:center;width:100%}
.vid{position:relative;width:min(640px,100%,calc((100dvh - 230px) * 16 / 9))}
.vtxt{display:flex;flex-direction:column;gap:.5em;line-height:1.45}
.vfacade{position:relative;display:block;width:100%;aspect-ratio:16/9;border:0;padding:0;border-radius:14px;overflow:hidden;cursor:pointer;background:#000}
.vfacade img{width:100%;height:100%;object-fit:cover;display:block}
.vfacade .play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:72px;height:72px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-size:30px;box-shadow:0 6px 24px rgba(0,0,0,.45)}
.vid iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:14px;display:block}
.vcap{font-weight:800;margin-top:.35em}
.ytlink{color:var(--salmon);font-weight:800;text-decoration:underline}
.levels{font-weight:800;color:var(--salmon)}
/* S8 rule of 72 bars (A muted, B red: bars allowed on charcoal) */
.t72{max-width:1000px}.t72 td{position:relative;font-variant-numeric:tabular-nums;overflow:hidden}
.t72 td span{position:absolute;left:0;top:0;bottom:0;width:calc(var(--w) * 100%);z-index:-1;transform-origin:left;transform:scaleX(0)}
.t72 td{z-index:0}
.bar-a{background:rgba(184,175,166,.28)}.bar-b{background:rgba(211,17,69,.45)}
.on .t72 td span{animation:grow .45s ease-out forwards;animation-delay:calc(.3s + var(--k,0) * .09s)}  /* all rows settled by ~1.2s (G1 settled shots) */
.t72 tr{--k:0}
@keyframes grow{to{transform:scaleX(1)}}
/* S11/S12 case */
.prof{display:flex;flex-wrap:wrap;gap:.4em;align-items:center;width:100%}
.prof b{font-size:1.2em;margin-right:.4em}
.vchip{display:inline-block;border-radius:999px;padding:.15em .7em;font-weight:800;line-height:1.35}
.vchip.red{background:var(--red);color:#fff}.vchip.sal{background:rgba(232,153,141,.2);color:var(--salmon);border:1px solid rgba(232,153,141,.5)}
.take{color:var(--salmon);font-weight:800;line-height:1.45}
.tot{display:flex;flex-direction:column;gap:.2em}.tot span{color:var(--muted)}
/* S13 sailboat */
.sbw{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(12px,2vw,32px);align-items:center;width:100%}
.boat{width:100%;max-height:48vh}
.boat path,.boat line{fill:none;stroke:rgba(255,255,255,.45);stroke-width:3;stroke-linejoin:round;stroke-linecap:round;transition:stroke .4s,fill .4s}
.boat .water{stroke:rgba(255,255,255,.2)}
.sailb:has(.l1.shown) .p-sail,.sailb.revealed .p-sail{stroke:var(--red);fill:rgba(211,17,69,.18)}
.sailb:has(.l2.shown) .p-mast,.sailb.revealed .p-mast{stroke:var(--red)}
.sailb:has(.l3.shown) .p-hull,.sailb.revealed .p-hull{stroke:var(--red);fill:rgba(211,17,69,.18)}
.sailb:has(.l4.shown) .p-anchor,.sailb.revealed .p-anchor{stroke:var(--red)}
.sbl{list-style:none;display:flex;flex-direction:column;gap:.5em;line-height:1.45}
/* S14 */
.lv2 .card.sm{background:rgba(255,255,255,.05);padding:.4em .7em}
.lv2 .thread{gap:.35em}.lv2 .bub{max-width:100%}
/* S16 6 steps */
.six6 li{gap:.2em}.six6 .dl{font-weight:400;color:#e9e6e3;line-height:1.35}
/* S17 pyramid: base first */
.pyr{list-style:none;display:flex;flex-direction:column;align-items:center;gap:.3em;width:100%;max-width:1000px}
.pyr li{display:flex;flex-wrap:wrap;justify-content:center;align-items:baseline;gap:.2em .6em;text-align:center;padding:.4em 1em;border:1.5px solid var(--line);background:rgba(38,38,44,.85);
  clip-path:polygon(4% 0,96% 0,100% 100%,0 100%);line-height:1.35;opacity:0;transform:translateY(10px)}
.pyr li.top{width:46%;color:var(--muted)}.pyr li.t3{width:62%;color:var(--muted)}.pyr li.t2{width:80%}.pyr li.base{width:100%}
.pyr li.key{border-color:var(--red);background:rgba(211,17,69,.14)}
.pyr li b{color:#fff}
.on .pyr li{animation:up .5s ease-out forwards;animation-delay:calc(.4s + (3 - var(--i)) * .35s)}
@keyframes up{to{opacity:1;transform:none}}
/* S18 appointments */
.ap3{list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.7em;width:100%}
.ap3 li{border:1.5px solid var(--line);border-radius:14px;padding:.6em .8em;display:flex;flex-direction:column;gap:.3em;background:rgba(28,28,33,.82);line-height:1.4}
.ap3 li.opt,.apf .flow li.opt span{border-style:dashed}.ap3 .al{color:var(--salmon);font-weight:800}.ap3 .ok{color:var(--salmon);font-weight:700}.ap3 .bub{max-width:100%}
/* S20/S21 workshops (white) */
.vstep{list-style:none;display:flex;flex-direction:column;gap:.45em;width:100%;max-width:1100px}
.vstep li{display:flex;align-items:center;gap:.8em;font-weight:700;line-height:1.35;color:var(--ink)}
.big5{font-size:clamp(48px,min(7vw,12vh),120px);font-weight:900;color:var(--red);line-height:1}
.crit{list-style:none;display:flex;flex-direction:column;gap:.4em}
.crit li{display:flex;align-items:center;gap:.7em;font-weight:700;color:var(--ink)}
.crit .tick{width:1.2em;height:1.2em;border:2px solid rgba(28,28,33,.45);border-radius:4px;flex:none}
/* S22 close */
.quote .one{max-width:26ch;line-height:var(--qlh,1.45)}
.quote .one .ql{display:block;text-wrap:balance}
.quote .one .ql+.ql{margin-top:.08em}
.next{font-weight:800;color:var(--salmon)}
.on .late2.rv{animation-delay:2.2s}
@media (max-width:680px){
  .tb.cmp,.tb.rat,.tb.c11,.tb.c12{display:none}
  .rcards{display:flex}
  .sbw{grid-template-columns:1fr}.boat{max-height:34vh}
  .vwrap{grid-template-columns:1fr}.vid{width:100%}
  .ap3{grid-template-columns:1fr}
  .pyr li{padding:.35em .6em}
  .pyr li.top{width:64%}.pyr li.t3{width:76%}.pyr li.t2{width:88%}
  .quote .one{font-size:clamp(20px,6.2vw,26px);max-width:none}
  .smap{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (prefers-reduced-motion:reduce){.pyr li{opacity:1;transform:none}.t72 td span{transform:none}}
'''

VIDJS = '''
/* T2250 video facade: no iframe until ▶ is tapped (an iframe eats taps/swipes and costs bandwidth on load) */
document.querySelectorAll('.vfacade').forEach((b) => {
  b.addEventListener('click', (e) => {
    e.stopPropagation();
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.vid + '?autoplay=1&rel=0';
    f.title = b.getAttribute('aria-label');
    f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true;
    b.replaceWith(f);
    // designer G1 (T2250): leaving the slide must stop the audio, so the facade comes back when the slide loses .on
    const slide = f.closest('.slide');
    const mo = new MutationObserver(() => { if (!slide.classList.contains('on')) { mo.disconnect(); f.replaceWith(b); } });
    mo.observe(slide, { attributes: true, attributeFilter: ['class'] });
  });
});
document.querySelectorAll('.ytlink').forEach((a) => a.addEventListener('click', (e) => e.stopPropagation()));
'''

CSS = open(os.path.join(SERIES, 'deck.css'), encoding='utf-8').read() + T5CSS
JS = open(os.path.join(SERIES, 'deck.js'), encoding='utf-8').read() + VIDJS
BGS = {k: bg(k) for k in ['cover', 'listen', 'coach', 'light', 'group', 'leader']}
bgcss = '\n'.join(f'.slide[data-bg="{k}"]{{--bg:{v}}}' for k, v in BGS.items())

html = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>iTraining T.5/6 · Need Approach</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700;800&family=Noto+Color+Emoji&display=swap" rel="stylesheet">
<style>
{CSS}
{bgcss}
</style>
</head>
<body>
<div class="prog" id="prog"></div>
<div class="wm"><i>i</i>Agency<span class="a">AIA</span></div>
<div class="pg"><span id="cur">1</span> / <span id="tot">1</span></div>
<main id="deck" tabindex="-1">
{chr(10).join(SLIDES)}
</main>
<button class="arrow" id="prev" aria-label="ก่อนหน้า">‹</button>
<button class="arrow" id="next" aria-label="ถัดไป">›</button>
<nav id="dots" aria-label="สไลด์"></nav>
<script>
{JS}
</script>
</body>
</html>
'''
body = html.split('<main', 1)[1].split('</main>', 1)[0]
text = re.sub(r'<[^>]+>', ' ', body)
assert '—' not in html and '–' not in html, 'em/en dash found'
assert not re.search(r'\S - \S', text), 'spaced ASCII hyphen used as a dash'
assert 'รอยืนยัน' not in html and 'iCheck' not in html and 'Circle of Life' not in html and '9,434,000' not in html
assert '<iframe' not in body, 'videos must be facades until tapped'
assert html.count('class="ql gold"') == 1 and html.count('class="bar gbar rv"') == 1, 'gold must be on S22 only'
assert len(SLIDES) == 32, len(SLIDES)
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html), 'bytes,', len(SLIDES), 'slides,', html.count('data-pending='), 'pending')
