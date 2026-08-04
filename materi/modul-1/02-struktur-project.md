# 1.2 — Generate Struktur Project

**Durasi**: 1 hari (±3 jam)
**Tujuan pembelajaran**:
- Menulis prompt pertama yang menghasilkan skeleton aplikasi
- Memahami output AI: apa yang perlu dipertahankan vs dibuang
- Memilih stack: kapan framework, kapan plain code

---

## Prompt pertama

Sekarang kamu punya `BRIEF.md`. Gunakan itu sebagai konteks. Prinsip: **minta AI membuat struktur, bukan langsung semua fitur**.

### Prompt awal yang baik

```
Baca file BRIEF.md di project ini.

Buatkan struktur project untuk aplikasi catatan pribadi dengan:
1. Folder dan file skeleton yang masuk akal (pisahkan logika, data, dan tampilan)
2. Pilih teknologi sederhana: Python + SQLite (data tersimpan lokal)
3. Jangan tulis implementasi penuh — cukup file kosong/kerangka dengan
   komentar singkat di tiap file tentang fungsinya
4. Jelaskan struktur folder yang kamu buat
```

### Kenapa prompt ini bagus?
- **Konteks jelas**: rujuk BRIEF.md (AI membaca file, bukan kamu menyalin isinya)
- **Constraint eksplisit**: Python + SQLite (bukan "terserah kamu")
- **Scope dibatasi**: minta skeleton dulu, bukan full app — lebih mudah dikoreksi
- **Minta penjelasan**: "jelaskan struktur" membuat AI berpikir, dan kamu belajar

## Memahami output AI

AI akan membuat folder seperti:
```
catatan/
├── app.py            # entry point & menu utama
├── database.py       # koneksi & fungsi CRUD SQLite
├── models.py         # struktur data catatan
├── requirements.txt  # dependency
└── BRIEF.md
```

Yang perlu kamu lakukan:
1. **Baca file-nya** — jangan Accept All buta. Ini beda vibe coder pemula vs yang paham.
2. **Tanyakan hal yang tidak kamu pahami** — prompt: *"Jelaskan baris per baris apa fungsi app.py"*
3. **Koreksi struktur yang tidak masuk akal** — misal AI membuat 20 file untuk aplikasi 5 fitur → minta disederhanakan

## Memilih stack (teknologi)

| Situasi | Rekomendasi |
|---|---|
| Belum pernah coding / fokus belajar konsep | Python (sederhana, mudah dibaca AI) |
| Mau web app cepat | Node.js + Express, atau Next.js (framework) |
| CLI tool / bot / script | Python atau Node tanpa framework |
| Sudah punya preferensi bahasa | Ikuti yang kamu kenal — AI bisa bahasa apa saja |

**Aturan praktis**: untuk belajar, mulai dari yang paling sedikit dependency. Framework menambah magic yang menyulitkan debugging di awal.

## Verifikasi: jalankan skeleton

Sebelum lanjut, pastikan skeleton tidak error:
```
python app.py
```
Kalau error, jangan panik — itu materi lesson 1.3.

## Latihan

1. Prompt AI untuk membuat struktur project dari BRIEF.md kamu
2. Baca setiap file yang dihasilkan; minta AI menjelaskan 1 file yang paling tidak kamu pahami
3. Jalankan skeleton; catat error-nya (untuk lesson 1.3)
4. Tanyakan ke AI: *"Apakah ada file/folder di struktur ini yang tidak perlu? Kenapa?"*

**Output lesson ini**: struktur project yang kamu pahami (bukan sekadar hasil generate), siap diisi fitur.
