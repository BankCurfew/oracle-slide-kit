/* iTraining series deck (T1-T6) · T2194 · navigation + slide effects.
   Nav: keys (→ Space PageDown / ← PageUp / Home End), swipe (dx > 48), tap (right 2/3 = next, left 1/3 = back),
   counter + progress + dots. Uses the oracle-slide-kit stepper hook: a slide may carry
   el.stepper = { next(), prev(), enter(dir) } (see components/timeline + template/deck-template.html).
   Thai is never split mid-word: masks work on whole <br> lines, the reading reveal on dictionary words. */
(function () {
  'use strict';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const deck = document.getElementById('deck');
  const slides = [...deck.querySelectorAll('.slide')];
  const dots = document.getElementById('dots');
  const cur = document.getElementById('cur');
  const prog = document.getElementById('prog');
  document.getElementById('tot').textContent = slides.length;

  /* ---------- prepare effects ---------- */
  // 21st 19257 Text Reveal (Mask): part titles + questions, one mask per <br> line
  deck.querySelectorAll('.part:not(.notes) h2, .q .qtext').forEach((h) => {
    const lines = h.innerHTML.split(/<br\s*\/?>/i);
    h.innerHTML = lines.map((l) => '<span class="ml"><span class="mi">' + l + '</span></span>').join('');
    h.classList.add('mask');
  });
  // 21st 9386 Reading Text Reveal: the takeaway quote lights up word by word (Intl.Segmenter keeps Thai words whole)
  const seg = window.Intl && Intl.Segmenter ? new Intl.Segmenter('th', { granularity: 'word' }) : null;
  deck.querySelectorAll('.quote .one').forEach((el) => {
    let w = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((c) => {
        if (c.nodeType === 3) {
          const parts = seg ? [...seg.segment(c.textContent)].map((s) => s.segment) : c.textContent.split(/(\s+)/);
          const frag = document.createDocumentFragment();
          parts.forEach((p) => {
            if (!p.trim()) { frag.appendChild(document.createTextNode(p)); return; }
            const s = document.createElement('span');
            s.className = 'w'; s.style.setProperty('--w', w++); s.textContent = p;
            frag.appendChild(s);
          });
          c.replaceWith(frag);
        } else if (c.nodeType === 1 && c.tagName !== 'BR') walk(c);
      });
    };
    walk(el);
  });
  // 21st 989 Spotlight on the cover (follows the pointer on desktop, static on touch)
  deck.querySelectorAll('.cover').forEach((s) => {
    const l = document.createElement('div'); l.className = 'spot-light'; s.prepend(l);
    s.addEventListener('pointermove', (e) => {
      if (e.pointerType !== 'mouse') return;
      const r = s.getBoundingClientRect();
      s.style.setProperty('--mx', (e.clientX - r.left) + 'px'); s.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
  // 21st 26797 + 1567: card spotlight follows the pointer; glow sweeps the cards in order on enter
  deck.querySelectorAll('.slide').forEach((s) => s.querySelectorAll('.card.spot').forEach((c, k) => {
    c.style.setProperty('--ci', k);
    c.addEventListener('pointermove', (e) => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  }));
  // light rays on the break, background circles (21st 664) on the close
  deck.querySelectorAll('.brk').forEach((s) => { const r = document.createElement('div'); r.className = 'rays'; s.prepend(r); });
  deck.querySelectorAll('.close').forEach((s) => {
    const c = document.createElement('div'); c.className = 'circles'; c.setAttribute('aria-hidden', 'true');
    c.innerHTML = '<i></i><i></i><i></i>'; s.prepend(c);
  });

  // work cycle: ring on the stepper (landscape) / vertical stepper with a loop-back arrow (portrait)
  deck.querySelectorAll('.cyc').forEach((s) => {
    const wrap = s.querySelector('.cycwrap');
    const items = [...s.querySelectorAll('.ring li')];
    const n = items.length;
    items.forEach((li) => { const node = document.createElement('div'); node.className = 'node'; while (li.firstChild) node.appendChild(li.firstChild); li.appendChild(node); });
    const C = 2 * Math.PI * 50;
    wrap.insertAdjacentHTML('afterbegin',
      '<svg class="ring-svg" viewBox="0 0 100 100" aria-hidden="true">' +
      '<circle class="trk" cx="50" cy="50" r="50" vector-effect="non-scaling-stroke"/>' +
      '<circle class="arc" cx="50" cy="50" r="50" transform="rotate(-90 50 50)" vector-effect="non-scaling-stroke" stroke-dasharray="' + C + '" stroke-dashoffset="' + C + '"/>' +
      '<path class="loop" d="M 38 -1 A 12 12 0 0 1 50 -12" vector-effect="non-scaling-stroke"/></svg>');
    wrap.insertAdjacentHTML('afterend', '<div class="loopback" aria-hidden="true">↺ 1</div>');
    // the closing lines appear once the loop closes
    s.querySelectorAll('.sub, .foot').forEach((el) => { el.classList.remove('rv'); el.classList.add('after'); });
    const arc = wrap.querySelector('.arc');
    let step = 0;
    const draw = () => {
      items.forEach((li, k) => { li.classList.toggle('on', k < step); li.classList.toggle('cur', k === step - 1); });
      const frac = step >= n ? 1 : Math.max(0, step - 1) / n;
      arc.setAttribute('stroke-dashoffset', String(C * (1 - frac)));
      s.classList.toggle('done', step >= n);
    };
    s.stepper = {
      next() { if (reduce || step >= n) return false; step++; draw(); return true; },
      prev() { if (reduce || step <= 0) return false; step--; draw(); return true; },
      enter(dir) { step = reduce ? n : (dir < 0 ? n : 0); draw(); },
      get step() { return step; },
      get steps() { return n; },
    };
  });

  // generic tap-to-reveal (T2229): a slide with .stp children reveals them one per tap (stepper hook), all at once when reduced motion
  deck.querySelectorAll('.slide').forEach((s) => {
    const st = [...s.querySelectorAll('.stp')];
    if (!st.length || s.stepper) return;
    const n = st.length; let step = 0;
    const draw = () => { st.forEach((el, k) => el.classList.toggle('shown', k < step)); s.classList.toggle('revealed', step >= n); };
    s.stepper = {
      next() { if (reduce || step >= n) return false; step++; draw(); return true; },
      prev() { if (reduce || step <= 0) return false; step--; draw(); return true; },
      enter(dir) { step = reduce ? n : (dir < 0 ? n : 0); draw(); },
      get step() { return step; }, get steps() { return n; },
    };
  });

  /* ---------- navigation ---------- */
  let i = 0;
  slides.forEach((_, k) => { const b = document.createElement('button'); b.className = 'dot'; b.setAttribute('aria-label', String(k + 1)); b.onclick = (e) => { e.stopPropagation(); go(k); }; dots.appendChild(b); });
  const dot = [...dots.children];
  const isLight = (s) => s.classList.contains('part');
  function go(n) {
    const was = i;
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, k) => s.classList.toggle('on', k === i));
    dot.forEach((d, k) => d.classList.toggle('on', k === i));
    document.body.classList.toggle('light', isLight(slides[i]));
    cur.textContent = i + 1;
    prog.style.width = ((i + 1) / slides.length * 100) + '%';
    const s = slides[i].stepper;
    if (s && (i !== was || n === was)) s.enter(i >= was ? 1 : -1);
  }
  function fwd() { const s = slides[i].stepper; if (s && s.next()) return; go(i + 1); }
  function back() { const s = slides[i].stepper; if (s && s.prev()) return; go(i - 1); }
  document.getElementById('next').onclick = (e) => { e.stopPropagation(); fwd(); };
  document.getElementById('prev').onclick = (e) => { e.stopPropagation(); back(); };
  addEventListener('keydown', (e) => {
    if (['ArrowRight', ' ', 'PageDown'].includes(e.key)) { e.preventDefault(); fwd(); }
    if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); back(); }
    if (e.key === 'Home') go(0);
    if (e.key === 'End') go(slides.length - 1);
  });
  // swipe; a swipe must not also count as a tap
  let x0 = null, swiped = 0;
  addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', (e) => {
    if (x0 == null) return;
    const dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 48) { swiped = Date.now(); (dx < 0 ? fwd : back)(); }
  }, { passive: true });
  // tap: right 2/3 = next, left 1/3 = back. Inside SharedDocument (iframe/blob) the first tap also gives the deck key focus.
  deck.addEventListener('click', (e) => {
    deck.focus({ preventScroll: true });
    if (Date.now() - swiped < 450) return;
    if (e.target.closest('a,button,input,textarea,select')) return;
    (e.clientX < innerWidth / 3 ? back : fwd)();
  });
  deck.focus({ preventScroll: true });
  go(0);
  window.__deck = { go, fwd, back, get i() { return i; }, get n() { return slides.length; } };
})();
