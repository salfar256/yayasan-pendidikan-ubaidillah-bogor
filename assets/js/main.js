document.addEventListener('DOMContentLoaded', () => {
  const tahun = document.getElementById('tahun');
  if (tahun) tahun.textContent = new Date().getFullYear();

  // Menu HP
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('nav-utama');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Tutup menu' : 'Buka menu');
    });
  }

  // Lightbox: semua foto bertanda data-zoom bisa diperbesar
  const items = [];
  document.querySelectorAll('img[data-zoom]').forEach(img => {
    items.push({ src: img.currentSrc || img.src, alt: img.alt, est: img.dataset.est === '1', el: img });
  });
  document.querySelectorAll('a[data-zoom-link]').forEach(a => {
    items.push({ src: a.href, alt: a.textContent.trim(), est: false, el: a });
  });
  if (!items.length) return;

  const box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Pratinjau foto');
  box.innerHTML = '<span class="lb-count"></span>' +
    '<button type="button" class="lb-btn lb-close" aria-label="Tutup">×</button>' +
    '<button type="button" class="lb-btn lb-prev" aria-label="Foto sebelumnya">‹</button>' +
    '<img alt=""><p class="lb-cap"></p>' +
    '<button type="button" class="lb-btn lb-next" aria-label="Foto berikutnya">›</button>';
  document.body.appendChild(box);
  const bImg = box.querySelector('img');
  const bCap = box.querySelector('.lb-cap');
  const bCount = box.querySelector('.lb-count');
  const multi = items.length > 1;
  box.querySelector('.lb-prev').hidden = !multi;
  box.querySelector('.lb-next').hidden = !multi;
  let cur = 0, lastFocus = null;

  const show = i => {
    cur = (i + items.length) % items.length;
    const it = items[cur];
    bImg.src = it.src;
    bImg.alt = it.alt;
    bCap.innerHTML = '';
    bCap.textContent = it.alt;
    if (it.est) {
      const s = document.createElement('small');
      s.textContent = 'Foto estimasi ketika bangunan selesai';
      bCap.appendChild(s);
    }
    bCount.textContent = multi ? (cur + 1) + ' / ' + items.length : '';
  };
  const open = i => {
    lastFocus = document.activeElement;
    show(i);
    box.classList.add('open');
    document.body.classList.add('lb-lock');
    box.querySelector('.lb-close').focus();
  };
  const close = () => {
    box.classList.remove('open');
    document.body.classList.remove('lb-lock');
    if (lastFocus) lastFocus.focus();
  };

  items.forEach((it, i) => {
    const target = it.el.closest('figure') || it.el;
    if (target.tagName !== 'A') {
      target.setAttribute('tabindex', '0');
      target.setAttribute('role', 'button');
      target.setAttribute('aria-label', 'Perbesar foto: ' + it.alt);
    }
    target.addEventListener('click', e => { e.preventDefault(); open(i); });
    target.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
    });
  });

  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', e => { e.stopPropagation(); show(cur - 1); });
  box.querySelector('.lb-next').addEventListener('click', e => { e.stopPropagation(); show(cur + 1); });
  box.addEventListener('click', e => { if (e.target === box) close(); });
  document.addEventListener('keydown', e => {
    if (!box.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
  });

  // Geser di HP
  let x0 = null;
  box.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', e => {
    if (x0 === null || !multi) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1));
    x0 = null;
  });
});
