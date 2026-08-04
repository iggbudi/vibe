# 0.5 — Menulis Prompt Efektif

**Durasi**: 1 hari (±3 jam) + praktikum
**Tujuan pembelajaran**:
- Menulis prompt dengan struktur: konteks → instruksi → constraints → acceptance criteria
- Mengevaluasi kualitas output AI dengan rubrik
- Memperbaiki prompt berdasarkan evaluasi (iterasi)

---

## Struktur prompt: 4 bagian

```
[1. KONTEKS]   — apa yang AI perlu tahu (project, file, latar belakang)
[2. INSTRUKSI] — apa yang harus AI lakukan (spesifik, terukur)
[3. CONSTRAINTS] — apa yang TIDAK boleh (teknologi, file, dependency)
[4. ACCEPTANCE CRITERIA] — bagaimana tahu hasilnya benar
```

### Contoh kurang vs baik

**❌ Kurang:**
```
Buatkan kalkulator
```

**✅ Baik:**
```
[KONTEKS]
Aku sedang belajar Python di Termux. Versi Python: 3.12. Aku belum
pernah menulis program sebelumnya.

[INSTRUKSI]
Buatkan program kalkulator CLI bernama kalkulator.py yang bisa:
- Menambah, mengurangi, mengalikan, membagi dua angka
- User memasukkan angka lewat input (misal: "5 + 3")
- Loop: setelah selesai, tanya "lagi? (y/n)" dan ulangi jika y

[CONSTRAINTS]
- Pakai Python standar saja, tanpa library tambahan
- Tampilkan pesan error ramah jika input tidak valid
- Kode harus mudah dibaca pemula: beri komentar singkat

[ACCEPTANCE]
- Menjalankan `python kalkulator.py` lalu input "5 + 3" → output "8"
- Input "10 / 0" → pesan error yang jelas, program tidak crash
```

Kenapa prompt ini jauh lebih baik: AI tidak perlu menebak platform, gaya, scope, atau definisi "selesai".

## Rubrik evaluasi output AI

Gunakan ini untuk menilai tiap output:

| Aspek | Pertanyaan | Skor 1-5 |
|---|---|---|
| **Fungsional** | Apakah berjalan & menghasilkan output yang diminta? | |
| **Akurat** | Apakah sesuai instruksi, tidak menambah/mengurangi? | |
| **Terverifikasi** | Apakah kamu bisa membuktikan hasilnya (bukan cuma percaya)? | |
| **Dapat dipahami** | Apakah kamu bisa menjelaskan cara kerjanya? | |
| **Aman** | Tidak ada secret, validasi input, error handling wajar? | |

Skor total < 15 → perbaiki prompt & minta ulang. 15-20 → bagus. 20-25 → luar biasa.

## Pola prompt yang sering dipakai

| Tujuan | Pola |
|---|---|
| Minta penjelasan | *"Jelaskan [konsep/kode] dengan analogi sederhana, seperti menjelaskan ke anak SMA"* |
| Minta generate | *"[struktur 4 bagian]"* |
| Minta review | *"Review [kode/file] untuk [aspek]: sebutkan baris spesifik + perbaikan"* |
| Minta perbaiki error | *"Aku menjalankan X dan dapat error: [tempel lengkap]. Jelaskan penyebab + perbaiki"* |
| Minta alternatif | *"Ada pendekatan lain untuk [masalah]? Bandingkan trade-off-nya"* |
| Minta ajarkan | *"Ajar aku konsep [X] sambil kita kerjakan [tugas] — jangan beri jawaban dulu, bimbing langkah demi langkah"* |

## Kesalahan umum menulis prompt

| ❌ Kesalahan | ✅ Perbaikan |
|---|---|
| Terlalu umum ("buatkan aplikasi") | Sebutkan platform, fitur, constraint |
| Terlalu panjang & campur aduk | Satu prompt = satu tugas, pisahkan dengan sesi baru |
| Tidak menyebut batasan | AI akan memilih sendiri — sering salah pilih |
| Tidak menyebut "selesai" seperti apa | AI berhenti lebih awal / tidak tahu kapan selesai |
| Menyalin error setengah-setengah | Tempel traceback lengkap |
| Memakai istilah yang kamu sendiri tidak paham | Minta AI jelaskan istilah itu dulu |

## Latihan: 5 prompt percobaan (praktikum akhir modul)

Buat 5 prompt coding dengan tingkat kesulitan meningkat:

1. **Prompt #1** (mudah): program mencetak "Halo" 10 kali
2. **Prompt #2**: program menghitung FPB dua angka
3. **Prompt #3**: program menyimpan & menampilkan daftar tugas (list)
4. **Prompt #4**: program membaca file teks & menghitung jumlah kata
5. **Prompt #5** (paling sulit): gabungkan — program daftar tugas yang simpan ke file

Untuk tiap prompt:
1. Tulis dengan struktur 4 bagian lengkap
2. Kirim ke AI
3. Evaluasi dengan rubrik di atas
4. Jika skor < 15: perbaiki prompt → kirim ulang → bandingkan
5. Catat di `JURNAL_PROMPT.md`: prompt awal, perbaikan, skor, pelajaran

**Output lesson ini**: kebiasaan menulis prompt terstruktur + jurnal 5 percobaan dengan evaluasi.

---

## Ceklist Praktikum Akhir Modul 0

- [ ] Semua tools terinstall (ceklist 0.3)
- [ ] 5 prompt percobaan ditulis & dievaluasi (rubrik 0.5)
- [ ] Minimal 2 prompt diperbaiki & hasilnya lebih baik
- [ ] Secret management dipraktikkan (tidak ada secret di kode)
- [ ] Paham perbedaan assistant vs agent vs IDE
- [ ] Bisa menjelaskan apa itu vibe coding ke orang lain
