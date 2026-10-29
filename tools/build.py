#!/usr/bin/env python3
"""Generator halaman statis TK & SDIT Ibnu Aqil 2.

Jalankan dari akar repositori:  python3 tools/build.py
Semua halaman .html di akar repositori dibuat ulang dari isi berkas ini.
"""
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://tk-sd.ibnuaqileducationcenter.id"

WA_NUMBER = "6285693934394"
PHONE = "0856 9393 4394"
MAPS = "https://share.google/VIJD6dRZKIfdeL0yL"
MAP_EMBED = "https://www.google.com/maps?q=" + quote("Bukit Karomah, Purwasari, Dramaga, Bogor") + "&output=embed"
DRIVE_TK = "https://drive.google.com/drive/folders/1Q1IVCjDc2Mf_Pj50k4ff62XZ2u_joKuC?usp=drive_link"
DRIVE_SD = "https://drive.google.com/drive/folders/1cqnQtO6H3PEX_ySuPmG6P8R3kqZDfRZ8?usp=drive_link"
ADDRESS = "Kp. Cihideung Kramat (Bukit Karomah), Desa Purwasari, Kec. Dramaga, Kabupaten Bogor 16680"
EST = "Foto estimasi ketika bangunan selesai"


def wa(msg="Assalamu'alaikum, saya ingin bertanya tentang pendaftaran di TK/SDIT Ibnu Aqil 2."):
    return f"https://wa.me/{WA_NUMBER}?text={quote(msg)}"


# ---------- Ikon garis sederhana (24x24) ----------
ICONS = {
    'whatsapp': '<path d="M20 11.8a8 8 0 0 1-11.9 7L4 20l1.2-4A8 8 0 1 1 20 11.8Z"/><path d="M8.6 8.4c-.6 1.8 1.8 5.6 4.7 6.7 1.1.4 2-.8 2-1.1l-2-1-.7.7c-1.2-.7-2.2-1.6-2.7-2.7l.6-.7-1-2Z" fill="currentColor" stroke="none"/>',
    'phone': '<path d="M5 4h3.5l1.7 4.3-2.2 1.4a11 11 0 0 0 6.3 6.3l1.4-2.2L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16 16 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4Z"/>',
    'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.6"/>',
    'form': '<rect x="5" y="3.5" width="14" height="17" rx="2"/><path d="M9 3.5h6v3H9zM8.5 11h7M8.5 14.5h7M8.5 18h4"/>',
    'school': '<path d="m3 9 9-5 9 5-9 5-9-5Z"/><path d="M7 11.3V16c0 1.4 2.2 3 5 3s5-1.6 5-3v-4.7M21 9v6"/>',
    'wallet': '<rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10h18M16 14.5h2"/><path d="M6 6 15.5 3 17 6"/>',
    'calendar': '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4M8 14h2M14 14h2M8 17h2"/>',
    'home': '<path d="m4 11 8-7 8 7"/><path d="M6 9.5V20h4.5v-5.5h3V20H18V9.5"/>',
    'mosque': '<path d="M12 3v2M7 12a5 5 0 0 1 10 0"/><path d="M5 12h14v8H5zM10 20v-3.5a2 2 0 0 1 4 0V20M2.5 20V9M21.5 20V9M2.5 9l1-2 1 2M19.5 9l1-2 1 2M2.5 20h19"/>',
    'book': '<path d="M12 6.5C10 5 7.5 4.5 4 4.5v13c3.5 0 6 .5 8 2 2-1.5 4.5-2 8-2v-13c-3.5 0-6 .5-8 2Z"/><path d="M12 6.5v13"/>',
    'star': '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8-4.3-4.1 5.9-.9Z"/>',
    'clock': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    'check': '<circle cx="12" cy="12" r="8.5"/><path d="m8.2 12.2 2.6 2.6 5-5.2"/>',
    'user': '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20a7.5 7.5 0 0 1 15 0"/>',
    'people': '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 19.5a6 6 0 0 1 12 0M15.5 5.5a3 3 0 0 1 0 6M17.5 14a5.5 5.5 0 0 1 3.5 5.5"/>',
    'camera': '<path d="M4 8h3.2L9 5.5h6L16.8 8H20a1 1 0 0 1 1 1v9.5a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1Z"/><circle cx="12" cy="13.5" r="3.5"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'chev': '<path d="m9 6 6 6-6 6"/>',
    'sparkle': '<path d="M12 3c.6 4.2 2.8 6.4 7 7-4.2.6-6.4 2.8-7 7-.6-4.2-2.8-6.4-7-7 4.2-.6 6.4-2.8 7-7Z"/>',
    'compass': '<circle cx="12" cy="12" r="8.5"/><path d="m15.5 8.5-2 5-5 2 2-5Z"/>',
    'download': '<path d="M12 4v11M7 10.5l5 5 5-5M5 19.5h14"/>',
    'leaf': '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14"/><path d="M5 19c3-4 6-6.5 10-8.5"/>',
    'heart': '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10C19.5 15.4 12 20 12 20Z"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    'drop': '<path d="M12 3.5c3 4.3 6 7.8 6 10.8a6 6 0 0 1-12 0c0-3 3-6.5 6-10.8Z"/>',
    'sprout': '<path d="M12 20v-8M12 12c0-4 3-6.5 7-6.5 0 4-3 6.5-7 6.5ZM12 14.5c0-3-2.5-5.5-6-5.5 0 3.5 2.5 5.5 6 5.5Z"/>',
    'fish': '<path d="M3 12c3-4 7-5.5 11-4.5 2.5.6 4.5 2.4 5.5 4.5-1 2.1-3 3.9-5.5 4.5-4 1-8-.5-11-4.5Z"/><path d="M3 12 1.5 9M3 12l-1.5 3"/><circle cx="16" cy="11" r=".8" fill="currentColor"/>',
    'swim': '<circle cx="16" cy="6" r="2"/><path d="m5 13 4-4 3 2.5 3-1.5M3 17c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>',
    'bus': '<rect x="4" y="4" width="16" height="13" rx="2"/><path d="M4 11h16M7.5 17v2.5M16.5 17v2.5"/><circle cx="8" cy="14" r=".8" fill="currentColor"/><circle cx="16" cy="14" r=".8" fill="currentColor"/>',
    'palette': '<path d="M12 3.5a8.5 8.5 0 1 0 0 17c1.2 0 1.8-.8 1.8-1.6 0-1-.8-1.4-.8-2.3 0-.9.7-1.6 1.6-1.6h2a3.9 3.9 0 0 0 3.9-3.9c0-4.3-3.8-7.6-8.5-7.6Z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7.5" r="1"/><circle cx="14.5" cy="7.5" r="1"/>',
    'blocks': '<rect x="3.5" y="13" width="7" height="7" rx="1"/><rect x="13.5" y="13" width="7" height="7" rx="1"/><rect x="8.5" y="4" width="7" height="7" rx="1"/>',
    'kaaba': '<path d="M4 8 12 4l8 4v10l-8 3-8-3Z"/><path d="M4 8l8 3 8-3M12 11v10M4 11.5l8 3 8-3"/>',
    'pray': '<circle cx="12" cy="5.5" r="2"/><path d="M8 20l1-6 3-3 3 3 1 6M9 14h6"/>',
    'smile': '<circle cx="12" cy="12" r="8.5"/><path d="M8.5 14a4 4 0 0 0 7 0"/><circle cx="9" cy="10" r=".8" fill="currentColor"/><circle cx="15" cy="10" r=".8" fill="currentColor"/>',
    'sunrise': '<path d="M4 18h16M7 18a5 5 0 0 1 10 0M12 4v4M5.5 8.5l2 2M18.5 8.5l-2 2"/>',
    'image': '<rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m4 17 5-5 4 4 2.5-2.5L20 18"/>',
    'play': '<circle cx="12" cy="12" r="8.5"/><path d="m10 8.5 5.5 3.5-5.5 3.5Z"/>',
    'drive': '<path d="M8.5 4h7l5 8.5-3.5 6H7l-3.5-6Z"/><path d="M8.5 4 12 10.5M15.5 4 9 15M3.5 12.5h13"/>',
    'tag': '<path d="M3.5 12.5V4.5h8l9 9-8 8Z"/><circle cx="8" cy="9" r="1.3"/>',
    'shirt': '<path d="m8 4-4.5 3 2 4L7 10v10h10V10l1.5 1 2-4L16 4c-.5 1.5-2 2.5-4 2.5S8.5 5.5 8 4Z"/>',
    'list': '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><circle cx="4.5" cy="6.5" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="17.5" r="1"/>',
    'info': '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5.5"/><circle cx="12" cy="7.8" r=".9" fill="currentColor"/>',
    'tree': '<path d="M12 21v-6M12 15c-4 0-6.5-2.3-6.5-5.3S8.2 4 12 3.5c3.8.5 6.5 3 6.5 6.2S16 15 12 15Z"/>',
}


def ic(name, size=24, cls=""):
    c = f' class="ic {cls}"' if cls else ' class="ic"'
    return (f'<svg{c} viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def ikon(name, alt="", size=64):
    return f'<img class="ikon" src="assets/ikon/{name}.png" alt="{alt}" width="{size}" height="{size}" loading="lazy">'


def photo(src, alt, cls="", est=False, lazy=True, w=1600, h=900):
    est_attr = ' data-est="1"' if est else ''
    note = f'<span class="photo-note">{EST}</span>' if est else ''
    lz = ' loading="lazy"' if lazy else ''
    return (f'<figure class="zoom {cls}"><img src="{src}" alt="{alt}" width="{w}" height="{h}"{lz} data-zoom{est_attr}>'
            f'{note}</figure>')


# ---------- Data ----------
FOTO = [
    ('05-gedung-tk-dan-sdit', 'Gedung TK dan SDIT', True),
    ('12-kolam-berenang', 'Kolam berenang', False),
    ('13-area-bermain-outdoor', 'Area bermain outdoor', False),
    ('07-ruang-kelas', 'Ruang kelas', False),
    ('11-kolam-ikan-dan-perkebunan', 'Kolam ikan dan perkebunan', False),
    ('14-tampak-depan-gedung', 'Tampak depan gedung', True),
    ('09-aula-serbaguna', 'Aula serbaguna', False),
    ('10-aula-indoor', 'Aula indoor', False),
    ('06-koridor-sekolah', 'Koridor sekolah', False),
    ('08-tempat-wudhu', 'Tempat wudhu', False),
    ('04-kolam-dan-lingkungan', 'Kolam dan lingkungan', True),
    ('02-gerbang-utama', 'Gerbang utama', False),
    ('01-pintu-masuk', 'Pintu masuk', True),
    ('03-lapangan-parkir', 'Lapangan parkir', False),
    ('04-halaman-sekolah', 'Halaman sekolah', True),
    ('05-kegiatan-kolam-ikan', 'Kegiatan di kolam ikan', False),
    ('01-kegiatan-aula', 'Kegiatan di aula terbuka', False),
    ('02-kegiatan-aula', 'Latihan di aula terbuka', False),
    ('03-foto-bersama-pramuka', 'Foto bersama kegiatan Pramuka', False),
]
FOTO_MAP = {k: (k, a, e) for k, a, e in FOTO}

STEPS = [
    ('cari-info', 'Cari informasi', 'Baca brosur atau tanya admin lewat WhatsApp.'),
    ('isi-formulir', 'Isi formulir', 'Formulir pendaftaran diisi di sekolah.'),
    ('serahkan-berkas', 'Serahkan berkas', 'Akta kelahiran, KTP orang tua, KK, dan berkas lainnya.'),
    ('wawancara', 'Tes dan wawancara', 'Jadwalnya ditentukan oleh panitia SPMB.'),
    ('verifikasi', 'Selesaikan administrasi', 'Lengkapi administrasi sebelum batas waktu.'),
    ('diterima', 'Resmi diterima', 'Selamat bergabung di Ibnu Aqil 2!'),
]

NAV = [
    ('index.html', 'Beranda', 'home'),
    ('tentang.html', 'Tentang', 'info'),
    ('tk.html', 'TK', 'smile'),
    ('sdit.html', 'SDIT', 'school'),
    ('fasilitas.html', 'Fasilitas', 'camera'),
    ('kontak.html', 'Kontak', 'phone'),
]


# ---------- Kerangka halaman ----------
def page(slug, title, desc, body, og_image="assets/foto/04-halaman-sekolah.jpg"):
    url = SITE + "/" + ("" if slug == "index.html" else slug)
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>' for h, t, _ in NAV if h != 'index.html')
    bottom = (
        f'<a href="index.html"{" aria-current=\"page\"" if slug == "index.html" else ""}>{ic("home")}<span>Beranda</span></a>'
        f'<a href="tentang.html"{" aria-current=\"page\"" if slug == "tentang.html" else ""}>{ic("info")}<span>Tentang</span></a>'
        f'<a class="bn-wa" href="{wa()}" target="_blank" rel="noopener">{ic("whatsapp")}<span>WhatsApp</span></a>'
        f'<a href="pendaftaran.html"{" aria-current=\"page\"" if slug == "pendaftaran.html" else ""}>{ic("form")}<span>Daftar</span></a>'
        f'<a href="{MAPS}" target="_blank" rel="noopener">{ic("pin")}<span>Lokasi</span></a>'
    )
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1f4d2e">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_image}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/main.js" defer></script>
</head>
<body>
<a class="skip-link" href="#utama">Lewati ke konten</a>
<div class="topline"><div class="container"><span>{ic("calendar", 15)} SPMB 2027/2028 dibuka 14 November 2026</span><a href="{wa()}" target="_blank" rel="noopener">{ic("whatsapp", 15)} Tanya admin: {PHONE}</a></div></div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Ibnu Aqil 2, beranda">
      <img src="assets/img/logo-yhasb.png" alt="Logo Yayasan Haji Agus Salim Bogor" width="48" height="43">
      <span class="brand-text"><strong>Ibnu Aqil 2</strong><small>TK · SDIT · Bukit Karomah</small></span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav-utama" aria-label="Buka menu"><span></span><span></span><span></span></button>
    <nav class="primary-nav" id="nav-utama" aria-label="Navigasi utama">
      {links}
      <a class="btn btn-small" href="pendaftaran.html">{ic("form", 18)} Info pendaftaran</a>
    </nav>
  </div>
</header>
<main id="utama">
{body}
</main>
<footer class="site-footer">
  <div class="container footer-main">
    <div class="footer-brand">
      <a class="brand brand-light" href="index.html"><img src="assets/img/logo-yhasb.png" alt="Logo Yayasan Haji Agus Salim Bogor" width="48" height="43"><span class="brand-text"><strong>Ibnu Aqil 2</strong><small>TK · SDIT · Bukit Karomah</small></span></a>
      <p>Di bawah naungan Yayasan Haji Agus Salim Bogor (YHASB).</p>
    </div>
    <div><h2>Jelajahi</h2><a href="tentang.html">Tentang Ibnu Aqil 2</a><a href="tk.html">TK Ibnu Aqil 2</a><a href="sdit.html">SDIT Ibnu Aqil 2</a><a href="fasilitas.html">Fasilitas</a><a href="pendaftaran.html">Info pendaftaran</a></div>
    <div><h2>Hubungi kami</h2>
      <ul class="foot-list">
        <li>{ic("whatsapp", 18)}<a href="{wa()}" target="_blank" rel="noopener">{PHONE} (Bu Fuzna)</a></li>
        <li>{ic("pin", 18)}<a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></li>
        <li>{ic("clock", 18)}<span>Pendaftaran: Senin-Jum'at, 08.00-13.00 WIB</span></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom"><span>© <span id="tahun">2026</span> TK &amp; SDIT Ibnu Aqil 2 · Bukit Karomah</span><a href="#utama">Kembali ke atas ↑</a></div>
</footer>
<nav class="bottom-nav" aria-label="Menu cepat">{bottom}</nav>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Tanya pendaftaran lewat WhatsApp">{ic("whatsapp", 24)}<span>Tanya pendaftaran</span></a>
</body>
</html>
"""


def page_head(eyebrow, title, lead, icon=None, img=None):
    pic = f'<img class="ph-ikon" src="{img}" alt="" width="120" height="120">' if img else (f'<span class="ph-ic">{ic(icon, 40)}</span>' if icon else '')
    return f"""<section class="page-head"><div class="container page-head-inner"><div>
<nav class="crumb" aria-label="Lokasi halaman"><a href="index.html">Beranda</a> <span aria-hidden="true">›</span> <span>{eyebrow}</span></nav>
<h1>{title}</h1><p>{lead}</p></div>{pic}</div></section>"""


def cta(title="Masih ada yang ingin ditanyakan?", text="Admin kami siap menjelaskan dengan sabar, termasuk soal biaya dan jadwal tes."):
    return f"""<section class="cta-band"><div class="container cta-inner">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="cta-actions"><a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ic("whatsapp")} Chat WhatsApp</a>
<a class="btn btn-light" href="tel:+{WA_NUMBER}">{ic("phone")} Telepon</a></div></div></section>"""


def founders(cls=""):
    return f"""<div class="founders {cls}">
  <figure class="founder zoom"><img src="assets/foto/pendiri-kh-ubaidillah.jpg" alt="Almarhum Drs. KH. Ubaidillah" width="700" height="875" data-zoom><figcaption><strong>Drs. KH. Ubaidillah</strong><span>Pendiri (Allahu yarham)</span></figcaption></figure>
  <figure class="founder zoom"><img src="assets/foto/pendiri-hj-saidah-hilmiyah.jpg" alt="Hj. Saidah Hilmiyah, S.Pd., M.M." width="700" height="875" data-zoom><figcaption><strong>Hj. Saidah Hilmiyah, S.Pd., M.M.</strong><span>Pendiri</span></figcaption></figure>
</div>"""


def steps_html():
    items = "".join(
        f'<li><span class="step-num">{i}</span>{ikon(n, "", 72)}<strong>{t}</strong><span>{d}</span></li>'
        for i, (n, t, d) in enumerate(STEPS, 1))
    return f'<ol class="steps">{items}</ol>'


def strip(keys):
    figs = "".join(photo(f"assets/foto/{k}.jpg", FOTO_MAP[k][1], est=FOTO_MAP[k][2]) for k in keys)
    return f'<div class="strip strip-{len(keys)}">{figs}</div>'


# ---------- BERANDA ----------
home = f"""
<section class="hero">
  <img class="hero-bg" src="assets/foto/04-halaman-sekolah.jpg" alt="" width="1600" height="900" fetchpriority="high">
  <span class="photo-note hero-note">{EST}</span>
  <div class="container hero-inner">
    <div class="hero-copy">
      <p class="pill">{ic("sparkle", 16)} SPMB 2027/2028 · dibuka 14 November 2026</p>
      <h1>Assalamu'alaikum,<br><span>selamat datang di Ibnu Aqil 2</span></h1>
      <p class="hero-lead">TK dan SDIT di Bukit Karomah, Dramaga, Bogor. Anak belajar ilmu, akhlak, dan kemandirian di tengah alam yang hijau dan sejuk.</p>
      <div class="hero-actions">
        <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ic("whatsapp")} Chat WhatsApp</a>
        <a class="btn btn-light" href="pendaftaran.html">{ic("form")} Info pendaftaran</a>
      </div>
      <p class="hero-hint">{ic("clock", 18)} Pendaftaran Senin-Jum'at, 08.00-13.00 WIB</p>
    </div>
    <div class="hero-side">
      <p class="hero-side-title">Pendiri Ibnu Aqil 2</p>
      {founders("founders-hero")}
    </div>
  </div>
</section>

<section class="quick">
  <div class="container">
    <h2 class="title">Bapak/Ibu ingin apa hari ini?</h2>
    <div class="quick-grid">
      <a class="tile tile-green" href="pendaftaran.html">{ikon("pendaftaran", "", 56)}<strong>Cara daftar</strong><span>Syarat dan alur</span></a>
      <a class="tile" href="pendaftaran.html#biaya">{ic("wallet", 34)}<strong>Lihat biaya</strong><span>TK dan SDIT</span></a>
      <a class="tile" href="pendaftaran.html#brosur">{ic("download", 34)}<strong>Unduh brosur</strong><span>PDF dan Google Drive</span></a>
      <a class="tile" href="fasilitas.html">{ic("camera", 34)}<strong>Fasilitas</strong><span>Lihat foto</span></a>
      <a class="tile" href="{MAPS}" target="_blank" rel="noopener">{ic("pin", 34)}<strong>Lokasi</strong><span>Buka Google Maps</span></a>
      <a class="tile" href="{wa()}" target="_blank" rel="noopener">{ikon("whatsapp", "", 56)}<strong>Tanya admin</strong><span>Lewat WhatsApp</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="head"><h2 class="title">Pilih sekolah</h2></div>
    <div class="units">
      <a class="unit unit-tk" href="tk.html">
        <img src="assets/img/logo-tk-ibnu-aqil.png" alt="Logo TK Ibnu Aqil" width="88" height="88">
        <div><strong>TK Ibnu Aqil 2</strong><span>Bermain sambil belajar, metode sentra, manasik haji, dan berenang.</span>
        <em>{ic("clock", 16)} Senin-Kamis 07.30-11.00</em></div>{ic("chev", 26, "unit-arrow")}
      </a>
      <a class="unit unit-sd" href="sdit.html">
        <img src="assets/img/logo-sdit-ibnu-aqil.jpg" alt="Logo SDIT Ibnu Aqil" width="88" height="114">
        <div><strong>SDIT Ibnu Aqil 2</strong><span>Full day school dengan program kepesantrenan dan bimbingan mengaji.</span>
        <em>{ic("clock", 16)} Senin-Kamis 07.00-14.00</em></div>{ic("chev", 26, "unit-arrow")}
      </a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="title">Kenapa Ibnu Aqil 2?</h2>
    <ul class="reasons">
      <li>{ic("tree", 32)}<strong>Alam asri dan luas</strong><span>Udara sejuk, banyak ruang bermain</span></li>
      <li>{ic("drop", 32)}<strong>Air melimpah</strong><span>Kolam renang dan kolam ikan</span></li>
      <li>{ic("sprout", 32)}<strong>Belajar mandiri</strong><span>Berkebun dan merawat hewan</span></li>
      <li>{ic("book", 32)}<strong>Bimbingan mengaji</strong><span>Hafalan surat dan doa harian</span></li>
      <li>{ic("mosque", 32)}<strong>Praktik ibadah</strong><span>Wudhu, shalat, dan manasik</span></li>
      <li>{ic("heart", 32)}<strong>Akhlak mulia</strong><span>Lewat keteladanan guru</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="head"><h2 class="title">Enam langkah mudah mendaftar</h2><a class="more" href="pendaftaran.html">Syarat lengkap {ic("chev", 18)}</a></div>
    {steps_html()}
  </div>
</section>

<section class="section section-soft karomah-teaser">
  <div class="container teaser-inner">
    {ikon("bukit", "", 96)}
    <div>
      <h2 class="title">Kenapa namanya Bukit Karomah?</h2>
      <p>Sekolah ini berdiri di Kampung Cihideung Kramat. Para pendiri mengganti kata <em>kramat</em> menjadi <em>karomah</em>, yang berarti kemuliaan dari Allah, sebagai doa agar setiap anak yang belajar di sini tumbuh mulia akhlaknya.</p>
      <a class="more" href="tentang.html">Baca kisah kami {ic("chev", 18)}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container"><div class="head"><h2 class="title">Suasana Bukit Karomah</h2><a class="more" href="fasilitas.html">Semua foto {ic("chev", 18)}</a></div></div>
  <div class="container">{strip(['05-gedung-tk-dan-sdit','12-kolam-berenang','13-area-bermain-outdoor','07-ruang-kelas','11-kolam-ikan-dan-perkebunan','09-aula-serbaguna'])}</div>
</section>

{cta()}
"""

# ---------- TENTANG ----------
tentang = page_head("Tentang", "Kisah Ibnu Aqil 2", "Sebuah ikhtiar yang ditanam dengan cinta, di atas bukit yang hijau di Dramaga, Bogor.", img="assets/ikon/sekolah.png") + f"""
<section class="section">
  <div class="container story">
    <div class="story-copy">
      <h2 class="title">Didirikan dengan sebuah cita-cita</h2>
      <p>Ibnu Aqil 2 didirikan oleh <strong>Almarhum Drs. KH. Ubaidillah</strong> bersama istrinya, <strong>Hj. Saidah Hilmiyah, S.Pd., M.M.</strong> Keduanya ingin menghadirkan sekolah yang tidak hanya mencerdaskan, tapi juga membekali anak dengan kemandirian.</p>
      <p>Tempat ini dipilih karena lahannya luas, sumber airnya melimpah, dan suasananya asri. Lokasinya cocok untuk bertani dan beternak, sehingga anak bisa belajar di kelas sekaligus belajar langsung dari alam.</p>
      <p>Saat ini Ibnu Aqil 2 berada di bawah naungan <strong>Yayasan Haji Agus Salim Bogor</strong>.</p>
    </div>
    {founders("founders-story")}
  </div>
</section>

<section class="section karomah">
  <div class="container karomah-inner">
    <div class="arabic" aria-hidden="true">كَرَامَة</div>
    <h2>Dari <span class="strike">Kramat</span> menjadi <em>Karomah</em></h2>
    <div class="karomah-cols">
      <div>{ic("pin", 30)}<p>Sekolah ini berada di <strong>Kampung Cihideung Kramat</strong>, Desa Purwasari, Kecamatan Dramaga. Para pendiri mengganti kata <em>kramat</em> menjadi <em>karomah</em>.</p></div>
      <div>{ic("star", 30)}<p><em>Karomah</em> berarti kemuliaan yang Allah berikan kepada hamba-Nya yang saleh. Nama ini adalah doa agar anak-anak tumbuh mulia akhlaknya dan berkah ilmunya.</p></div>
      <div>{ic("heart", 30)}<p>Pergantian nama ini juga menjauhkan kesan mistis dari kata "keramat". Bukit ini ingin dikenal karena kebaikan yang lahir darinya.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="title">Pendidikan yang berjalan bersama kemandirian</h2>
    <ul class="reasons reasons-3">
      <li>{ic("book", 32)}<strong>Iman dan Al-Qur'an</strong><span>Mengaji, praktik ibadah, hafalan surat dan doa harian</span></li>
      <li>{ic("heart", 32)}<strong>Akhlak mulia</strong><span>Adab kepada guru, orang tua, teman, dan alam</span></li>
      <li>{ic("blocks", 32)}<strong>Belajar menyenangkan</strong><span>Metode sentra dan media pembelajaran menarik</span></li>
      <li>{ic("sprout", 32)}<strong>Bertani</strong><span>Menanam dan merawat kebun bersama</span></li>
      <li>{ic("fish", 32)}<strong>Beternak dan kolam ikan</strong><span>Belajar sayang dan tanggung jawab</span></li>
      <li>{ic("leaf", 32)}<strong>Peduli lingkungan</strong><span>Menjaga air, tanah, dan pepohonan</span></li>
    </ul>
  </div>
</section>

<section class="section section-soft">
  <div class="container principal">
    <figure class="zoom principal-photo"><img src="assets/foto/kepsek-fuzna-nur-aqilah.jpg" alt="Dr. Hj. Fuzna Nur Aqilah, M.Pd." width="700" height="700" loading="lazy" data-zoom></figure>
    <div>
      <p class="eyebrow">Kepala Sekolah</p>
      <h2 class="title">Dr. Hj. Fuzna Nur Aqilah, M.Pd.</h2>
      <p>Kepala TK Ibnu Aqil 2 dan SDIT Ibnu Aqil 2. Bersama para guru, beliau mendampingi setiap anak agar tumbuh berilmu, berakhlak, dan berprestasi.</p>
      <a class="btn btn-wa btn-small" href="{wa('Assalamualaikum Bu Fuzna, saya ingin bertanya tentang TK/SDIT Ibnu Aqil 2.')}" target="_blank" rel="noopener">{ic("whatsapp", 18)} Hubungi Bu Fuzna</a>
    </div>
  </div>
</section>

<section class="legacy">
  <div class="container legacy-inner">
    <p class="arabic-small" aria-hidden="true">اَللّٰهُمَّ اغْفِرْ لَهُ وَارْحَمْهُ</p>
    <h2>Beliau tidak sempat menyaksikan bukit ini berkembang.<br><em>Kini kitalah yang melanjutkan.</em></h2>
    <p>Almarhum Drs. KH. Ubaidillah lebih dahulu berpulang sebelum sempat melihat cita-citanya tumbuh. Namun benih yang beliau tanam terus tumbuh. Setiap anak yang belajar di sini dan setiap kebaikan yang lahir dari bukit ini adalah kelanjutan ikhtiar beliau. Semoga menjadi amal jariyah yang terus mengalir.</p>
    <a class="btn" href="pendaftaran.html">{ic("form")} Mari bergabung bersama kami</a>
  </div>
</section>
"""


# ---------- UNIT ----------
def unit_page(kind):
    if kind == 'tk':
        name, logo, lw, lh = "TK Ibnu Aqil 2", "assets/img/logo-tk-ibnu-aqil.png", 120, 120
        visi = "Mewujudkan generasi muslim yang berakhlak mulia, mandiri, terampil, cerdas, dan kreatif."
        lead = "Taman kanak-kanak di Bukit Karomah. Anak bermain sambil belajar, dekat dengan alam."
        progs = [("manasik", "Praktik manasik haji"), ("mengaji", "Bimbingan mengaji"), ("sentra", "Pembelajaran metode sentra"),
                 ("ibadah", "Bimbingan praktik ibadah"), ("berenang", "Berenang"), ("doa", "Hafalan surat, hadits, dan doa harian"),
                 ("outing", "Outing class"), ("ekskul", "Ekstrakurikuler"), ("media", "Media pembelajaran menarik")]
        siswa = ("assets/siswa/tk-formal.webp", "Siswa TK Ibnu Aqil 2 dengan seragam sekolah", 1300, 775)
        seragam_foto = [("tk-seragam-formal", "Baju khas"), ("tk-seragam-olahraga", "Baju olahraga"), ("tk-seragam-putih", "Baju batik")]
        brosur = [("assets/brosur/poster-spmb-tk-2027.jpg", "Poster SPMB TK Ibnu Aqil 2"),
                  ("assets/brosur/brosur-tk-depan-2026.jpg", "Brosur TK halaman depan"),
                  ("assets/brosur/brosur-tk-belakang-2026.jpg", "Brosur TK halaman belakang")]
        jadwal = [("Senin-Kamis", "07.30-11.00 WIB"), ("Jum'at", "07.30-09.30 WIB")]
        fotos = ['07-ruang-kelas', '13-area-bermain-outdoor', '12-kolam-berenang', '05-gedung-tk-dan-sdit']
        biaya = "Rp760.000 (putra) · Rp810.000 (putri)"
        drive = DRIVE_TK
        pdf = "assets/brosur/brosur-tk-ibnu-aqil-2.pdf"
    else:
        name, logo, lw, lh = "SDIT Ibnu Aqil 2", "assets/img/logo-sdit-ibnu-aqil.jpg", 110, 142
        visi = "Mewujudkan generasi yang beriman dan bertakwa, berilmu, berakhlak, berprestasi, mandiri, dan peduli lingkungan."
        lead = "Sekolah dasar Islam terpadu dengan sistem full day school dan program kepesantrenan."
        progs = [("ibadah", "Bimbingan praktik ibadah"), ("mengaji", "Bimbingan mengaji"), ("media", "Media pembelajaran menarik"),
                 ("ekskul", "Program Happy School"), ("kepesantrenan", "Program kepesantrenan"), ("outing", "Outing class"),
                 ("fasilitas", "Fasilitas indoor dan outdoor"), ("fullday", "Full day school")]
        siswa = ("assets/siswa/sd-formal.webp", "Siswa SDIT Ibnu Aqil 2 dengan seragam sekolah", 1300, 880)
        seragam_foto = [("sd-seragam-batik", "Baju batik"), ("sd-seragam-olahraga", "Baju olahraga")]
        brosur = [("assets/brosur/poster-spmb-sdit-2027.jpg", "Poster SPMB SDIT Ibnu Aqil 2"),
                  ("assets/brosur/brosur-sdit-ibnu-aqil-2.jpg", "Brosur SDIT Ibnu Aqil 2 lengkap")]
        jadwal = [("Senin-Kamis", "07.00-14.00 WIB"), ("Jum'at", "07.00-10.00 WIB")]
        fotos = ['05-gedung-tk-dan-sdit', '06-koridor-sekolah', '09-aula-serbaguna', '12-kolam-berenang']
        biaya = "Rp600.000 (laki-laki) · Rp650.000 (perempuan)"
        drive = DRIVE_SD
        pdf = "assets/brosur/brosur-sdit-ibnu-aqil-2.pdf"
    prog_html = "".join(f'<li><img src="assets/program/{i}.webp" alt="" width="64" height="64" loading="lazy"><span>{t}</span></li>' for i, t in progs)
    sw, sh = siswa[2], siswa[3]
    ser_html = "".join(f'<figure class="zoom seragam-item"><img src="assets/siswa/{f}.webp" alt="Siswa {name} memakai {t.lower()}" width="700" height="1050" loading="lazy" data-zoom><figcaption>{t}</figcaption></figure>' for f, t in seragam_foto)
    br_html = "".join(f'<figure class="zoom brosur-show"><img src="{src}" alt="{alt}" width="1500" height="2000" loading="lazy" data-zoom><figcaption>{alt}</figcaption></figure>' for src, alt in brosur)
    jad_html = "".join(f"<div><dt>{d}</dt><dd>{j}</dd></div>" for d, j in jadwal)
    promo = ""
    if kind == 'sd':
        promo = f'<p class="promo">{ic("tag", 20)} <span>Khusus alumni TK Ibnu Aqil 2 dan 10 pendaftar pertama: <b>diskon 50%</b> dan <b>bonus tas sekolah</b>.</span></p>'
    body = f"""
<section class="unit-head unit-head-{kind}"><div class="container unit-head-inner">
  <div class="unit-head-copy"><nav class="crumb" aria-label="Lokasi halaman"><a href="index.html">Beranda</a> <span aria-hidden="true">›</span> <span>{name}</span></nav>
  <div class="unit-title"><img class="unit-logo" src="{logo}" alt="Logo {name}" width="{lw}" height="{lh}"><h1>{name}</h1></div>
  <p>{lead}</p>
  <div class="hero-actions"><a class="btn btn-wa" href="{wa(f'Assalamualaikum, saya ingin bertanya tentang pendaftaran di {name}.')}" target="_blank" rel="noopener">{ic("whatsapp")} Tanya admin</a>
  <a class="btn btn-light" href="#brosur">{ic("image")} Lihat brosur</a></div></div>
  <img class="unit-students" src="{siswa[0]}" alt="{siswa[1]}" width="{sw}" height="{sh}" fetchpriority="high">
</div></section>

<section class="section">
  <div class="container unit-grid">
    <div class="card visi">{ic("compass", 30)}<h2>Visi</h2><p>{visi}</p></div>
    <div class="card">{ic("clock", 30)}<h2>Jadwal belajar</h2><dl class="schedule">{jad_html}</dl></div>
    <div class="card">{ic("wallet", 30)}<h2>Biaya masuk</h2><p class="big">{biaya}</p><p class="small">Uang bangunan gratis. <a href="pendaftaran.html#biaya">Lihat rincian</a></p></div>
  </div>
  <div class="container">{promo}</div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="title">Program unggulan</h2>
    <ul class="programs">{prog_html}</ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="head"><h2 class="title">Fasilitas pendukung</h2><a class="more" href="fasilitas.html">Semua foto {ic("chev", 18)}</a></div>
    <div class="facts">
      <p>{ic("sun", 22)} <b>Outdoor:</b> area bermain, lapangan olahraga, dan kolam berenang</p>
      <p>{ic("home", 22)} <b>Indoor:</b> ruang kelas, media edukasi, toilet, dan aula serbaguna</p>
    </div>
    {strip(fotos)}
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="title">Seragam sekolah</h2>
    <div class="seragam seragam-{len(seragam_foto)}">{ser_html}</div>
  </div>
</section>

<section class="section" id="brosur">
  <div class="container">
    <div class="head"><h2 class="title">Brosur {name}</h2>
    <div class="dl-actions"><a class="btn btn-small" href="{pdf}" download>{ic("download", 18)} Unduh PDF</a>
    <a class="btn btn-small btn-outline" href="{drive}" target="_blank" rel="noopener">{ic("drive", 18)} Google Drive</a></div></div>
    <p class="small">Ketuk brosur untuk melihat lebih jelas.</p>
    <div class="brosur-show-grid brosur-show-{len(brosur)}">{br_html}</div>
  </div>
</section>
{cta()}
"""
    return name, lead, body


# ---------- FASILITAS ----------
gal = "".join(photo(f"assets/foto/{k}.jpg", a, "g-item", est=e) .replace("</figure>", f"<figcaption>{a}</figcaption></figure>") for k, a, e in FOTO)
fasilitas = page_head("Fasilitas", "Fasilitas dan suasana", "Ketuk foto untuk melihat lebih jelas. Geser atau gunakan tombol panah untuk foto berikutnya.", icon="camera") + f"""
<section class="section">
  <div class="container">
    <div class="facts">
      <p>{ic("sun", 22)} <b>Outdoor:</b> area bermain, lapangan olahraga, kolam berenang, kolam ikan, dan kebun</p>
      <p>{ic("home", 22)} <b>Indoor:</b> ruang kelas, media edukasi, tempat wudhu, toilet, dan aula serbaguna</p>
    </div>
    <div class="gallery">{gal}</div>
  </div>
</section>
<section class="section video-section">
  <div class="container video-inner">
    <div>{ic("play", 36)}<h2>Video perkenalan</h2><p>Lihat suasana belajar dan fasilitas Ibnu Aqil 2 dari dekat.</p></div>
    <video controls preload="none" playsinline poster="assets/video/perkenalan-poster.jpg"><source src="assets/video/perkenalan-ibnu-aqil-2.mp4" type="video/mp4"></video>
  </div>
</section>
""" + cta()


# ---------- PENDAFTARAN ----------
def brosur_card(img, title, pdf, drive):
    return f"""<article class="brosur">
  <figure class="zoom brosur-img"><img src="{img}" alt="{title}" width="1500" height="2000" loading="lazy" data-zoom></figure>
  <div class="brosur-body"><h3>{title}</h3>
  <a class="btn btn-small" href="{pdf}" download>{ic("download", 18)} Unduh PDF</a>
  <a class="btn btn-small btn-outline" href="{drive}" target="_blank" rel="noopener">{ic("drive", 18)} Google Drive</a></div>
</article>"""


pendaftaran = page_head("Info pendaftaran", "SPMB Tahun Ajaran 2027/2028", "Pendaftaran dibuka 14 November 2026 sampai kuota terpenuhi.", img="assets/ikon/pendaftaran.png") + f"""
<section class="section">
  <div class="container">
    <div class="key-facts">
      <div>{ic("calendar", 30)}<strong>14 November 2026</strong><span>Pendaftaran dibuka</span></div>
      <div>{ic("clock", 30)}<strong>08.00-13.00 WIB</strong><span>Senin-Jum'at</span></div>
      <div>{ic("pin", 30)}<strong>Bukit Karomah</strong><span>Purwasari, Dramaga</span></div>
      <div>{ic("people", 30)}<strong>Kuota terbatas</strong><span>Ditutup jika kuota penuh</span></div>
    </div>
    <h2 class="title">Alur pendaftaran</h2>
    {steps_html()}
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="title">Persyaratan</h2>
    <div class="two">
      <div class="card">{ikon("serahkan-berkas", "", 56)}<h3>TK Ibnu Aqil 2</h3>
        <ul class="checks"><li>Mengisi formulir pendaftaran</li><li>Fotokopi akta kelahiran (2 lembar)</li><li>Fotokopi KTP orang tua/wali (2 lembar)</li><li>Fotokopi kartu keluarga (2 lembar)</li><li>Pas foto ukuran 3x4 (2 lembar)</li></ul></div>
      <div class="card">{ikon("serahkan-berkas", "", 56)}<h3>SDIT Ibnu Aqil 2</h3>
        <ul class="checks"><li>Mengisi formulir pendaftaran</li><li>Fotokopi akta kelahiran (2 lembar)</li><li>Fotokopi KTP orang tua/wali (2 lembar)</li><li>Fotokopi kartu keluarga (2 lembar)</li><li>Fotokopi ijazah TK/PAUD (2 lembar)</li></ul></div>
    </div>
    <div class="note-box">{ikon("wawancara", "", 56)}<p><b>Seleksi penerimaan.</b> Tes seleksi dan jadwal wawancara ditentukan oleh panitia SPMB. Calon peserta didik diterima setelah mengikuti tes dan wawancara serta menyelesaikan administrasi sampai batas waktu yang ditentukan.</p></div>
  </div>
</section>

<section class="section" id="biaya">
  <div class="container">
    <h2 class="title">Biaya pendidikan</h2>
    <p class="promo">{ic("tag", 20)} <span><b>Uang bangunan gratis!</b> Khusus SDIT, alumni TK Ibnu Aqil 2 dan 10 pendaftar pertama mendapat <b>diskon 50%</b> dan <b>bonus tas sekolah</b>.</span></p>
    <div class="two">
      <div class="card fee"><h3>{ic("smile", 24)} TK Ibnu Aqil 2</h3>
        <table><tr><td>Biaya pendaftaran</td><td>Rp25.000</td></tr><tr><td>Infaq syahriyah dan kas</td><td>Rp100.000</td></tr><tr><td>Media pembelajaran (1 tahun)</td><td>Rp110.000</td></tr><tr><td>Pakaian seragam</td><td>Rp550.000 (L)<br>Rp600.000 (P)</td></tr><tr class="total"><td>Jumlah</td><td>Rp760.000 (putra)<br>Rp810.000 (putri)</td></tr></table></div>
      <div class="card fee"><h3>{ic("school", 24)} SDIT Ibnu Aqil 2</h3>
        <table><tr><td>Biaya pendaftaran</td><td>Gratis</td></tr><tr><td>Baju seragam</td><td>Rp500.000 (L)<br>Rp550.000 (P)</td></tr><tr><td>SPP dan kas</td><td>Rp100.000/bulan</td></tr><tr class="total"><td>Total</td><td>Rp600.000 (laki-laki)<br>Rp650.000 (perempuan)</td></tr></table>
        <p class="small">Belum termasuk buku LKS.</p></div>
    </div>
  </div>
</section>

<section class="section section-soft" id="brosur">
  <div class="container">
    <h2 class="title">Unduh brosur</h2>
    <div class="brosur-grid">
      {brosur_card("assets/brosur/poster-spmb-tk-2027.jpg", "Brosur TK Ibnu Aqil 2", "assets/brosur/brosur-tk-ibnu-aqil-2.pdf", DRIVE_TK)}
      {brosur_card("assets/brosur/poster-spmb-sdit-2027.jpg", "Brosur SDIT Ibnu Aqil 2", "assets/brosur/brosur-sdit-ibnu-aqil-2.pdf", DRIVE_SD)}
    </div>
    <p class="small center">Brosur lengkap juga bisa dilihat: <a href="assets/brosur/brosur-tk-depan-2026.jpg" data-zoom-link>TK halaman depan</a> · <a href="assets/brosur/brosur-tk-belakang-2026.jpg" data-zoom-link>TK halaman belakang</a> · <a href="assets/brosur/brosur-sdit-ibnu-aqil-2.jpg" data-zoom-link>SDIT lengkap</a></p>
  </div>
</section>
""" + cta("Siap mendaftar?", "Datang langsung ke sekolah atau tanya dulu lewat WhatsApp. Kami senang membantu.")


# ---------- KONTAK ----------
kontak = page_head("Kontak", "Hubungi kami", "Silakan datang langsung atau hubungi admin lewat WhatsApp.", icon="phone") + f"""
<section class="section">
  <div class="container contact-grid">
    <div class="contact-cards">
      <a class="contact-card" href="{wa()}" target="_blank" rel="noopener">{ikon("whatsapp", "", 52)}<div><strong>WhatsApp</strong><span>{PHONE} (Bu Fuzna)</span></div></a>
      <a class="contact-card" href="tel:+{WA_NUMBER}">{ic("phone", 32)}<div><strong>Telepon</strong><span>{PHONE}</span></div></a>
      <a class="contact-card" href="{MAPS}" target="_blank" rel="noopener">{ic("pin", 32)}<div><strong>Alamat</strong><span>{ADDRESS}</span></div></a>
      <div class="contact-card">{ic("clock", 32)}<div><strong>Jam pendaftaran</strong><span>Senin-Jum'at, 08.00-13.00 WIB</span></div></div>
    </div>
    <div class="map">
      <iframe title="Peta lokasi Bukit Karomah" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="btn" href="{MAPS}" target="_blank" rel="noopener">{ic("compass")} Petunjuk arah di Google</a>
    </div>
  </div>
</section>
"""


def main():
    pages = {
        'index.html': ("TK & SDIT Ibnu Aqil 2 · Bukit Karomah, Dramaga, Bogor",
                       "TK Ibnu Aqil 2 dan SDIT Ibnu Aqil 2 di Bukit Karomah, Purwasari, Dramaga, Bogor. SPMB 2027/2028 dibuka 14 November 2026.", home),
        'tentang.html': ("Tentang Ibnu Aqil 2 · Kisah Bukit Karomah",
                         "Kisah berdirinya Ibnu Aqil 2 oleh Almarhum Drs. KH. Ubaidillah dan Hj. Saidah Hilmiyah, S.Pd., M.M., serta makna nama Bukit Karomah.", tentang),
        'fasilitas.html': ("Fasilitas TK & SDIT Ibnu Aqil 2",
                           "Foto fasilitas TK dan SDIT Ibnu Aqil 2: kolam berenang, area bermain, ruang kelas, aula, kolam ikan, dan kebun.", fasilitas),
        'pendaftaran.html': ("Info Pendaftaran SPMB 2027/2028 · TK & SDIT Ibnu Aqil 2",
                             "Alur, persyaratan, biaya, dan brosur SPMB TK dan SDIT Ibnu Aqil 2 tahun ajaran 2027/2028. Dibuka 14 November 2026.", pendaftaran),
        'kontak.html': ("Kontak TK & SDIT Ibnu Aqil 2",
                        "WhatsApp, telepon, alamat, dan peta lokasi TK dan SDIT Ibnu Aqil 2 di Bukit Karomah, Dramaga, Bogor.", kontak),
    }
    for kind, slug in (('tk', 'tk.html'), ('sd', 'sdit.html')):
        name, lead, body = unit_page(kind)
        pages[slug] = (f"{name} · Bukit Karomah, Dramaga, Bogor", f"{name}: {lead}", body)
    for slug, (title, desc, body) in pages.items():
        html = page(slug, title, desc, body)
        assert "—" not in html, f"em dash di {slug}"
        (ROOT / slug).write_text(html, encoding="utf-8")
        print("tulis", slug)
    urls = "".join(f"<url><loc>{SITE}/{'' if s == 'index.html' else s}</loc></url>" for s in pages)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    main()
