/* Timeline slide (T2182) · step-driven port of 21st.dev "Product Timeline" (Hyperiux Vault).
   Needs GSAP 3.13.0 (cdnjs gsap.min.js). No ScrollTrigger, no SplitText: Thai is revealed per block, never split.

   Use in a deck (template/deck-template.html has the stepper hook):
     <section class="slide tl-slide" data-timeline data-tl-preset="aia-dark"> holding one
       script tag of type application/json with
       {"periodLabel":"2012 · 2026","title":"...","items":[
         {"year":"2012","month":"","title":"...","text":"...","row":"top","highlight":false}]}
     (see timeline-demo.html; this comment must never contain a closing script tag, the demo inlines this file)
   Auto-mounts every [data-timeline] on load, or call TimelineSlide.mount(sectionEl, data).
   Sets sectionEl.stepper = { next(), prev(), enter(dir) }:
     step 0 = heading only · step k = milestones 1..k shown · next() returns false after the last one,
     prev() returns false at step 0, enter(1) = step 0, enter(-1) = fully revealed.
   Reduced motion (or no GSAP): every milestone shown, no tweens; steps only pan the track while
   something is still off screen, then return false. */
(function () {
  'use strict';
  const mq = (q) => window.matchMedia && window.matchMedia(q).matches;
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const THAI = /[\u0E00-\u0E7F]/;
  const langOf = (s) => (THAI.test(s || '') ? 'th' : 'en');

  function render(slide, data) {
    const items = (data.items || []).map((it, k) => Object.assign({}, it, { row: it.row || (k % 2 ? 'bottom' : 'top') }));
    const ms = items.map((it, k) => {
      const when = [it.month, it.year].filter(Boolean).join(' ');
      return '<div class="tl-m' + (it.highlight ? ' is-hl' : '') + '" data-row="' + (it.row === 'bottom' ? 'bottom' : 'top') + '" style="--i:' + k + '">' +
        '<span class="tl-stem"></span><span class="tl-dot"></span>' +
        '<div class="tl-year tl-b">' + esc(when) + '</div>' +
        '<div class="tl-title tl-b" lang="' + langOf(it.title) + '">' + esc(it.title) + '</div>' +
        (it.text ? '<div class="tl-text tl-b" lang="' + langOf(it.text) + '">' + esc(it.text) + '</div>' : '') +
        '</div>';
    }).join('');
    const root = document.createElement('div');
    root.className = 'tl';
    root.innerHTML =
      '<div class="tl-head">' +
        (data.periodLabel ? '<div class="tl-period rv">' + esc(data.periodLabel) + '</div>' : '') +
        (data.title ? '<h2 class="tl-heading rv" lang="' + langOf(data.title) + '">' + esc(data.title) + '</h2>' : '') +
      '</div>' +
      '<div class="tl-view"><div class="tl-track">' +
        '<span class="tl-line"></span><span class="tl-fill"></span><span class="tl-cap"></span>' + ms +
      '</div></div>';
    slide.querySelectorAll('.tl').forEach((n) => n.remove());
    slide.appendChild(root);
    return { root, n: items.length };
  }

  function mount(slide, data) {
    const { root, n } = render(slide, data);
    const view = root.querySelector('.tl-view');
    const track = root.querySelector('.tl-track');
    const fill = root.querySelector('.tl-fill');
    const ms = [...root.querySelectorAll('.tl-m')];
    const part = ms.map((m) => ({ stem: m.querySelector('.tl-stem'), dot: m.querySelector('.tl-dot'), blocks: [...m.querySelectorAll('.tl-b')] }));
    const g = window.gsap;
    let step = 0;
    let vert = false;
    let live = []; // running tweens, finished instantly on the next input

    const still = () => !g || mq('(prefers-reduced-motion: reduce)');

    function layout() {
      vert = mq('(max-width: 680px)');
      if (vert) {
        track.style.width = '';
        root.style.removeProperty('--tl-step');
        root.style.removeProperty('--tl-col');
      } else {
        const w = view.clientWidth;
        const stepPx = w / 3.2; // about 3 milestones in view (designer font floor)
        const col = stepPx * 1.75; // rows alternate, so a column may span ~2 steps
        const pad = parseFloat(getComputedStyle(root).fontSize) * 1.4;
        root.style.setProperty('--tl-step', stepPx + 'px');
        root.style.setProperty('--tl-col', col + 'px');
        root.style.setProperty('--tl-pad', pad + 'px');
        track.style.width = Math.max(w, pad + (n - 1) * stepPx + col) + 'px';
      }
    }

    // centre of milestone k's dot along the line, in track coordinates (-1 = start of line)
    function anchor(k) {
      if (k < 0) return 0;
      const d = part[k].dot.getBoundingClientRect();
      const t = track.getBoundingClientRect();
      return vert ? d.top + d.height / 2 - t.top : d.left + d.width / 2 - t.left;
    }
    function viewSize() { return vert ? view.clientHeight : view.clientWidth; }
    function trackSize() { return vert ? track.scrollHeight : track.offsetWidth; }
    function offsetFor(k) {
      const max = Math.max(0, trackSize() - viewSize());
      return -Math.max(0, Math.min(max, anchor(k) - viewSize() * 0.4)); // active lands at ~40%, never past the ends
    }

    // soft edge on each side that still hides content (off = track offset, <= 0)
    function edges(off) {
      const max = Math.max(0, trackSize() - viewSize());
      view.classList.toggle('fade-a', -off > 1);
      view.classList.toggle('fade-b', -off < max - 1);
    }

    function finish() { live.forEach((t) => t.progress(1)); live = []; }

    function setShown(k, on) {
      const p = part[k];
      if (g) {
        g.set(p.stem, { scaleY: on ? 1 : 0 });
        g.set(p.dot, { scale: on ? 1 : 0 });
        g.set(p.blocks, { autoAlpha: on ? 1 : 0, y: on ? 0 : 12 });
      } else {
        [p.stem, p.dot, ...p.blocks].forEach((el) => { el.style.visibility = on ? '' : 'hidden'; });
      }
    }

    function setActive(k) { ms.forEach((m, j) => m.classList.toggle('is-active', j === k && !still())); }

    // move the track + grow the line so milestone k (index) is in view
    function place(k, animate) {
      const axis = vert ? 'y' : 'x';
      const off = offsetFor(k);
      const len = still() ? trackSize() : anchor(k);
      const size = vert ? 'height' : 'width';
      edges(off);
      if (g) {
        g.set(track, vert ? { x: 0 } : { y: 0 });
        if (animate) {
          live.push(g.to(track, { [axis]: off, duration: 0.55, ease: 'power2.inOut' }));
          live.push(g.to(fill, { [size]: len, duration: 0.55, ease: 'power2.inOut' }));
        } else {
          g.set(track, { [axis]: off });
          g.set(fill, { [size]: len });
        }
      } else {
        track.style.transform = vert ? 'translateY(' + off + 'px)' : 'translateX(' + off + 'px)';
        fill.style[size] = len + 'px';
      }
    }

    function apply() {
      for (let k = 0; k < n; k++) setShown(k, still() || k < step);
      setActive(step - 1);
      if (still()) panTo(pan); else place(step - 1, false);
    }

    // reduced motion / no GSAP: all milestones shown; a step pages the track by ~80% of the view
    // while something is still off screen, then returns false so the deck moves on
    let pan = 0;
    function panMax() { return Math.max(0, trackSize() - viewSize()); }
    function panTo(p) {
      pan = Math.max(0, Math.min(panMax(), p));
      edges(-pan);
      const t = vert ? 'translateY(' + -pan + 'px)' : 'translateX(' + -pan + 'px)';
      if (g) g.set(track, vert ? { x: 0, y: -pan } : { y: 0, x: -pan }); else track.style.transform = t;
      const size = vert ? 'height' : 'width';
      if (g) g.set(fill, { [size]: trackSize() }); else fill.style[size] = trackSize() + 'px';
    }
    function panBy(dir) {
      const before = pan;
      panTo(pan + dir * viewSize() * 0.8);
      return Math.abs(pan - before) > 1;
    }

    function reveal(k) {
      const p = part[k];
      const t = g.timeline();
      t.fromTo(p.stem, { scaleY: 0 }, { scaleY: 1, duration: 0.3, ease: 'power2.out' }, 0.15)
        .fromTo(p.dot, { scale: 0 }, { scale: 1.12, duration: 0.14, ease: 'power2.out' }, 0.4)
        .to(p.dot, { scale: 1, duration: 0.1, ease: 'power1.inOut' }, 0.54)
        .fromTo(p.blocks, { autoAlpha: 0, y: 12 }, { autoAlpha: 1, y: 0, duration: 0.32, stagger: 0.06, ease: 'power2.out' }, 0.46);
      live.push(t);
    }
    function conceal(k) {
      const p = part[k];
      const t = g.timeline();
      t.to(p.blocks, { autoAlpha: 0, y: 12, duration: 0.2, stagger: { each: 0.04, from: 'end' }, ease: 'power2.in' }, 0)
        .to(p.dot, { scale: 0, duration: 0.16, ease: 'power2.in' }, 0.12)
        .to(p.stem, { scaleY: 0, duration: 0.2, ease: 'power2.in' }, 0.18);
      live.push(t);
    }

    const stepper = {
      next() {
        finish();
        if (still()) return panBy(1);
        if (step >= n) return false;
        step++;
        setActive(step - 1);
        place(step - 1, true);
        reveal(step - 1);
        return true;
      },
      prev() {
        finish();
        if (still()) return panBy(-1);
        if (step <= 0) return false;
        conceal(step - 1);
        step--;
        setActive(step - 1);
        place(step - 1, true);
        return true;
      },
      enter(dir) {
        finish();
        step = dir < 0 ? n : 0;
        layout(); // the slide was display:none until now, so measure again
        pan = dir < 0 ? Infinity : 0; // clamped in panTo
        apply();
      },
      get step() { return step; },
      get steps() { return n; },
    };
    slide.stepper = stepper;

    layout();
    apply();
    let raf = 0;
    const relayout = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => { finish(); layout(); apply(); }); };
    window.addEventListener('resize', relayout);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
    // measuring needs the slide on screen: re-apply when it becomes visible
    if (window.ResizeObserver) new ResizeObserver(relayout).observe(view);
    return stepper;
  }

  function autoMount() {
    document.querySelectorAll('[data-timeline]').forEach((slide) => {
      if (slide.stepper) return;
      const src = slide.querySelector('script[type="application/json"]');
      if (!src) return;
      try { mount(slide, JSON.parse(src.textContent)); } catch (e) { console.error('[timeline-slide]', e); }
    });
  }

  window.TimelineSlide = { mount, autoMount };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', autoMount);
  else autoMount();
})();
