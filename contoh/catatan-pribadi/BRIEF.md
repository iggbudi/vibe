# BRIEF — Aplikasi Catatan Pribadi

Aplikasi: **Catatan Pribadi**
Deskripsi: aplikasi CLI untuk menyimpan, mengelola, dan mencari catatan pribadi — offline, data tersimpan lokal.

Fitur (urut prioritas):
1. Tambah catatan baru (judul, isi, kategori)
2. Lihat daftar semua catatan
3. Lihat detail satu catatan
4. Edit catatan (judul/isi/kategori)
5. Hapus catatan (dengan konfirmasi)
6. Cari catatan berdasarkan kata kunci (judul/isi/kategori)

User flow:
- User membuka aplikasi → melihat menu
- User memilih "Tambah" → mengisi judul/isi/kategori → tersimpan
- User memilih "Daftar" → melihat semua catatan (id, judul, kategori, tanggal)
- User memilih "Detail" → memasukkan id → melihat isi lengkap
- User memilih "Edit" → memasukkan id → mengubah field → tersimpan
- User memilih "Hapus" → memasukkan id → konfirmasi → terhapus
- User memilih "Cari" → memasukkan kata kunci → melihat hasil

Data yang disimpan:
- Catatan: id (angka), judul (teks), isi (teks panjang), kategori (teks), tanggal_dibuat, tanggal_diubah

Batasan:
- Tidak perlu login
- Offline-only, data di SQLite (file catatan.db)
- CLI sederhana, tanpa library tambahan (Python standar)
