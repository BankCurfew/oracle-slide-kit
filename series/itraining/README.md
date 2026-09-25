# iTraining series template (T1-T6) · T2194

One deck = one self-contained HTML file (inline CSS/JS, images embedded once, Google Fonts only), so it works when
FA Tools shows it inside `MaterialViewer` (`<iframe srcDoc sandbox="allow-scripts allow-same-origin">`).

| Path | What |
|---|---|
| `deck.css` | Series look, CONDUCT-SLIDE-001 v1.3: charcoal content, white editorial part dividers + notes, AIA red #D31145 (text only on white), salmon emphasis on charcoal, gold only on the takeaway slide |
| `deck.js` | Nav (keys, swipe, tap right 2/3 = next / left 1/3 = back, counter, progress, dots) + the kit's `slide.stepper` hook + effects |
| `t1-mindset/build.py` | T1 content (verbatim, from Designer-Oracle 5d1209b) → `output/itraining-t1-mindset.html` |
| `t4-product-approach/build.py` | T4 content (writer inventory + rulings R1-R7, verbatim) → `output/itraining-t4-product-approach.html` (T2229) |
| `t4-product-approach/make_rulings.py` | The writer's recorded rulings as a parity map → `rulings.json` |
| `tools/parity.py` | Every line of the writer's inventory is on its slide, in order: `parity.py <inventory.md> <deck.html>` · `--rulings rulings.json` applies ruled replacements/additions · `--order` checks line order across the whole deck when question slides were split (T4: 28 → 37 slides) |

## Slide types (class on `<section class="slide ...">`)
`cover` (21st 989 spotlight) · `part` white divider with giant part number (19257 mask reveal on the title) ·
`q` question (19257 mask) · `ans` cards `.card.spot` (26797 spotlight + 1567 glow, red/salmon) · `appr` compare with `.star` (26826) ·
`cyc` work-cycle ring driven by the stepper, vertical stepper in portrait (29815) · `part notes` writing page (1536 grid) ·
`brk` break (light rays) · `quote` takeaway (9386 reading reveal, the only gold) · `close` (664 background circles + marquee).
T2229 additions (reusable T2-T6): `part ed` white editorial section slide with content · `chn` channel chip · `thread` + `bub me/them` chat bubbles (29393) ·
`flow` chevron chain (`lite` = pills light up in order) · `hstep` horizontal stepper, vertical at portrait (29815) · `smap` 6-slot series map · `ladder` + `axis` graded channel ladder ·
`table.obj` objection table (chat pairs at 390) · `shot` + `phone` screenshot in a phone frame (6474) · `.stp` tap-to-reveal steps (generic stepper in deck.js) · `scroll` slide may scroll in short landscape/portrait.
Backgrounds: `img` + `data-bg="<name>"` (photo + charcoal/red overlay) or `dots` (drifting dot grid).

## New episode (T2-T6)
1. Copy `t1-mindset/` to `t2-.../`, keep `SERIES` pointing at `..`, replace the `SLIDES` list with the writer-checked content.
2. `python3 build.py` → `output/itraining-tN-*.html`, then `tools/parity.py` against the writer's inventory (must be N of N).
3. Render check at 390×844 · 844×390 · 1280×720 (FE-Oracle `scripts/t2194-deck-verify.js`) and inside the SharedDocument replica
   (`scripts/t2194-shareddoc-sim.js`), then designer G1.

Rules: Thai is never split mid-word (masks work on whole `<br>` lines, the reading reveal on `Intl.Segmenter` words) ·
reduced motion = final states, ring fully drawn · no em/en dashes (build asserts) · content text ≥ 28px @1920.
