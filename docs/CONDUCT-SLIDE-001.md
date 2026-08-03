# CONDUCT-SLIDE-001 · iAgencyAIA Slide HTML Conduct (v1.1)

> มาตรฐานบังคับสำหรับ HTML slide/deck ทุกชิ้นของ office ตั้งแต่ 2026-07-26
> สั่งโดย: แบงค์ ("I want this to be our iAgencyAIA slide html conduct from now on")
> Reference builds: `BoB-Oracle/output/slides/t181-iagencyclub-sales-idea.html` (T181v3) · `BoB-Oracle/output/slides/aia-workshop-first-visit.html` (workshop redo, image+motion pattern)
> Reusable starter: `BoB-Oracle/output/reference/deck-template.html` (โครง compliant เริ่ม deck ใหม่)
> Mood guide: `~/.maw/inbox/IMG_0251.jpeg` · "Quiet Confidence. Built, Not sold."
> Effect catalog (เลือก effect ต่อ deck จากที่นี่): `BoB-Oracle/output/reference/UI-EFFECTS-CATALOG.md`

## 0. AUDIENCE-FIRST (กฎข้อแรก, แบงค์ feedback 2026-07-26)

- **สไลด์ = ให้ผู้ฟังดู ไม่ใช่คำอธิบาย** ("มันเหมือนคุณบอกผมมากกว่า" = ผิด): หัวเรื่องใหญ่ + คำถาม + คำสั้น เท่านั้น, **ห้าม paragraph อธิบาย/lede/แนวคิด** บนสไลด์ — ผู้พูดเป็นคนเล่า
- bullet ยาว → chip 2-3 คำ · สไลด์ละ ≤1 ประเด็น · ≤3 effect เด่นต่อสไลด์
- **ภาพนำ ตัวหนังสือตาม**: สไลด์คน/บรรยากาศใช้ภาพจริง (Designer GPT gen หรือ free stock license แท้)
- **ภาพคน = คนเอเชีย/ไทยเสมอ** (แบงค์ order)

---

## 1. Visual Identity (บังคับ, จาก official mood guide)

| Token | Hex | ใช้กับ |
|---|---|---|
| Digital Red | `#D31145` | สีหลักของ brand: kicker, เลขคำถาม, part number, accent, beam |
| Digital Charcoal | `#1C1C21` | พื้นหลังหลักของสไลด์มืด |
| Monotone White | `#FFFFFF` | สไลด์ divider แบบ editorial + ตัวอักษรบนพื้นมืด |
| **Leader Gold** | `#C9A227` | **เฉพาะ moment ผู้นำ/ความสำเร็จเท่านั้น** (takeaway, badge ผ่านเกณฑ์, ตัวเลขความสำเร็จ) ห้ามใช้เป็นสีตกแต่งทั่วไป |
| Digital Salmon | `#E8998D` | secondary accent: sub-text, particle, gradient คู่กับ red |
| Digital Purple | `#8C7BAE` | secondary (ใช้น้อย) |
| Digital Warm Grey | `#B8AFA6` | secondary (ใช้น้อย) |

- **Wordmark**: `iAgencyAIA` มุมขวาบนทุกสไลด์ (i=red, Agency=white บนมืด/charcoal บนขาว, AIA=red)
- **สไลด์สลับจังหวะ**: เนื้อหา = charcoal + dot pattern · Part divider = ขาว editorial (เลขยักษ์แดงเอียง -3deg + แถบแดง skew) · ภาพ BG = charcoal+red tinted overlay
- Typography: Sarabun / Noto Sans Thai / Leelawadee UI · headline font-weight 800-900, letter-spacing ติดลบเล็กน้อย · kicker uppercase tracking 4px สีแดง

## 2. Motion Standard (แปลงจาก Magic UI / 21st.dev / MotionSites เป็น vanilla CSS/JS)

ทุก deck ต้องมีอย่างน้อยข้อ 1-6, ที่เหลือตามเหมาะ:

| # | Effect | Implementation |
|---|---|---|
| 1 | Blur-fade staggered reveal | `.on .rv` keyframe blur(9px)+translateY → ชัด, delay ไล่ .05-.7s |
| 2 | Spring slide transition | `cubic-bezier(.22,1.2,.36,1)` translateY+scale |
| 3 | Number ticker | JS นับ 0→N ease-out 600ms บน `[data-tick]` ตอนเข้าสไลด์ |
| 4 | Aurora gradient text | gradient red→salmon→white, `background-clip:text`, pan 7s (คำ key ใน title) |
| 5 | Progress bar + dots nav | gradient red→salmon เรืองแสง + จุดคลิกได้ (ซ่อนบนมือถือ) |
| 6 | Ken Burns บน BG ภาพ | `::before` scale 1→1.08 26s alternate |
| 7 | Border beam | conic-gradient หมุนรอบ badge/card (`@property --angle`) |
| 8 | Bento grid | overview + takeaway (grid 4 คอลัมน์ → 2 บนมือถือ) |
| 9 | Glassmorphism | `backdrop-filter:blur(14px)` + border ขาวจาง (การ์ด speaker/เนื้อหาบน BG) |
| 10 | Dot pattern | radial-gradient 1px ทุก 26px บนสไลด์ไม่มีภาพ · **ต้อง ANIMATE เลื่อนช้าๆ** (`@keyframes gridmove{to{background-position:26px 26px}}` + `animation:gridmove 14s linear infinite` + `inset:-26px` กันขอบโผล่) ไม่ใช่ static (แบงค์ order 2026-07-27 "bg ลายจุดมันต้องเลื่อนได้") |
| 11 | Particles | canvas ~26 จุด salmon ลอยขึ้นช้า (cover + closing เท่านั้น) |
| 12 | Marquee | แถบเลื่อน key phrases (closing) |
| 13 | Spotlight cursor | radial red 10% ตามเมาส์ (desktop เท่านั้น + ปิดบนสไลด์ขาว) |
| 14 | Swipe gesture | touchstart/touchend deltaX>48 เปลี่ยนสไลด์ |
| 15 | Keyboard nav | Arrow/Space/PageUp-Down/Home/End |

## 3. โครงสร้าง deck มาตรฐาน

```
Cover (BG + aurora title + particles)
→ Overview bento (map ทั้ง session)
→ Speakers / context (glass cards)
→ [Part divider ขาว → เนื้อหา charcoal] × N
→ Takeaway bento (gold = จุดเดียวที่ใช้ได้)
→ Closing (marquee + particles + brand line)
```

## 4. Technical (บังคับทุกไฟล์)

1. **Self-contained ไฟล์เดียว** เปิด offline ได้: CSS/JS inline, ภาพ BG = data-URI (webp, รวมแล้ว < ~500KB)
2. **Mobile-responsive ทั้ง 2 แนว** (มาตรฐานถาวรของแบงค์):
   - `@media (max-width:680px)` portrait: font scale ด้วย vw, layout เต็มจอ, bento → 2 คอลัมน์, speakers → 1 คอลัมน์
   - `@media (orientation:landscape) and (max-height:520px)`: font scale ด้วย vh ให้ fit จอเตี้ย
   - `100dvh` + `viewport-fit=cover` + `.slide{overflow-y:auto}` กัน clip
3. เสิร์ฟผ่าน http ตอน render-verify (file:// ใน headless ไม่โหลด)
4. **T142: ห้าม em-dash** ทุกที่ (ใช้ · : , แทน)
5. **Thai badge/chip CSS (บังคับ)**: ป้ายหรือ badge ที่มีข้อความไทยต้องใช้:
   ```css
   .badge, .chip, .kicker {
     line-height: 1.7;   /* ≥1.7 เสมอ สำหรับอักษรไทยที่มีสระบน+ล่าง */
     height: auto;        /* ห้าม fixed height */
     overflow: visible;   /* ห้าม hidden/clip */
   }
   ```
   **Why**: บนมือถือ ข้อความไทยหายทั้งบรรทัดเพราะ line-height ต่ำเกินไป + overflow hidden ตัดสระ ในขณะที่จอคอมดูปกติ (แบงค์ จับได้ 2 ส.ค. 69, เกิดซ้ำในเด็คใหม่ 3 ส.ค.)
6. ส่งมอบ: commit repo + chip `~/.maw/inbox/` + OneDrive `iAgencyAIA/iTraining-Slides/`

## 5. Verify ก่อนส่ง (BoB gate): Two-Sided Acceptance

> **กฎ: เกณฑ์ต้องมีทั้ง 2 ด้านเสมอ** ทั้งสิ่งที่ต้องไม่มี (ข้อห้าม) และสิ่งที่ต้องยังอยู่ (ข้อบังคับ) พร้อมจำนวน
> ไฟล์เปล่าผ่านเกณฑ์ที่มีแต่ข้อห้าม, เด็คที่หายไป 28 รูปผ่านเกณฑ์ที่ไม่นับของที่ต้องมี
> Source: BoB audit 3 ส.ค. 69, เด็คข้อโต้แย้ง 6 รอบ 5 รอบเพราะ "ของใหม่ขาดสิ่งที่ของเดิมมี"

### 5A. สิ่งที่ต้องไม่มี (MUST NOT)

- [ ] em-dash / en-dash / double-hyphen: grep = 0 (T142)
- [ ] gold นอก takeaway/success: grep สี #C9A227 เฉพาะ section ที่อนุญาต
- [ ] CSS-in-JS: 0 occurrences
- [ ] interactive button/form: 0
- [ ] paragraph อธิบายบนสไลด์ (ผู้พูดเป็นคนเล่า): 0
- [ ] ภาพคนที่ไม่ใช่เอเชีย/ไทย: 0

### 5B. สิ่งที่ต้องยังอยู่ (MUST HAVE) พร้อมจำนวน

- [ ] **หน้าปก (Cover)**: 1 หน้า มี aurora title + particles + BG image
- [ ] **พื้นหลังภาพ**: ≥N หน้า (N คำนวณจากจำนวนสไลด์ที่ต้องมีภาพตาม brief)
- [ ] **Wordmark iAgencyAIA**: ทุกสไลด์ (จำนวน = จำนวนสไลด์ทั้งหมด)
- [ ] **เลขหน้า/progress**: คำนวณจาก JS (`document.querySelectorAll('.slide').length`) ห้ามพิมพ์ตายเป็นตัวเลข
- [ ] **Part divider ขาว**: ตรงจำนวน Part ตาม brief (เช่น 4 Parts = 4 dividers)
- [ ] **คำพูด/ข้อความตรงต้นฉบับ**: ตรวจนับจำนวนข้อความสำคัญ (เช่น 77/77 ประโยค)
- [ ] **ภาพ data-URI**: ทุกรูป embed เป็น data-URI (ไม่มี external URL)
- [ ] **Closing slide**: 1 หน้า มี marquee + particles + brand line
- [ ] **กลไกซ่อนสไลด์ไกล**: `.slide.far { visibility: hidden }` ต้องมีครบ 3 จุด (CSS rule + JS add/remove class + initial state) ถ้าไม่มี Safari บนมือถือจะล่มเพราะวาดทุกสไลด์พร้อมกัน

### 5C. Render Verify (3 viewports)

- [ ] desktop 1280x720: text อ่านชัดบน BG, layout ไม่ล้น
- [ ] portrait 390x844: font scale ด้วย vw, bento → 2 คอลัมน์
- [ ] landscape 844x390: font scale ด้วย vh, fit จอเตี้ย
- [ ] Screenshot ต้องถ่ายหลัง animation จบ (sleep ≥2s หลัง show)
- [ ] **badge/chip ข้อความไทย**: ต้องตรวจบน mobile จริง (ดูข้อ 4.5)
- [ ] Editor review (T142) + chip preview ส่งแบงค์

---

## 6. Brief ถาวร: ข้อมูลข้อเท็จจริงคำต่อคำ (Verbatim Facts Rule)

> **ช่องว่างในบรีฟจะถูกเติมเสมอ** ถ้าเราไม่ระบุ คนถัดไปจะเติมด้วยสิ่งที่เขาคิดว่าน่าจะใช่
> ข้อมูลทั่วไปอาจไม่เป็นไร แต่แหล่งที่มา/ตัวเลข/วันที่ คือการพูดแทนคนอื่น
> Source: BoB lesson 3 ส.ค. 69, เหตุการณ์ คปภ. ที่ไม่เคยเป็นแหล่งข้อมูล

### 6.1 ข้อมูลที่ต้องระบุคำต่อคำใน brief

| ประเภท | ตัวอย่าง | ห้ามเว้น |
|--------|---------|---------|
| แหล่งที่มา (Source line) | "Source: สมาคมประกันชีวิตไทย, InfoQuest 1 ส.ค. 69" | ห้าม: "ใส่แหล่งที่มาด้วย" (ไม่บอกว่าอะไร) |
| ตัวเลข/สถิติ | "เบี้ยรวม 341,523 ล้านบาท +4.57%" | ห้าม: "ใส่ตัวเลขจากข่าว" |
| วันที่/ช่วงเวลา | "แคมเปญ 1 ถึง 31 สิงหาคม 2569" | ห้าม: "ใส่ช่วงเวลาแคมเปญ" |
| ชื่อองค์กร/บุคคล | "ฝ่ายผลิตภัณฑ์ช่องทางตัวแทน (Agency Sales Propositions)" | ห้าม: "ใส่ชื่อฝ่าย" |

### 6.2 Template brief สำหรับ dispatch (ห้ามเว้นช่องว่าง ถ้ายังไม่รู้จำนวน = ยังไม่พร้อมสั่งงาน)

```
TASK: [ชื่องาน]
หัวข้อ: [headline คำต่อคำ]
Badge: [badge text]
ตัวเลข: [ทุกตัวเลข ระบุค่าจริง]
SOURCE LINE (คำต่อคำ ห้ามเปลี่ยน): "[exact source text]"
วันที่ข่าว: [วันที่ของ source]

โครงสร้าง (ห้ามเว้น):
  จำนวนสไลด์ทั้งหมด: [N]
  จำนวนหน้าที่ต้องมีพื้นหลังภาพ: [N จาก M]
  จำนวน Part divider: [N]
  จำนวนภาพ data-URI: [N]
  คำพูด/ข้อความสำคัญ: [N ข้อความ]

ห้าม: em-dash/en-dash/double-hyphen (T142)
```

---

## Lessons ที่ฝังในมาตรฐานนี้

- flex-column ทำ inline chip ยืดเต็มจอ → `align-self:flex-start` เสมอ (T181v2 จับได้จาก render-verify)
- pw-cli session เก็บ CWD ตอน `open` → screenshot ลง `.playwright-cli/` ของ dir นั้น
- emoji ใน headless = tofu แต่บนเครื่องจริงปกติ (ไม่ใช่ defect)
- gold-discipline คือหัวใจ mood guide: ใช้พร่ำเพรื่อ = ทำลายความหมาย "Leader Gold"
- Thai text ใน badge/chip ต้อง line-height ≥1.7 + height:auto + overflow:visible (แบงค์ จับ 2+3 ส.ค. 69: สระไทยหายบนมือถือ จอคอมดูปกติ)
- เกณฑ์รับงานต้องมี 2 ด้าน: ของที่ต้องหาย + ของที่ต้องยังอยู่พร้อมจำนวน (BoB 3 ส.ค.: เด็คหายไป 28 รูปเพราะเกณฑ์มีแต่ข้อห้าม)
- ข้อเท็จจริงใน brief ต้องคำต่อคำ ช่องว่างจะถูกเติม (BoB 3 ส.ค.: คปภ. ถูกเติมเพราะไม่ได้ระบุ source verbatim)
- เลขหน้า/จำนวนสไลด์ต้องคำนวณจาก DOM ห้ามพิมพ์ตาย (BoB 3 ส.ค.: พื้นหลังกี่หน้าจากกี่หน้า)
- ขนาดไฟล์ไม่ใช่สาเหตุที่เด็คล่ม: t56 หนัก 1,854KB เปิดได้ปกติ, t1 แค่ 54KB เคยล่ม ตัวแปรเดียวคือมีกลไกซ่อนสไลด์ `.far` หรือไม่ (BoB 3 ส.ค.: เดาผิดเรื่องขนาดไฟล์ครึ่งวัน สาเหตุจริงคือ Safari วาดทุกสไลด์พร้อมกันเมื่อไม่มี visibility:hidden)
