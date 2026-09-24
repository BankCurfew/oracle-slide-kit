# oracle-slide-kit: Directory

> Updated: 2026-07-23 | Maintained by Forge Oracle

## File Index

| Path | Description | Owner | Status |
|------|-------------|-------|--------|
| `README.md` | Overview + quick start | Forge | Done |
| `CLAUDE.md` | Repo identity + conduct | Forge | Done |
| `DIRECTORY.md` | This file | Forge | Done |
| `docs/HOW-IT-WORKS.md` | System architecture, tech stack, render flow | Prism | Placeholder |
| `docs/PLAYBOOK.md` | Full creation workflow: brief to deliver | Quill | Placeholder |
| `docs/CAR-PAR-slide-production.md` | CAR-PAR process for slide production | Nobi | Pending assembly |
| `docs/SOP-SLIDE-001.md` | QA checklist + delivery SOP | Lens | Placeholder |
| `template/deck-template.html` | Master HTML slide template; `slide.stepper` hook (next/prev/enter) for step-driven slides (T2182) | Prism | Placeholder |
| `components/timeline/timeline-slide.js` + `.css` | Step-driven timeline slide (T2182): JSON data, presets aia-dark / aia-light / wb-prestige, portrait vertical, reduced motion | FE | Done (designer G1 pending) |
| `components/timeline/timeline-demo.html` | Demo deck (7 milestones incl. Thai, 3 presets); `build-demo.py` inlines it to `output/timeline-demo.html` | FE | Done |
| `examples/T1-simple/` | Type 1 (simple) reference deck | Prism/team | Empty |
| `examples/T2-advanced/` | Type 2 (advanced) reference deck | Prism/team | Empty |

## Status

Scaffold created 2026-07-23 (Forge, nobi#102). Content owners fill placeholders:
- Prism: HOW-IT-WORKS + deck-template.html + examples
- Quill: PLAYBOOK
- Nobi: CAR-PAR-slide-production.md (source: ~/.maw/inbox/20260723_slide-kit-car-par.md)
- Lens: SOP-SLIDE-001 (number + team เติม)
