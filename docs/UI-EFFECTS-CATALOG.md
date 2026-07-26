# UI Effects Catalog · Magic UI + 21st.dev (สำหรับ iAgencyAIA Slides)

> Companion ของ CONDUCT-SLIDE-001 · fetched จากเว็บจริง 2026-07-26 · BoB
> ใช้เลือก effect ต่อ deck: ทุกตัว mark ว่า vanilla-portable ไหม (สไลด์เรา = ไฟล์เดียว offline, ไม่มี React)

## 1. Magic UI — full component list (magicui.design/docs/components)

| Category | Components |
|---|---|
| Special Effects | Animated Beam, Border Beam, Shine Border, Magic Card, Glare Hover, Meteors, Confetti, Particles, Animated Theme Toggler |
| Animations | Blur Fade |
| Text Animations | Text Animate, Typing Animation, Line Shadow Text, Aurora Text, Video Text, Number Ticker, Animated Shiny Text, Animated Gradient Text, Text Reveal, Dia Text Reveal, Hyper Text, Word Rotate, Scroll Based Velocity, Sparkles Text, Morphing Text, Spinning Text, Text Highlighter, Text 3D Flip |
| Device Mocks | Safari, iPhone, Android |
| Buttons | Rainbow Button, Shimmer Button, Ripple Button |
| Backgrounds | Flickering Grid, Animated Grid Pattern, Retro Grid, Ripple, Dot Pattern, Grid Pattern, Hexagon Pattern, Striped Pattern, Interactive Grid Pattern, Light Rays, Noise Texture |
| Community | Shiny Button, File Tree, Code Comparison, Scroll Progress, Neon Gradient Card, Comic Text, Kinetic Text, Cool Mode, Pixel Image, Pulsating Button, Warp Background, Interactive Hover Button, Animated Circular Progress Bar, Backlight, Glyph Matrix |
| Main | Marquee, Terminal, Hero Video Dialog, Bento Grid, Animated List, Dock, Globe, Tweet Card, Orbiting Circles, Avatar Circles, Icon Cloud, Lens, Pointer, Smooth Cursor, Progressive Blur, Dotted Map |

## 2. 21st.dev — categories (2,000+ marketing blocks / 2,100+ UI components)

- Marketing: animated heroes, hero sections, **shaders**, **liquid & metal effects**, backgrounds, **gradient meshes**, footers
- UI: buttons, AI chats, cards & grids, galleries & 3D carousels, navigation, sign-ins, sections
- Libraries รวมใน registry: Aceternity UI, Magic UI, Origin UI, Motion Primitives ฯลฯ (700+ contributors)

## 3. Fit matrix สำหรับ slide deck (คัดแล้ว)

### ✅ ใช้ (เหมาะ brand "Quiet Confidence" + vanilla ได้)
| Effect | ที่มา | ใช้ตรงไหน | Vanilla |
|---|---|---|---|
| **Light Rays** | Magic UI bg | cover + closing: ลำแสงจากบนลงล่าง premium | conic/linear gradient แถบเฉียง + blur + animation opacity |
| **Animated Grid Pattern** | Magic UI bg | สไลด์คำถามมืด: เส้น grid วิ่งจางๆ แทน dot นิ่ง | CSS bg-position keyframe |
| **Noise Texture** | Magic UI bg | divider ขาว: ผิวกระดาษ editorial | SVG feTurbulence data-URI |
| **Ripple** | Magic UI bg | speakers: วงคลื่นหลัง avatar | CSS ring scale keyframes |
| **Magic Card** | Magic UI fx | speaker cards + bento: gradient border ตามเมาส์ | radial-gradient at var(--mx) |
| **Glare Hover** | Magic UI fx | bento cells: แสง sweep ตอน hover/เข้า | ::after skew translate keyframe |
| **Sparkles Text** | Magic UI text | คำ key บน cover | tiny absolute ✦ spans + twinkle |
| **Word Rotate** | Magic UI text | cover: อาชีพหมุน (แอร์โฮสเตส→พนักงานออฟฟิศ→...) | keyframe translateY stack |
| **Line Shadow Text** | Magic UI text | เลข Part ยักษ์: เงาเส้นเฉียง editorial | text-shadow ซ้อน + stripe gradient clip |
| **Box/Text Reveal** | Magic UI text | คำถามโผล่จากแถบแดง sweep | ::after block slide-away |
| **Confetti** | Magic UI fx | closing "ขอบคุณ" burst ครั้งเดียว | canvas ~80 ชิ้น one-shot |
| **Avatar Circles** | Magic UI | speakers/closing | รูปวงซ้อน border แดง |
| **Progressive Blur** | Magic UI | ขอบภาพ BG ละลายเข้าพื้น | mask-image linear-gradient |
| **Gradient Mesh hero** | 21st.dev | divider ขาว: blob แดง/salmon เบลอเคลื่อนช้า | 2-3 radial-gradient blobs + keyframe |
| เดิมจาก v2 (คงไว้) | | Aurora Text, Number Ticker, Border Beam, Blur-Fade, Bento, Ken Burns, Particles, Marquee, Spotlight, Glass, Swipe, Dots nav | ✓ ทั้งหมด |

### ❌ ไม่ใช้ (เหตุผล)
- Meteors, Warp Background, Retro Grid, Glyph Matrix, Terminal: sci-fi/tech เกิน brand ประกัน (Designer T143 note เดิม)
- Comic Text, Cool Mode, Pixel Image: playful เกิน
- Globe, Dotted Map, Icon Cloud, Tweet Card, Device Mocks, Dock, File Tree: ไม่เข้า context สัมภาษณ์
- Lens, Smooth Cursor, Animated Theme Toggler: interaction เกินจำเป็นบนโปรเจกเตอร์
- Liquid metal shaders (21st): ต้อง WebGL จริง, หนัก + เสี่ยงบนมือถือ; ใช้ gradient mesh แทน

## 4. กติกาการใช้ (ผูกกับ CONDUCT-SLIDE-001)
1. สไลด์ = **ให้ผู้ฟังดู ไม่ใช่คำอธิบาย**: หัวเรื่อง + คำถาม + คำสั้น เท่านั้น, ห้าม paragraph อธิบาย (ผู้พูดเป็นคนเล่า)
2. ≤3 effect เด่นต่อสไลด์ (แสง+text+entrance) ไม่ stack จนรก
3. ภาพคน = **คนเอเชีย/ไทยเสมอ** (แบงค์ order 2026-07-26)
4. gold = success moment เท่านั้น (เดิม)
5. ทุก effect ต้อง vanilla CSS/JS ในไฟล์เดียว + ผ่าน mobile ทั้ง 2 แนว
