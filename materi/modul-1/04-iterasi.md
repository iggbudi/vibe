# 1.4 — Iterasi Fitur & UX

**Durasi**: 3 hari (±9 jam)
**Tujuan pembelajaran**:
- Menambah fitur incremental tanpa merusak yang sudah jalan
- Menjaga kualitas: minta AI menjelaskan perubahan, minta test
- Mengenali kapan kode perlu refactor vs dibiarkan

---

## Prinsip: satu fitur per iterasi

Setelah skeleton jalan, mulailah dari BRIEF.md:
1. Kerjakan **fitur #1** sampai benar-benar berfungsi
2. Verifikasi manual
3. Commit (lesson 1.5)
4. Lanjut fitur #2

Jangan minta AI "kerjakan semua fitur sekaligus" — error menjadi mustahil dilacak.

## Prompt untuk menambah fitur

Pola yang terbukti (dari best practices: scope + verifikasi):

```
Tambah fitur "edit catatan" ke aplikasi:
1. Lihat dulu struktur yang ada (app.py, database.py) — ikuti pola kode existing
2. Implementasi edit: pilih catatan dari daftar → ubah judul/isi → simpan
3. Jangan ubah fitur tambah & hapus yang sudah ada
4. Setelah selesai, jalankan aplikasi dan pastikan: tambah → edit → hapus
   semua berfungsi. Laporkan hasilnya.
```

Kenapa prompt ini bagus:
- **"Lihat dulu... ikuti pola existing"** → AI konsisten dengan kode lama
- **"Jangan ubah fitur yang sudah ada"** → mencegah regresi
- **"Setelah selesai, jalankan dan pastikan"** → AI memverifikasi sendiri

## Verifikasi: jangan pernah percaya "sudah jadi"

Pola kegagalan paling umum: AI bilang selesai, kamu jalankan, error. Best practice Anthropic menyebutnya *trust-then-verify gap*.

Rutinitas wajib setelah AI selesai:
1. **Jalankan aplikasi** dan tes semua alur inti (tambah, lihat, edit, hapus)
2. **Baca diff-nya** — minta AI: *"Tunjukkan perubahan yang kamu buat, file apa saja dan fungsi apa yang berubah"*
3. **Tanyakan edge case**: *"Apa yang terjadi kalau user mengisi judul kosong? Kalau catatan tidak ada?"* — minta AI menanganinya atau setidaknya menjelaskan

## Menjaga kualitas kode

| Situasi | Tindakan |
|---|---|
| AI menambah 100 baris untuk fitur 10 baris | Minta penjelasan: *"Kenapa perlu X? Bisa disederhanakan?"* |
| Fungsi yang sama ada di 3 tempat | Minta refactor kecil: *"Gabungkan logika duplikat jadi satu fungsi"* |
| Kode jalan tapi kamu tidak paham | *"Jelaskan cara kerja fungsi ini dengan analogi sederhana"* |
| Fitur baru membuat fitur lama rusak | Git revert / rollback (lesson 1.5) — jangan perbaiki manual di atasnya |

**Aturan emas**: kamu harus bisa menjelaskan setiap fungsi di aplikasimu dalam 1-2 kalimat. Kalau tidak, kamu tidak punya aplikasi — kamu punya teks ajaib yang kebetulan jalan.

## Kapan "cukup" untuk MVP?

Fitur inti BRIEF selesai semua & jalan → itu MVP (Minimum Viable Product). Berhenti menambah fitur. Sisanya:
- Polish UX (pesan error yang ramah, konfirmasi sebelum hapus)
- Ditulis di daftar "ide lanjutan" (backlog) untuk nanti

## Latihan

1. Kerjakan fitur BRIEF satu per satu, pakai pola prompt di atas
2. Untuk setiap fitur: jalankan, tes semua alur, minta AI jelaskan perubahan
3. Setelah 2 fitur, review kode bersama AI: *"Review kode ini: mana yang bisa disederhanakan, mana yang berisiko bug?"*
4. Tulis backlog 3 ide fitur lanjutan di README (bukan implementasi sekarang)

**Output lesson ini**: MVP aplikasi catatan — semua fitur inti berfungsi, kamu bisa menjelaskan cara kerjanya.
