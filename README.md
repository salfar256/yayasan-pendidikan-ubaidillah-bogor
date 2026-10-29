# TK & SDIT Ibnu Aqil 2 · Bukit Karomah

Website statis (HTML/CSS/JS) untuk TK Ibnu Aqil 2 dan SDIT Ibnu Aqil 2, Bukit Karomah — Kp. Cihideung Kramat, Desa Purwasari, Kec. Dramaga, Kabupaten Bogor 16680.
Saat ini berada di bawah naungan **Yayasan Haji Agus Salim Bogor (YHASB)**, sehingga logo yang dipakai adalah logo YHASB.

Target hosting: `tk-sd.ibnuaqileducationcenter.id`

## Struktur

```
index.html
assets/
  css/style.css
  js/main.js        ← daftar foto galeri (GALERI)
  img/              ← logo YHASB & favicon
  foto/             ← foto kegiatan & lokasi
```

## Isi & sumber

Semua foto, logo, brosur, dan video diambil dari folder **YPUB** (dikompres untuk web).
Kontak, biaya, jadwal, program unggulan, dan persyaratan SPMB 2027/2028 diambil dari brosur TK & SDIT Ibnu Aqil 2.

- Foto fasilitas: `assets/foto/` (daftar galeri di `assets/js/main.js`)
- Brosur unduhan: `assets/brosur/`
- Video perkenalan: `assets/video/`

## Unggah ke hosting

1. Buat subdomain `tk-sd` di panel hosting.
2. Unggah seluruh isi repositori (kecuali `README.md` dan `.git`) ke folder dokumen subdomain tersebut.
3. Aktifkan SSL untuk subdomain.

Tidak memerlukan PHP maupun database.
