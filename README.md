# TK–SD Ibnu Aqil 2 · Bukit Karomah

Website statis (HTML/CSS/JS) untuk TK dan SD Ibnu Aqil 2, Bukit Karomah, Cihideung, Bogor.
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

## Foto

Letakkan foto di `assets/foto/` dengan nama berikut (format .jpg, lebar ±1600 px):

| Berkas | Dipakai di |
|---|---|
| `hero.jpg` | Latar utama bagian atas |
| `tentang.jpg` | Bagian "Kisah Kami" |
| `galeri-1.jpg` … `galeri-8.jpg` | Galeri (keterangan bisa diubah di `assets/js/main.js`) |

Bila foto belum ada, halaman tetap tampil rapi dengan latar warna pengganti.

## Unggah ke hosting

1. Buat subdomain `tk-sd` di panel hosting.
2. Unggah seluruh isi repositori (kecuali `README.md` dan `.git`) ke folder dokumen subdomain tersebut.
3. Aktifkan SSL untuk subdomain.

Tidak memerlukan PHP maupun database.
