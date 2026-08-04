# 2.4 — Menambah Fitur Kecil

**Durasi**: 4 hari (±12 jam)
**Tujuan pembelajaran**:
- Menambah fitur CRUD/validasi/UI baru dengan pola existing
- Membuat keputusan: kapan tanya AI, kapan ubah sendiri
- Menulis acceptance criteria sebelum mulai

---

## Pola penambahan fitur kecil

Fitur kecil = bisa dijelaskan dalam 1-2 kalimat, menyentuh 1-3 file. Contoh: field baru, validasi baru, endpoint baru, tombol baru.

Workflow:
```
1. Tulis acceptance criteria (bagaimana tahu fitur SELESAI?)
2. Beri AI konteks (template 2.2)
3. Minta implementasi + verifikasi
4. Review diff + tes manual
5. Commit
```

## Acceptance criteria dulu

Sebelum minta AI melakukan apa pun, tulis "cara tahu ini selesai":

```
Fitur: tambah field "kategori" di form transaksi.
Selesai ketika:
1. Form transaksi punya input kategori (dropdown: Makanan, Transport, Lainnya)
2. Kategori tersimpan di database (cek tabel)
3. Kategori tampil di daftar transaksi
4. Transaksi lama tanpa kategori tampil sebagai "Tanpa kategori" (tidak crash!)
```

Perhatikan poin 4 — edge case yang sering dilupakan AI. Acceptance criteria yang baik menangkapnya.

## Prompt untuk fitur kecil

```
[KONTEKS]
Project: [nama]. Baca file-file relevan dulu: @app.py @models.py @templates/

[FITUR]
Tambah field "kategori" di transaksi sesuai acceptance criteria berikut:
[tempel criteria]

[INSTRUKSI]
- Ikuti pola existing untuk field lain (lihat bagaimana field "catatan" dibuat)
- Perhatikan migrasi data lama: transaksi yang sudah ada tidak boleh rusak

[VERIFIKASI]
- Jalankan aplikasi, tes criteria 1-4
- Laporkan hasil tiap criteria: lolos/gagal
```

## Menangani perubahan database (migrasi)

Fitur kecil sering mengubah struktur data. Aturan penting:

1. **Backup dulu**: salin file database sebelum mengubah skema
   ```bash
   cp app.db app.db.bak-$(date +%Y%m%d)
   ```
2. **Minta AI menulis migrasi**:
   ```
   Ubah skema: tambah kolom kategori (TEXT, default NULL) di tabel transaksi.
   Tulis script migrasi yang aman: cek kolom belum ada sebelum ALTER TABLE,
   dan JANGAN hapus data lama.
   ```
3. **Jangan pernah** minta AI "reset database" saat data masih dipakai

## Kapan tanya AI vs ubah sendiri?

| Situasi | Keputusan |
|---|---|
| Mengubah 1 baris yang jelas (fix typo, ganti angka) | **Ubah sendiri** — lebih cepat dari prompt |
| Fitur baru yang butuh paham arsitektur | **Tanya AI** (dengan konteks) |
| Kamu sudah tahu persis solusinya, tinggal ketik | **Ubah sendiri** — latihan yang bagus |
| Tidak tahu file mana yang harus diubah | **Tanya AI**: *"File mana yang perlu diubah untuk X?"* |
| Butuh kode boilerplate / pola yang berulang | **Tanya AI** — ini kekuatan utamanya |

Prinsip: **AI untuk yang tidak kamu tahu, tanganmu untuk yang sudah kamu tahu**. Semakin sering kamu mengubah sendiri, semakin baik kamu mengevaluasi output AI.

## Latihan

Di aplikasi 2.1, tambahkan 2 fitur kecil. Rekomendasi (pilih sesuai app):
1. Validasi input (misal: field wajib, format email, angka positif)
2. Field baru dengan migrasi aman (misal: tambah "kategori" seperti contoh)
3. Sorting/filter di halaman daftar
4. Konfirmasi sebelum hapus data

Untuk tiap fitur:
- Tulis acceptance criteria dulu
- Kerjakan via AI dengan template prompt
- Verifikasi tiap criteria, catat hasilnya
- Satu fitur = satu commit

**Output lesson ini**: 2 fitur kecil terimplementasi + 2 commit rapi + pengalaman menulis acceptance criteria.
