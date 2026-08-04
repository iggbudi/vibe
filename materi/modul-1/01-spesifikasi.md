# 1.1 — Spesifikasi dari Ide

**Durasi**: 1 hari (±3 jam)
**Tujuan pembelajaran**:
- Menerjemahkan ide mentah menjadi requirement: fitur, user flow, data
- Menulis *product brief* singkat yang bisa dibaca AI
- Mengetahui kapan ide "cukup jelas" untuk di-generate

---

## Mengapa spesifikasi penting?

Kesalahan terbesar pemula vibe coding: langsung prompt "buatkan aplikasi toko online" lalu kecewa hasilnya. AI bukan pembaca pikiran — **kualitas output dibatasi kualitas input**. Semakin jelas kamu tahu *apa yang kamu mau*, semakin jarang kamu harus mengulang.

Perumpamaan: kamu tidak menyuruh tukang bangunan "bangun rumah". Kamu jelaskan: berapa kamar, di mana, budget berapa. AI sama.

## 3 komponen brief yang baik

Product brief untuk AI terdiri dari 3 bagian:

### 1. Fitur (apa yang bisa dilakukan aplikasi)
Daftar verb-based, urut dari paling penting:
```
Fitur:
1. Tambah catatan baru (judul + isi + tanggal)
2. Lihat daftar semua catatan
3. Edit catatan
4. Hapus catatan
5. Cari catatan berdasarkan judul
```

### 2. User flow (alur pemakaian)
Cerita singkat bagaimana user memakai aplikasi:
```
User flow:
- User membuka aplikasi → melihat daftar catatan
- User menekan "Tambah" → mengisi form → simpan → kembali ke daftar
- User klik satu catatan → melihat detail → bisa edit atau hapus
```

### 3. Data (apa yang disimpan)
Jelaskan entitas data dan field-nya — ini yang nanti jadi struktur database:
```
Data:
- Catatan: id, judul (teks), isi (teks panjang), tanggal_dibuat, tanggal_diubah
```

## Template product brief

```
Aplikasi: [nama]
Deskripsi satu kalimat: [buat apa, untuk siapa]
Fitur (urut prioritas):
1. ...
2. ...
User flow:
- ...
Data yang disimpan:
- [Entitas]: [field, tipe]
Batasan (optional):
- Tidak perlu login
- Offline-only
```

## Latihan: tulis brief untuk "aplikasi catatan pribadi"

Ikuti contoh di atas. Target: **10 baris atau kurang** — brief yang baik itu pendek. Tulis di file `BRIEF.md` di folder project barumu.

**Checklist brief yang baik:**
- [ ] Bisa dibaca orang lain (atau AI) tanpa bertanya
- [ ] Fitur diurutkan prioritas (fitur inti di atas)
- [ ] Data punya tipe yang jelas (teks, angka, tanggal)
- [ ] Ada batasan jika penting (platform, login, dll)
- [ ] Pendek! Kalau > 15 baris, potong

## Antipattern yang harus dihindari

| ❌ Jangan | ✅ Lakukan |
|---|---|
| "Buatkan aplikasi to-do yang keren" | Sebutkan fitur, alur, dan data konkret |
| Menulis 3 paragraf deskripsi panjang | Gunakan struktur bullet yang ringkas |
| Menambah semua ide sekaligus | Batasi fitur inti dulu (MVP) — sisanya nanti di 1.4 |
| Langsung minta AI menulis kode | Validasi brief sendiri dulu: apa yang ambigu? |

## Praktikum

1. Tulis brief untuk aplikasi catatan pribadi (10 baris)
2. Baca ulang: jika kamu tidak bisa menjelaskan ke teman dalam 1 menit, perbaiki
3. Simpan sebagai `BRIEF.md` — ini akan dipakai di lesson 1.2

**Output lesson ini**: file `BRIEF.md` yang berisi product brief siap pakai.
