# Capstone — Evaluasi & Rubrik

## Bobot Penilaian

| Aspek | Bobot | Yang dinilai |
|---|---|---|
| **Fungsionalitas** | 40% | Aplikasi benar-benar bekerja, fitur sesuai brief |
| **Kualitas kode & dokumentasi** | 20% | Struktur, README, secret aman, error handling |
| **Kemampuan prompt & iterasi** | 20% | Git history + refleksi menunjukkan proses yang matang |
| **Presentasi** | 20% | Demo video jelas, menjelaskan dengan percaya diri |

---

## Rubrik per aspek (level 1-4)

### A. Fungsionalitas (40%)

| Level | Deskripsi |
|---|---|
| **1** | Fitur inti tidak berjalan / banyak yang error |
| **2** | Fitur inti jalan, tapi rapuh: crash pada input aneh, data mudah hilang |
| **3** | Semua fitur brief berfungsi stabil; integrasi jalan; edge case utama ditangani |
| **4** | Fitur berfungsi penuh + tahan banting: kegagalan eksternal ditangani anggun, ada verifikasi (test/checklist), UX dipoles |

### B. Kualitas Kode & Dokumentasi (20%)

| Level | Deskripsi |
|---|---|
| **1** | Satu file raksasa tanpa struktur; README kosong |
| **2** | Ada struktur folder; README minimal; secret mulai aman |
| **3** | Struktur jelas & logis; README lengkap (install + pakai); secret aman (env); error handling ada |
| **4** | Kode mudah dibaca & dipahami (komentar bermakna, fungsi kecil); README profesional; dokumentasi integrasi & cara test; `.gitignore` sempurna |

### C. Kemampuan Prompt & Iterasi (20%) — dinilai dari git history & refleksi

| Level | Deskripsi |
|---|---|
| **1** | 1-2 commit besar "semua"; tidak ada bukti iterasi |
| **2** | Commit per fitur; refleksi ada tapi dangkal |
| **3** | Git history menceritakan proses nyata: fitur bertahap, perbaikan setelah gagal, pesan commit bermakna; refleksi jujur tentang kegagalan & perbaikan |
| **4** | History menunjukkan *kebiasaan*: fitur kecil dulu lalu refactor, revert yang beralasan, test sebelum fix; refleksi menunjukkan pemahaman mendalam kenapa prompt tertentu berhasil/gagal |

### D. Presentasi (20%)

| Level | Deskripsi |
|---|---|
| **1** | Video tidak ada / tidak bisa menjelaskan projectnya |
| **2** | Demo berjalan tapi penjelasan datar; tidak ada konteks masalah |
| **3** | Struktur video sesuai panduan (masalah → solusi → cara kerja → tantangan); menjelaskan keputusan dengan alasan |
| **4** | Presentasi mengalir, menunjukkan bagian yang menantang secara jujur, mendemonstrasikan ketahanan (kegagalan yang ditangani), dan menjawab "kenapa" di setiap keputusan |

---

## Penilaian akhir

```
Total = 0.40×A + 0.20×B + 0.20×C + 0.20×D
```

| Rentang | Predikat |
|---|---|
| 3.5 - 4.0 | 🏆 **Luar biasa** — siap bekerja dengan workflow AI di tim profesional |
| 2.8 - 3.4 | ✅ **Lulus** — pola vibe coding yang sehat terbentuk |
| 2.0 - 2.7 | 🔄 **Lulus bersyarat** — perbaiki aspek yang lemah (biasanya verifikasi & dokumentasi), kumpulkan ulang |
| < 2.0 | 📚 **Ulangi** — ada gap fundamental (biasanya: tidak paham kode sendiri / secret bocor) |

## Catatan penting

1. **Kamu tidak perlu level 4 di semua aspek** — level 3 di semua aspek sudah predikat "Lulus"
2. **Secret bocor = langsung diskusi serius** — tidak peduli level lain, ini menunjukkan Modul 0.4 belum tertanam
3. **"AI yang salah" bukan alasan** — evaluasi menilai bagaimana kamu *menangani* kesalahan AI: apakah diverifikasi, apakah diperbaiki, apakah dipahami
4. **Kejujuran lebih dihargai daripada kesempurnaan** — refleksi yang jujur tentang kegagalan (level 3-4 di aspek C) jauh lebih baik daripada klaim sempurna yang tidak didukung bukti

## Sebelum presentasi, self-review dengan rubrik

1. Baca rubrik level 3 untuk keempat aspek
2. Periksa deliverable-mu satu per satu terhadap level 3
3. Catat kekurangan → perbaiki
4. Kalau ragu, tanyakan ke AI: *"Review repo ini terhadap kriteria ini: [tempel rubrik level 3]. Sebutkan gap spesifik dengan file/baris."*
