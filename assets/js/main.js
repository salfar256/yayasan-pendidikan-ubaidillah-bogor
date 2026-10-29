// Daftar foto galeri. Letakkan berkas di assets/foto/ lalu sesuaikan daftar ini.
const GALERI = [
  { src: 'assets/foto/galeri-1.jpg', alt: 'Pemandangan Bukit Karomah' },
  { src: 'assets/foto/galeri-2.jpg', alt: 'Kegiatan belajar anak-anak' },
  { src: 'assets/foto/galeri-3.jpg', alt: 'Kebun dan lahan pertanian' },
  { src: 'assets/foto/galeri-4.jpg', alt: 'Sumber air di Bukit Karomah' },
  { src: 'assets/foto/galeri-5.jpg', alt: 'Area peternakan' },
  { src: 'assets/foto/galeri-6.jpg', alt: 'Suasana asri lingkungan sekolah' },
  { src: 'assets/foto/galeri-7.jpg', alt: 'Bangunan sekolah' },
  { src: 'assets/foto/galeri-8.jpg', alt: 'Kegiatan bersama' }
];

document.addEventListener('DOMContentLoaded', () => {
  // Tahun footer
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
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }

  // Galeri
  const grid = document.getElementById('gallery-grid');
  const lightbox = document.createElement('div');
  lightbox.className = 'lightbox';
  lightbox.innerHTML = '<button type="button" aria-label="Tutup">×</button><img alt="">';
  document.body.appendChild(lightbox);
  const lbImg = lightbox.querySelector('img');
  const closeLb = () => lightbox.classList.remove('open');
  lightbox.addEventListener('click', e => { if (e.target !== lbImg) closeLb(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLb(); });

  if (grid) {
    GALERI.forEach(item => {
      const fig = document.createElement('figure');
      fig.className = 'reveal';
      const img = new Image();
      img.loading = 'lazy';
      img.alt = item.alt;
      img.src = item.src;
      img.onerror = () => img.remove();
      img.addEventListener('click', () => {
        lbImg.src = item.src; lbImg.alt = item.alt;
        lightbox.classList.add('open');
      });
      img.style.cursor = 'zoom-in';
      const empty = document.createElement('span');
      empty.className = 'g-empty';
      empty.textContent = item.alt;
      fig.append(img, empty);
      grid.appendChild(fig);
    });
  }

  // Animasi muncul saat digulir
  document.querySelectorAll('.section-head, .pillar, .level, .split-copy, .split-media, .karomah-inner, .legacy-inner, .join-inner, .nature-item')
    .forEach(el => el.classList.add('reveal'));
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
  }
});
