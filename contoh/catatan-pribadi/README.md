# 📝 Catatan Pribadi

Aplikasi CLI untuk menyimpan, mengelola, dan mencari catatan pribadi — offline, data tersimpan lokal di SQLite.

> **Project contoh kurikulum Vibe Coding** — implementasi nyata dari proyek akhir Modul 1 ("Aplikasi Todo list + catatan pribadi"). Dibangun dengan pendekatan vibe coding: AI menulis, manusia mengarahkan & memverifikasi.

## Fitur

- ➕ Tambah catatan (judul, isi, kategori)
- 📋 Lihat daftar semua catatan
- 🔍 Lihat detail satu catatan
- ✏️ Edit catatan (nilai lama tampil sebagai default)
- 🗑️ Hapus catatan (dengan konfirmasi)
- 🔎 Cari catatan (judul/isi/kategori, case-insensitive)

## Cara Install

Tanpa dependency eksternal — hanya Python 3 standar:

```bash
# 1. Clone atau salin folder ini
git clone https://github.com/iggbudi/vibe.git
cd vibe/contoh/catatan-pribadi

# 2. (opsional) pastikan Python 3 terinstall
python --version
```

## Cara Pakai

```bash
python app.py
```

Contoh sesi:
```
=== CATATAN PRIBADI ===
1. Tambah catatan
...
Pilih (0-6): 1
Judul: Resep Nasi Goreng
Isi: Nasi, telur, kecap, bawang
Kategori (default: umum): makanan
✅ Catatan tersimpan (id 1).
```

Data tersimpan di `catatan.db` (file lokal, dibuat otomatis saat pertama dijalankan).

## Menjalankan Test

```bash
python tests/test_database.py
```

Test memakai database sementara — tidak menyentuh data asli.

## Struktur

```
catatan-pribadi/
├── app.py            # entry point & menu (validasi input, konfirmasi)
├── database.py       # semua akses SQLite (query parameterized)
├── tests/
│   └── test_database.py  # test CRUD, edge case, pencarian, persistensi
├── BRIEF.md          # product brief awal (Modul 1.1)
└── .gitignore        # database & file sensitif tidak di-commit
```

## Keputusan desain (refleksi singkat)

| Keputusan | Alasan |
|---|---|
| SQLite (bukan file JSON) | Query terstruktur, anti-corruption, siap upgrade ke PostgreSQL (Modul 4.3) |
| Layer database terpisah (`database.py`) | Logic data bisa di-test tanpa UI; nanti gampang ganti backend |
| Query parameterized selalu (`?`) | Mencegah SQL injection (Modul 0.4) |
| Konfirmasi sebelum hapus | Data tidak hilang karena salah ketik (Modul 1.4 edge case) |
| Try/except di loop utama | Satu error tidak mematikan aplikasi (Modul 4.5) |

## Backlog (fitur lanjutan)

- [ ] Ekspor semua catatan ke file (Modul 4: integrasi penyimpanan)
- [ ] Notifikasi reminder via Telegram bot (Modul 3)
- [ ] Kategori dengan filter
- [ ] Backup otomatis `catatan.db`
