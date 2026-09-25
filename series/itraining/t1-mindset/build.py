#!/usr/bin/env python3
"""T2194 · iTraining T1/6 Mindset redesign builder (Designer-Oracle).
Text source = FIXED copy (Dev-Oracle/output/t2194/backup/T1-shared-documents_itraining-t1-mindset-FIXED.html),
carried verbatim (see source-text.txt). Layout = CONDUCT-SLIDE-001 v1.3 + T1-T6 series template.
21st.dev per part (bob picks, see ../ART-DIRECTION.md §2): cover 989 · openers + questions 19257 · principles 26797+1567 ·
compare 26826 · exercise 1536 · close 664 · OVERRIDES: cycle = ring on the T2182 stepper (29815 portrait), quote = 9386.
ROLE (bob 25/9 01:18): fe BUILDS the deck on the T2182 kit.
fe (T2194): copied from Designer-Oracle 5d1209b output/t2194-mindset/build/build.py. SLIDES content is unchanged
(wording changes only via writer). Only the paths below changed: series CSS/JS = ../deck.css + ../deck.js (shared by T1-T6),
images = img/bg-*.webp, output = oracle-slide-kit output/itraining-t1-mindset.html.
"""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.join(HERE, '..')
OUT = os.path.join(HERE, '..', '..', '..', 'output', 'itraining-t1-mindset.html')

def img(name):
    b = open(os.path.join(HERE, 'img', f'bg-{name}.webp'), 'rb').read()
    return "url('data:image/webp;base64," + base64.b64encode(b).decode() + "')"

# ---------- slide builders ----------
def cover():
    return '''<section class="slide img cover" data-bg="cover">
  <div class="kick rv">iTRAINING · T.1/6</div>
  <h1 class="rv"><span class="aurora">Mindset</span></h1>
  <div class="bar rv"></div>
  <div class="lead rv">Mindset + วงจรการทำงาน</div>
  <div class="sub rv">รากฐานของตัวแทนที่ลูกค้าไว้วางใจ</div>
  <div class="hint rv">แตะ · ปัด · หรือกด → เพื่อเริ่ม</div>
</section>'''

def part(n, title_html):
    return f'''<section class="slide part">
  <div class="pnum rv" aria-hidden="true">{n}</div>
  <div class="kick rv">Part {n}</div>
  <h2 class="rv">{title_html}</h2>
  <div class="skew rv"></div>
</section>'''

def q(kick, words_html, prompt, chips=None, bg=None):
    chips_html = ''
    if chips:
        chips_html = '<div class="chips rv">' + ''.join(f'<span class="chip">{c}</span>' for c in chips) + '</div>'
    cls = f'slide img q" data-bg="{bg}' if bg else 'slide dots q'
    return f'''<section class="{cls}">
  <div class="kick rv">{kick}</div>
  <h2 class="qtext rv" data-read>{words_html}</h2>
  {chips_html}
  <div class="prompt rv">{prompt}</div>
</section>'''

def ans(kick, title_html, cards, foot=None, bg=None, cols=2, intro=None):
    cls = f'slide img ans" data-bg="{bg}' if bg else 'slide dots ans'
    intro_html = f'<div class="intro rv">{intro}</div>' if intro else ''
    cards_html = ''.join(
        f'<div class="card spot"><div class="ct">{t}</div>' + (f'<div class="cd">{d}</div>' if d else '') + '</div>'
        for t, d in cards)
    foot_html = f'<div class="foot rv">{foot}</div>' if foot else ''
    return f'''<section class="{cls}">
  <div class="kick rv">{kick}</div>
  <h2 class="rv">{title_html}</h2>
  {intro_html}
  <div class="grid c{cols} rv">{cards_html}</div>
  {foot_html}
</section>'''

def notes(kick, title, lines):
    ls = ''.join(f'<div class="nl"><span>{l}</span><i></i></div>' for l in lines)
    return f'''<section class="slide part notes">
  <div class="kick rv">{kick}</div>
  <h2 class="rv">{title}</h2>
  <div class="nls rv">{ls}</div>
</section>'''

SLIDES = []
S = SLIDES.append

# 00 cover
S(cover())
# 01 Part 1
S(part(1, 'ทำไมประกันชีวิต<br><span class="r">"จำเป็น"?</span>'))
# 02 question
S(q('คำถามฝึกคิด', 'ถ้าคุณ <span class="r">ไม่ได้เป็น</span> ตัวแทนประกัน<br>คุณจะซื้อประกันไหม?',
    '💬 ยกมือ · ไม่มีคำตอบผิด', chips=['🤔 ซื้อ', '😅 ไม่ซื้อ', '🤷 ไม่แน่ใจ']))
# 03 answer
S(f'''<section class="slide img ans" data-bg="listen">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">คำตอบของคุณ =<br><span class="aurora">คำตอบของลูกค้า</span></h2>
  <div class="card spot rv narrow"><div class="ct">ข้อคิด</div><div class="cd">ถ้าคุณเองยังไม่เชื่อ · ลูกค้าจะเชื่อได้ยังไง?</div></div>
  <div class="vs rv">
    <div class="row">ประกันจำเป็นเพราะ <span class="r">ความเสี่ยงมีจริง</span><small>ไม่ใช่เพราะต้องขาย</small></div>
  </div>
  <div class="foot rv">ตัวแทนที่ดี = คนที่เชื่อก่อนขาย</div>
</section>''')
# 04 question
S(q('คำถามฝึกคิด', 'ลูกค้าตัดสินใจซื้อประกัน<br>เพราะ <span class="r">อะไร</span> ?', '💬 บอกมาคนละ 1 เหตุผล'))
# 05 answer: feelings
S(ans('เฉลย', 'ลูกค้าซื้อเพราะ <span class="aurora">"ความรู้สึก"</span>',
      [('😰 กลัว', 'กลัวป่วยไม่มีเงิน กลัวเป็นภาระ'), ('❤️ รัก', 'อยากให้คนที่รักมีเงินใช้'),
       ('🛡️ ห่วง', 'ห่วงลูก ห่วงพ่อแม่ ห่วงอนาคต'), ('🤝 รับผิดชอบ', 'หนี้สิน ค่าเทอม · ต้องมีแผนสำรอง')],
      foot='ลูกค้าไม่ได้ซื้อสินค้า · เขาซื้อ <span class="r">"ความอุ่นใจ"</span>', bg='group', cols=2))
# 06 question
S(q('คำถามฝึกคิด', 'แล้วคนส่วนใหญ่ <span class="r">"กลัว"</span> อะไร<br>เกี่ยวกับประกัน?', '💬 ช่วยกันตอบ · เขียนขึ้นกระดาน'))
# 07 answer: 3 fears + solutions
S(f'''<section class="slide dots ans">
  <div class="kick rv">เฉลย + ทางออก</div>
  <h2 class="rv">3 ความกลัว + <span class="r">ทางออก</span></h2>
  <div class="grid c3 rv">
    <div class="card spot"><div class="ct">😰 กลัวสินค้า</div><div class="cq">"ซับซ้อน เคลมยาก"</div><div class="fix">✅ อธิบายด้วยภาษาลูกค้า + แสดง case เคลมจริง</div></div>
    <div class="card spot"><div class="ct">😰 กลัวตัวแทน</div><div class="cq">"จะมาขาย จะหายไป"</div><div class="fix">✅ สร้างไว้วางใจก่อน ให้ความรู้ก่อน ดูแลหลังขาย</div></div>
    <div class="card spot"><div class="ct">😰 กลัวตัวเอง</div><div class="cq">"ไม่มีเงิน ยังไม่ถึงเวลา"</div><div class="fix">✅ เริ่มเล็กๆ ได้ · วันละ 30 บาทก็คุ้มครองได้</div></div>
  </div>
  <div class="foot rv">💡 งานของเราคือ <span class="r">"ลดความกลัว"</span> ไม่ใช่ "ฝืนขาย"</div>
</section>''')
# 08 question with product chips
S(q('คำถามฝึกคิด', 'สินค้าประกันตัวไหน<br><span class="r">"ดีที่สุด"</span> ?', '💬 เลือก 1 ตัว · บอกเหตุผล',
    chips=['สะสมทรัพย์', 'ตลอดชีพ', 'ชั่วระยะเวลา', 'Unit Linked']))
# 09 answer
S(f'''<section class="slide img ans" data-bg="coach">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">ไม่มี "ดีที่สุด" · มีแค่<br><span class="aurora">"ตอบโจทย์ที่สุด"</span></h2>
  <div class="grid c2 rv">
    <div class="card spot"><div class="ct">หลักคิด</div><div class="cd">สินค้าดี = ตอบโจทย์ชีวิตลูกค้า <b>คนนั้น</b></div><div class="cd dim">ลูกค้าเกษียณปีหน้า ≠ ลูกค้าเพิ่งเริ่มทำงาน</div></div>
    <div class="card spot"><div class="ct">มืออาชีพ</div><div class="cq">"แนะนำตัวที่ลูกค้าต้องการ"</div></div>
  </div>
</section>''')
# 10 notes part 1
S(notes('📝 จดบันทึก · Part 1', 'เขียนสิ่งที่ได้เรียนรู้',
        ['ลูกค้าของฉันส่วนใหญ่กลัวเรื่อง', 'วิธีที่ฉันจะลดความกลัว', 'สิ่งที่จะลองทำสัปดาห์นี้']))
# 11 break
S('''<section class="slide img brk" data-bg="light">
  <div class="cup rv" aria-hidden="true">☕</div>
  <h2 class="rv">พัก <span class="aurora">10 นาที</span></h2>
  <div class="sub rv">กลับมาคุยเรื่อง "วงจรการทำงาน" + "กับดักความคิด"</div>
</section>''')
# 12 Part 2
S(part(2, 'วงจรการทำงาน<br><span class="r">ในอาชีพตัวแทน</span>'))
# 13 question
S(q('คำถามฝึกคิด', 'ตัวแทนประกัน<br>ทำอะไรบ้างใน <span class="r">1 สัปดาห์</span> ?', '💬 เรียงลำดับ · อะไรทำก่อน อะไรทำหลัง'))
# 14 cycle ring
steps = ['📋 สร้างรายชื่อ', '📞 ทำนัดหมาย', '🤝 พบลูกค้า', '📊 นำเสนอ', '✅ ปิดการขาย', '💬 บริการหลังขาย']
ring = ''.join(f'<li style="--k:{k}"><span class="rn">{k+1}</span><span class="rt">{t}</span></li>' for k, t in enumerate(steps))
S(f'''<section class="slide dots cyc">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">วงจรการทำงาน</h2>
  <div class="cycwrap rv"><ol class="ring">{ring}</ol><div class="hub">🔄</div></div>
  <div class="sub rv">🔄 วงจรนี้วนซ้ำ · ลูกค้าเก่าแนะนำลูกค้าใหม่</div>
  <div class="foot rv">ตัวแทนที่สำเร็จ = คนที่ <span class="r">ทำวงจรนี้สม่ำเสมอ</span></div>
</section>''')
# 15 Part 3
S(part(3, 'กับดักความคิด<br><span class="r">ตัวแทน</span>'))
# 16 question
S(q('คำถามฝึกคิด', 'ตัวแทนใหม่มักจะ<br><span class="r">"ติดกับดัก"</span> อะไร?', '💬 นึกจากประสบการณ์ตัวเอง'))
# 17 traps
S(ans('เฉลย', 'กับดักความคิดตัวแทน',
      [('🪤 "รอให้พร้อมก่อน"', 'ไม่มีวันพร้อม 100% · เริ่มแล้วเรียนรู้ระหว่างทาง'),
       ('🪤 "กลัวคนปฏิเสธ"', 'ปฏิเสธ ≠ ปฏิเสธตัวคุณ แค่ยังไม่ใช่เวลาของเขา'),
       ('🪤 "เปรียบเทียบตัวเองกับคนอื่น"', 'ทุกคนเริ่มจากศูนย์ · เทียบกับตัวเองเมื่อวาน'),
       ('🪤 "ขายอย่างเดียว ไม่เรียนรู้"', 'ขายโดยไม่มีระบบ = เหนื่อยแต่ไม่โต')],
      foot='💡 รู้ตัวว่าติดกับดัก = ก้าวแรกของการหลุดออกมา', cols=2))
# 18 Part 4
S(f'''<section class="slide part">
  <div class="pnum rv" aria-hidden="true">4</div>
  <div class="kick rv">Part 4</div>
  <h2 class="rv">ทำไม FA หลายคน<br><span class="r">ไปไม่ถึงเป้าหมาย?</span></h2>
  <div class="psub rv">4 ความท้าทาย + ทางออกจาก iAgencyAIA</div>
  <div class="skew rv"></div>
</section>''')
# 19 challenge -> solution
cs = [('😰 1. กลัวถูกปฏิเสธ', 'ไม่กล้าเข้าหาคน ไม่มั่นใจ', 'iTraining + iAgency Club · Coaching, Role Play, One on One'),
      ('📭 2. ไม่มีรายชื่อ', 'ไม่รู้จะเริ่มจากใคร', 'iAgency FA Tools · หาลูกค้าต่อเนื่อง + สร้างตัวตน'),
      ('⏰ 3. บริหารเวลาไม่ได้', 'วุ่นวาย ไม่มีระบบ', 'iProcess + iCareer · โครงสร้างชัด ติดตามผลได้'),
      ('🏝️ 4. โดดเดี่ยว ไม่มีคนสอน', 'ไม่รู้จะปรึกษาใคร', 'Culture "จริงใจ ลงมือ อยู่ด้วยกัน" · มีพี่เลี้ยงดูแล')]
cards = ''.join(f'<div class="card spot"><div class="ct">{a}</div><div class="cd dim">{b}</div><div class="fix">→ {c}</div></div>' for a, b, c in cs)
S(f'''<section class="slide dots ans">
  <div class="kick rv">Challenge → Solution</div>
  <h2 class="rv">4 ความท้าทาย + <span class="r">ทางออก</span></h2>
  <div class="grid c2 rv">{cards}</div>
</section>''')
# 20 Part 5
S(part(5, 'เคล็ดลับ<br><span class="r">4 เชื่อ</span> ไว้วางใจ'))
# 21 question
S(q('คำถามฝึกคิด', 'ลูกค้าต้อง <span class="r">"เชื่อ"</span> อะไรบ้าง<br>ก่อนตัดสินใจซื้อ?', '💬 ลองคิด 4 อย่าง'))
# 22 4 beliefs wrapped by career belief
S(f'''<section class="slide dots ans">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">4 เชื่อ · ครอบด้วย <span class="r">ความเชื่อมั่นในอาชีพ</span></h2>
  <div class="wrapbox rv">
    <div class="wraplabel">🌐 เชื่อมั่นในอาชีพ · ที่ปรึกษาการเงิน มีคุณค่า มั่นคง ช่วยคนได้จริง</div>
    <div class="grid c4">
      <div class="card spot"><div class="n">1</div><div class="ct">เชื่อบริษัท</div><div class="cd">AIA แข็งแกร่ง เชื่อถือได้</div></div>
      <div class="card spot"><div class="n">2</div><div class="ct">เชื่อสินค้า</div><div class="cd">แบบประกันตอบโจทย์จริง</div></div>
      <div class="card spot"><div class="n">3</div><div class="ct">เชื่อผู้นำทีม</div><div class="cd">ทีม iAgencyAIA พาเติบโตได้</div></div>
      <div class="card spot"><div class="n">4</div><div class="ct">เชื่อตนเอง</div><div class="cd">ฉันทำได้ ฉันช่วยคนได้</div></div>
    </div>
  </div>
  <div class="foot rv">💡 ขาดข้อไหน ลูกค้ารู้สึกได้ · ทั้ง 4 ต้องครบ</div>
</section>''')
# 23 workshop pairs
S(ans('Workshop คู่', 'ลองถามตัวเอง',
      [('เชื่อบริษัท?', 'AIA มีอะไรที่ทำให้คุณภูมิใจ?'), ('เชื่อสินค้า?', 'ถ้าลูกค้าถาม "ทำไมต้องซื้อ?" ตอบได้มั่นใจไหม?'),
       ('เชื่อผู้นำทีม?', 'คุณเชื่ออะไรในทีมและตัวผู้นำทีมของคุณ?'), ('เชื่อตนเอง?', 'จุดแข็งคุณคืออะไร? ทำไมลูกค้าควรเลือกคุณ?')],
      foot='💬 จับคู่คุยกัน 3 นาที · แชร์คำตอบ', bg='coach', cols=2))
# 24 notes part 2
S(notes('📝 จดบันทึก · Part 2', 'กับดัก + ความเชื่อของฉัน',
        ['กับดักที่ฉันเคยติด', 'ข้อ "เชื่อ" ที่ยังไม่มั่นใจ', 'สิ่งที่จะเปลี่ยนตั้งแต่สัปดาห์นี้']))
# 25 Part 6
S(part(6, 'การทำนัดหมาย<br><span class="r">+ การเข้าหาผู้มุ่งหวัง</span>'))
# 26 question
S(q('คำถามฝึกคิด', 'ทำไมตัวแทนใหม่<br><span class="r">ไม่กล้าทำนัดหมาย?</span>', '💬 คุณเคยรู้สึกแบบนี้ไหม?'))
# 27 change perspective
S(f'''<section class="slide img ans" data-bg="listen">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">เปลี่ยน <span class="aurora">มุมมอง</span></h2>
  <div class="intro rv">ทัศนคติที่ถูกต้อง</div>
  <div class="vs rv">
    <div class="row">นัดหมาย ≠ ไปขาย → นัดหมาย = <span class="r">ไปช่วย</span></div>
  </div>
  <div class="grid c2 rv">
    <div class="card spot"><div class="cd">10 นัด ปิดได้ 2-3 ก็เก่งแล้ว</div></div>
    <div class="card spot"><div class="cd">ถ้าเขาป่วยพรุ่งนี้ แล้วไม่มีใครบอกเรื่องประกัน?</div></div>
    <div class="card spot"><div class="cd">คุณไม่ได้ขอเงิน · คุณ <b class="r">เสนอทางเลือก</b></div></div>
    <div class="card spot"><div class="cd">ยิ่งทำเยอะ ยิ่งชินเร็ว ความกลัวหายเอง</div></div>
  </div>
</section>''')
# 28 two approaches
S(f'''<section class="slide dots ans appr">
  <div class="kick rv">Approach</div>
  <h2 class="rv">2 วิธีเข้าหา <span class="r">ผู้มุ่งหวัง</span></h2>
  <div class="grid c2 rv">
    <div class="card spot"><div class="ct">Product Approach</div><div class="cd">เริ่มจากสินค้า → เสนอลูกค้า</div><div class="cq">"มีแบบประกันดีๆ มาแนะนำ"</div><div class="cd dim">เหมาะกับลูกค้าที่รู้ตัวว่าต้องการ</div></div>
    <div class="card spot star"><div class="ct">⭐ Need Approach</div><div class="cd">เริ่มจากความต้องการลูกค้า</div><div class="cq">"คุณมีความกังวลอะไรบ้าง?"</div><div class="cd dim">ลูกค้ารู้สึกเป็น <b>ที่ปรึกษา</b> ไม่ใช่พนักงานขาย</div></div>
  </div>
  <div class="foot rv">💡 2 วิธีนี้ ดีทั้งคู่ · แต่ยุคนี้ Need Approach ดีกว่า · สิ่งที่ลูกค้าขาดคือ <span class="r">"คนที่เข้าใจเขาจริงๆ"</span></div>
  <div class="evo rv"><span>ตัวแทนประกัน</span><b>→</b><span>ที่ปรึกษาการเงิน</span><b>→</b><span class="on">นักวางแผนการเงิน</span></div>
  <div class="sub rv">บทบาทยุคใหม่ยิ่งขยับไปทาง "วางแผน" · Need Approach คือภาษาของมัน</div>
</section>''')
# 29 foundation skill
fs = [('ฟังมากกว่าพูด', 'ลูกค้าบอกทุกอย่างที่คุณต้องรู้'), ('ถามคำถามดีๆ', 'ทำให้ลูกค้าคิด ไม่ใช่บังคับตอบ'),
      ('ใส่ใจจริง', 'จำชื่อลูก จำวันเกิด จำสิ่งที่เขาเคยบอก'), ('ติดตามต่อเนื่อง', 'ไม่ใช่แค่ตอนจะขาย'), ('ไม่ push', 'ให้เวลาลูกค้าคิด')]
S(ans('Foundation Skill', 'ทักษะการสร้าง <span class="aurora">ความสัมพันธ์</span>', [(a, '· ' + b) for a, b in fs],
      intro='กุญแจสำคัญของทั้ง 2 วิธี', foot='ไม่ว่าจะ Product หรือ Need · <span class="r">ความสัมพันธ์คือพื้นฐาน</span>', bg='group', cols=2))
# 30 question
S(q('คำถามฝึกคิด', 'ลูกค้าตกลงซื้อประกันแล้ว<br><span class="r">ซื้อกับใครก็เหมือนกันไหม?</span>', '💬 ทำไมลูกค้าต้องซื้อกับเรา? ไม่ใช่คนอื่น?'))
# 31 like + trust
S(f'''<section class="slide dots ans">
  <div class="kick rv">เฉลย</div>
  <h2 class="rv">ลูกค้าซื้อกับคนที่...</h2>
  <div class="grid c3 rv">
    <div class="card spot"><div class="ct">😊 ชอบ</div><div class="cd">คุยแล้วสบายใจ อยากเจออีก</div></div>
    <div class="card spot"><div class="ct">🤝 ไว้ใจ</div><div class="cd">เชื่อว่าแนะนำจริง ดูแลจริง</div></div>
    <div class="card spot dim"><div class="ct">⏰ รีบไม่ทัน</div><div class="cd">ต้องซื้อเดี๋ยวนี้ ใครอยู่ก็ได้</div></div>
  </div>
  <div class="foot rv">💡 ดีที่สุดคือ <span class="r">"ชอบ และ ไว้ใจ"</span> · ซื้อเพราะรีบอาจยกเลิกภายหลัง</div>
  <div class="sub rv">ซื้อเพราะชอบและไว้ใจ = อยู่ยาว + แนะนำคนอื่นให้</div>
</section>''')
# 32 reflection question
S(q('คำถามชวนคิด', 'แล้วคุณจะทำยังไง<br>ให้ลูกค้า <span class="r">"ชอบและไว้ใจ"</span> คุณ?',
    '💬 แชร์กับกลุ่ม', chips=None, bg='leather').replace(
    '<div class="prompt rv">', '<div class="sub rv">คิด 3 สิ่งที่คุณทำได้ตั้งแต่วันนี้ เพื่อให้ลูกค้ารู้สึกว่า <b>"คนนี้แหละ ที่ฉันอยากซื้อด้วย"</b></div>\n  <div class="prompt rv">', 1))
# 33 Part 7
S(part(7, 'การลิสรายชื่อ<br><span class="r">+ ไอเดียหาผู้มุ่งหวัง</span>'))
# 34 workshop list 10
srcs = ['👨‍👩‍👧‍👦 ครอบครัว+ญาติ', '🎓 เพื่อนเก่า', '🏢 เพื่อนร่วมงาน', '🏋️ กิจกรรม', '🏘️ ชุมชน', '📱 รายชื่อในโทรศัพท์']
rows = ''.join(f'<div class="lr"><b>{k}.</b><i></i><span>จาก</span><i class="s"></i><span>เพราะ</span><i></i></div>' for k in range(1, 11))
S(f'''<section class="slide part notes list10">
  <div class="kick rv">Workshop</div>
  <h2 class="rv">ไอเดียลิสรายชื่อ · <span class="r">เขียน 10 คน</span></h2>
  <div class="chips rv">{''.join(f'<span class="chip lt">{c}</span>' for c in srcs)}</div>
  <div class="tip rv">💡 เปิดรายชื่อโทรศัพท์ scroll ทีละคน · "เขาเคยคุยเรื่องเงิน/สุขภาพกับฉันไหม?" ถ้าเคย = ใส่ลิส</div>
  <div class="lrs rv">{rows}</div>
</section>''')
# 35 takeaway quote (gold allowed: takeaway)
S('''<section class="slide img quote" data-bg="leader">
  <div class="kick g rv">จำไว้เสมอ...</div>
  <div class="one rv" data-read>ผลประโยชน์อยู่ใน "เล่ม"<br>แต่เหตุผลที่ลูกค้าเซ็น<br>คือ <span class="gold">"คุณ"</span> ที่อยู่ตรงหน้า</div>
  <div class="bar gbar rv"></div>
  <div class="sub rv">กรมธรรม์ไหนก็คุ้มครองได้เหมือนกัน<br>แต่ความไว้ใจ... มีแค่คุณที่ให้ได้</div>
</section>''')
# 36 closing + homework
S('''<section class="slide img close" data-bg="cover">
  <div class="kick rv">🌟 สัปดาห์หน้าเจอกัน</div>
  <h2 class="rv">T.2/6 · <span class="aurora">เทคนิค การขายประกันชีวิต</span></h2>
  <div class="card hw rv"><div class="ct">📌 การบ้าน</div>
    <ol><li>นัดพบจากรายชื่อ 10 คน อย่างน้อย <b class="r">3 คน</b></li><li>ลอง Need Approach กับ 1 คน · ฟังก่อนพูด</li><li>ทบทวนสไลด์นี้ เปิดอ่านซ้ำเมื่อไหร่ก็ได้</li></ol></div>
  <div class="tag rv">จริงใจ · ลงมือ · อยู่ด้วยกัน · iAgencyAIA.com</div>
  <div class="marq" aria-hidden="true"><div>จริงใจ · ลงมือ · อยู่ด้วยกัน · จริงใจ · ลงมือ · อยู่ด้วยกัน · จริงใจ · ลงมือ · อยู่ด้วยกัน · จริงใจ · ลงมือ · อยู่ด้วยกัน ·&nbsp;</div></div>
</section>''')

CSS = open(os.path.join(SERIES, 'deck.css'), encoding='utf-8').read()
JS = open(os.path.join(SERIES, 'deck.js'), encoding='utf-8').read()
BGS = {k: img(k) for k in ['cover', 'listen', 'coach', 'leather', 'group', 'light', 'leader']}
bgcss = '\n'.join(f'.slide[data-bg="{k}"]{{--bg:{v}}}' for k, v in BGS.items())

html = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>iTraining T.1/6 · Mindset</title>
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
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html), 'bytes,', len(SLIDES), 'slides')
