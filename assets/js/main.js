// Daftar foto galeri (berkas di assets/foto/).
const GALERI = [
  { src: 'assets/foto/05-gedung-tk-dan-sdit.jpg', alt: 'Gedung TK dan SDIT' },
  { src: 'assets/foto/12-kolam-berenang.jpg', alt: 'Kolam berenang' },
  { src: 'assets/foto/13-area-bermain-outdoor.jpg', alt: 'Area bermain outdoor' },
  { src: 'assets/foto/07-ruang-kelas.jpg', alt: 'Ruang kelas' },
  { src: 'assets/foto/04-kolam-dan-lingkungan.jpg', alt: 'Kolam dan lingkungan' },
  { src: 'assets/foto/14-tampak-depan-gedung.jpg', alt: 'Tampak depan gedung' },
  { src: 'assets/foto/09-aula-serbaguna.jpg', alt: 'Aula serbaguna' },
  { src: 'assets/foto/10-aula-indoor.jpg', alt: 'Aula indoor' },
  { src: 'assets/foto/06-koridor-sekolah.jpg', alt: 'Koridor sekolah' },
  { src: 'assets/foto/08-tempat-wudhu.jpg', alt: 'Tempat wudhu' },
  { src: 'assets/foto/02-gerbang-utama.jpg', alt: 'Gerbang utama' },
  { src: 'assets/foto/01-pintu-masuk.jpg', alt: 'Pintu masuk' },
  { src: 'assets/foto/03-lapangan-parkir.jpg', alt: 'Lapangan parkir' },
  { src: 'assets/foto/05-kegiatan-kolam-ikan.jpg', alt: 'Kegiatan di kolam ikan' },
  { src: 'assets/foto/01-kegiatan-aula.jpg', alt: 'Kegiatan di aula' },
  { src: 'assets/foto/02-kegiatan-aula.jpg', alt: 'Kegiatan di aula terbuka' },
  { src: 'assets/foto/03-foto-bersama-pramuka.jpg', alt: 'Foto bersama kegiatan Pramuka' }
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
      const cap = document.createElement('figcaption');
      cap.textContent = item.alt;
      fig.append(img, cap);
      grid.appendChild(fig);
    });
  }

  // Animasi muncul saat digulir
  document.querySelectorAll('.section-head, .pillar, .level, .split-copy, .founders, .karomah-inner, .principal, .fee, .spmb-card, .video-inner, .legacy-inner, .join-inner, .nature-item')
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
