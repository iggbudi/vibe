# 1.3 — Menjalankan & Debugging Pertama

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Menjalankan aplikasi dan membaca error log dengan benar
- Memberi error ke AI dengan format yang efektif (loop: run → error → fix → run)
- Berhenti dari siklus yang tidak produktif dan menulis ulang pendekatan

---

## Siklus vibe coding yang benar

```
1. RUN      → jalankan aplikasi
2. ERROR?   → salin pesan error LENGKAP
3. FIX      → kirim error ke AI + konteks
4. RUN      → jalankan lagi
5. Ulangi sampai jalan, lalu lanjut fitur berikutnya
```

Karpathy menyebut ini "see stuff, say stuff, run stuff" — tapi versi yang benar tetap **memahami** apa yang terjadi, bukan asal salin-tempel.

## Membaca error log

Error di terminal terlihat menakutkan, tapi punya struktur:

```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    db = Database("catatan.db")
  File "database.py", line 3, in __init__
    import sqlite3
ModuleNotFoundError: No module named 'sqlite3'
```

Yang penting:
1. **Jenis error** (baris terakhir): `ModuleNotFoundError`
2. **Lokasi**: `database.py, line 3`
3. **Pesan**: `No module named 'sqlite3'`

Kamu tidak perlu paham semua baris — AI yang akan menganalisis. Tugasmu: **menyalin error yang lengkap**.

## Memberi error ke AI: 3 aturan

### 1. Salin pesan error LENGKAP
❌ *"aplikasiku error, tolong betulin"*
✅ Salin seluruh traceback (bisa sampai 20 baris — salin semua)

### 2. Beri konteks minimal: apa yang kamu lakukan
```
Aku menjalankan `python app.py` dan mendapat error ini:
[tempel traceback]
Aku baru saja generate skeleton dari BRIEF. Belum ada perubahan manual.
```

### 3. Minta penjelasan singkat + perbaikan
```
Jelaskan penyebab error ini dalam 2-3 kalimat, lalu perbaiki.
Jangan ganti teknologi yang sudah dipilih.
```

## Teknik penting: failing test dulu

Untuk bug yang sulit, minta AI menulis **test yang mereproduksi bug** sebelum memperbaiki:
```
Buat test yang mereproduksi error ini dulu, jalankan sampai test-nya gagal
sesuai ekspektasi, baru perbaiki kode sampai test-nya lolos.
```
Ini membuat perbaikan bisa diverifikasi — prinsip "beri AI cara memverifikasi" dari best practices.

## Kapan harus berhenti & mulai ulang

Jika AI sudah dikoreksi **2-3 kali untuk masalah yang sama** dan tetap gagal:
1. Jangan lanjut menebak-nebak di sesi yang sama (context sudah kotor oleh pendekatan gagal)
2. **Mulai sesi baru** dengan prompt yang lebih spesifik, sertakan apa yang sudah dicoba dan gagal:
```
[Proyek baru] Aku mencoba X, mendapat error Y. Sudah dicoba: fix A, fix B —
tetap error yang sama. Analisis ulang dari awal: apa kemungkinan penyebab
root cause yang belum dicoba?
```

## Latihan (proyek: aplikasi catatan)

1. Jalankan skeleton dari 1.2 → salin error pertama (pasti ada!)
2. Kirim ke AI dengan format 3 aturan di atas → aplikasi jalan
3. Sekarang buat bug *dengan sengaja*: hapus 1 baris penting di salah satu file
4. Jalankan → salin error → minta AI menemukan & memperbaiki
5. Ulangi sampai kamu bisa memprediksi jenis error dari pesannya

**Output lesson ini**: aplikasi skeleton yang jalan tanpa error, plus pengalaman 5+ siklus debug.
