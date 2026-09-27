#!/usr/bin/env python3
"""T2248 · iTraining T2/6 Sales Technique builder (fe, on the T2194/T2229 series template).
Text source = Writer-Oracle output/t2248-inventory/T2248-T2-sales-technique-inventory.md (41 slides / 304 lines after R4),
verbatim, with the recorded rulings applied (highest R wins: R4 > R3 > R2 > R1; F7 start hint). rulings.json = make_rulings.py.
Layout = Designer-Oracle output/t2248-t2-sales-technique/ART-DIRECTION.md (b05951f, F5 ruled bob 25/9 13:59):
41 slides kept, answers/hints reveal on the next tap (.stp), S17 scripts one bubble per tap.
Background deviation for designer G1: S5 and S17 are white part openers (§1 rhythm = 8 white), so the group and coach photos
the slide map puts there sit on the next question slides instead (S9 group, S18 coach).
"""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
SERIES = os.path.join(HERE, '..')
BG_DIR = os.path.join(SERIES, 't1-mindset', 'img')  # series backgrounds, shared with T1/T4
OUT = os.path.join(HERE, '..', '..', '..', 'output', 'itraining-t2-sales-technique.html')

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

def bg(name):
    return "url('data:image/webp;base64," + b64(os.path.join(BG_DIR, f'bg-{name}.webp')) + "')"

def pending(flag):
    return f'<div class="pend" data-pending="{flag}" hidden></div>'

# ---------- slide builders ----------
def q(words_html, prompt, kick='คำถามฝึกคิด', bg_name=None, after=''):
    """R1 hero question; `after` = answer/hint blocks, each .stp so it reveals on the next tap."""
    cls = f'slide img q" data-bg="{bg_name}' if bg_name else 'slide dots q'
    return f'''<section class="{cls}">
  <div class="kick rv">{kick}</div>
  <h2 class="qtext rv">{words_html}</h2>
  <div class="prompt rv">💬 {prompt}</div>{after}
</section>'''

def reveal(title, lines, cls=''):
    """answer card revealed on tap: salmon title + lines"""
    t = f'<div class="ct">{title}</div>' if title else ''
    return '\n  <div class="card qa stp ' + cls + '">' + t + ''.join(f'<div class="cd">{x}</div>' for x in lines) + '</div>'

def cards(items, cols, numbered=False, cls=''):
    out = []
    for k, (t, d) in enumerate(items):
        n = f'<div class="n">{k + 1}</div>' if numbered else ''
        out.append(f'<div class="card spot" style="--ci:{k}">{n}<div class="ct">{t}</div>' + (f'<div class="cd">{d}</div>' if d else '') + '</div>')
    return f'<div class="grid c{cols} rv {cls}">' + ''.join(out) + '</div>'

def risk(n, title, example, result, bad=False):
    ex = example
    if bad:  # S11 risk 1: the quoted BAD example (words verbatim; the strike + label are visual)
        ex = ex.replace('"คุ้มครองทุกโรคแน่นอน"', '<s class="bad">"คุ้มครองทุกโรคแน่นอน"</s>')
    lab = '<span class="nope">ตัวอย่างที่ไม่ควรพูด</span>' if bad else ''
    res = f'<div class="res">{result}</div>' if result else ''
    return f'''<div class="risk rv"><div class="rh"><span class="rno">{n}</span><b>{title}</b></div>
    <div class="exq">{lab}{ex}</div>{res}</div>'''

def part_head(kick, title):
    return f'''<div class="kick rv">{kick}</div>
  <h2 class="rv">{title}</h2>
  <div class="skew rv"></div>'''

def objection(who, said):
    return f'''<section class="slide dots objn">
  <div class="kick rv">Part 7: Q&amp;A &amp; Objection</div>
  <div class="thread rv"><div class="lbl">{who}</div><div class="bub them">{said}</div></div>
  <h2 class="rv">คุณจะตอบว่าอย่างไร?</h2>
  <div class="prompt rv">💬 ช่วยกันตอบ จดโน้ต</div>
  <div class="nl wl rv"><span>คำตอบที่ชอบ:</span><i></i></div>
</section>'''

SLIDES = []
S = SLIDES.append

# 01 · cover (F6: series title + Thai subtitle verbatim · F7 start hint)
S('''<section class="slide img cover" data-bg="cover">
  <div class="kick rv">iTRAINING · T.2/6</div>
  <h1 class="rv"><span class="aurora">Sales Technique</span></h1>
  <div class="bar rv"></div>
  <div class="lead rv">เทคนิคการขายประกันชีวิต</div>
  <div class="sub rv">เทคนิค + ข้อควรระวัง + จุดขาย</div>
  <div class="sub rv">สำหรับตัวแทนที่ต้องการขายอย่างมืออาชีพ</div>
  <div class="hint rv">แตะ · ปัด · หรือกด → เพื่อเริ่ม</div>
</section>''')

# 02 · agenda: vertical numbered list, numbers red
ag = ['ขายยังไง ให้บริการง่าย ลูกค้าประทับใจ', 'ข้อควรระวัง และ ควรรู้ เรื่องประกัน', 'คำมั่นสัญญาต่อลูกค้า',
      'เคล็ด(ไม่)ลับ ประกันชีวิต + ประกันสุขภาพ', 'การวางแผนขยายตลาด', 'เทคนิคเฉพาะสำหรับตัวแทน iAgencyAIA',
      'Q&amp;A และ การตอบข้อโต้แย้ง + Workshop']
li = ''.join(f'<li style="--k:{k}"><span class="an">{k + 1}</span><span>{t}</span></li>' for k, t in enumerate(ag))
S(f'''<section class="slide dots">
  <div class="kick rv">AGENDA</div>
  <h2 class="rv">โครงสร้างเนื้อหา</h2>
  <ol class="agenda rv">{li}</ol>
</section>''')

# 03 · why this class (principle, listen bg)
S('''<section class="slide img ans" data-bg="listen">
  <div class="kick rv">ทำไมต้องเรียนเรื่องนี้</div>
  <h2 class="rv">ขายเก่งไม่พอ<br><span class="aurora">ต้อง "ขายแล้วลูกค้าอยู่กับเรานาน"</span></h2>
  <div class="foot rv">ความประทับใจ คือสิ่งที่ทำให้ลูกค้าบอกต่อ</div>
  <div class="foot rv">และการขายอย่างถูกต้องจะทำให้ลูกค้าไม่ยกเลิกกรมธรรม์</div>
</section>''')

# 04 · question + answer on tap (R4 F1: no quantifier)
S(q('ลูกค้าซื้อประกัน<br><span class="r">เพราะอะไร?</span>', 'ยกมือ / บอกเหตุผลคนละข้อ',
    after=reveal('', ['ลูกค้าซื้อเพราะ "เชื่อใจคน" ไม่ใช่แค่ตัวสินค้า'])))

# 05 · Part 1 opener (white): expectations vs hard parts
S(f'''<section class="slide part ed">
  {part_head('Part 1', 'ขายยังไง ให้บริการง่าย ลูกค้าประทับใจ')}
  <div class="grid c2 rv">
    <div class="card"><div class="ct">ลูกค้าคาดหวังอะไร?</div><ul class="pts">
      <li>ตอบเร็ว ติดต่อได้จริง ไม่หาย</li><li>อธิบายให้เข้าใจง่าย ไม่พูดศัพท์ยาก</li>
      <li>ช่วยตอนเคลม ไม่ใช่หายไปหลังปิดการขาย</li><li>ซื่อสัตย์ บอกทั้งข้อดีข้อจำกัด</li></ul></div>
    <div class="card"><div class="ct">ตัวแทนบริการยากเรื่องอะไร?</div><ul class="pts">
      <li>ลูกค้าเยอะ ดูแลไม่ทั่วถึง</li><li>ลูกค้าคาดหวังสูง/เข้าใจผิดเรื่องความคุ้มครอง</li>
      <li>งานเอกสาร/เคลมซับซ้อน</li><li>ตามต่ออายุ/จ่ายเบี้ยไม่ทัน</li></ul></div>
  </div>
</section>''')

# 06 · priority order 1-3, top to bottom, #1 larger; then its question
pr = [('เคลม', 'ลูกค้าเดือดร้อน มาก่อนเสมอ'), ('คลับ/ประชุม', 'พัฒนาตัวเอง + ทีม'), ('ลูกค้า', 'หาลูกค้าใหม่/ติดตาม')]
li = ''.join(f'<li class="{"top" if k == 0 else ""}" style="--ci:{k}"><span class="pn">{k + 1}</span><b>{t}</b><span>{d}</span></li>'
             for k, (t, d) in enumerate(pr))
S(f'''<section class="slide dots">
  <div class="kick rv">การลำดับความสำคัญ</div>
  <h2 class="rv">เรียงตามนี้</h2>
  <ol class="prio rv">{li}</ol>
  <div class="card qa rv"><div class="lbl">คำถามฝึกคิด</div><div class="ct">ถ้าลูกค้าโทรมาตอนคุณยุ่งมาก จะทำยังไง?</div><div class="cd">💬 ช่วยกันตอบ</div></div>
</section>''')

# 07 · how customers are delighted (4 cards)
S(f'''<section class="slide dots ans">
  <div class="kick rv">Part 1</div>
  <h2 class="rv">ลูกค้าประทับใจยังไง</h2>
  {cards([('จำเรื่องเล็กๆ', 'จำเรื่องส่วนตัวของลูกค้าได้ ทำให้เขารู้สึกพิเศษ'),
          ('Proactive', 'เตือนต่ออายุ แจ้งสิทธิใหม่ ก่อนลูกค้าถาม'),
          ('อยู่ด้วยตอนลำบาก', 'อยู่ตอนเคลม/ตอนลำบาก ไม่หายไป'),
          ('ทำเกินสัญญา', 'ทำเกินที่สัญญาไว้นิดหน่อย เสมอ')], 2)}
</section>''')

# 08 · service tips (4 cards)
S(f'''<section class="slide dots ans">
  <div class="kick rv">Part 1</div>
  <h2 class="rv">เทคนิค เคล็ด(ไม่)ลับ ด้านบริการ</h2>
  {cards([('ฟัง 80/20', 'ฟังมากกว่าพูด ให้ลูกค้าเป็นคนเล่า'),
          ('ถามให้คิด', 'ถามคำถามที่ทำให้ลูกค้าคิดเอง'),
          ('สรุปสั้น', 'สรุปสั้น จำง่าย ทวนความเข้าใจทุกครั้ง'),
          ('นัดติดตาม', 'นัดติดตามทุกครั้ง ไม่ปล่อยหาย')], 2)}
</section>''')

# 09 · question + follow-up question (group bg, see docstring)
S(q('คุณจะทำให้ลูกค้าประทับใจ<br><span class="r">ได้อย่างไร?</span>', 'ระดมไอเดีย ช่วยกันตอบ', bg_name='group',
    after=reveal('คำถามเพิ่ม', ['คุณเคยทำให้ลูกค้าประทับใจคุณแล้ว อย่างไรบ้าง?', 'เล่าประสบการณ์จริง คนละเรื่อง'])))

# 10 · question + answer
S(q('ลูกค้าจำอะไร<br><span class="r">จากที่เราพูด?</span>', 'ช่วยกันตอบ',
    after=reveal('ทุกคำที่ตัวแทนพูด = ความคาดหวังของลูกค้า', ['พูดอะไรไว้ ลูกค้าจำและคาดหวังตามนั้น'])))

# 11 · Part 2 opener (white): risks 1-2 side by side
S(f'''<section class="slide part ed risks">
  {part_head('Part 2: ข้อควรระวัง', '5 ประเด็นเสี่ยง (1-2)')}
  <div class="grid c2 rv">
    {risk(1, 'พูด/รับประกันเกินจริง', 'ตัวอย่าง: บอก "คุ้มครองทุกโรคแน่นอน" ทั้งที่มีข้อยกเว้น', 'ผล: เคลมไม่ได้จริง ลูกค้ารู้สึกโดนหลอก ร้องเรียน เสียใบอนุญาต', bad=True)}
    {risk(2, 'แถลงข้อมูลไม่ครบ', 'ตัวอย่าง: ไม่ถามประวัติสุขภาพให้ครบ หรือช่วยลูกค้าปิดข้อมูล', 'ผล: บริษัทปฏิเสธการจ่าย (แถลงเท็จ) กรมธรรม์เป็นโมฆะ')}
  </div>
</section>''')

# 12 · risk 3 (R2 fasai #8: exclusions split by contract type)
S(f'''<section class="slide dots risks">
  <div class="kick rv">Part 2: ข้อควรระวัง</div>
  {risk(3, 'เรื่องที่ไม่คุ้มครอง', 'ตัวอย่าง: ลูกค้าชอบดำน้ำลึก ทำประกันอุบัติเหตุ แต่ตัวแทนไม่ได้บอกว่ากีฬาอันตรายเป็นข้อยกเว้น พอเกิดอุบัติเหตุเคลมไม่ผ่าน', 'ผล: ลูกค้าคาดหวังผิด เสียความเชื่อใจถาวร').replace('<div class="exq">', '''<div class="sub">ต้องบอกให้ชัดก่อนเซ็น</div>
    <div class="excl"><div class="lbl">ข้อยกเว้นหลัก</div>
      <div class="cd">กรมธรรม์ชีวิต: ไม่จ่ายถ้าฆ่าตัวตายภายใน 1 ปีนับจากวันเริ่มคุ้มครอง หรือถูกผู้รับประโยชน์ฆ่า</div>
      <div class="cd">สัญญาเพิ่มเติม: สงคราม · กีฬาอันตราย (PA) · โรคที่เป็นมาก่อน (สุขภาพ) · ทำร้ายตัวเองทุกกรณี</div></div>
    <div class="exq">''', 1)}
</section>''')

# 13 · risk 4: waiting periods as big numbers (R1 list · R2 #7 health-rider scope + CI line)
S(f'''<section class="slide dots risks">
  <div class="kick rv">Part 2: ข้อควรระวัง</div>
  <div class="risk rv"><div class="rh"><span class="rno">4</span><b>ช่วงระยะเวลารอคอย</b></div></div>
  <div class="wp rv">
    <div class="wpi"><div class="big">30<small>วัน</small></div><div class="cd">เจ็บป่วยทั่วไป (สัญญาสุขภาพ)</div></div>
    <div class="wpi"><div class="big">120<small>วัน</small></div><div class="cd">โรคเฉพาะ (AIA Health Happy / AIA Health Saver): ไส้เลื่อน / ต้อเนื้อ-ต้อกระจก / ทอนซิล-อดีนอยด์ / เยื่อบุโพรงมดลูกเจริญผิดที่</div></div>
  </div>
  <div class="cd dim rv">สัญญา CI / Care for Cancer มีระยะรอคอยของแต่ละแบบ</div>
  <div class="exq rv">ตัวอย่าง: ลูกค้าทำประกันสุขภาพ 1 มกราคม สัปดาห์ที่ 3 ไม่สบายไปหาหมอ เคลมค่ารักษา ปรากฏว่ายังอยู่ในช่วงรอคอย 30 วัน เคลมไม่ได้</div>
  <div class="foot rv">ถ้าไม่บอกไว้ = ทะเลาะกันแน่</div>
</section>''')

# 14 · risk 5 (+ link to Part 3)
S(f'''<section class="slide dots risks">
  <div class="kick rv">Part 2: ข้อควรระวัง</div>
  {risk(5, 'ลูกค้าติดต่อตัวแทนไม่ได้', 'ตัวอย่าง: ลูกค้าจะเคลม/สอบถามด่วน โทรหาตัวแทนไม่รับ ไลน์ไม่ตอบ หายไปเลย', 'ผล: ลูกค้ารู้สึกถูกทอดทิ้ง เสียความเชื่อใจ ยกเลิกกรมธรรม์ หรือย้ายไปตัวแทนอื่น')}
  <div class="foot rv">โยง Part 3: คำมั่นว่าติดต่อได้เสมอ + มีทีมดูแลต่อ</div>
</section>''')

# 15 · question; the 4 promise levels reveal next as a numbered ladder
lv = [('ส่วนตัว', 'ซื่อสัตย์ ตั้งใจ พัฒนาตัวเอง ดูแลระยะยาว ติดต่อได้เสมอ'), ('ต่อสังคม', 'สร้างคุณค่า ต่อยอด ช่วยเหลือสังคม'),
      ('ต่อ iAgencyAIA', 'รักษาชื่อเสียงทีม ทำงานมาตรฐานเดียวกัน'), ('ต่อ AIA', 'รักษาภาพลักษณ์ ทำถูกต้องตามหลักบริษัท')]
li = ''.join(f'<li><span class="lvn">ระดับ {k + 1}</span><b>{t}</b><span>{d}</span></li>' for k, (t, d) in enumerate(lv))
S(q('คำมั่นสัญญาของคุณ<br><span class="r">ต่อลูกค้าคืออะไร?</span>', 'เขียนขึ้นกระดาน คนละ 1 ข้อ',
    after=f'\n  <ol class="lvls stp">{li}</ol>'))

# 16 · vote: ได้ / ไม่ได้ chips, answer next
S(q('เราสัญญากับลูกค้าได้ 100% ไหมว่า<br><span class="r">"ผมจะดูแลคุณไปตลอด"?</span>', 'ยกมือ + เหตุผล',
    after=reveal('ห้ามสัญญาเกินจริง', ['ตัวแทนเอง เจ็บป่วยได้ เสียชีวิตได้ ออกจากอาชีพได้', 'นี่คือเหตุผลที่ต้องมี "ทีม" และ "ระบบ" ดูแลต่อ'])).replace(
    '<div class="prompt rv">', '<div class="vote rv"><span class="vc">ได้</span><span class="vc">ไม่ได้</span></div>\n  <div class="prompt rv">', 1))

# 17 · Part 3 opener (white): 5 scripts, one bubble per tap, heading pinned (R4 F3: "แน่นอน" dropped)
sc = ['"ผมอาจไม่ได้อยู่ดูแลคุณได้ตลอด แต่ผมวางระบบและทีมไว้ ให้คุณได้รับการดูแลต่อเนื่องครับ"',
      '"ผมสัญญาว่าจะบอกความจริงกับคุณทุกอย่าง ทั้งข้อดีและข้อจำกัด"',
      '"กรมธรรม์นี้คุ้มครอง A B C ส่วนที่ไม่คุ้มครองคือ X Y ผมอยากให้คุณเข้าใจครบก่อนตัดสินใจ"',
      '"ถ้าวันหนึ่งผมไม่อยู่ จะมีทีม iAgencyAIA และ AIA ดูแลคุณต่อ"',
      '"ผมขายสิ่งที่คุณได้ใช้จริง ไม่ใช่สิ่งที่ผมอยากขาย"']
S(f'''<section class="slide part ed scripts">
  {part_head('Part 3: ตัวอย่างคำพูดดี', 'จริงใจ มืออาชีพ ไม่ over-promise')}
  <div class="thread rv">{''.join(f'<div class="bub me stp">{x}</div>' for x in sc)}</div>
</section>''')

# 18 · question only (coach bg, see docstring)
S(q('ประกันชีวิตกับประกันสุขภาพ<br><span class="r">ขายต่างกันอย่างไร?</span>', 'ช่วยกันตอบ', bg_name='coach'))

# 19 · Part 4A opener (white): 4 options 2x2 + R2 #10 scope line + the saying
S(f'''<section class="slide part ed">
  {part_head('Part 4A: ประกันชีวิต', 'ความยืดหยุ่นของประกันชีวิต')}
  <div class="intro rv">สินค้าการเงินตัวอื่นทำไม่ได้</div>
  {cards([('กู้เงินกรมธรรม์', 'ยามจำเป็น'), ('ใช้เงินสำเร็จ', 'หยุดส่งเบี้ยแต่ยังคุ้มครอง'),
          ('ขยายระยะเวลา', 'ปรับแผนได้ตามชีวิต'), ('เวนคืนได้', 'ได้เงินกลับ')], 2)}
  <div class="sub rv">ใช้ได้กับแบบที่มีมูลค่าเวนคืน (ตลอดชีพ / สะสมทรัพย์ / บำนาญบางแบบ) · ไม่ใช้กับ Term และสัญญาเพิ่มเติม · Unit Linked ใช้ถอนหน่วยลงทุน / หยุดพักชำระเบี้ยแทน</div>
  <div class="foot rv">"ประกันยาว ทำให้สั้นได้ แต่ประกันสั้น ทำให้ยาวไม่ได้"</div>
</section>''')

# 20 · question + hint on tap (R3 reframe line)
S(q('ส่งเบี้ยสั้นหรือยาว<br><span class="r">ดีกว่ากัน?</span>', 'ชวนคิด',
    after=reveal('', ['อายุเยอะ ส่งได้แค่แบบสั้น / อายุน้อย ส่งแบบยาวได้', '= ยิ่งเริ่มเร็วยิ่งมีทางเลือก']) +
    reveal('คุ้มครองยาว = อุ่นใจตลอดชีวิต', ['ชี้ให้เห็นความคุ้มค่าระยะยาว']) +
    reveal('รับมือ "ประกันไม่คุ้ม"', ['Reframe: ประกันชีวิต = เพื่อนแท้ยามยาก คุ้มครองตั้งแต่วันที่กรมธรรม์มีผล ไม่ต้องรอสะสม'])))

# 21 · fact sheet (R2 fasai #2/#3/#4, all lines confirmed so the heading stays)
S('''<section class="slide dots facts">
  <div class="kick rv">Part 4A: จุดแข็ง AIA (ชีวิต)</div>
  <h2 class="rv">จุดขายที่ยืนยันแล้ว</h2>
  <div class="grid c3 rv">
    <div class="card spot" style="--ci:0"><div class="ct">สิทธิลดหย่อนภาษี</div><div class="cd">ชีวิต (สัญญา 10 ปีขึ้นไป) + สุขภาพ ≤25,000 รวมกันไม่เกิน 100,000 · บำนาญ ≤200,000 และไม่เกิน 15% ของเงินได้ (รวมกองทุนเกษียณอื่นไม่เกิน 500,000)</div></div>
    <div class="card spot" style="--ci:1"><div class="ct">Prestige</div><div class="cd">แบบ Prestige (ทุน ≥10 ล้าน): Preferred Rate (สุขภาพดีเบี้ยถูกกว่า) · สุขภาพต่ำกว่ามาตรฐานไม่เกินขั้น D ไม่เพิ่มเบี้ย · UL Prestige ลด COI 10-20% (Preferred 15-30% ตามแบบและทุน) · สิทธิ์ Prestige Club โดยไม่กำหนดเบี้ยขั้นต่ำ</div></div>
    <div class="card spot" style="--ci:2"><div class="ct">ผลตอบแทนสะสมทรัพย์</div><div class="cd">IRR ต่างกันตามแบบ คำนวณจากตารางผลประโยชน์ของแบบนั้น</div></div>
  </div>
</section>''')

# 22 · question + answer (R2 #11)
S(q('บริษัทชอบให้ลูกค้าซื้อวงเงิน<br><span class="r">เยอะ หรือ น้อย?</span>', 'ชวนคิด',
    after=reveal('', ['ซื้อวงเงินเพิ่ม = พิจารณาสุขภาพใหม่ + นับระยะรอคอยใหม่เฉพาะส่วนที่เพิ่ม',
                      'แต่ลดวงเงิน ไม่ต้องพิจารณาใหม่ คุ้มครองต่อ (PPR ลดได้ทุกงวดเบี้ย · UDR มีผลรอบปีกรมธรรม์ถัดไป)']) +
    reveal('= ซื้อวงเงินพอดีถึงสูงไว้ตอนสุขภาพดี คุ้มกว่า', [])))

# 23 · Part 4B opener (white): R2 heading/quote + R3 co-pay line (F2 ruled, fasai 14:10 verbatim)
S(f'''<section class="slide part ed">
  {part_head('Part 4B: ประกันสุขภาพ', 'เบี้ยปรับตามพอร์ต ไม่ใช่ตามเคลมของคนเดียว')}
  <div class="hero rv">"เบี้ยไม่ขึ้นเพราะเคลมของเราคนเดียว"</div>
  <div class="card rv"><div class="cd">เบี้ยปรับได้เฉพาะ: (1) ตามอายุ + ชั้นอาชีพ (2) ต้นทุนค่ารักษาของพอร์ตรวม ตามที่นายทะเบียนอนุมัติ แจ้งล่วงหน้า 30 วัน</div></div>
  <div class="foot rv">แต่: สัญญาสุขภาพมาตรฐานใหม่ (ออกตั้งแต่ 20 มี.ค. 68) อาจมี Copayment 30-50% ในปีถัดไป ถ้าเคลมนอนโรงพยาบาลด้วยโรคทั่วไป (ไม่รวมการผ่าตัดใหญ่และโรคร้ายแรง) ตั้งแต่ 3 ครั้ง และอัตราเคลมเกินเกณฑ์ ทบทวนใหม่ทุกปี</div>
</section>''')

# 24 · quiz of S13 (bob 27/9 keep · R2 #6 rebuilt question)
S(q('ระยะรอคอยของ AIA Health Happy<br><span class="r">นานแค่ไหน?</span>', 'ชวนคิด เดาก่อน',
    after=reveal('คำตอบ: เจ็บป่วยทั่วไป 30 วัน · 120 วันเฉพาะ 4 กลุ่ม', ['ไส้เลื่อน / ต้อเนื้อ-ต้อกระจก / ทอนซิล-อดีนอยด์ / เยื่อบุโพรงมดลูกเจริญผิดที่'])))

# 25 · Vitality (R2 #1/#9 + R3 payout line; unsourced figures dropped, so no stat tiles)
S('''<section class="slide dots facts">
  <div class="kick rv">Part 4B: AIA Vitality</div>
  <h2 class="rv">Vitality Bonus = เงินคืน ไม่ใช่ส่วนลดเบี้ย</h2>
  <div class="sub rv">(คู่มือสมาชิก ณ 25 ก.ย. 68)</div>
  <div class="card rv"><div class="ct">จ่ายเป็นเงินคืนทุกปีตามสถานะ Vitality</div>
    <div class="vb"><div class="cd">ค่ารักษา+ชดเชยรายวัน สูงสุด 15% (ปีที่ไม่เคลม IPD · ถ้าเคลม สูงสุด 5%)</div>
    <div class="cd">โรคร้าย (CI) กลุ่ม AIA CI Plus สูงสุด 20% (CI ProCare สูงสุด 9%)</div>
    <div class="cd">นับตั้งแต่ปีกรมธรรม์แรก จ่ายเมื่อพ้น 90 วันนับจากวันครบรอบปีกรมธรรม์</div></div></div>
  <div class="card dim rv"><div class="ct">ข้อมูลน่าสนใจ</div><div class="cd">AIA Vitality เปิดตัวในไทยปี 2559 (ครบ 10 ปี)</div></div>
</section>''')

# 26 · quote (salmon kicker, never gold)
S('''<section class="slide dots quote">
  <div class="bar rv"></div>
  <div class="one rv" data-read><span class="ql">"เราซื้อประกันด้วย สุขภาพ ไม่ใช่ด้วย เงิน</span><span class="ql r">วันที่อยากซื้อ อาจเป็นวันที่ซื้อไม่ได้แล้ว"</span></div>
</section>''')

# 27 · question + worked example (the "คิดเลขเล่นๆ" label sits with the numbers, F1 note)
S(q('ลูกค้า 1 คน<br><span class="r">ต่อยอดเป็นกี่คนได้?</span>', 'คิดเลขเล่นๆ',
    after=reveal('คิดเลขเล่นๆ', ['ลูกค้า 1 คนที่ประทับใจ แนะนำเพื่อน 3 คน ใน 1 ปี', '= ฐานโต 4 เท่า โดยไม่ต้องหาคนแปลกหน้า'])))

# 28 · Part 5 opener (white): 4 cards
S(f'''<section class="slide part ed">
  {part_head('Part 5', 'การวางแผนขยายตลาด')}
  {cards([('Referral', 'บริการดี = ลูกค้าบอกต่อ ขอแนะนำอย่างเป็นธรรมชาติ'),
          ('Segment', 'แบ่งกลุ่ม: มนุษย์เงินเดือน / เจ้าของธุรกิจ / ครอบครัว / เกษียณ พูดให้ตรงกลุ่ม'),
          ('Network', 'Social media, กิจกรรม, content ให้ความรู้ = ลูกค้าเดินมาหาเอง'),
          ('ตั้งเป้า', 'นัด/สัปดาห์ อัตราปิด ฐานเก่าที่ต่อยอดได้ วัดผลได้ = รู้ว่าต้องเพิ่มตรงไหน')], 2)}
</section>''')

# 29 · question with writing lines for its blanks
S(q('คุณมีลูกค้าเก่าที่ยังไม่ได้ขอ referral<br><span class="r">กี่คน?</span>', 'ลองนับ จดโน้ต',
    after='''
  <div class="nls wl rv">
    <div class="nl"><span>จดจำนวนลูกค้าเก่าที่ยังไม่ได้ขอ referral: <i class="blank"></i> คน</span></div>
    <div class="nl"><span>สัปดาห์นี้จะขอ referral จากใคร:</span><i></i></div>
  </div>'''))

# 30 · question + answer (R4 F3: guarantees -> mechanism / standard)
S(q('อะไรทำให้ตัวแทน iAgencyAIA<br><span class="r">ต่างจากตัวแทนทั่วไป?</span>', 'บอกมาคนละข้อ',
    after='''
  <div class="grid c3 stp ans3">
    <div class="card"><div class="ct">"จริงใจ ลงมือ อยู่ด้วยกัน"</div><div class="cd">ขายด้วยความจริงใจ ไม่ hard sell</div></div>
    <div class="card"><div class="ct">มีทีม + ระบบดูแลต่อ</div><div class="cd">ถ้าตัวแทนไม่อยู่ มีทีมดูแลลูกค้าต่อ</div></div>
    <div class="card"><div class="ct">มาตรฐานเดียวกัน</div><div class="cd">ตัวแทนทุกคนใช้มาตรฐานบริการเดียวกัน</div></div>
  </div>'''))

# 31 · Part 6 opener (white): tool (R4 = bob F5: iKnow + tier line, no screenshot)
S(f'''<section class="slide part ed">
  {part_head('Part 6: เครื่องมือ', 'ใช้ iKnow ใน FA Tools ให้ลูกค้าเห็นตัวเลขจริง')}
  {cards([('เปิดตัวเลขจริง', 'คำนวณให้เห็นว่า "เกษียณต้องมี X ล้าน ตอนนี้มี Y = ช่องว่าง Z" ลูกค้าเชื่อเพราะเห็นภาพ'),
          ('Proposal มืออาชีพ', 'ทำ proposal สวยในไม่กี่คลิก ดูน่าเชื่อถือ'),
          ('Review พอร์ตเก่า', 'หาช่องว่างความคุ้มครอง ต่อยอดขายเพิ่ม')], 3)}
  <div class="foot rv">iKnow ปลดล็อกเมื่อเป็น FA ขึ้นไป · ตัวแทนใหม่เริ่มจาก uKnow</div>
</section>''')

# 32 · Part 7 opener (white) + objection 1; 33-35 · same layout on charcoal
S(objection('ลูกค้าพูดว่า', '"ขอคิดดูก่อน"').replace('class="slide dots objn"', 'class="slide part objn"'))
S(objection('ลูกค้าคิดว่า', '"มีประกันเยอะแล้ว"'))
S(objection('ลูกค้าบอก', '"แพงไป / ไม่มีเงิน"'))
S(objection('ลูกค้าบอก', '"ขอปรึกษาที่บ้านก่อน"').replace('</section>', '''  <div class="foot rv">ไม่ใส่คำตอบสำเร็จรูป ปล่อยให้ Club ระดมคำตอบ<br>แล้วสรุปคำตอบที่ดีที่สุดร่วมกัน = ตัวแทนได้ของจริงไปใช้</div>
</section>'''))

# 36 · workshop: role-play rules as 4 steps (light bg)
S('''<section class="slide img ans" data-bg="light">
  <div class="kick rv">Workshop</div>
  <h2 class="rv">ฝึกจริง: จับคู่ Role-Play</h2>
  <div class="intro rv">ขาย + ตอบ objection + ใช้คำพูดจาก Part 3</div>
  <div class="lbl rv">กติกา</div>
  <ol class="vstep rv"><li><span class="rn">1</span><span>จับคู่: สลับกันเป็น ตัวแทน และ ลูกค้า</span></li><li><span class="rn">2</span><span>ลูกค้าเลือก objection จาก Part 7 มาใช้</span></li><li><span class="rn">3</span><span>ตัวแทนใช้คำพูดจาก Part 3 + เทคนิค Part 1</span></li><li><span class="rn">4</span><span>จดสิ่งที่ได้เรียนรู้</span></li></ol>
</section>''')

# 37 · notes (white, 3 writing lines)
S('''<section class="slide part notes">
  <div class="kick rv">จดโน้ต</div>
  <h2 class="rv">สิ่งที่จะเอาไปใช้จริงสัปดาห์นี้</h2>
  <div class="nls rv">
    <div class="nl"><span>📝 1 เทคนิค ที่จะลอง:</span><i></i></div>
    <div class="nl"><span>📝 1 คำพูด ที่จะใช้:</span><i></i></div>
    <div class="nl"><span>📝 1 objection-answer ที่เตรียมไว้:</span><i></i></div>
  </div>
</section>''')

# 38 · Q&A (question-hero style)
S('''<section class="slide dots q">
  <div class="kick rv">Q&amp;A</div>
  <h2 class="qtext rv">ถาม-ตอบ <span class="r">สิ่งที่สงสัย</span></h2>
</section>''')

# 39 · quote (salmon kicker, never gold)
S('''<section class="slide dots quote">
  <div class="bar rv"></div>
  <div class="one rv" data-read><span class="ql">"ตัวแทนที่ดี ไม่ได้ขายประกัน</span><span class="ql r">แต่ขาย ความอุ่นใจ</span><span class="ql">ที่ลูกค้าจะรู้สึกได้</span><span class="ql">ในวันที่เขาต้องการมันที่สุด"</span></div>
</section>''')

# 40 · closing quote (the only gold)
S('''<section class="slide img quote" data-bg="leader">
  <div class="bar gbar rv"></div>
  <div class="one rv" data-read><span class="ql">"ประกันไม่ใช่ค่าใช้จ่าย</span><span class="ql gold">แต่คือความรักที่ยังทำงาน</span><span class="ql">ในวันที่เราไม่อยู่"</span></div>
  <div class="tag rv">จริงใจ · ลงมือ · อยู่ด้วยกัน • iAgencyAIA</div>
</section>''')

# 41 · close: next class T.3/6 + tagline + marquee (F8: counts once)
S('''<section class="slide img close" data-bg="cover">
  <div class="circles" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="kick rv">iTRAINING</div>
  <h2 class="rv">T.2/6 <span class="aurora">Sales Technique</span></h2>
  <div class="lead rv">T.2/6 เทคนิคการขายประกันชีวิต</div>
  <div class="card hw rv"><div class="ct">🌟 คลาสถัดไป</div><div class="cd">T.3/6 Sale Process &amp; MANHA</div></div>
  <div class="tag rv">จริงใจ · ลงมือ · อยู่ด้วยกัน · iAgencyAIA</div>
  <div class="marq" aria-hidden="true"><div>จริงใจ · ลงมือ · อยู่ด้วยกัน · iAgencyAIA · จริงใจ · ลงมือ · อยู่ด้วยกัน · iAgencyAIA · จริงใจ · ลงมือ · อยู่ด้วยกัน · iAgencyAIA ·&nbsp;</div></div>
</section>''')

T2CSS = '''
/* T2-only layout */
.q .card.qa{max-width:900px;background:rgba(38,38,44,.85);border-color:rgba(232,153,141,.45)}
.q .card.qa .ct{color:var(--salmon)}
.card.qa .lbl{color:var(--salmon);font-weight:800;letter-spacing:.06em}
/* S2 agenda: vertical numbered list, numbers red */
.agenda{list-style:none;display:flex;flex-direction:column;gap:.35em;width:100%;max-width:980px}
.agenda li{display:flex;align-items:center;gap:.8em;border-bottom:1px solid var(--line);padding:.35em 0;font-weight:700;line-height:1.3;min-height:clamp(40px,6.4vh,56px)}
.agenda .an{color:var(--red);font-weight:900;font-size:max(24px,1.5em);min-width:1.4em;text-align:center}
/* S6 priority (ordered top to bottom, #1 larger) */
.prio{list-style:none;display:flex;flex-direction:column;gap:.5em;width:100%;max-width:980px}
.prio li{display:grid;grid-template-columns:auto auto 1fr;align-items:center;gap:.4em 1em;border:1px solid var(--line);border-radius:14px;padding:.5em .9em;background:rgba(38,38,44,.78)}
.prio li b{font-weight:900}.prio li>span:last-child{color:var(--muted)}
.prio .pn{color:var(--red);font-weight:900;font-size:max(24px,1.6em);line-height:1}
.prio li.top{font-size:1.18em;border-color:rgba(232,153,141,.55)}
/* S11-S14 risk cards: number chip · title · example bubble · result after a red rule */
.risk{display:flex;flex-direction:column;gap:.5em;width:100%}
.risk .rh{display:flex;align-items:center;gap:.6em;font-size:1.15em}
.rno{display:inline-grid;place-items:center;width:1.7em;height:1.7em;border-radius:9px;background:var(--red);color:#fff;font-weight:900}
.exq{background:rgba(255,255,255,.09);border:1px solid var(--line);border-radius:1em 1em 1em .3em;padding:.6em .9em;line-height:1.45;max-width:980px}
.slide.part .exq{background:rgba(28,28,33,.06);border-color:rgba(28,28,33,.12)}
.res{border-top:3px solid var(--red);padding-top:.45em;font-weight:700;line-height:1.45}
.exq .nope{display:block;font-weight:800;color:var(--red);margin-bottom:.15em}
s.bad{text-decoration-color:var(--red);text-decoration-thickness:3px}
.excl{display:flex;flex-direction:column;gap:.3em}.excl .lbl{color:var(--salmon);font-weight:800}
/* S13 waiting periods: big red numbers (>= 24px bold on charcoal) */
.wp{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(10px,2vw,28px);width:100%}
.wpi{display:flex;flex-direction:column;gap:.3em}
.wpi .big{color:var(--red);font-weight:900;font-size:clamp(40px,min(6vw,10vh),96px);line-height:1}
.wpi .big small{font-size:.38em;color:var(--salmon);margin-left:.2em}
/* S15 promise ladder */
.lvls{list-style:none;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.6em;width:100%;max-width:1200px;text-align:left}
.lvls li{border-top:4px solid var(--red);background:rgba(38,38,44,.85);border-radius:0 0 12px 12px;padding:.5em .7em;display:flex;flex-direction:column;gap:.2em;line-height:1.35}
.lvls .lvn{color:var(--salmon);font-weight:800}.lvls li>span:last-child{color:var(--muted)}
/* S16 vote chips */
.vote{display:flex;gap:1em;justify-content:center}
.vote .vc{border:2px solid rgba(232,153,141,.6);border-radius:999px;padding:.35em 1.4em;font-weight:900;font-size:clamp(22px,min(2.6vw,4.6vh),44px)}
/* S17 scripts */
.scripts .thread{max-width:1100px}
/* S21 / S25 fact cards */
.facts .card .cd{line-height:1.5}
.vb{display:flex;flex-direction:column;gap:.35em;margin-top:.3em}
/* S23 hero line */
.hero{font-size:clamp(24px,min(3.2vw,5.6vh),52px);font-weight:900;color:var(--red);line-height:1.3}
/* S30 answer cards */
.q .ans3{max-width:1200px;text-align:left}
/* S29 / S32-S35 writing lines */
.wl{width:100%;max-width:980px}
.nl i.blank{display:inline-block;width:5em;height:1em;border-bottom:2px solid rgba(255,255,255,.35);vertical-align:baseline}
.slide:not(.part) .nl span{color:#fff}
.slide:not(.part) .nl i{border-bottom-color:rgba(255,255,255,.3)}
/* S32-S35 objection prompts: identical layout (S32 = white Part 7 opener) */
.objn .thread{max-width:980px}
.slide.objn h2{font-size:clamp(24px,min(3.4vw,6vh),56px);max-width:none} /* S32 (white) = S33-S35 size, measured in G1 */.objn .bub.them{font-size:1.4em;font-weight:800}
.objn .thread .lbl{color:var(--salmon);font-weight:800}
.slide.part.objn .thread .lbl{color:var(--red)}
/* S36 vertical stepper */
.vstep{list-style:none;display:flex;flex-direction:column;gap:.5em;width:100%;max-width:980px}
.vstep li{display:flex;align-items:center;gap:.8em;font-weight:700;line-height:1.35}
/* quotes: Thai display lines need room for stacked marks (T4 R1) */
.quote .one{max-width:26ch;line-height:var(--qlh,1.45)}
.quote .one .ql{display:block;text-wrap:balance}
.quote .one .ql+.ql{margin-top:.08em}
.quote .one .ql.r{color:var(--salmon)}
@media (max-width:680px){
  .quote .one{font-size:clamp(20px,6.2vw,26px);max-width:none}
  .wp{grid-template-columns:1fr}
  .lvls{grid-template-columns:1fr}
  .agenda li{min-height:56px}
}
@media (max-height:500px){.agenda{gap:0}.agenda li{min-height:0;padding:.12em 0}}
'''

CSS = open(os.path.join(SERIES, 'deck.css'), encoding='utf-8').read() + T2CSS
JS = open(os.path.join(SERIES, 'deck.js'), encoding='utf-8').read()
BGS = {k: bg(k) for k in ['cover', 'listen', 'group', 'coach', 'light', 'leader']}
bgcss = '\n'.join(f'.slide[data-bg="{k}"]{{--bg:{v}}}' for k, v in BGS.items())

html = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>iTraining T.2/6 · Sales Technique</title>
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
assert 'iCheck' not in html, 'iCheck found'
assert html.count('class="ql gold"') == 1 and html.count('class="bar gbar rv"') == 1, 'gold must be on S40 only'
assert len(SLIDES) == 41, len(SLIDES)
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote', OUT, len(html), 'bytes,', len(SLIDES), 'slides,', html.count('data-pending='), 'pending')
