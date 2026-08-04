# 2.2 — Memberi Konteks ke AI

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Format prompt untuk codebase besar (file paths, snippet, error, expected behavior)
- Menulis prompt yang memaksa AI membaca kode, bukan menebak
- Mengelola context window agar tetap efisien

---

## Masalah utama: AI tidak tahu codebase-mu

Berbeda dengan Modul 1 (project kecil yang AI generate sendiri), di codebase existing AI sering:
- Menebak struktur yang salah
- Menulis kode dengan gaya berbeda dari pola existing
- Membuat file baru padahal seharusnya mengubah file yang ada

Solusinya: **beri konteks yang cukup + perintahkan AI membaca kode dulu**.

## Template prompt untuk codebase existing

```
[KONTEKS]
Project: [nama, 1 kalimat]
File yang relevan: [daftar path spesifik]
Bagian yang dipahami: [ringkas 2-3 kalimat tentang struktur]
Bug/fitur: [deskripsi gejala ATAU spesifikasi]

[INSTRUKSI]
1. Baca file yang relevan dulu sebelum menjawab
2. Ikuti pola & gaya kode yang sudah ada
3. [tugas spesifik]

[CONSTRAINTS]
- Jangan ubah: [file/feature yang tidak boleh disentuh]
- Jangan tambah dependency baru tanpa konfirmasi
- [batasan lain]

[VERIFIKASI]
- Setelah selesai, jalankan [perintah] dan pastikan [hasil yang diharapkan]
- Laporkan file yang kamu ubah
```

## Contoh nyata (kurang vs baik)

**❌ Kurang (AI akan menebak-nebak):**
```
Tambah fitur export CSV di aplikasi penjualan
```

**✅ Baik:**
```
[KONTEKS]
Project: aplikasi penjualan kasir. Stack: Python Flask + SQLite.
File relevan:
- app.py (routes & entry point)
- models.py (struktur data)
- templates/ (HTML)

[INSTRUKSI]
1. Baca app.py dan models.py dulu
2. Tambah endpoint /export-csv yang mengekspor daftar transaksi
   ke file CSV (ikutkan pola route yang sudah ada)
3. Tambah link "Export" di halaman daftar transaksi (templates/)

[CONSTRAINTS]
- Jangan ubah cara penyimpanan data di models.py
- Jangan tambah library baru — pakai csv bawaan Python

[VERIFIKASI]
- Jalankan app dan tes endpoint /export-csv
- Pastikan halaman daftar transaksi masih normal
```

## Teknik "@" dan rujukan file

Kalau tool-mu mendukung (seperti pi/Claude Code), sebutkan path file dengan `@` agar AI membacanya otomatis:
```
@app.py @models.py — jelaskan bagaimana data transaksi mengalir dari form ke database
```

Lebih baik lagi: biarkan AI menemukan sendiri dengan prompt:
```
Cari tahu di file mana transaksi disimpan (grep untuk "transaksi"),
lalu usulkan di mana fitur export CSV sebaiknya ditambahkan.
```

## Mengelola context window

Context window adalah resource paling penting (best practice #1). Di codebase besar:

1. **Jangan tempel 10 file sekaligus** — cukup file yang relevan dengan tugas ini
2. **Minta ringkasan dulu**: *"Baca app.py dan ringkas strukturnya dalam 10 baris"* sebelum minta perubahan
3. **Satu tugas per sesi** — selesai satu fitur, `/clear`, mulai tugas baru
4. **Gunakan file instruksi** (CLAUDE.md/AGENTS.md): tulis aturan project di sana agar tidak perlu diulang di setiap prompt
5. Kalau AI mulai "lupa" instruksi awal → context penuh → `/clear` dan mulai sesi baru

## Latihan

Di project yang sama dengan 2.1:
1. Tulis prompt untuk fitur kecil (misal: "tambah validasi: nama tidak boleh kosong") pakai template di atas
2. Sebelum mengirim, periksa: apakah prompt sudah punya konteks, instruksi, constraints, verifikasi?
3. Kirim. Setelah AI selesai, cek: apakah AI benar-benar membaca file yang diminta (lihat apakah jawabannya konsisten dengan isi file)?
4. Ulangi dengan prompt yang sengaja TANPA konteks → bandingkan kualitasnya

**Output lesson ini**: kemampuan menulis prompt konteks-lengkap yang bisa dipakai berulang.
