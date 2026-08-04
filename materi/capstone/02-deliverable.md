# Capstone — Deliverable

Tiga hal yang dikumpulkan: **Repo GitHub**, **Demo video**, **Refleksi tertulis**. Semua wajib — ketiganya dinilai (lihat 03-evaluasi.md).

---

## 1. Repo GitHub

### Struktur minimum
```
nama-project/
├── README.md          # wajib — lihat template
├── BRIEF.md           # (pilihan A & C) product brief awal
├── PETA.md            # (pilihan B) pemetaan codebase
├── REFLEKSI.md        # wajib — refleksi capstone
├── .gitignore         # wajib — .env, database, dependency
├── src/ atau struktur project-mu
└── tests/ (jika ada)
```

### README yang baik
```
# Nama Project

Deskripsi 1 kalimat: [apa & untuk siapa]

## Fitur
- [fitur 1]
- [fitur 2]
- [fitur 3]

## Cara Install
[perintah dari nol — orang lain harus bisa menjalankan]

## Cara Pakai
[contoh penggunaan]

## Integrasi
[layanan pihak ketiga yang dipakai & mengapa]

## Struktur
[file penting & fungsinya]
```

### Git history yang dinilai
- Commit per fitur/step dengan pesan deskriptif (bukan "update", "fix", "asd")
- Commit kecil & logis: `feat: tambah input kategori`, `fix: tangani transaksi tanpa kategori`
- Tidak ada secret di history (periksa: `git log -p | grep -i "sk-\|password\|token"`)

## 2. Demo Video (±5 menit)

### Struktur video
| Waktu | Isi |
|---|---|
| 0:00-0:30 | Masalah: apa yang kamu pecahkan & kenapa |
| 0:30-1:30 | Solusi: demo aplikasi berfungsi (fitur utama) |
| 1:30-3:30 | Cara kerja: struktur, alur data, bagian menarik/menantang |
| 3:30-4:30 | Integrasi: layanan eksternal & bagaimana kegagalan ditangani |
| 4:30-5:00 | Tantangan: hal tersulit & bagaimana kamu mengatasinya |

### Aturan
- Rekam layar (screencast) — tidak perlu wajah, tapi suara jelas
- **Tunjukkan aplikasi berjalan**, bukan slide
- Tunjukkan minimal 1 kegagalan yang ditangani dengan baik (misal: API mati → pesan error ramah) — ini bukti penguasaan Modul 4.5
- 5 menit, tidak lebih. Padat.

## 3. Refleksi Tertulis (`REFLEKSI.md`)

Template (jawab semua):

```markdown
# Refleksi Capstone

## Ringkasan
- Project: [nama] — [1-2 kalimat]
- Pilihan: A / B / C

## Prompt Terbaik
- Tempel 1 prompt yang menghasilkan output terbaik
- Kenapa efektif? (struktur apa yang kamu pakai?)

## Prompt Terburuk / Kegagalan
- Tempel 1 prompt yang gagal total (atau hasil yang menyesatkan)
- Apa yang salah? Bagaimana kamu memperbaikinya?

## Momen AI Menyesatkan
- Ceritakan 1 momen AI "mengaku sukses" padahal gagal, atau mengarang sesuatu
- Bagaimana kamu mengetahuinya? (verifikasi apa yang kamu lakukan?)

## Keputusan Penting
- 2 keputusan arsitektur/desain yang kamu buat
- Kenapa memilih itu? Alternatif apa yang ditolak & kenapa?

## Keterampilan yang Tumbuh
- [keterampilan] → [bukti di project ini]
- Minimal 3

## Masih Ingin Dipelajari
- [topik lanjutan yang kamu incar setelah kursus]

## Feedback Pengguna (opsional, untuk pilihan C)
- [siapa yang mencoba bot-mu? Apa feedback-nya? Apa yang kamu ubah?]
```

### Kenapa refleksi dinilai?
Kemampuan prompt & iterasi **tidak terlihat dari kode jadi** — hanya terlihat dari prosesnya. Git history menunjukkan proses (20%), refleksi menjelaskan *mengapa*. Dua-duanya dibutuhkan.

---

## Checklist pengumpulan
- [ ] Repo publik di GitHub (pilihan B: PR ke project lain + repo catatanmu sendiri)
- [ ] README lengkap (orang lain bisa menjalankan)
- [ ] Git history bersih & bermakna
- [ ] Tidak ada secret di repo (audit!)
- [ ] Video demo ±5 menit sesuai struktur
- [ ] REFLEKSI.md lengkap (semua bagian terisi)
