(() => {
  'use strict';
  const W = 1920, H = 1080;
  const doc = document, body = doc.body;
  const stage = doc.getElementById('stage');
  const deckEl = doc.getElementById('deck');
  const reader = doc.getElementById('reader');
  stage.tabIndex = -1;
  const slides = Array.from(doc.querySelectorAll('.slide'));
  const articles = Array.from(reader.querySelectorAll('article'));
  body.classList.add('mode-audience');

  let index = 0, digits = '', digitTimer = 0, toastTimer = 0, pillTimer = 0, reading = false;
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
    if (!reading && location.hash !== h) history.replaceState(null, '', h);
    if (!ov.hidden) markOverview();
    return index;
  }

  const go = i => show(i);
  const next = () => show(index + 1);
  const prev = () => show(index - 1);
  const qa = () => { const i = slides.findIndex(s => s.dataset.qa === 'true'); return i < 0 ? index : go(i); };

  function toast(msg, ms = 1300) {
    let t = doc.querySelector('.toast');
    if (!t) { t = doc.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => t.classList.remove('show'), ms);
  }

  function fullscreen() {
    if (doc.fullscreenElement) doc.exitFullscreen();
    else doc.documentElement.requestFullscreen?.().catch(() => toast('Fullscreen unavailable'));
  }

  const ov = doc.createElement('div');
  ov.id = 'ov'; ov.className = 'overlay'; ov.hidden = true;
  ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true'); ov.setAttribute('aria-label', 'Slide overview');
  body.appendChild(ov);
  function buildOverview() {
    const grid = doc.createElement('div'); grid.className = 'grid';
    slides.forEach((s, i) => {
      const b = doc.createElement('button'); b.className = 'cell'; b.type = 'button';
      const mini = doc.createElement('div'); mini.className = 'mini';
      const c = s.cloneNode(true); c.removeAttribute('id'); c.classList.remove('active', 'on');
      mini.appendChild(c); b.appendChild(mini);
      const l = doc.createElement('span'); l.className = 'cl';
      l.textContent = `${s.dataset.page} · ${s.getAttribute('aria-label')}`;
      b.appendChild(l);
      b.addEventListener('click', () => { closeOverlays(); go(i); });
      grid.appendChild(b);
    });
    ov.appendChild(grid);
  }
  function sizeOverview() {
    ov.querySelectorAll('.mini').forEach(m => { m.firstChild.style.transform = `scale(${m.clientWidth / W})`; });
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
  help.setAttribute('role', 'dialog'); help.setAttribute('aria-modal', 'true'); help.setAttribute('aria-label', 'Deck controls'); help.tabIndex = -1;
  help.innerHTML = `<div class="box"><h3>Deck controls</h3><table>
    <tr><td>→ · Space · PageDown · N</td><td>Next page</td></tr>
    <tr><td>← · PageUp · Backspace · P</td><td>Previous page</td></tr>
    <tr><td>Home · End</td><td>First · last page</td></tr>
    <tr><td>T</td><td>Read with notes, one slide after another (T or Esc returns)</td></tr>
    <tr><td>Q</td><td>Q&amp;A page</td></tr>
    <tr><td>Digits then Enter</td><td>Jump to page number</td></tr>
    <tr><td>O or G</td><td>Overview grid (click a page)</td></tr>
    <tr><td>F</td><td>Fullscreen</td></tr>
    <tr><td>Click left · right edge</td><td>Previous · next page</td></tr>
    <tr><td>#12 or #read in the URL</td><td>Open a page, or the reading version, directly</td></tr>
    <tr><td>Esc</td><td>Close overlay</td></tr></table></div>`;
  body.appendChild(help);
  help.addEventListener('click', () => closeOverlays());
  const helpToggle = () => { const open = help.hidden; closeOverlays(); help.hidden = !open; if (open) { stage.inert = true; help.focus(); } };
  function closeOverlays() { ov.hidden = true; help.hidden = true; stage.inert = reading; if (!reading) stage.focus(); }

  // Reading version: every slide in order with its notes, for phones and for reading instead of presenting.
  const zoom = doc.createElement('div');
  zoom.id = 'zoom'; zoom.className = 'overlay'; zoom.hidden = true;
  zoom.setAttribute('role', 'dialog'); zoom.setAttribute('aria-modal', 'true'); zoom.setAttribute('aria-label', 'Enlarged picture');
  zoom.innerHTML = '<button type="button" class="z-close">Close</button><div class="z-wrap"><img alt=""></div>';
  body.appendChild(zoom);
  const zoomImg = zoom.querySelector('img');
  function openZoom(img) {
    zoomImg.src = img.src; zoomImg.alt = img.alt;
    zoom.hidden = false; reader.inert = true; zoom.scrollTo(0, 0); zoom.querySelector('button').focus();
  }
  function closeZoom() { if (zoom.hidden) return; zoom.hidden = true; reader.inert = false; }
  zoom.addEventListener('click', closeZoom);
  reader.addEventListener('click', e => { const img = e.target.closest('figure:not(.r-anim) img'); if (img) openZoom(img); });

  const pill = doc.createElement('button');
  pill.type = 'button'; pill.id = 'read-pill'; pill.textContent = 'Read with notes';
  pill.addEventListener('click', () => openReader());
  body.appendChild(pill);

  function openReader() {
    if (reading) return;
    closeOverlays();
    reader.querySelectorAll('img[data-slide]').forEach(img => {
      if (!img.getAttribute('src')) img.src = slides[+img.dataset.slide].querySelector('img.figure').src;
    });
    reading = true; body.classList.add('reading'); reader.hidden = false; stage.inert = true;
    articles[index].scrollIntoView();
    if (location.hash !== '#read') history.replaceState(null, '', '#read');
  }
  function closeReader() {
    if (!reading) return;
    const top = reader.querySelector('.r-head').getBoundingClientRect().bottom;
    const current = articles.findIndex(a => a.getBoundingClientRect().bottom > top + 1);
    closeZoom();
    reading = false; body.classList.remove('reading'); reader.hidden = true; stage.inert = false;
    window.scrollTo(0, 0); fit(); show(current < 0 ? index : current); stage.focus(); showPill(4000);
  }
  doc.getElementById('to-slides').addEventListener('click', closeReader);

  doc.addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    const dialog = [zoom, ov, help].find(d => !d.hidden);
    if (k === 'Tab' && dialog) {
      const buttons = Array.from(dialog.querySelectorAll('button'));
      const first = buttons[0], last = buttons[buttons.length - 1];
      if (!first) { e.preventDefault(); return; }
      if (e.shiftKey && doc.activeElement === first) { last.focus(); e.preventDefault(); }
      else if (!e.shiftKey && doc.activeElement === last) { first.focus(); e.preventDefault(); }
      return;
    }
    if (e.target.closest('input, textarea, select, [contenteditable]')) return;
    if (reading) {
      if (k === 'Escape' && !zoom.hidden) closeZoom();
      else if (k === 'Escape' || k === 't' || k === 'T') closeReader();
      else return;  // other keys scroll the page as usual
      e.preventDefault(); return;
    }
    if (dialog && k !== 'Escape' && !['o', 'O', 'g', 'G', 'h', 'H', '?'].includes(k)) return;
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
      case 't': case 'T': openReader(); break;
      case 'o': case 'O': case 'g': case 'G': overview(); break;
      case '?': case 'h': case 'H': helpToggle(); break;
      case 'Escape': closeOverlays(); break;
      default: return;
    }
    e.preventDefault();
  });
  stage.addEventListener('click', e => {
    const r = stage.getBoundingClientRect(), x = (e.clientX - r.left) / r.width;
    if (x > .75) next(); else if (x < .25) prev();
  });
  let touchX = null;
  stage.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; showPill(); }, { passive: true });
  stage.addEventListener('touchend', e => {
    if (touchX === null) return;
    const dx = e.changedTouches[0].clientX - touchX; touchX = null;
    if (Math.abs(dx) > 50) dx < 0 ? next() : prev();
  });
  function showPill(ms = 3000) {  // the reading button shows while the mouse moves or a finger touches the slides
    if (reading) return;
    pill.classList.add('show'); clearTimeout(pillTimer);
    pillTimer = setTimeout(() => pill.classList.remove('show'), ms);
  }
  doc.addEventListener('mousemove', () => showPill());
  window.addEventListener('resize', () => { if (!reading) fit(); if (!ov.hidden) sizeOverview(); });
  window.addEventListener('hashchange', () => {
    if (location.hash === '#read') { openReader(); return; }
    const i = fromHash(); if (!reading && i !== index) show(i);
  });

  const fontsLoaded = Promise.all(Array.from(doc.fonts, f => f.load().catch(() => f)));

  window.deck = {
    get count() { return slides.length; }, get index() { return index; }, get reading() { return reading; },
    slides, go, next, prev, qa, overview, help: helpToggle, fullscreen, show, read: openReader, unread: closeReader,
    ready: Promise.all([fontsLoaded, doc.fonts.ready, ...Array.from(doc.images).map(im => im.decode ? im.decode().catch(() => 0) : 0)])
  };
  const askedToRead = location.hash === '#read';  // read before show() rewrites the hash
  fit();
  show(fromHash());
  const phone = innerWidth < 700 && innerHeight > innerWidth;
  if (askedToRead || phone) openReader();
  else if (matchMedia('(pointer: coarse)').matches) showPill(4000);
  else toast('Press T to read with notes · ? for help', 3000);
})();
