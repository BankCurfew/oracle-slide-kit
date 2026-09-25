#!/usr/bin/env python3
"""T2229 · iTraining T4/6 Product Approach builder (fe, on the T2194 series template).
Text source = Writer-Oracle output/t2229-inventory/T2229-T4-product-approach-inventory.md (28 slides / 281 lines),
verbatim, with the recorded rulings applied (R1 S10 stat dropped, R2 Promotion, R3 question split, R4 fasai facts,
F5 start hint). Layout = Designer-Oracle output/t2229-product-approach/ART-DIRECTION.md (192a19d + F7 45d032d):
37 slides = 28 + 9 split question slides. Lines still waiting on a ruling render nothing and carry
data-pending="<flag>" so G1/parity count them (no "[รอยืนยัน" ever reaches trainees).
Screenshots = live uKnow via the FE-Oracle harness ([TEST] profile, Supabase mocked, 0 prod writes):
S17 question screen, S18 = result beat s26 (coverage gap), S19 = result beat s27 (fill the gap) · designer pick A.
"""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.join(HERE, '..')
BG_DIR = os.path.join(SERIES, 't1-mindset', 'img')  # series backgrounds, shared with T1
OUT = os.path.join(HERE, '..', '..', '..', 'output', 'itraining-t4-product-approach.html')

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def bg(name):
    return "url('data:image/webp;base64," + b64(os.path.join(BG_DIR, f'bg-{name}.webp')) + "')"

def shot(name):
    return 'data:image/webp;base64,' + b64(os.path.join(HERE, 'img', f'shot-{name}.webp'))

def pending(flag):
    return f'<div class="pend" data-pending="{flag}" hidden></div>'

# ---------- slide builders ----------
def q(words_html, prompt, kick='คำถามฝึกคิด', bg_name=None, pre='', after=''):
    cls = f'slide img q" data-bg="{bg_name}' if bg_name else 'slide dots q'
    return f'''<section class="{cls}">
  {pre}<div class="kick rv">{kick}</div>
  <h2 class="qtext rv">{words_html}</h2>
  <div class="prompt rv">{prompt}</div>{after}
</section>'''

def chan(n, title, sub, body, script=None):
    s = f'<div class="thread rv"><div class="lbl">บทเปิด:</div><div class="bub me">{script}</div></div>' if script else ''
    return f'''<section class="slide dots chn-s">
  <div class="chn rv">ช่องทาง {n}</div>
  <h2 class="rv">{title}</h2>
  <div class="sub rv">{sub}</div>
  {body}
  {s}
</section>'''

def pts(items):
    return '<ul class="pts rv">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def flow(items, lite=False):
    li = ''.join(f'<li style="--k:{k}"><span>{t}</span>' + ('<i>→</i>' if k < len(items) - 1 else '') + '</li>'
                 for k, t in enumerate(items))
    return f'<ol class="flow{" lite" if lite else ""} rv">{li}</ol>'

def hstep(items):
    li = ''.join(f'<li><span class="rn">{k + 1}</span><span>{t}</span></li>' for k, t in enumerate(items))
    return f'<ol class="hstep rv" style="--n:{len(items)}">{li}</ol>'

def shot_slide(img, alt, kick, title, body):
    return f'''<section class="slide dots shot-s">
  <div class="shot">
    <div class="phone rv"><img src="{shot(img)}" alt="{alt}"></div>
    <div class="txt">
      <div class="kick rv">{kick}</div>
      <h2 class="rv">{title}</h2>
      {body}
    </div>
  </div>
</section>'''

SLIDES = []
S = SLIDES.append

# 01 · S01 cover (F5 hint = T1 ruling)
S('''<section class="slide img cover" data-bg="cover">
  <div class="kick rv">iTRAINING · T.4/6</div>
  <h1 class="rv"><span class="aurora">Product Approach</span></h1>
  <div class="bar rv"></div>
  <div class="lead rv">เข้าให้เร็ว นัดให้ได้ ด้วยข้อมูลที่มีอยู่ในมือ</div>
  <div class="hint rv">แตะ · ปัด · หรือกด → เพื่อเริ่ม</div>
</section>''')

# 02 · S02 series map (F4 ruled bob 11:2x: 6 slots; T.5/T.6 titles from storage names, writer confirms)
smap = [('T.1 Mindset', 'ขายเพราะเชื่อในคุณค่าการวางแผน', ''),
        ('T.2 เทคนิคการขาย', 'คำมั่นสัญญา จุดขาย AIA รับมือความเสี่ยง', ''),
        ('T.3 กระบวนการขาย', 'อ่านคน เปิดใจ สร้างปัญหา นำเสนอ ปิด', ''),
        ('T.4 Product Approach', 'ทางเข้าที่เร็วขึ้น ใช้สินค้าเป็น "ประตู" ทำนัด', 'now'),
        ('T.5 Need Approach', 'เริ่มจากความต้องการลูกค้า', ''),
        ('T.6 Workshop ปิดการขาย', 'ฝึกปิดการขายแบบลงมือทำ', '')]
li = ''.join(f'<li class="{c}"><b>{t}</b>' + (f'<span>{d}</span>' if d else '') + '</li>' for t, d, c in smap)
S(f'''<section class="slide dots">
  <div class="kick rv">T.4 อยู่ตรงไหน</div>
  <h2 class="rv">ใน 6 คลาส</h2>
  <ol class="smap rv">{li}</ol>
</section>''')

# 03 · S03 concept
S('''<section class="slide dots ans">
  <div class="kick rv">Product Approach</div>
  <h2 class="rv"><span class="aurora">= ประตู</span> ไม่ใช่ปลายทาง</h2>
  <div class="intro rv">วัตถุประสงค์คือ ทำนัดให้ได้ ไม่ใช่ปิดการขายด้วยสินค้าที่ใช้เปิด</div>
  <div class="grid c2 rv">
    <div class="card spot"><div class="ct">เปิดด้วยสุขภาพ</div><div class="cd">อาจจบที่แบบเก็บเงิน หรือโรคร้ายแรงก็ได้</div></div>
    <div class="card spot"><div class="ct">เปิดด้วยการลงทุน</div><div class="cd">อาจจบที่ประกันคุ้มครองก็ได้</div></div>
  </div>
</section>''')
# 04 · S03 question + its answer (one tap reveals the answer lines)
S(q('ถ้าเปิดด้วยประกันสุขภาพ<br>แต่คุยไปลูกค้าเหมาะกับแบบออมเงินมากกว่า<br><span class="r">คุณควรทำยังไง?</span>', '💬 เดาก่อน แล้วเฉลย',
    after='''
  <div class="card qa stp"><div class="ct">เปลี่ยนได้เลย เป้าคือแผนที่ใช่สำหรับลูกค้า</div><div class="cd">ไม่ใช่ขายให้ได้สินค้าที่ตั้งใจมา</div></div>'''))

# 05 · S04 mindset
S('''<section class="slide img ans" data-bg="listen">
  <div class="kick rv">ทัศนคติ</div>
  <h2 class="rv">Product Approach</h2>
  <div class="vs rv"><div class="row"><s>ไม่ใช่ขายมักง่าย</s></div></div>
  <div class="card spot rv narrow"><div class="ct">คือ การเคารพเวลาลูกค้า เมื่อมีข้อมูลชี้ทางแล้ว</div></div>
  <div class="foot rv">ยังยึดประโยชน์ลูกค้าเป็นหลัก (T.1) แค่เดินเข้าประตูที่เปิดอยู่</div>
</section>''')
# 06 · S04 question
S(q('Product Approach<br>= <span class="r">ขายของมักง่าย</span> จริงไหม?', '💬 คิดว่าใช่หรือไม่ เพราะอะไร'))

# 07 · S05 core: 5 channels (white editorial, graded ladder; R2 Promo -> Promotion)
lad = [('1', 'สินค้านี้ น่าจะเหมาะ', 'ข้อมูลเฉพาะเจาะจง'), ('2', 'Promotion ลูกค้าเก่า', 'มีความสัมพันธ์เดิม'),
       ('3', 'กระแส ลูกค้าทักมา', 'Need เริ่มก่อตัว'), ('4', 'Promotion ลูกค้าใหม่', 'สร้างจากศูนย์'),
       ('5', 'Knock Door', 'ข้อมูลน้อยสุด')]
li = ''.join(f'<li><span class="n">{n}</span><b>{t}</b><span>{d}</span></li>' for n, t, d in lad)
S(f'''<section class="slide part ed">
  <div class="kick rv">แกนหลัก</div>
  <h2 class="rv">5 ช่องทางโอกาส</h2>
  <div class="skew rv"></div>
  <div class="axis rv">เรียงจากข้อมูลมาก (ง่าย) ไปข้อมูลน้อย (ยาก)</div>
  <ol class="ladder rv">{li}</ol>
</section>''')
# 08 · S05 question
S(q('<span class="r">ช่องทางไหนโอกาสปิดสูงสุด</span><br>เพราะอะไร?', '💬 เรียง 5 ช่องทาง แล้วเฉลยว่าทำไม "ข้อมูล" คือตัวกำหนด', bg_name='group'))

# 09 · S06 channel 1 (life-event map verbatim, fasai F2 PASS as categories)
ev = [('เพิ่งมีลูก', 'ประกันการศึกษา / คุ้มครองผู้นำรายได้'), ('เพิ่งซื้อบ้าน', 'คุ้มครองภาระหนี้'),
      ('ญาติป่วย', 'สุขภาพ / โรคร้ายแรง'), ('ใกล้เกษียณ', 'บำนาญ / วางแผนเกษียณ')]
emap = '<div class="emap rv">' + ''.join(f'<span class="ev">{a}</span><span class="ar">→</span><span class="pr">{b}</span>' for a, b in ev) + '</div>'
S(chan(1, 'สินค้านี้น่าจะเหมาะ', 'ข้อมูลเฉพาะเจาะจง = โอกาสสูงสุด', emap,
       '"ที่พี่เพิ่งมีน้อง ผมมีแผนที่คนเป็นพ่อแม่มือใหม่ส่วนใหญ่เตรียมไว้ ขอเล่าให้ฟังสั้นๆ นะครับ"'))
# 10 · S07 channel 2
S(chan(2, 'Promotion ลูกค้าเก่า', 'มีความสัมพันธ์เดิม + ประวัติในระบบ',
       pts(['ลูกค้าที่มีกรมธรรม์ + สัญญาณสนใจเพิ่ม (เคยถาม, เปรยว่าคุ้มครองไม่พอ, ใกล้ครบสัญญา)',
            'ใช้ Promotion เป็นเหตุผลติดต่อที่เป็นธรรมชาติ ไม่ใช่โผล่มาขายเฉยๆ',
            'ได้เปรียบ: ดูได้ว่าคุ้มครองอะไรไปแล้ว ขาดอะไร']),
       '"พี่คะ ช่วงนี้มีโปรสำหรับลูกค้าเดิมพอดี หนูเห็นว่าแผนพี่ยังไม่มีส่วนชดเชยรายวัน เลยนึกถึงพี่ ขอเล่าสั้นๆ นะคะ"'))
# 11 · S08 channel 3
S(chan(3, 'กระแส: ลูกค้าทักมาถามเอง', 'Need เริ่มก่อตัวแล้ว ตอบเร็ว + เปลี่ยนแชทเป็นนัด',
       '''<div class="grid c2 rv">
    <div class="card spot"><div class="ct">อย่าตอบหมดในแชท</div><div class="cd">ให้ข้อมูลพอให้อยากเจอ ไม่ใช่ให้จนไม่ต้องเจอ</div></div>
    <div class="card spot"><div class="ct">อย่ายิงราคา</div><div class="cd">ลูกค้าเอาไปเทียบเจ้าอื่นแล้วเงียบ</div></div>
  </div>''',
       '"ขอบคุณที่สนใจนะครับ เรื่องนี้มีรายละเอียดที่ต้องปรับตามข้อมูลพี่ ขอนัดคุยสั้นๆ 20 นาที จะตอบได้ตรงกว่าครับ พุธบ่ายหรือศุกร์เช้าดีครับ"'))
# 12 · S09 channel 4
S(chan(4, 'Promotion ลูกค้าใหม่', 'ข้อมูลน้อยกว่า 3 ช่องแรก ต้องสร้างความสัมพันธ์จากศูนย์',
       pts(['เข้าถึงผ่าน Promotion / แคมเปญ (event, ออกบูธ, แนะนำต่อ, ยิงแอด)',
            'Promotion เป็นแค่ประตู ต้องรีบสร้าง trust + หา Need จริงหลังได้นัด']),
       '"ตอนนี้มีแคมเปญตรวจสุขภาพการเงินฟรีด้วย uKnow ใช้เวลาไม่กี่นาที ได้เห็นภาพความคุ้มครองของตัวเอง สนใจลองไหมครับ"'))
# 13 · S10 channel 5 (R1: stat number dropped, Editor PASS wording)
S(chan(5, 'Knock Door', 'ข้อมูลน้อยสุด ถูกปฏิเสธสูงสุด',
       pts(['มักต้องเจอคำปฏิเสธหลายครั้ง กว่าจะได้นัด 1 ครั้ง',
            'ต้องอาศัยจำนวน (volume) + ใจสู้ + ไม่เอาการถูกปฏิเสธมาเป็นเรื่องส่วนตัว',
            'ทัศนคติ: ทุก no คือทางผ่าน ทุก no ทำให้เข้าใกล้ yes ขึ้น',
            'เหมาะเป็นสนามฝึกใจ + ฝึกบทเปิด แต่ไม่ควรเป็นช่องทางหลักถ้ามีช่องทางที่ข้อมูลเยอะกว่า'])))
# 14 · S10 question
S(q('ถ้าโดนปฏิเสธ <span class="r">9 ครั้งติด</span><br>คุณจะบอกตัวเองว่าอะไร?', '💬 เขียนขึ้นกระดาน คนละ 1 ประโยค'))

# 15 · S11 notes (white, 1536 grid)
S('''<section class="slide part notes">
  <div class="kick rv">จดโน้ต</div>
  <h2 class="rv">แก่นที่ได้</h2>
  <ul class="pts rv"><li>เลือกช่องทางตามข้อมูลที่มี ยิ่งข้อมูลเยอะ นัดยิ่งง่าย</li><li>Knock Door ไว้ฝึกใจ ไม่ใช่ช่องทางหลัก</li></ul>
  <div class="nls rv">
    <div class="nl"><span>📝 ช่องทางที่ผมใช้บ่อยที่สุดตอนนี้:</span><i></i></div>
    <div class="nl"><span>📝 ช่องทางที่ควรลองเพิ่ม:</span><i></i></div>
  </div>
</section>''')

# 16 · S12 class core: 3 keys (white editorial)
S('''<section class="slide part ed">
  <div class="kick rv">หัวใจของคลาส</div>
  <h2 class="rv">การทำนัดหมาย</h2>
  <div class="skew rv"></div>
  <div class="intro rv">เป้าของการติดต่อ = ได้นัดเจอ ไม่ใช่ขายจบในสาย/แชท</div>
  <div class="grid c3 rv">
    <div class="card spot"><div class="n">1</div><div class="ct">เหตุผล</div><div class="cd">ลูกค้าได้ประโยชน์อะไร</div></div>
    <div class="card spot"><div class="n">2</div><div class="ct">ทางเลือกเวลา</div><div class="cd">เสนอ 2 ช่อง</div></div>
    <div class="card spot"><div class="n">3</div><div class="ct">สั้น มั่นใจ</div><div class="cd">ขอ 20 นาที ไม่ต้องตัดสินใจ</div></div>
  </div>
  <div class="foot rv">ยิ่งพูดเยอะในการติดต่อครั้งแรก ยิ่งถูกปฏิเสธ</div>
</section>''')
# 17 · S12 question
S(q('โทรนัดลูกค้า แล้วเขาถามรายละเอียดเยอะ<br><span class="r">คุณจะตอบหรือเลี่ยง?</span>', '💬 ชวนคิด', bg_name='coach'))

# 18 · S13 phone: 5 steps + 2 scripts
S(f'''<section class="slide dots">
  <div class="kick rv">การทำนัด</div>
  <h2 class="rv">ทางโทรศัพท์</h2>
  {hstep(['ทักทาย + แนะนำตัวสั้น', 'เหตุผลที่โทร (อิงข้อมูล)', 'ขอเวลา "20 นาที"', 'เสนอเวลา 2 ช่อง', 'ยืนยัน + ทวนวันเวลา'])}
  <div class="grid c2 rv">
    <div class="thread"><div class="lbl">บทโทร: คนรู้จัก</div><div class="bub me">"สวัสดีครับพี่ ผมเอ (ตัวแทน AIA) พอดีช่วงนี้ผมทำเรื่องวางแผนคุ้มครองสุขภาพ นึกถึงพี่เลยครับ ขอเวลาสั้นๆ 20 นาที ไปเล่าให้ฟัง ไม่ต้องตัดสินใจอะไร พุธบ่ายหรือศุกร์เช้าสะดวกกว่ากันครับ"</div></div>
    <div class="thread"><div class="lbl">บทโทร: ลูกค้าเก่า + โปร</div><div class="bub me">"สวัสดีครับพี่ ช่วงนี้มีโปรสำหรับลูกค้าเดิมพอดี ผมดูแล้วแผนพี่ยังไม่มีส่วนชดเชยรายวัน เลยอยากเล่าให้ฟัง ขอ 20 นาที พฤหัสหรือเสาร์ดีครับ"</div></div>
  </div>
</section>''')

# 19 · S14 chat: rules + 3-part script sent one bubble per tap + iCheck invite + exercise line
S('''<section class="slide dots chat14 scroll">
  <div class="kick rv">การทำนัด</div>
  <h2 class="rv">ทางข้อความ (แชท)</h2>
  <div class="c14 rv">
    <div class="rules">
      <div class="card"><div class="ct">ส่งทีละท่อน</div><div class="cd">ห้ามยิงยาวรวดเดียว ให้ลูกค้าตอบโต้</div></div>
      <div class="card"><div class="ct">ห้ามยิงราคาก่อนนัด</div><div class="cd">ลูกค้าเอาไปเทียบแล้วเงียบ</div></div>
    </div>
    <div class="thread">
      <div class="lbl">บทแชท 3 ท่อน</div>
      <div class="bub me stp">"ขอบคุณที่สนใจนะคะ 🙏 เรื่องนี้มีรายละเอียดที่ต้องปรับตามอายุและความต้องการของพี่ค่ะ"</div>
      <div class="bub me stp">"หนูขอชวนคุยสั้นๆ สัก 20 นาที จะแนะนำได้ตรงกว่าตอบในแชทค่ะ"</div>
      <div class="bub me stp">"พี่สะดวกพุธบ่าย หรือ ศุกร์เช้า ดีคะ"</div>
      <div class="stp inv"><div class="lbl">ชวนทำ uKnow (เดิมชื่อ iCheck) ก่อนนัด</div><div class="bub me">"ก่อนเจอกัน ลองทำ uKnow ดูไหมคะ ใช้เวลาไม่กี่นาที จะได้เห็นภาพความคุ้มครองของตัวเองก่อน แล้วเราค่อยคุยจากผลจริงค่ะ"</div></div>
    </div>
    <div class="ex"><span>📝 เขียนบทแชทของคุณเอง 1 เวอร์ชัน (แบ่ง 3 ท่อน):</span><i></i></div>
  </div>
</section>''')

# 20 · S15 objection table (semantic table; chat pairs at 390)
rows = [('ยุ่ง ไม่มีเวลา', 'เข้าใจครับ เลยขอแค่ 20 นาที เลือกวันที่พี่สบายใจสุด'),
        ('ส่งมาทางไลน์ได้ไหม', 'ได้ครับ แต่บางส่วนต้องปรับตามข้อมูลพี่ เจอกันสั้นๆ จะตรงกว่า'),
        ('มีอยู่แล้ว', 'ดีเลยครับ ผมช่วยดูให้ว่าที่มีครอบคลุมพอไหม ใช้ uKnow เช็คสั้นๆ ได้'),
        ('ไม่สนใจ', 'ไม่เป็นไรครับ ขอเก็บชื่อไว้ ถ้ามีข้อมูลที่เป็นประโยชน์จะส่งให้')]
tr = ''.join(f'<tr><td class="c">{a}</td><td class="gap"></td><td class="a">{b}</td></tr>' for a, b in rows)
S(f'''<section class="slide dots scroll">
  <div class="kick rv">การทำนัด</div>
  <h2 class="rv">รับมือคำปฏิเสธ</h2>
  <table class="obj rv"><thead><tr><th scope="col">ลูกค้าพูด</th><th></th><th scope="col">เราตอบ</th></tr></thead><tbody>{tr}</tbody></table>
</section>''')
# 21 · S15 question
S(q('<span class="r">คำปฏิเสธไหนที่คุณกลัวที่สุด</span><br>และจริงๆ มันแปลว่าอะไร?', '💬 ช่วยกันแปลความ "ไม่" ของลูกค้า'))

# 22 · S16 on site (white editorial)
S(f'''<section class="slide part ed">
  <div class="kick rv">หน้างาน</div>
  <h2 class="rv">ได้นัดแล้ว ยังต้องทำกระบวนการขาย</h2>
  <div class="skew rv"></div>
  <div class="intro rv">Product Approach ไม่ได้ข้ามกระบวนการขาย แค่ทำให้เริ่มต้นได้เร็วขึ้น</div>
  {flow(['เปิดใจ', 'สร้างปัญหา', 'เสนอ', 'ปิดการขาย'])}
  <div class="foot rv">สินค้าที่ใช้เปิดอาจไม่ใช่สินค้าที่ปิด</div>
  <div class="sub rv">ขึ้นกับสิ่งที่เจอตอนทำกระบวนการ (เชื่อม T.3)</div>
</section>''')

# 23-25 · S17-S19 uKnow screenshots (F7 wording pending writer; S17 name/scoring line pending writer from fe 11:16 fact)
S(shot_slide('s17', 'หน้าคำถามของ uKnow: อายุเท่าไหร่แล้วครับ', 'uKnow ตอน 1', 'uKnow คืออะไร', f'''<div class="cd rv">เครื่องมือประเมินความคุ้มครองจากคำถามง่ายๆ</div>
      <ul class="pts rv"><li><b>uKnow · รู้จักความคุ้มครอง</b></li><li>เข้า iKYS → uKnow</li><li>เบื้องหลังคะแนน (เต็ม 100): ความคุ้มครอง 40 · ภาษี 20 · สำรอง (หนี้และการออม) 15 · เกษียณ 15 · CRP (ประสบการณ์และความสนใจการลงทุน) 10</li></ul>
      <div class="foot rv">ลูกค้า เห็นตัวเลขของตัวเอง แทนการฟังตัวแทนพูดฝ่ายเดียว = เชื่อและเปิดใจง่ายขึ้น</div>'''))
S(shot_slide('s18', 'ผลวิเคราะห์ของ uKnow: ช่องว่างความคุ้มครอง', 'uKnow ตอน 2', 'ผลลัพธ์ที่ลูกค้าเห็น', f'''<div class="cd rv">คะแนนรวม → ค่ารักษาจริง → ช่องว่างความคุ้มครอง → แผนเติมเต็ม</div>
      <div class="foot rv">จุดที่ลูกค้าอึ้ง: เห็นว่าความคุ้มครองที่มีอยู่ยังไม่พอ<br><span class="r">ขาดอีก 96% ของที่ควรมี</span> (ตัวอย่าง: ชาย 30 ปี รายได้ 96,700 บาท/เดือน) = เห็นช่องว่างชัดด้วยตัวเลข</div>'''))
S(shot_slide('s19', 'ผลวิเคราะห์ของ uKnow: เติมเต็มตรงจุดที่ขาด', 'uKnow ตอน 3', 'ช่องว่างที่ควรเติม', f'''<div class="cd rv">ตัวอย่างเดียวกัน: มีอยู่ 1.0M ต้องการ 25.3M ต้องเพิ่มอีก 24.3M</div>
      <div class="foot rv">uKnow เปลี่ยน "ช่องว่าง" ให้เป็น "สิ่งที่ต้องเติม" ด้วยตัวเลข = สร้างปัญหาให้ลูกค้าเห็นเอง ไม่ต้องขู่</div>'''))
# 26 · S19 question
S(q('ทำไมลูกค้าเชื่อตัวเลขจาก uKnow<br><span class="r">มากกว่าคำพูดของตัวแทน?</span>', '💬 ช่วยกันตอบ'))

# 27 · S20 create the problem
S('''<section class="slide dots ans">
  <div class="kick rv">หน้างาน</div>
  <h2 class="rv">สร้างปัญหา</h2>
  <div class="intro rv">ให้ลูกค้าเห็น <span class="r">ขนาดของความเสี่ยง</span> จริง</div>
  <div class="grid c2 rv">
    <div class="card spot"><div class="ct">ใช้คำถาม</div><div class="cq">"ถ้าต้องหยุดทำงาน 6 เดือน ครอบครัวจะเป็นยังไง"</div><div class="cd dim">ให้ลูกค้าคิดเอง ไม่ขู่</div></div>
    <div class="card spot"><div class="ct">ใช้ uKnow</div><div class="cd">ช่องว่างที่เห็นเป็นตัวเลข = ปัญหาที่จับต้องได้</div></div>
  </div>
  <div class="foot rv">ต่อยอด T.2 จุดขาย AIA</div>
</section>''')
# 28 · S20 question
S(q('ถ้าลูกค้าบอก "ผมรู้นะว่ามันสำคัญ แต่ยังไม่พร้อม"<br><span class="r">คุณจะสร้างปัญหาอย่างไรโดยไม่กดดัน?</span>', '💬 ช่วยกันตอบ', bg_name='listen'))

# 29 · S21 propose
S(f'''<section class="slide dots">
  <div class="kick rv">หน้างาน</div>
  <h2 class="rv">เสนอ</h2>
  <div class="intro rv">เสนอสินค้าที่ตอบช่องว่างจาก uKnow เลือก 1-2 แบบที่ใช่</div>
  {flow(['ช่องว่างที่เห็น', 'ผลถ้าไม่เติม', 'แผนที่ตอบ', 'เบี้ย/ตัวเลข', 'ปิด'])}
  <div class="foot rv">สินค้าที่เสนอ อาจไม่ใช่สินค้าที่ใช้เปิดนัด</div>
  <div class="sub rv">เช่น เปิดด้วยสุขภาพ แต่ uKnow ชี้ว่าช่องว่างใหญ่สุดคือคุ้มครองชีวิต</div>
</section>''')

# 30 · S22 close
S('''<section class="slide dots ans">
  <div class="kick rv">หน้างาน</div>
  <h2 class="rv">ปิดการขาย</h2>
  <div class="grid c3 rv">
    <div class="card spot"><div class="ct">ปิดเมื่อพร้อม</div><div class="cd">ลูกค้าเห็นภาพ + ยอมรับปัญหา + เห็นว่าแผนตอบโจทย์</div></div>
    <div class="card spot"><div class="ct">ให้เลือก A หรือ B</div><div class="cd">แทนถามว่า "เอาไหม" ใช้ "แผน A หรือ B ตรงกับพี่มากกว่ากัน"</div></div>
    <div class="card spot"><div class="ct">ไม่ปิดวันนี้?</div><div class="cd">ต้องได้ next step ชัด (นัดตามผล, นัดส่งเอกสาร)</div></div>
  </div>
  <div class="foot rv">ปิดด้วยความจริงใจ ไม่กดดัน รักษาคำมั่นสัญญาที่ให้ไว้ (T.2)</div>
  <div class="vs rv"><div class="row">📝 Product Approach เปิดประตูได้เร็ว แต่ปิดการขายด้วยกระบวนการที่ถูกต้องเสมอ</div></div>
</section>''')

# 31 · S23 two routes (26826 comparison, no "recommended"; R4: route A = categories, IC/UL line = aia file text, fasai PASS)
S('''<section class="slide dots ans routes">
  <div class="kick rv">2 เส้นทางเข้า</div>
  <h2 class="rv">ประกัน หรือ Investment</h2>
  <div class="grid c2 rv">
    <div class="card spot"><div class="ct">เส้นทาง A: ประกัน</div><div class="cd">Need คุ้มครอง/ออม: สุขภาพ, ชีวิต, สะสมทรัพย์, บำนาญ</div></div>
    <div class="card spot"><div class="ct">เส้นทาง B: การลงทุน (IC)</div><div class="cd">Need ลงทุน/เกษียณ: เข้าผ่านมุมการเงินก่อน ต่อยอดสู่คุ้มครอง</div>
      <div class="cd dim">การแนะนำและขาย Unit Linked ต้องมี ใบอนุญาตตัวแทนประกันชีวิต และ ใบอนุญาตผู้แนะนำการลงทุน (IC License) จาก ก.ล.ต. และขึ้นทะเบียนเป็นตัวแทนขาย Unit Linked กับ คปภ.</div></div>
  </div>
  <div class="foot rv">ทั้ง 2 เส้นทางเป็นแค่ประตู ปลายทางเดียวกัน = แผนที่ตอบชีวิตลูกค้า</div>
</section>''')
# 32 · S23 question
S(q('ลูกค้าคนเดียวกัน<br>เข้าด้วยประกัน กับเข้าด้วยการลงทุน<br><span class="r">ต่างกันไหม?</span>', '💬 เลือกประตูที่ลูกค้าเปิดใจที่สุด'))

# 33 · S24 summary: 7 pills light up in order (single focal animation), then the 2 closing lines
S(f'''<section class="slide dots">
  <div class="kick rv">สรุป</div>
  <h2 class="rv">Product Approach ทั้งกระบวน</h2>
  {flow(['ข้อมูล/โอกาส', 'เลือกสินค้าเปิด', 'ทำนัด', 'เปิดใจ+uKnow', 'สร้างปัญหา', 'เสนอ', 'ปิด'], lite=True)}
  <div class="foot rv late">เร็วที่ทางเข้า ครบที่กระบวนการ</div>
  <div class="sub rv late">ยึดประโยชน์ลูกค้าตลอด</div>
</section>''')

# 34 · S25 Q&A (already a question-only slide)
S(q('<span class="r">โยนเคสลูกค้าจริงที่ยังปิดไม่ได้</span>', '💬 ยกเคสคนละ 1 เรื่อง',
    pre='<div class="qa-top rv"><b>Q&amp;A</b> · ถาม-ตอบ สถานการณ์จริง</div>\n  ',
    after='').replace('<div class="prompt rv">', '<div class="sub rv">ช่วยกันวิเคราะห์ว่าควรเข้าช่องทางไหน เปิดด้วยสินค้าอะไร</div>\n  <div class="prompt rv">', 1))

# 35 · S26 workshop (white editorial, 6-step stepper)
S(f'''<section class="slide part ed">
  <div class="kick rv">Workshop</div>
  <h2 class="rv">Product Approach 1 รอบเต็ม</h2>
  <div class="skew rv"></div>
  <div class="intro rv">Role-play จับคู่</div>
  {hstep(['เลือกช่องทาง (1 ใน 5) + สินค้าที่ใช้เปิดตามข้อมูลที่มี', 'เขียน + เล่นบทนัด (โทร หรือ แชท)', 'เปิดใจ + ทำ uKnow ให้ลูกค้าเห็นช่องว่าง',
          'สร้างปัญหา + เสนอ 1-2 แบบ (อาจต่างจากสินค้าเปิด)', 'ปิด หรือ นัด next step', 'นำเสนอหน้าห้อง 3 นาที รับ feedback'])}
</section>''')

# 36 · S27 assessment
S('''<section class="slide dots ans">
  <div class="kick rv">Workshop</div>
  <h2 class="rv">เกณฑ์ประเมิน</h2>
  <div class="grid c4 rv">
    <div class="card spot"><div class="n">1</div><div class="ct">เลือกช่องทาง</div><div class="cd">ตามข้อมูล</div></div>
    <div class="card spot"><div class="n">2</div><div class="ct">นัดได้จริง</div></div>
    <div class="card spot"><div class="n">3</div><div class="ct">กระบวนการ</div><div class="cd">ขายครบ</div></div>
    <div class="card spot"><div class="n">4</div><div class="ct">ยึดประโยชน์</div><div class="cd">ลูกค้า (T.1)</div></div>
  </div>
</section>''')

# 37 · S28 closing quote (the only gold)
S('''<section class="slide img quote" data-bg="leader">
  <div class="bar gbar rv"></div>
  <div class="one rv" data-read>"Product Approach ที่ดี<br>ไม่ใช่การขายสินค้าที่เราถือมา<br><span class="gold">แต่คือการใช้สินค้านั้นเปิดประตู</span><br>แล้วมอบแผนที่ลูกค้าต้องการจริงๆ ให้เขา"</div>
  <div class="tag rv">จริงใจ · ลงมือ · อยู่ด้วยกัน • iAgencyAIA</div>
</section>''')

T4CSS = '''
/* T4-only layout */
.q .card.qa{max-width:900px;background:rgba(38,38,44,.85);border-color:rgba(232,153,141,.45)}
.q .card.qa .ct{color:var(--salmon)}
.qa-top{color:var(--muted);font-weight:700}.qa-top b{color:var(--salmon);letter-spacing:.12em}
.vs .row s{text-decoration-color:var(--red);text-decoration-thickness:3px;color:var(--muted)}
.c14{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);grid-template-areas:"r t" "e t";gap:.6em clamp(14px,2.4vw,36px);width:100%;align-items:start}
.c14 .rules{grid-area:r;display:flex;flex-direction:column;gap:.5em}.c14 .thread{grid-area:t}.c14 .ex{grid-area:e}
.c14 .inv{display:flex;flex-direction:column;gap:.3em;margin-top:.3em}.c14 .inv .bub{align-self:flex-end}
.ex{display:flex;flex-direction:column;gap:.4em;font-weight:700}.ex i{display:block;height:2.2em;border-bottom:2px dashed rgba(255,255,255,.3)}
.on .late.rv{animation-delay:2.9s} /* S24: the 2 closing lines blur-in after the 7 pills */
.quote .one{max-width:26ch}
@media (max-width:680px){.c14{grid-template-columns:1fr;grid-template-areas:"r" "t" "e"}}
'''

CSS = open(os.path.join(SERIES, 'deck.css'), encoding='utf-8').read() + T4CSS
JS = open(os.path.join(SERIES, 'deck.js'), encoding='utf-8').read()
BGS = {k: bg(k) for k in ['cover', 'group', 'coach', 'listen', 'leader']}
bgcss = '\n'.join(f'.slide[data-bg="{k}"]{{--bg:{v}}}' for k, v in BGS.items())

html = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>iTraining T.4/6 · Product Approach</title>
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
assert '—' not in html and '–' not in html, 'em/en dash found'
assert 'รอยืนยัน' not in html, 'placeholder bracket found'
assert len(SLIDES) == 37, len(SLIDES)
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html), 'bytes,', len(SLIDES), 'slides,', html.count('data-pending='), 'pending')
