/* cine.js · T3503 cinematic kit (designer direction 21acc9bd, fe build) · PREVIEW ONLY until แบงค์ OKs the REVIEW
 * Wires the pieces in cine.css onto deck.js, without changing deck.js:
 *   data-cam="push:1.06:8000"          BG photo push, once, holds the end (css)
 *   data-cam="pan:y:-24:1600:500"       the .cine-cam TEXT block glides (css; ms, delay)
 *   data-depth="0.4"                    a layer that follows the camera at that factor (css vars set here)
 *   data-fly="<key>"  (source + target) FLIP flight between two slides, 640 ms, move curve; a tap mid-flight lands it
 *   data-keep="<key>" (both slides)     stays put across the pair: no re-reveal; the target slide is padded so it lines up
 *   data-exit / data-enter              rows that leave (up + fade 240 ms) / arrive (rise 320 ms, stagger 60 ms)
 *   data-sweep[="ms after show"]        one light pass inside the letters, 640 ms
 * Slides that are not showing are display:none, so positions are snapshotted BEFORE deck.js moves (capture-phase
 * input listeners) and whenever the showing slide settles. Reduced motion: no flight / sweep / push / pan (end frames).
 */
(() => {
  if (window.__cine) return; window.__cine = 1;
  const RM = matchMedia('(prefers-reduced-motion: reduce)'), MOVE = 'cubic-bezier(.65,0,.35,1)', IN = 'cubic-bezier(.22,1,.36,1)';
  const slides = [...document.querySelectorAll('.slide')];
  let cur = slides.findIndex(s => s.classList.contains('on')), snap = null, flying = [];

  // ---- cam / depth: turn the data attributes into the css vars cine.css reads ----
  for (const s of slides) {
    const c = (s.dataset.cam || '').split(':');
    if (c[0] === 'push') { s.style.setProperty('--cam-scale', c[1] || 1.06); s.style.setProperty('--cam-ms', (c[2] || 8000) + 'ms'); }
    if (c[0] === 'pan') { s.style.setProperty('--pan-y', (c[2] || -24) + 'px'); s.style.setProperty('--pan-ms', (c[3] || 1600) + 'ms'); s.style.setProperty('--pan-delay', (c[4] || 0) + 'ms'); }
    s.querySelectorAll('[data-depth]').forEach(l => {
      const f = Number(l.dataset.depth) || 0.4;
      if (c[0] === 'push') l.style.setProperty('--depth-scale', 1 + ((Number(c[1]) || 1.06) - 1) * f);
      if (c[0] === 'pan') l.style.setProperty('--depth-y', ((Number(c[2]) || -24) * f) + 'px');
    });
    // sweep: a white copy of the text, masked by a moving band (stays inside the letters)
    s.querySelectorAll('[data-sweep]').forEach(el => {
      el.classList.add('cine-sweep-host');
      const g = document.createElement('span'); g.className = 'cine-sweep'; g.setAttribute('aria-hidden', 'true'); g.textContent = el.textContent;
      const cs = getComputedStyle(el); g.style.font = cs.font; g.style.letterSpacing = cs.letterSpacing; g.style.lineHeight = cs.lineHeight; g.style.textAlign = cs.textAlign;
      el.appendChild(g);
    });
  }

  // ---- snapshot: positions + looks of the flight / keep / exit elements on the showing slide ----
  const take = () => {
    const s = slides[cur]; if (!s) return;
    const LOOK = ['font', 'color', 'letterSpacing', 'lineHeight', 'textAlign', 'whiteSpace'];   // inherited looks a body-level copy would lose
    const pick = sel => [...s.querySelectorAll(sel)].map(el => { const cs = getComputedStyle(el);
      return { el, key: el.dataset.fly || el.dataset.keep, r: el.getBoundingClientRect(), look: Object.fromEntries(LOOK.map(k => [k, cs[k]])) }; }).filter(x => x.r.width);
    snap = { from: cur, fly: pick('[data-fly]'), keep: pick('[data-keep]'), exit: pick('[data-exit]') };
  };
  ['keydown', 'pointerdown', 'touchstart', 'click'].forEach(t => addEventListener(t, take, { capture: true, passive: true }));
  addEventListener('resize', () => setTimeout(take, 50));

  const finishFlights = () => { flying.forEach(a => { try { a.finish(); } catch {} }); flying = []; };
  // interruptible: a tap mid-flight lands it, and that tap does nothing else (the deck does not also move)
  let swallow = false;
  addEventListener('pointerdown', e => { if (flying.some(a => a.playState === 'running')) { swallow = true; finishFlights(); e.stopImmediatePropagation(); } }, { capture: true });
  addEventListener('click', e => { if (swallow) { swallow = false; e.stopImmediatePropagation(); e.preventDefault(); } }, { capture: true });

  const ghost = (x, inner) => {   // a fixed copy of an element at its old place (the source slide is gone already)
    const g = x.el.cloneNode(true); g.classList.add('cine-ghost'); g.querySelectorAll('.cine-sweep').forEach(n => n.remove());
    g.removeAttribute('data-fly'); g.removeAttribute('data-keep'); g.removeAttribute('data-exit');
    Object.assign(g.style, x.look, { left: x.r.left + 'px', top: x.r.top + 'px', width: x.r.width + 'px', height: x.r.height + 'px', animation: 'none', opacity: 1, transform: 'none' });
    (inner || document.body).appendChild(g); return g;
  };

  // ---- one transition: from snap.from to the slide that just got .on ----
  const onShow = (to) => {
    const s = slides[to], from = snap && snap.from;
    const adjacent = snap && from !== to && from !== -1;
    // keep: line the target up with the source (pad its top), no re-reveal
    if (adjacent && snap.keep.length) {
      const tk = [...s.querySelectorAll('[data-keep]')];
      const pair = snap.keep.map(k => [k, tk.find(t => t.dataset.keep === k.key)]).filter(p => p[1]);
      if (pair.length) {
        pair.forEach(([, t]) => t.classList.add('cine-still'));   // first: no entry offset in what we measure
        s.style.paddingTop = ''; const base = parseFloat(getComputedStyle(s).paddingTop) || 0; let pad = 0;
        for (let n = 0; n < 4; n++) {   // a centred slide moves by dy/2 per px of padding: converge instead of guessing
          const dy = pair[0][0].r.top - pair[0][1].getBoundingClientRect().top; if (Math.abs(dy) <= 0.5) break;
          pad += dy * (getComputedStyle(s).justifyContent === 'center' ? 2 : 1); s.style.paddingTop = Math.max(0, base + pad) + 'px';
        }
      }
    } else s.querySelectorAll('.cine-still').forEach(t => t.classList.remove('cine-still'));
    if (!(adjacent && snap.keep.length)) s.querySelectorAll('[data-fly].cine-still').forEach(t => t.classList.remove('cine-still'));
    if (RM.matches) { take(); return; }
    // exit: the old rows leave (they are gone from the DOM view; ghosts carry the move)
    if (adjacent && snap.exit.length && s.querySelector('[data-enter]')) snap.exit.forEach(x => {
      const g = ghost(x); g.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(-16px)' }], { duration: 240, easing: 'ease-in', fill: 'forwards' }).finished.then(() => g.remove(), () => g.remove());
    });
    // enter: the new rows rise, stagger 60 ms (after the exit)
    s.querySelectorAll('[data-enter]').forEach(box => {
      if (!(adjacent && snap.exit.length)) return; box.classList.add('cine-rows');
      [...box.querySelectorAll('tbody tr, .rc')].forEach((row, i) => row.animate([{ opacity: 0, transform: 'translateY(14px)' }, { opacity: 1, transform: 'none' }],
        { duration: 320, delay: 200 + i * 60, easing: IN, fill: 'backwards' }));
    });
    // flight: source copy flies (translate + scale) onto the target, which is hidden until it lands
    if (adjacent) snap.fly.forEach(x => {
      const t = [...s.querySelectorAll('[data-fly]')].find(e => e.dataset.fly === x.key); if (!t) return;
      t.classList.add('cine-hold');
      requestAnimationFrame(() => {   // the target's layout after this slide's first frame
        const tr = t.getBoundingClientRect(), g = ghost(x), k = tr.height / x.r.height;
        const a = g.animate([{ transform: 'none', opacity: 1 }, { transform: `translate(${tr.left - x.r.left}px,${tr.top - x.r.top}px) scale(${k})`, opacity: 1 }],
          { duration: 640, easing: MOVE, fill: 'forwards' });
        flying.push(a);
        const land = () => { t.classList.add('cine-still'); t.classList.remove('cine-hold'); g.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 160, fill: 'forwards' }).finished.then(() => g.remove(), () => g.remove()); };
        a.finished.then(land, land);
      });
    });
    // sweep: one pass after the entry (data-sweep = ms after show, default 900)
    s.querySelectorAll('.cine-sweep').forEach(g => { g.classList.remove('go'); const ms = Number(g.parentNode.dataset.sweep) || 900;
      setTimeout(() => { if (slides[to].classList.contains('on')) { void g.offsetWidth; g.classList.add('go'); } }, ms); });
    setTimeout(() => { if (cur === to) take(); }, 1300);   // settled positions for the next move
  };

  new MutationObserver(() => {
    const now = slides.findIndex(s => s.classList.contains('on'));
    if (now === -1 || now === cur) return;
    finishFlights(); cur = now; onShow(now);
  }).observe(document.getElementById('deck') || document.body, { subtree: true, attributes: true, attributeFilter: ['class'] });
  if (cur >= 0) onShow(cur);   // the opening slide (no move into it, so no flight / keep)
  setTimeout(take, 1300);
})();
