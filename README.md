# TK & SDIT Ibnu Aqil 2 · Bukit Karomah

Website statis untuk TK Ibnu Aqil 2 dan SDIT Ibnu Aqil 2 di Kp. Cihideung Kramat (Bukit Karomah), Desa Purwasari, Kec. Dramaga, Kabupaten Bogor 16680.
Berada di bawah naungan Yayasan Haji Agus Salim Bogor (YHASB). Tayang di https://tk-sd.ibnuaqileducationcenter.id melalui GitHub Pages.

## Halaman

| Berkas | Isi |
|---|---|
| `index.html` | Beranda ringkas: menu cepat, pilih sekolah, alasan, alur daftar, foto |
| `tentang.html` | Kisah pendiri, makna Bukit Karomah, kepala sekolah |
| `tk.html`, `sdit.html` | Profil tiap sekolah |
| `fasilitas.html` | Galeri foto (bisa diperbesar) dan video perkenalan |
| `pendaftaran.html` | Alur, persyaratan, biaya, unduh brosur PDF dan Google Drive |
| `kontak.html` | WhatsApp, telepon, alamat, peta |

## Cara mengubah isi

Semua halaman dibuat dari `tools/build.py`. Ubah teks atau data di berkas itu, lalu jalankan:

```sh
python3 tools/build.py
```

Aset: foto di `assets/foto/`, ikon pendaftaran di `assets/ikon/`, brosur di `assets/brosur/`, video di `assets/video/`.
Foto fasilitas yang menampilkan lantai dua diberi keterangan "Foto estimasi ketika bangunan selesai".
