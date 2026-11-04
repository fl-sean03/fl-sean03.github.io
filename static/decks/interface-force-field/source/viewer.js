

(() => {
  'use strict';
  const W = 1920, H = 1080;
  const doc = document, body = doc.body;
  const stage = doc.getElementById('stage');
  const deckEl = doc.getElementById('deck');
  stage.tabIndex = -1;
  const slides = Array.from(doc.querySelectorAll('.slide'));
  body.classList.add('mode-audience');

  let index = 0, digits = '', digitTimer = 0, backupKey = 0, toastTimer = 0;
  const clamp = i => Math.max(0, Math.min(slides.length - 1, i | 0));
  const idIndex = id => slides.findIndex(s => String(id).toLowerCase() === 'q' ? s.dataset.qa === 'true' : s.dataset.id.toLowerCase() === String(id).toLowerCase());

  function fit() {
    const r = stage.getBoundingClientRect();
    const k = Math.min(r.width / W, r.height / H);
    deckEl.style.transform = `translate(${(r.width - W * k) / 2}px, ${(r.height - H * k) / 2}px) scale(${k})`;
  }

  function fromHash() {
    let h;
    try { h = decodeURIComponent(location.hash.slice(1)); } catch { return 0; }
    if (!h) return 0;
    if (/^\d+$/.test(h)) return clamp(parseInt(h, 10) - 1);
    const i = idIndex(h);
    return i < 0 ? 0 : i;
  }


  function show(i) {
    index = clamp(i);
    slides.forEach((s, j) => {
      const on = j === index;
      s.classList.toggle('active', on);
      s.classList.toggle('on', on);
      s.style.display = '';
      s.setAttribute('aria-hidden', on ? 'false' : 'true');
    });
    const h = '#' + (index + 1);
    if (location.hash !== h) history.replaceState(null, '', h);
    if (!ov.hidden) markOverview();
    return index;
  }

  const go = i => show(i);
  const next = () => show(index + 1);
  const prev = () => show(index - 1);
  const goId = id => { const i = idIndex(id); return i < 0 ? index : show(i); };
  const qa = () => { const i = slides.findIndex(s => s.dataset.qa === 'true'); return i < 0 ? index : go(i); };

  function toast(msg) {
    let t = doc.querySelector('.toast');
    if (!t) { t = doc.createElement('div'); t.className = 'toast'; body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => t.classList.remove('show'), 1300);
  }

  function fullscreen() {
    if (doc.fullscreenElement) doc.exitFullscreen();
    else doc.documentElement.requestFullscreen?.().catch(() => toast('Fullscreen unavailable'));
  }


  const ov = doc.createElement('div');
  ov.id = 'ov'; ov.className = 'overlay'; ov.hidden = true;
  ov.setAttribute('role','dialog'); ov.setAttribute('aria-modal','true'); ov.setAttribute('aria-label','Slide overview');
  body.appendChild(ov);
  function buildOverview() {
    const grid = doc.createElement('div'); grid.className = 'grid';
    slides.forEach((s, i) => {
      const b = doc.createElement('button'); b.className = 'cell'; b.type = 'button';
      const mini = doc.createElement('div'); mini.className = 'mini';
      const c = s.cloneNode(true); c.removeAttribute('id'); c.classList.remove('active', 'on');
      mini.appendChild(c); b.appendChild(mini);
      const l = doc.createElement('span'); l.className = 'cl';
      l.textContent = `${s.dataset.page} · ${s.dataset.section === 'backup' || s.dataset.section === 'supplementary' ? s.dataset.id + ' · ' : ''}${s.getAttribute('aria-label')}`;
      b.appendChild(l);
      b.addEventListener('click', () => { closeOverlays(); go(i); });
      grid.appendChild(b);
    });
    ov.appendChild(grid);
  }
  function sizeOverview() {
    ov.querySelectorAll('.mini').forEach(m => { const c = m.firstChild; c.style.transform = `scale(${m.clientWidth / W})`; });
  }
  function markOverview() { ov.querySelectorAll('.cell').forEach((c, i) => c.classList.toggle('cur', i === index)); }
  function overview() {
    if (!ov.hidden) { closeOverlays(); return; }
    closeOverlays();
    if (!ov.firstChild) buildOverview();
    ov.hidden = false; stage.inert = true; sizeOverview(); markOverview();
    ov.querySelectorAll('.cell')[index]?.scrollIntoView({ block: 'center' });
    ov.querySelectorAll('.cell')[index]?.focus();
  }


  const help = doc.createElement('div');
  help.id = 'help'; help.className = 'overlay'; help.hidden = true;
  help.setAttribute('role','dialog'); help.setAttribute('aria-modal','true'); help.setAttribute('aria-label','Deck controls'); help.tabIndex = -1;
  help.innerHTML = `<div class="box"><h3>Deck controls</h3><table>
    <tr><td>→ · Space · PageDown · N</td><td>Next page</td></tr>
    <tr><td>← · PageUp · Backspace · P</td><td>Previous page</td></tr>
    <tr><td>Home · End</td><td>First · last page</td></tr>
    <tr><td>Q</td><td>Q&amp;A page</td></tr>
    <tr><td>B then 1–6</td><td>Backup B1–B6</td></tr>
    <tr><td>Digits then Enter</td><td>Jump to page number</td></tr>
    <tr><td>O or G</td><td>Overview grid (click a page)</td></tr>
    <tr><td>F</td><td>Fullscreen</td></tr>
    <tr><td>Click left · right edge</td><td>Previous · next page</td></tr>
    <tr><td>#12 or #B3 in the URL</td><td>Open a page directly</td></tr>
    <tr><td>Esc</td><td>Close overlay</td></tr></table></div>`;
  body.appendChild(help);
  help.addEventListener('click', () => closeOverlays());
  const helpToggle = () => { const open = help.hidden; closeOverlays(); help.hidden = !open; if (open) { stage.inert = true; help.focus(); } };
  function closeOverlays() { ov.hidden = true; help.hidden = true; stage.inert = false; stage.focus(); }


  doc.addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (k === 'Tab' && (!ov.hidden || !help.hidden)) {
      const dialog = ov.hidden ? help : ov;
      const buttons = Array.from(dialog.querySelectorAll('button'));
      const first = buttons[0], last = buttons[buttons.length - 1];
      if (!first) { e.preventDefault(); return; }
      if (e.shiftKey && doc.activeElement === first) { last.focus(); e.preventDefault(); }
      else if (!e.shiftKey && doc.activeElement === last) { first.focus(); e.preventDefault(); }
      return;
    }
    if (e.target.closest('input, textarea, select, [contenteditable]')) return;
    if ((!ov.hidden || !help.hidden) && k !== 'Escape' && !['o','O','g','G','h','H','?'].includes(k)) return;
    if (backupKey && /^[1-9]$/.test(k)) { backupKey = 0; goId('B' + k); e.preventDefault(); return; }
    if (/^[0-9]$/.test(k)) {
      digits += k; clearTimeout(digitTimer); digitTimer = setTimeout(() => { digits = ''; }, 2000);
      toast('Page ' + digits + ' · Enter'); e.preventDefault(); return;
    }
    if (k === 'Enter' && digits) { const n = parseInt(digits, 10); digits = ''; go(n - 1); e.preventDefault(); return; }
    switch (k) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ': case 'Enter': case 'n': case 'N': case 'j': case 'J': next(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace': case 'p': case 'P': case 'k': case 'K': prev(); break;
      case 'Home': go(0); break;
      case 'End': go(slides.length - 1); break;
      case 'f': case 'F': fullscreen(); break;
      case 'q': case 'Q': qa(); break;
      case 'b': case 'B': backupKey = 1; setTimeout(() => { backupKey = 0; }, 1600); toast('Backup: press 1–6'); break;
      case 'o': case 'O': case 'g': case 'G': overview(); break;
      case '?': case 'h': case 'H': helpToggle(); break;
      case 'Escape': closeOverlays(); break;
      default: return;
    }
    e.preventDefault();
  });
  stage.addEventListener('click', e => {
    if (e.target.closest('a, button')) return;
    const r = stage.getBoundingClientRect(), x = (e.clientX - r.left) / r.width;
    if (x > .75) next(); else if (x < .25) prev();
  });
  let touchX = null;
  stage.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', e => {
    if (touchX === null) return;
    const dx = e.changedTouches[0].clientX - touchX; touchX = null;
    if (Math.abs(dx) > 50) dx < 0 ? next() : prev();
  });
  doc.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (a) { e.preventDefault(); const t = a.getAttribute('href').slice(1); /^\d+$/.test(t) ? go(parseInt(t, 10) - 1) : goId(t); }
  });
  window.addEventListener('resize', () => { fit(); if (!ov.hidden) sizeOverview(); });
  window.addEventListener('hashchange', () => { const i = fromHash(); if (i !== index) show(i); });


  const fontsLoaded = Promise.all(Array.from(doc.fonts, f => f.load().catch(() => f)));


  window.deck = {
    get count() { return slides.length; }, get index() { return index; },
    slides, go, next, prev, goId, qa, overview, help: helpToggle, fullscreen, show,
    ready: Promise.all([fontsLoaded, doc.fonts.ready, ...Array.from(doc.images).map(im => im.decode ? im.decode().catch(() => 0) : 0)])
  };
  fit();
  show(fromHash());
})();
