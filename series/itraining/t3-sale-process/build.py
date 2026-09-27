#!/usr/bin/env python3
"""T2249 · iTraining T3/6 Sale Process & MANHA builder (fe, on the T2194/T2229 series template).
Text source = Writer-Oracle output/t2249-inventory/T2249-T3-sales-process-inventory.md (28 slides / 257 lines),
verbatim, with the recorded rulings applied (highest R wins: R3 3ca751f > R2 > R1; S3 80/20 kept). rulings.json = make_rulings.py.
Layout = Designer-Oracle output/t2249-t3-sale-process/ART-DIRECTION.md: 28 slides kept (the 5 STOP & THINK cases are already
question -> solution), the MANHA row of S5 reused as a mini strip on S12-S20 with the case letter lit, one close (S28).
"""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.join(HERE, '..')
BG_DIR = os.path.join(SERIES, 't1-mindset', 'img')  # series backgrounds, shared with T1/T4
OUT = os.path.join(HERE, '..', '..', '..', 'output', 'itraining-t3-sale-process.html')

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def bg(name):
    return "url('data:image/webp;base64," + b64(os.path.join(BG_DIR, f'bg-{name}.webp')) + "')"

# ---------- F8 (writer R3 3ca751f): spaced hyphen -> ·
F8_S1 = '(คลาส 2 ชั่วโมง · Interactive Session)'
F8_S9 = 'อย่าเถียงลูกค้า ให้คล้อยตามก่อนแล้วค่อยดึงกลับ (Feel · Felt · Found)'

# ---------- components ----------
MANHA = [('M', 'Money', 'มีกำลังจ่ายเบี้ย โดยไม่เดือดร้อน'), ('A', 'Authority', 'มีอำนาจตัดสินใจ ด้วยตัวเอง'),
         ('N', 'Need', 'เห็นความจำเป็น ของปัญหา'), ('H', 'Health', 'สุขภาพอยู่ในเกณฑ์ รับพิจารณา'),
         ('A', 'Age', 'อายุอยู่ในช่วง ที่รองรับเงื่อนไข')]
FORM = [('F', 'Family', 'ครอบครัว ลูก พ่อแม่ ความรับผิดชอบในบ้าน'), ('O', 'Occupation', 'อาชีพ ธุรกิจ การงาน ความก้าวหน้า'),
        ('R', 'Recreation', 'งานอดิเรก สิ่งที่สนใจ กีฬา การใช้เวลาว่าง'), ('M', 'Message', 'โยงเรื่องทั้งหมดเข้าสู่เป้าหมายหรือปัญหา')]

def letters(items):
    """S5/S6 framework row: letter huge red, English, Thai line (1 col at 390, letter as a chip)"""
    li = ''.join(f'<li style="--ci:{k}"><span class="lt">{a}</span><b>{e}</b><span>{t}</span></li>' for k, (a, e, t) in enumerate(items))
    return f'<ol class="letters rv" style="--n:{len(items)}">{li}</ol>'

def strip(lit):
    """mini MANHA strip, the case's letters lit (by index: 0 M, 1 A Authority, 2 N, 3 H, 4 A Age)"""
    return '<div class="mstrip rv" aria-hidden="true">' + ''.join(
        f'<span class="{"lit" if k in lit else ""}">{a}</span>' for k, (a, _, _) in enumerate(MANHA)) + '</div>'

def case_q(n, situation, quote, ask):
    return f'''<section class="slide {'img' if n == 1 else 'dots'} q case"{' data-bg="listen"' if n == 1 else ''}>
  <div class="kick rv">🛑 STOP &amp; THINK (Case {n})</div>
  <div class="sit rv">{situation}</div>
  <div class="thread rv"><div class="bub them hero">{quote}</div></div>
  <div class="prompt rv">💬 {ask}</div>
</section>'''

def case_a(title, sub, lit, prevent_lbl, prevent_lines, fix_lbl, fix_lines):
    def col(lbl, lines):
        body = ''.join(lines)
        return f'<div class="col"><div class="ct">{lbl}</div>{body}</div>'
    return f'''<section class="slide dots sol">
  <div class="solhead"><div><div class="kick rv">REAL CASE SOLUTION</div>
  <h2 class="rv">{title}</h2></div>{strip(lit)}</div>
  <div class="sub rv">{sub}</div>
  <div class="cols rv">{col(prevent_lbl, prevent_lines)}{col(fix_lbl, fix_lines)}</div>
</section>'''

def ln(t):
    return f'<div class="cd">{t}</div>'

def say(t):
    return f'<div class="bub me">{t}</div>'

def aside(t):
    return f'<div class="cd dim">{t}</div>'

SLIDES = []
S = SLIDES.append

# 01 · cover (series title + source title as subtitle; ✦ decorative, dropped, F9)
S(f'''<section class="slide img cover" data-bg="cover">
  <div class="kick rv">iTRAINING · T.3/6</div>
  <h1 class="rv"><span class="aurora">Sale Process &amp; MANHA</span></h1>
  <div class="bar rv"></div>
  <div class="lead rv">กระบวนการขาย<br>&amp; วิเคราะห์ลูกค้า</div>
  <div class="sub rv">Framework สำหรับตัวแทนมืออาชีพ</div>
  <div class="sub rv">ทำงานอย่างเป็นระบบ และปิดการขายได้จริง</div>
  <div class="sub rv">{F8_S1}</div>
  <div class="hint rv">แตะ · ปัด · หรือกด → เพื่อเริ่ม</div>
</section>''')

# 02 · series map (T.3 lit) + agenda, 6 rows of 2 lines
smap = [('T.1 Mindset', ''), ('T.2 Sales Technique', ''), ('T.3 Sale Process &amp; MANHA', 'now'),
        ('T.4 Product Approach', ''), ('T.5 Need Approach', ''), ('T.6 iPoS+ & FA Tools', '')]
sm = ''.join(f'<li class="{c}"><b>{t}</b></li>' for t, c in smap)
ag = [('ปรับ Mindset &amp;', 'กฎเหล็กของนักขาย'), ('เจาะลึกเทคนิคเปิดใจ', 'และสังเกตภาษากาย'),
      ('การสร้างปัญหา &amp;', 'รับมือการบ่ายเบี่ยง'), ('Interactive Case Study:', 'ถอดรหัส MANHA<br>(5 เคสจริง)'),
      ('การวิเคราะห์เคสร่วมกับทีม', '(Framework บุคคลที่ 1)'), ('Workshop &amp;', 'Action Plan')]
li = ''.join(f'<li><span class="an">{k + 1}</span><span><b>{a}</b><br>{b}</span></li>' for k, (a, b) in enumerate(ag))
S(f'''<section class="slide dots">
  <ol class="smap sm-top rv">{sm}</ol>
  <div class="kick rv">AGENDA</div>
  <h2 class="rv">โครงสร้างเนื้อหา</h2>
  <ol class="agenda c2a rv">{li}</ol>
</section>''')

# 03 · iron rule + compare (R1: "พร้อมปิดการขาย")
S('''<section class="slide dots ans">
  <div class="kick rv">กฎเหล็กนักขายมืออาชีพ</div>
  <h2 class="rv"><span class="aurora">"MANHA ครบ เท่ากับ พร้อมปิดการขาย"</span></h2>
  <div class="grid c2 cmp rv">
    <div class="card dim"><div class="ct">❌ ยิ่งเสนอ = ยิ่งขายได้ช้า</div><div class="cd">รีบหยิบแบบมาเสนอตั้งแต่ 5 นาทีแรก ยัดเยียดโดยที่ลูกค้ายังไม่เห็นปัญหา มักนำไปสู่ข้อโต้แย้ง</div></div>
    <div class="card star"><div class="ct">✅ ยิ่งเปิดใจ = ขายได้เร็ว</div><div class="cd">ให้ลูกค้าพูด 80% เราพูด 20% หน้าที่ของเราคือ โยนคำถามเพื่อค้นหาความจริง ไม่ใช่ท่องสคริปต์ขาย!</div></div>
  </div>
</section>''')

# 04 · core process: 4 steps, rule pinned above
steps = [('เปิดใจ', '(Ice Breaking)', 'ถ้าเขาไม่ชอบและไม่เชื่อใจเรา เขาก็ยากที่จะฟังขั้นตอนต่อไป'),
         ('สร้างปัญหา', '(Fact Finding)', 'ค้นหาและทำให้ลูกค้าตระหนักถึงช่องโหว่ความเสี่ยงของตัวเอง'),
         ('เสนอ', '(Presentation)', 'นำเสนอเฉพาะทางออกที่แก้ปัญหาในข้อ 2 ได้ตรงจุดที่สุดเท่านั้น'),
         ('ปิดการขาย', '(Closing)', 'เมื่อทุกอย่างชัดเจน ต้องกล้าขอบัตรประชาชนเพื่อปิดจบ')]
li = ''.join(f'<li><span class="rn">{k + 1}</span><b>{a}</b><span class="en">{e}</span><span class="dl">{d}</span></li>' for k, (a, e, d) in enumerate(steps))
S(f'''<section class="slide dots">
  <div class="kick rv">The Core Process</div>
  <h2 class="rv">กระบวนการขาย 4 ขั้นตอน</h2>
  <div class="rule rv">"ห้ามสลับและห้ามข้ามขั้นตอนเด็ดขาด"</div>
  <ol class="hstep core rv" style="--n:4">{li}</ol>
</section>''')

# 05 · MANHA (the deck's anchor row)
S(f'''<section class="slide dots">
  <div class="kick rv">Analysis Framework</div>
  <h2 class="rv">M.A.N.H.A. <span class="sub2">เครื่องมือสแกนความพร้อม</span></h2>
  <div class="intro rv">ถ้าลูกค้าบอก "ขอคิดดูก่อน" มักแปลว่าเรายังตกหล่นตัวอักษรใดตัวอักษรหนึ่งไป</div>
  {letters(MANHA)}
</section>''')

# 06 · F.O.R.M. (same component, siblings)
S(f'''<section class="slide dots">
  <div class="kick rv">Step 1: การเปิดใจ</div>
  <h2 class="rv">เทคนิค F.O.R.M.</h2>
  <div class="intro rv">การเปิดใจไม่ใช่แค่คุยเล่นไปเรื่อยเปื่อย แต่คือการ "เก็บข้อมูลเงียบๆ"</div>
  {letters(FORM)}
</section>''')

# 07 · rapport: 2 principle cards
S('''<section class="slide dots ans">
  <div class="kick rv">Step 1: การเปิดใจ (ต่อ)</div>
  <h2 class="rv">เคล็ดลับซื้อใจลูกค้า</h2>
  <div class="grid c2 rv">
    <div class="card spot" style="--ci:0"><div class="ct">หาจุดร่วม (Common Ground)</div><div class="cd">คนเราจะชอบคนที่เหมือนกัน หรือมีความสนใจตรงกัน หาให้เจอเร็วที่สุด:</div>
      <ul class="pts"><li>ศิษย์เก่าสถาบันเดียวกัน</li><li>เลี้ยงสัตว์เหมือนกัน (สุนัข แมว)</li><li>ชอบเที่ยวสไตล์เดียวกัน หรือเชียร์กีฬาทีมเดียวกัน</li></ul></div>
    <div class="card spot" style="--ci:1"><div class="ct">ชื่นชมอย่างจริงใจ (Sincere Compliment)</div><div class="cd">ทุกคนชอบถูกชม แต่ต้อง "มาจากใจ เฟคไม่ได้":</div>
      <ul class="pts"><li>ชมสิ่งที่เขาตั้งใจทำ เช่น การตกแต่งบ้าน</li><li>ชมความใส่ใจที่เขามีต่อครอบครัว/ลูก</li><li>ชมความสำเร็จหรือความขยันในการทำงาน</li></ul></div>
  </div>
</section>''')

# 08 · body-language signals (stacked at 390, open first)
S('''<section class="slide dots ans sig">
  <div class="kick rv">Body Language Check</div>
  <h2 class="rv">ลูกค้า "เปิดใจ" หรือแค่ "เกรงใจ"?</h2>
  <div class="intro rv">การอ่านภาษากายก่อนข้ามไป Step 2 (สร้างปัญหา) สำคัญมาก</div>
  <div class="grid c2 rv">
    <div class="card go"><div class="ct">🟢 สัญญาณเปิดใจ (ไปต่อได้)</div><ul class="pts"><li>สบตาบ่อยขึ้น แววตาดูผ่อนคลาย</li><li>พยักหน้าตาม หรือเอนตัวเข้าหาเรา</li><li>เริ่มเล่าเรื่องส่วนตัวให้ฟัง</li><li>เริ่มถามคำถามกลับ (แสดงความสนใจ)</li></ul></div>
    <div class="card stop"><div class="ct">🔴 สัญญาณปิดใจ (หยุดขายทันที)</div><ul class="pts"><li>กอดอก นั่งพิงพนักแบบทิ้งตัว</li><li>มองนาฬิกา หรือหยิบมือถือมาดูบ่อยๆ</li><li>แววตาเหม่อลอย ไม่โฟกัส</li><li>ตอบสั้นๆ แบบตัดบท: "อืม", "ค่ะ", "ก็ดี"</li></ul></div>
  </div>
  <div class="foot rv">*หากเจอสัญญาณ "ปิดใจ" ห้ามเข้าเรื่องประกันเด็ดขาด ให้ถอยกลับไปชวนคุย F.O.R.M ใหม่</div>
</section>''')

# 09 · Feel-Felt-Found: customer bubble, then 3 agent bubbles one per tap, closing question last (R1 Found)
fff = [('Feel (เข้าใจความรู้สึก):', '"ผมเข้าใจเลยครับพี่..."'),
       ('Felt (คนอื่นก็รู้สึกแบบนี้):', '"ตอนแรกลูกค้าหลายคนของผมก็คิดแบบนี้เหมือนกันครับ..."'),
       ('Found (แต่สิ่งที่เราค้นพบคือ):', '"แต่พอเรามาลองกางตัวเลขเงินเฟ้อดู ถึงพบว่าถ้าเริ่มช้าไปแค่ 5 ปี ต้องเก็บเงินต่อเดือนมากกว่าที่คิดไว้เยอะเลยครับพี่..."')]
b = ''.join(f'<div class="stp tagb"><span class="tg">{t}</span> <div class="bub me">{x}</div></div>' for t, x in fff)
S(f'''<section class="slide dots fff">
  <div class="kick rv">Step 2: การสร้างปัญหา</div>
  <h2 class="rv">เมื่อลูกค้า "บ่ายเบี่ยง"</h2>
  <div class="intro rv">{F8_S9}</div>
  <div class="thread rv">
    <div class="bub them"><span class="lbl">ลูกค้า:</span> "เรื่องเกษียณพี่ว่ายังอีกไกล ค่อยคิดก็ได้"</div>
    {b}
    <div class="bub me stp">"พี่สะดวกให้ผมลองกดตัวเลขคร่าวๆ ให้ดูเป็นไอเดียไหมครับ?"</div>
  </div>
</section>''')

# 10 · part opener (white)
S('''<section class="slide part ed">
  <div class="kick rv">Interactive Session</div>
  <h2 class="rv">ถอดรหัส MANHA</h2>
  <div class="skew rv"></div>
  <div class="intro rv">ผ่าน 5 เคสจริง</div>
  <div class="sub rv">เตรียมจดโน้ต และร่วมตอบคำถามไปพร้อมกัน</div>
</section>''')

# 11-20 · 5 cases, question then solution
S(case_q(1, 'สถานการณ์: คุยมา 1 ชั่วโมง นำเสนอแผนอย่างดี ลูกค้าพยักหน้าเห็นด้วยทุกอย่าง แต่ตอนจบลูกค้าบอกว่า...',
         '"เดี๋ยวพี่ขอเอาไปคุยกับแฟนก่อนนะ"',
         'คำถามชวนคิด: เราพลาดตัวอักษรไหนใน MANHA? และเราจะป้องกันเหตุการณ์นี้ยังไงตั้งแต่ตอน "เปิดใจ"?'))
S(case_a('ทางแก้ปัญหาตัว "A" (Authority)', 'พลาดเรื่องอำนาจตัดสินใจ แก้ยากที่สุดเมื่อเสนอไปแล้ว', {1},
         'วิธีป้องกัน (ตอนเปิดใจ)', [ln('ตอนใช้ F.O.R.M ต้องถามอ้อมๆ ให้รู้ว่าใครคุมเงินในบ้าน เช่น:'),
                                    say('"ปกติเรื่องการเงินในบ้าน พี่ดูแลเองหรือต้องปรึกษาแฟนครับ?"'),
                                    aside('*ถ้าต้องใช้ 2 คนตัดสินใจ ต้องนัดเจอพร้อมกันเท่านั้น ห้ามฝากโบรชัวร์ไปให้เขาอธิบายกันเอง!')],
         'วิธีแก้หน้างาน (เมื่อพลาดไปแล้ว)', [ln('อย่าปล่อยให้ลูกค้าเอาแบบไปคุยเองเด็ดขาด ให้ใช้บทพูดนี้:'),
                                             say('"เข้าใจเลยครับพี่ เพื่อไม่ให้พี่เหนื่อยตอบคำถามแฟน วันเสาร์นี้ผมขออนุญาตเข้าไปอธิบายให้ฟังพร้อมกันเลยดีไหมครับ?"')]))
S(case_q(2, 'สถานการณ์: นำเสนอแผนสุขภาพเหมาจ่ายชุดใหญ่ ลูกค้าฟังจบแล้วตอบว่า...',
         '"เบี้ยแพงไป ตอนนี้ช็อต ยังไม่อยากเพิ่มภาระ"',
         'คำถามชวนคิด: ติดปัญหาตัว "M" ใช่หรือไม่? เราเสนอแพงไปจริงๆ หรือลูกค้าแค่ไม่เห็นความสำคัญ?'))
S(case_a('ทางแก้ปัญหาตัว "M" (Money)', 'ลูกค้าอาจจะไม่ได้ช็อต แค่รู้สึกว่า "ไม่คุ้มค่า" ที่จะจ่าย', {0},
         'วิธีป้องกัน (ตอนเปิดใจ)', [ln('เช็คกำลังทรัพย์และทัศนคติเรื่องเงินตั้งแต่แรก:'),
                                    say('"ปกติพี่แบ่งเงินออม หรือจัดสรรงบดูแลสุขภาพให้ครอบครัว ปีละประมาณเท่าไหร่ครับ?"'),
                                    aside('ถ้าเขามีงบในใจ เราจะได้จัด Proposal ไม่ให้เกินกำลัง')],
         'วิธีแก้หน้างาน (เมื่อพลาดไปแล้ว)', [ln('ถอยกลับมาตั้งหลัก เสนอทางเลือกที่สบายใจกว่า:'),
                                             say('"เข้าใจเลยครับพี่ งั้นถ้าผมปรับแผนให้เบาลง โดยเลือกคุ้มครองเรื่องที่สำคัญที่สุดก่อน พี่ว่าพอไหวไหมครับ?"')]))
S(case_q(3, 'สถานการณ์: เพิ่งเริ่มเข้าเรื่องประกัน ลูกค้ารีบเบรกทันทีว่า...',
         '"พี่มีประกันเยอะแล้ว / สวัสดิการที่ทำงานก็เบิกได้หมด"',
         'คำถามชวนคิด: ติดปัญหาตัว "N" (Need) เขาพูดความจริง หรือเป็นแค่ข้ออ้างปัดรำคาญ?'))
S(case_a('ทางแก้ปัญหาตัว "N" (Need)', 'ต้องชมก่อน แล้วค่อยเปิดแผล (สร้างปัญหา)', {2},
         'วิธีป้องกัน (สร้าง Need แบบเนียนๆ)', [ln('ชมก่อนเปิดแผล:'),
                                              say('"ดีเลยครับพี่ที่มีสวัสดิการพร้อม สมมติถ้าเราต้องพักรักษาตัวสัก 6 เดือน รายได้ส่วนอื่นของครอบครัวได้รับผลกระทบไหมครับ?"'),
                                              aside('(เพื่อชี้ให้เห็นว่าสวัสดิการส่วนใหญ่เน้นค่ารักษา ส่วนรายได้ที่หายไประหว่างพักรักษาอาจชดเชยได้ไม่ครบ)')],
         'วิธีแก้หน้างาน (ซื้อใจ)', [ln('เปลี่ยนจากคนขาย เป็นที่ปรึกษา:'),
                                    say('"พี่ไม่ต้องซื้อเพิ่มเลยครับ แต่วันนี้ผมขออนุญาตทำสรุปกรมธรรม์ที่มีอยู่ทั้งหมดให้ฟรี เผื่อวันไหนฉุกเฉิน แฟนพี่จะได้หยิบใช้ถูกเล่มครับ"')]))
S(case_q(4, 'สถานการณ์: คุยมา 2 ชั่วโมง ลูกค้าพร้อมโอนเงิน แต่จู่ๆ ก็หลุดปากว่า...',
         '"พี่เพิ่งผ่าตัดเนื้องอกมาเมื่อต้นปี ซื้อได้ไหมน้อง?"',
         'คำถามชวนคิด: เราพลาดอะไร ทำไมเพิ่งมารู้ปัญหาตัว "H" (Health) ในตอนจบ?'))
S(case_a('ทางแก้ปัญหาตัว "H" (Health)', 'ต้องกรองปัญหาสุขภาพให้เจอ ก่อนเสียเวลาทำ Proposal ฟรีๆ', {3},
         'วิธีป้องกัน (ตอนเปิดใจ)', [ln('โยนคำถามเช็คสุขภาพเนียนๆ:'),
                                    say('"ช่วง 1-2 ปีนี้ พี่ได้เข้าโรงพยาบาลหรือตรวจสุขภาพประจำปีบ้างไหมครับ ผลปกติดีไหม?"')],
         'วิธีแก้หน้างาน (ตอบตรงๆ)', [ln('ห้ามรับปากส่งเดช ให้บริหารความคาดหวัง:'),
                                     say('"เคสนี้อาจจะต้องแนบประวัติให้บริษัทพิจารณาก่อนครับ พี่โอเคไหมถ้าเราลองยื่นดูก่อน ได้หรือไม่ได้ยังไงผมตามเรื่องให้เต็มที่ครับ"')]))
S(case_q(5, 'สถานการณ์: ลูกค้าฟังจนจบ ไม่มีข้อโต้แย้งอะไรเลย แต่บอกว่า...',
         '"โอเคเลยน้อง... แต่พี่ขอคิดดูก่อนนะ"',
         'คำถามชวนคิด: เขาขอคิดดูก่อนจริงๆ หรือเราทำ MANHA หล่นหายไปข้อไหน?'))
S(f'''<section class="slide dots sol single">
  <div class="solhead"><div><div class="kick rv">REAL CASE SOLUTION</div>
  <h2 class="rv">รับมือคำว่า "ขอคิดดูก่อน"</h2></div>{strip({0, 1, 2})}</div>
  <div class="sub rv">คำว่าขอคิดดูก่อน มักเป็นฉากบังหน้าของข้อโต้แย้งที่แท้จริง (M, A, หรือ N)</div>
  <div class="col rv">
    <div class="ct sal">ห้ามปล่อยให้กลับไปคิดเงียบๆ เด็ดขาด!</div>
    <div class="cd">ให้ใช้ความ "จริงใจ" ถามเจาะลึกลงไปว่าปัญหาที่แท้จริงคืออะไร:</div>
    {say('"ผมเข้าใจครับว่าเรื่องนี้ต้องใช้เวลาตัดสินใจ ไม่แน่ใจว่าส่วนที่พี่กังวลอยู่ เป็นเรื่องงบประมาณ หรือเรื่องความคุ้มครองครับ เผื่อผมช่วยปรับให้พอดีได้?"')}
    {aside('(การถามแบบนี้ ช่วยให้ลูกค้าเล่าปัญหาที่แท้จริงออกมา เช่น "พอดีเงินช็อต" หรือ "ต้องถามแฟน")')}
  </div>
</section>''')

# 21 · part opener (white)
S('''<section class="slide part ed">
  <div class="kick rv">Professional Standard</div>
  <h2 class="rv">ยกระดับสู่กระบวนการที่ปรึกษาการเงิน</h2>
  <div class="skew rv"></div>
</section>''')

# 22 · 4 sales steps -> 6 planning steps (R2 heading); grouping shown as the source pairs them (2+3, 5+6)
pills = ''.join(f'<span class="chip">{t}</span>' for t in ['1.เปิดใจ', '2.สร้างปัญหา', '3.เสนอ', '4.ปิดการขาย'])
six = ['ขั้นที่ 1: สร้างความสัมพันธ์ และกำหนดขอบเขต', 'ขั้นที่ 2: รวบรวมข้อมูล', 'ขั้นที่ 3: วิเคราะห์ข้อมูลและประเมินสถานะ (Gap)',
       'ขั้นที่ 4: จัดทำและนำเสนอแผนการเงิน', 'ขั้นที่ 5: นำแผนไปปฏิบัติ (Sign)', 'ขั้นที่ 6: ทบทวนแผน (บริการหลังการขาย)']
li = ''.join(f'<li><span class="rn">{k + 1}</span><span>{t}</span></li>' for k, t in enumerate(six))
S(f'''<section class="slide dots map46">
  <div class="kick rv">จากการขาย สู่การวางแผนการเงิน</div>
  <h2 class="rv">การขาย 4 ขั้นตอนของเรา แท้จริงแล้วคือกระบวนการวางแผนการเงิน 6 ขั้นตอน</h2>
  <div class="m46 rv"><div class="chips four">{pills}</div><ol class="vstep six">{li}</ol></div>
</section>''')

# 23 · bias vs team (team recommended)
S('''<section class="slide dots ans">
  <div class="kick rv">Team Synergy</div>
  <h2 class="rv">ทำไมต้องวิเคราะห์เคสกับ "ทีม"?</h2>
  <div class="intro rv">อย่าแบกปัญหาไว้คนเดียว เพราะคนนอกมักมองเห็นจุดบอดได้ชัดเจนกว่า</div>
  <div class="grid c2 cmp rv">
    <div class="card dim"><div class="ct">จุดบอดของตัวแทน (Bias)</div><ul class="pts"><li>เกรงใจลูกค้ามากเกินไป ไม่กล้าถามตรงๆ</li><li>คิดเข้าข้างตัวเองว่าลูกค้าชอบแบบประกันแล้ว</li><li>ด่วนสรุปไปเองว่าลูกค้าไม่มีเงิน (ทั้งที่จริงๆ เขาแค่ไม่เห็นความสำคัญ)</li></ul></div>
    <div class="card star"><div class="ct">พลังของทีม</div><ul class="pts"><li>ช่วยถอดรหัสความจริงที่ซ่อนอยู่หลังคำว่า "ขอคิดดูก่อน"</li><li>แชร์ประสบการณ์จากเคสที่คล้ายกัน</li><li>ช่วยกันสแกน MANHA ว่าตกหล่นจุดไหนไป</li></ul></div>
  </div>
</section>''')

# 24 · 3rd vs 1st person
S('''<section class="slide dots ans">
  <div class="kick rv">Case Storytelling</div>
  <h2 class="rv">กฎการเล่าเคส: "ต้องเล่าแบบบุคคลที่ 1"</h2>
  <div class="intro rv">การเล่าแบบสรุป จะทำให้ทีมวิเคราะห์หาสาเหตุไม่เจอ</div>
  <div class="grid c2 cmp rv">
    <div class="card dim"><div class="ct">❌ ห้ามเล่าแบบสรุป (บุคคลที่ 3)</div><div class="bub them">"พี่ไปคุยมา ลูกค้าบอกว่าไม่มีเงิน เบี้ยแพงไป เขาเลยยังไม่ซื้อ"</div><div class="cd dim">(เล่าแบบนี้ทีมช่วยวิเคราะห์ไม่ได้ เพราะไม่รู้ว่าเกิดอะไรขึ้นก่อนหน้านั้น)</div></div>
    <div class="card star"><div class="ct">✅ ต้องเล่าแบบบทสนทนา (บุคคลที่ 1)</div><div class="bub me">"หนูถามลูกค้าว่า... แล้วลูกค้าตอบกลับมาแบบนี้ว่า... หนูเลยพูดต่อไปว่า..."</div><div class="cd dim">(ทีมต้องฟัง "คำถาม" ที่ใช้ เพื่อวิเคราะห์ว่าโยนคำถามผิดจังหวะหรือไม่)</div></div>
  </div>
</section>''')

# 25 · 4-step case analysis (one number only, F10)
k4 = [('Fact', 'ข้อมูลตั้งต้น: อายุ อาชีพ สถานะครอบครัว ลูกค้าเป็นใคร?'), ('Dialogue', 'บทสนทนา: ประโยคไหนที่ลูกค้าชะงัก ประโยคไหนที่เราไปต่อไม่เป็น?'),
      ('MANHA', 'สแกน: จากบทสนทนานั้น เราตกหล่นตัวอักษรไหนไป?'), ('Action', 'แผนขั้นต่อไป: กำหนดบทพูดและกลยุทธ์ สำหรับการโทร Follow-up')]
cs = ''.join(f'<div class="card spot" style="--ci:{k}"><div class="n">{k + 1}</div><div class="ct">{t}</div><div class="cd">{d}</div></div>' for k, (t, d) in enumerate(k4))
S(f'''<section class="slide dots ans">
  <div class="kick rv">Case Analysis Framework</div>
  <h2 class="rv">4 ขั้นตอนผ่าตัดเคส (Team Meeting)</h2>
  <div class="intro rv">โครงสร้างสำหรับนำไปใช้ปรึกษาเคสในคลับ หรือกับหัวหน้า</div>
  <div class="grid c4 rv">{cs}</div>
</section>''')

# 26 · workshop (white), labelled rows, กฎเหล็ก in red, writing lines under ผลลัพธ์
rows = [('กติกา:', 'จับคู่สลับกันเป็นตัวแทนและลูกค้า', ''), ('โจทย์:', 'ลูกค้าเป็น "เจ้าของกิจการที่มีลูกเล็ก" และมีกำแพงในใจว่า "ขอคิดดูก่อน"', ''),
        ('หน้าที่ตัวแทน:', 'ใช้ F.O.R.M เปิดใจ และโยนคำถามเพื่อหา Need', ''), ('กฎเหล็ก:', 'ห้ามเอ่ยชื่อแบบประกัน ทุนประกัน หรือค่าเบี้ย เด็ดขาด!', 'r'),
        ('ผลลัพธ์:', 'ตัวแทนต้องจดข้อมูล MANHA ที่ได้ มาแชร์ให้เพื่อนในคลับฟัง', '')]
rw = ''.join(f'<div class="wr {c}"><b>{a}</b><span>{b}</span></div>' for a, b, c in rows)
S(f'''<section class="slide part notes ws">
  <div class="kick rv">🛑 WORKSHOP (10 นาที)</div>
  <h2 class="rv">ฝึกเปิดใจ &amp; ขุดหา N (Need)</h2>
  <div class="timer rv" aria-hidden="true"><i></i><span>10:00</span></div>
  <div class="wrows rv">{rw}</div>
  <div class="nls rv"><div class="nl"><span>📝 M · A · N · H · A</span><i></i></div></div>
</section>''')

# 27 · Q&A
S('''<section class="slide dots q">
  <div class="kick rv">Q&amp;A</div>
  <h2 class="qtext rv">ถาม-ตอบ <span class="r">ปัญหาหน้างาน</span></h2>
</section>''')

# 28 · closing quote + close (the only gold); ticker = 4 items, counted once (F9)
S('''<section class="slide img quote close" data-bg="leader">
  <div class="kick g rv">iTRAINING T.3/6</div>
  <div class="bar gbar rv"></div>
  <div class="one rv" data-read><span class="ql">"เปิดใจให้สำเร็จก่อน ถึงจะสร้างปัญหาได้</span><span class="ql gold">MANHA คือแผนที่นำทาง</span><span class="ql">ถ้าหลงทางให้กลับมาเช็คว่าตกตัวอักษรไหนไป"</span></div>
  <div class="tag rv late2">จริงใจ · ลงมือ · อยู่ด้วยกัน •</div>
  <div class="next rv late2">🌟 คลาสถัดไป · T.4/6 Product Approach</div>
  <div class="marq" aria-hidden="true"><div>เปิดใจก่อนขาย · MANHA Framework · Feel Felt Found · ไม่เถียง คล้อยตามก่อน · F.O.R.M · เก็บข้อมูลเงียบๆ · จริงใจ · ลงมือ · อยู่ด้วยกัน ·&nbsp;</div></div>
  <ul class="tick-sr">
    <li>เปิดใจก่อนขาย · MANHA Framework</li><li>Feel Felt Found · ไม่เถียง คล้อยตามก่อน</li><li>F.O.R.M · เก็บข้อมูลเงียบๆ</li><li>จริงใจ · ลงมือ · อยู่ด้วยกัน</li>
  </ul>
</section>''')

T3CSS = '''
/* T3-only layout */
.sub2{display:block;font-size:var(--fs);color:var(--salmon);font-weight:800;margin-top:.2em}
/* S2: series map on top at 1280 + agenda 2 cols of 3 */
.sm-top{margin-bottom:.4em}
.agenda{list-style:none;display:grid;gap:.35em 2em;width:100%;max-width:1150px}
.agenda.c2a{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-flow:column;grid-template-rows:repeat(3,auto)}
.agenda li{display:flex;align-items:center;gap:.8em;border-bottom:1px solid var(--line);padding:.35em 0;line-height:1.3;min-height:56px}
.agenda .an{color:var(--red);font-weight:900;font-size:max(24px,1.5em);min-width:1.4em;text-align:center}
/* S3/S23/S24 compare: recommended side = .star */
.cmp .card{justify-content:flex-start}
/* S4 core steps */
.rule{font-weight:900;color:var(--salmon);font-size:1.15em}
.hstep.core li{gap:.25em}.hstep.core li b{font-size:1.2em}.hstep.core .en{color:var(--salmon);font-weight:700}
.hstep.core .dl{font-weight:400;color:#e9e6e3;line-height:1.4}
/* S5/S6 letter cards (reusable) */
.letters{list-style:none;display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:.6em;width:100%}
.letters li{background:rgba(38,38,44,.8);border:1px solid var(--line);border-radius:16px;padding:.6em .8em;display:flex;flex-direction:column;gap:.2em;line-height:1.35}
.letters .lt{color:var(--red);font-weight:900;font-size:clamp(40px,min(5.4vw,9vh),96px);line-height:1}
.letters li>span:last-child{color:#e9e6e3}
/* mini MANHA strip on the case solutions */
.solhead{display:flex;justify-content:space-between;align-items:flex-start;gap:1em;width:100%}
.mstrip{display:flex;gap:.25em;flex:none}
.mstrip span{width:1.9em;height:1.9em;display:grid;place-items:center;border-radius:8px;font-weight:900;font-size:clamp(18px,1.6vw,28px);border:1px solid var(--line);color:var(--muted)}
.mstrip span.lit{background:var(--red);border-color:var(--red);color:#fff}
/* S8 signals */
.sig .card.go{border-color:rgba(76,175,80,.45)}.sig .card.stop{border-color:rgba(211,17,69,.5)}
/* S9 Feel-Felt-Found */
.tagb{display:flex;flex-direction:column;align-items:flex-end;gap:.2em}
.tagb .tg{font-weight:800;color:var(--salmon)}
.bub.them .lbl{color:var(--salmon);font-weight:800;display:inline;font-size:1em}
/* S11-S19 case questions: one layout */
.case .sit{max-width:62ch;color:#e9e6e3;line-height:1.45;text-align:center}
.case .bub.hero{font-size:clamp(26px,min(3.6vw,6.4vh),58px);font-weight:900;line-height:1.3;align-self:center;max-width:min(92%,1000px)}
.case .thread{align-items:center}
/* S12-S20 solutions: one layout */
.sol .cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(12px,2vw,28px);width:100%}
.sol .col{display:flex;flex-direction:column;gap:.45em;background:rgba(38,38,44,.7);border:1px solid var(--line);border-radius:16px;padding:.7em .9em}
.sol .col .ct{color:var(--salmon);font-weight:800}
.sol .col .bub{max-width:100%;align-self:stretch}
.sol .ct.sal{color:var(--salmon);font-size:1.15em}
.sol.single .col{max-width:1000px}
/* S22 4 -> 6 */
.m46{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:clamp(12px,2vw,32px);width:100%;align-items:start}
.chips.four{flex-direction:column;align-items:flex-start}
.vstep{list-style:none;display:flex;flex-direction:column;gap:.45em;width:100%}
.vstep li{display:flex;align-items:center;gap:.8em;font-weight:700;line-height:1.35}
/* S26 workshop rows + timer strip */
.wrows{display:flex;flex-direction:column;gap:.4em;width:100%;max-width:1100px}
.wr{display:grid;grid-template-columns:9em 1fr;gap:.8em;border-bottom:1px solid rgba(28,28,33,.12);padding:.3em 0;line-height:1.4}
.wr b{color:var(--ink)}.wr.r span,.wr.r b{color:var(--red);font-weight:800}
.timer{display:flex;align-items:center;gap:.8em;width:100%;max-width:1100px}
.timer i{flex:1;height:6px;border-radius:3px;background:linear-gradient(90deg,var(--red),rgba(211,17,69,.15))}
.timer span{font-weight:900;color:var(--red)}
/* S28 close */
.quote .one{max-width:26ch;line-height:var(--qlh,1.45)}
.quote .one .ql{display:block;text-wrap:balance}
.quote .one .ql+.ql{margin-top:.08em}
.next{font-weight:800;color:var(--salmon)}
.on .late2.rv{animation-delay:2.2s}
.tick-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (max-width:680px){
  .agenda.c2a{grid-template-columns:1fr;grid-auto-flow:row;grid-template-rows:none}
  .letters{grid-template-columns:1fr}
  .letters li{display:grid;grid-template-columns:56px 1fr;grid-template-areas:"l e" "l t";align-items:center;column-gap:.7em}
  .letters .lt{grid-area:l;width:56px;height:56px;display:grid;place-items:center;font-size:32px;border-radius:12px;background:rgba(211,17,69,.15)}
  .letters li b{grid-area:e}.letters li>span:last-child{grid-area:t}
  .sol .cols{grid-template-columns:1fr}
  .sol .cols .col+.col{border-top:3px solid var(--red)}
  .solhead{flex-direction:column}
  .m46{grid-template-columns:1fr}
  .chips.four{flex-direction:row;flex-wrap:wrap}
  .wr{grid-template-columns:1fr;gap:.1em}
  .quote .one{font-size:clamp(20px,6.2vw,26px);max-width:none}
  .sm-top{grid-template-columns:repeat(3,minmax(0,1fr))}
}
@media (max-height:500px){.agenda li{min-height:0;padding:.12em 0}.agenda{gap:0 2em}}
'''

CSS = open(os.path.join(SERIES, 'deck.css'), encoding='utf-8').read() + T3CSS
JS = open(os.path.join(SERIES, 'deck.js'), encoding='utf-8').read()
BGS = {k: bg(k) for k in ['cover', 'listen', 'leader']}
bgcss = '\n'.join(f'.slide[data-bg="{k}"]{{--bg:{v}}}' for k, v in BGS.items())

html = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>iTraining T.3/6 · Sale Process &amp; MANHA</title>
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
import re
body = html.split('<main', 1)[1].split('</main>', 1)[0]  # slides only (deck.js has 'i - 1')
assert '—' not in html and '–' not in html, 'em/en dash found'
assert not re.search(r'\S - \S', re.sub(r'<[^>]+>', ' ', body)), 'spaced ASCII hyphen used as a dash (F8)'
assert 'รอยืนยัน' not in html and 'iCheck' not in html
assert html.count('class="ql gold"') == 1 and html.count('class="bar gbar rv"') == 1, 'gold must be on S28 only'
assert len(SLIDES) == 28, len(SLIDES)
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html), 'bytes,', len(SLIDES), 'slides,', html.count('data-pending='), 'pending')
