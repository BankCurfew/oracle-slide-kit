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
5. ส่งมอบ: commit repo + chip `~/.maw/inbox/` + OneDrive `iAgencyAIA/iTraining-Slides/`

## 5. Verify ก่อนส่ง (BoB gate)

- [ ] Render-verify จริง 3 viewport: desktop 1280x720 · portrait 390x844 · landscape 844x390
- [ ] Eyeball screenshot: text อ่านชัดบน BG, chip/badge ไม่ยืดเต็มจอ (`align-self:flex-start` บน flex-column), ไม่มี layout ล้น
- [ ] Screenshot ต้องถ่ายหลัง animation จบ (sleep ≥2s หลัง show)
- [ ] gold ปรากฏเฉพาะ takeaway/success · em-dash grep = 0 · wordmark ครบทุกหน้า
- [ ] Editor review (T142) + chip preview ส่งแบงค์

## Lessons ที่ฝังในมาตรฐานนี้

- flex-column ทำ inline chip ยืดเต็มจอ → `align-self:flex-start` เสมอ (T181v2 จับได้จาก render-verify)
- pw-cli session เก็บ CWD ตอน `open` → screenshot ลง `.playwright-cli/` ของ dir นั้น
- emoji ใน headless = tofu แต่บนเครื่องจริงปกติ (ไม่ใช่ defect)
- gold-discipline คือหัวใจ mood guide: ใช้พร่ำเพรื่อ = ทำลายความหมาย "Leader Gold"
