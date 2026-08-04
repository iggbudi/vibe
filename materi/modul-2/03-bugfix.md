# 2.3 — Bugfix

**Durasi**: 3 hari (±9 jam)
**Tujuan pembelajaran**:
- Mereproduksi bug dengan langkah yang bisa diulang
- Mengisolasi penyebab dengan teknik bisection
- Memastikan bugfix tidak merusak fitur lain (regression)

---

## Proses bugfix yang benar

```
1. REPRODUKSI  → buat langkah yang pasti memunculkan bug
2. ISOLASI     → persempit area kode penyebab
3. FAILING TEST→ tulis test yang mereproduksi (jika bisa)
4. FIX         → minta AI memperbaiki dengan evidence
5. VERIFIKASI  → test lolos + fitur lain tidak rusak
```

Mayoritas kesalahan bugfix: langsung lompat ke langkah 4 tanpa bukti. AI akan menebak, dan tebakan yang salah membuang waktu.

## 1. Reproduksi

Bug yang tidak bisa direproduksi = tidak bisa diperbaiki. Tulis langkahnya:
```
Bug: data penjualan tanggal kemarin tidak muncul di laporan.
Reproduksi:
1. Tambah transaksi kemarin (tanggal manual di set ke kemarin)
2. Buka halaman /laporan
3. Pilih rentang "7 hari terakhir"
4. Transaksi kemarin tidak tampil
```
Kirim ini ke AI sebagai gejala + langkah.

## 2. Isolasi dengan bisection

Kalau penyebab tidak jelas, sempitkan dengan **bisection** (belah dua):
- Matikan setengah fitur → cek apakah bug hilang
- Kalau hilang: bug di setengah itu → belah lagi
- Kalau tidak: bug di setengah lain

Untuk AI, minta bantuan isolasi:
```
Bug muncul di alur: input form → validasi → simpan → tampil di laporan.
Aku sudah pastikan simpan berhasil (data ada di database).
Jadi dugaan: bug di bagian baca/tampil. Konfirmasi dengan cara:
1. Baca file yang menangani query laporan
2. Identifikasi kondisi yang bisa membuat data kemarin terlewat
   (misal filter tanggal yang salah, timezone, atau perbandingan string vs datetime)
```

## 3. Failing test dulu (teknik terkuat)

Prinsip dari best practices: **beri AI cara memverifikasi**. Untuk bug:
```
Tulis dulu test yang mereproduksi bug ini (harus GAGAL dengan kode sekarang).
Jalankan sampai terbukti gagal, baru perbaiki kodenya sampai test LOLOS.
Jangan perbaiki sebelum test-nya ada.
```
Kenapa kuat: (a) kamu tahu persis kapan bug selesai, (b) test itu mencegah bug kembali, (c) AI tidak bisa bohong "sudah beres".

## 4. Minta fix dengan evidence

```
[KONTEKS]
Bug: [gejala + langkah reproduksi]
Sudah diisolasi: [temuan — file, baris, penyebab dugaan]
Test failing: [output test yang gagal]

[INSTRUKSI]
Perbaiki root cause-nya, jangan menutupi gejala (misal jangan cuma
menambah try-except yang menelan error).
Jelaskan apa akar masalahnya dalam 2-3 kalimat setelah perbaikan.
```

**"Jangan menutupi gejala"** penting — AI sering "menyembuhkan" dengan menelan error padahal datanya tetap salah.

## 5. Regression check

Setelah fix, pastikan tidak ada yang rusak:
1. Jalankan semua test: `pytest` / `npm test` / perintah test project
2. Kalau tidak ada test suite → tes manual alur inti: *"Jalankan aplikasi dan pastikan: tambah data, lihat laporan, edit data — semua normal"*
3. Minta AI: *"Review diff fix ini — apakah ada kemungkinan memengaruhi fitur X?"*

## Antipattern bugfix

| ❌ Jangan | ✅ Lakukan |
|---|---|
| "Betulin error ini" + tempel 1 baris error | Gejala lengkap + langkah reproduksi |
| Langsung minta fix tanpa isolasi | Minta AI isolasi dulu, atau bisection sendiri |
| Menerima fix yang "kelihatannya benar" | Minta test yang membuktikan |
| Fix berkali-kali di sesi sama (context kotor) | Setelah 2-3 gagal: `/clear`, prompt ulang dengan temuan |

## Latihan

1. Ambil aplikasi (dari 2.1). **Cari bug asli** — minta AI: *"Review kode ini, temukan 1 bug logika yang nyata (bukan gaya)"*
2. Reproduksi bug itu → tulis langkahnya
3. Minta AI menulis failing test → verifikasi test gagal
4. Minta fix (dengan evidence) → verifikasi test lolos
5. Regression: jalankan semua test / tes manual alur inti

**Output lesson ini**: 1 bug nyata diperbaiki dengan alur reproduksi → test → fix → regression.
