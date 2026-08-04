# Kurikulum Vibe Coding — Outline

> **Status**: DRAFT v0.1
> **Tujuan project**: Kurikulum praktis untuk belajar Vibe Coding — pendekatan pengembangan software dengan bantuan AI sebagai rekan kerja, bukan sekadar "menyalin kode".

---

## 1. Ringkasan Kursus

| Item | Detail |
|---|---|
| **Judul** | Vibe Coding: Dari Nol Sampai Integrasi |
| **Durasi total** | ± 12 minggu (bisa dipadatkan) |
| **Format** | Learning-by-doing, proyek tiap modul |
| **Target peserta** | Pemula yang bisa mengoperasikan komputer, sampai developer yang ingin beralih ke workflow AI-assisted |
| **Prasyarat** | Bisa menggunakan terminal dasar, memahami konsep file & folder |
| **Tools utama** | AI assistant (Claude/ChatGPT/Gemini), agent coding (pi/Cursor), runtime (Termux/Node/Python), git |

### Hasil belajar akhir (Course Learning Outcomes)
1. Peserta mampu membangun aplikasi baru dari nol hanya dengan mendeskripsikan kebutuhan ke AI, lalu mengiterasinya sampai berfungsi.
2. Peserta mampu menavigasi codebase existing, dan menambah fitur tanpa merusak fungsi yang ada.
3. Peserta mampu membangun chatbot yang mengotomasi pekerjaan dan menyajikan analitik data.
4. Peserta mampu mengintegrasikan aplikasi dengan API & tools pihak ketiga (webhook, database, payment, messaging).

### Alur pedagogi
Setiap modul mengikuti siklus: **Lihat → Coba → Bangun → Ulangi** dengan spiral difficulty — konsep yang sama (prompting, iterasi, debugging) diulang di level yang lebih dalam di setiap modul.

---

## 2. Modul 0 — Fondasi Vibe Coding (1 minggu)

**Tujuan**: Memahami paradigma vibe coding & menyiapkan lingkungan kerja.

| # | Lesson | Materi | Hasil belajar |
|---|---|---|---|
| 0.1 | Apa itu Vibe Coding | Sejarah singkat (Karpathy 2025), perbedaan dengan coding tradisional, kekuatan & batasannya | Bisa menjelaskan kapan vibe coding tepat digunakan |
| 0.2 | Ekosistem tools | AI assistant vs agent vs IDE; cara kerja LLM untuk kode; model & API | Bisa memilih tool yang sesuai kebutuhan |
| 0.3 | Setup lingkungan | Install runtime (Node/Python), terminal, git, agent coding (pi) di Termux/desktop | Lingkungan siap dipakai |
| 0.4 | Etika & keamanan | Review kode AI, secret management, bias & halusinasi AI | Mengetahui red flags & best practice keamanan |
| 0.5 | Menulis prompt efektif | Struktur prompt: konteks → instruksi → constraints → acceptance criteria | Bisa menulis prompt yang menghasilkan output berkualitas |

**Praktikum**: Install & konfigurasi semua tools, lalu buat 5 prompt percobaan ke AI dan evaluasi kualitasnya.

---

## 3. Modul 1 — Memulai dari Nol (3 minggu)

**Tujuan**: Membangun aplikasi baru dari halaman kosong.

### 1.1 Spesifikasi dari ide
- Menerjemahkan ide ke requirement: fitur, user flow, data apa saja yang disimpan
- Menulis *product brief* singkat yang bisa dibaca AI
- **Latihan**: tulis brief untuk "aplikasi catatan pribadi" dalam 10 baris

### 1.2 Generate struktur project
- Prompt pertama: meminta struktur folder + file skeleton
- Memahami output AI: apa yang perlu dipertahankan vs dibuang
- Stack choice: kapan memilih framework vs plain code

### 1.3 Menjalankan & debugging pertama
- Menjalankan aplikasi, membaca error log, memberi error ke AI
- Siklus: run → error → prompt perbaikan → run ulang
- **Praktikum**: buat aplikasi CLI sederhana (kalkulator/todo) sampai jalan tanpa bug

### 1.4 Iterasi fitur & UX
- Menambah fitur incremental: validasi input, persistensi data (file/JSON/SQLite)
- Menjaga kualitas: meminta AI menjelaskan perubahan, refactor bila perlu

### 1.5 Version control & dokumentasi
- Git dasar: init, commit, branch; menulis README dengan bantuan AI
- Kenapa dokumentasi penting untuk kolaborasi AI selanjutnya

**Proyek Modul 1**: Aplikasi "Todo list + catatan" dengan GUI terminal atau web sederhana, tersimpan di database SQLite, terdokumentasi di README.

**Kriteria penilaian**: (a) jalan tanpa error, (b) data persisten setelah restart, (c) README jelas, (d) history git rapi.

---

## 4. Modul 2 — Menambah Fitur di Aplikasi yang Sudah Jalan (3 minggu)

**Tujuan**: Bekerja di codebase existing tanpa merusaknya.

### 2.1 Membaca codebase
- Menemukan entry point, memahami arsitektur (folder, dependency)
- Teknik eksplorasi: grep, tree, membaca config, menjalankan test
- Membangun "peta mental" yang bisa dikomunikasikan ke AI

### 2.2 Memberi konteks ke AI
- Format prompt untuk codebase besar: file paths, snippet relevan, error log, expected behavior
- **Latihan**: ambil project Modul 1, minta AI menambah fitur hanya dengan konteks yang tepat

### 2.3 Bugfix
- Reproduksi bug, isolasi penyebab, prompt perbaikan yang menyertakan evidence
- Regression: memastikan bugfix tidak merusak fitur lain

### 2.4 Menambah fitur kecil
- Fitur CRUD baru, validasi baru, perubahan UI kecil
- Kapan harus bertanya ke AI vs mengubah sendiri (trade-off)

### 2.5 Fitur besar & refactoring aman
- Perubahan skema database, migration
- Refactoring dengan safety net: test sebelum & sesudah, git branch terpisah
- Strategi rollback

**Proyek Modul 2**: Pada aplikasi yang *diberikan* (bukan buatan sendiri), tambahkan 2 fitur baru + 1 bugfix, lengkap dengan dokumentasi perubahan dan test regresi.

**Kriteria penilaian**: (a) fitur berfungsi, (b) fitur lama tidak rusak, (c) perubahan terdokumentasi di git log, (d) konteks prompt bisa dijelaskan ulang oleh peserta.

---

## 5. Modul 3 — Chatbot untuk Otomasi & Analitik (3 minggu)

**Tujuan**: Membangun chatbot yang benar-benar bekerja (bukan demo).

### 3.1 Konsep chatbot & LLM API
- System prompt, user prompt, conversation context
- API LLM: struktur request/response, token, temperature
- **Praktikum**: chatbot CLI pertama dengan API LLM

### 3.2 Membangun chat service
- State management percakapan (session, history)
- Menambah fungsi: tool calling / function calling untuk aksi nyata

### 3.3 Otomasi
- Integrasi dengan platform chat (Telegram/WhatsApp API)
- Menjadwalkan tugas (cron/scheduler)
- **Praktikum**: bot Telegram yang menjalankan perintah (cek status server, kirim reminder, jalankan script)

### 3.4 Analitik
- Chatbot yang query database (SQL) dan merangkum hasil
- RAG sederhana: memuat dokumen, chunking, embedding, retrieval
- **Praktikum**: bot yang menjawab pertanyaan dari data penjualan & menghasilkan ringkasan harian

### 3.5 Production-readiness
- Logging, error handling, retry, rate limit
- Konfigurasi via environment variables (secret management)

**Proyek Modul 3**: Bot Telegram "asisten operasional" yang (a) menjalankan otomasi terjadwal, (b) menjawab pertanyaan dari database, (c) mengirim laporan analitik harian.

**Kriteria penilaian**: (a) bot berjalan 24 jam stabil, (b) perintah otomasi benar, (c) jawaban analitik akurat sesuai data, (d) secret tersimpan aman.

---

## 6. Modul 4 — Integrasi dengan Tools Existing & Third Party (2 minggu)

**Tujuan**: Menghubungkan aplikasi dengan ekosistem layanan nyata.

### 4.1 REST API & autentikasi
- Memanggil API pihak ketiga: request, headers, API key, OAuth
- Membaca dokumentasi API dengan bantuan AI (feed docs ke AI)
- **Praktikum**: integrasi weather API / currency converter

### 4.2 Webhook & event-driven
- Konsep webhook, endpoint penerima, signature verification
- **Praktikum**: webhook untuk notifikasi pembayaran / deploy

### 4.3 Database & storage
- Integrasi database eksternal (PostgreSQL/MySQL), ORM
- Upload & akses file storage (local/cloud)

### 4.4 Services populer
- Payment gateway, email/SMS service, cloud functions
- Pola integrasi yang umum: auth, logging, error mapping

### 4.5 Robustness
- Retry & backoff, timeout, idempotency
- Observability: log terstruktur, monitoring sederhana

**Proyek Modul 4**: Aplikasi Modul 1/2 diintegrasikan dengan 2+ layanan pihak ketiga (misal: notifikasi via bot, pembayaran, penyimpanan cloud), dengan error handling yang baik.

**Kriteria penilaian**: (a) integrasi berfungsi end-to-end, (b) kegagalan API tidak menjatuhkan aplikasi, (c) secret tidak bocor, (d) ada log & dokumentasi integrasi.

---

## 7. Capstone & Penutup (1 minggu)

### Capstone project
Peserta memilih salah satu:
- **A**: Bangun aplikasi baru dengan 3+ fitur yang diintegrasikan ke minimal 1 third-party service
- **B**: Ambil aplikasi open-source di GitHub, tambahkan fitur meaningful + buka PR
- **C**: Bangun chatbot multi-fungsi (otomasi + analitik) untuk kebutuhan nyata peserta

### Deliverable
- Repo GitHub rapi (README, struktur jelas, git history bermakna)
- Demo video 5 menit: masalah → solusi → cara kerja
- Refleksi tertulis: prompt paling sukses, kegagalan & cara mengatasinya

### Evaluasi akhir
| Aspek | Bobot |
|---|---|
| Fungsionalitas | 40% |
| Kualitas kode & dokumentasi | 20% |
| Kemampuan prompt & iterasi (terlihat dari git history & refleksi) | 20% |
| Presentasi | 20% |

---

## 8. Rubrik Umum (berlaku semua modul)

| Level | Deskripsi |
|---|---|
| **Dasar** | Bisa menghasilkan output AI yang berfungsi, tapi belum paham kenapa |
| **Mahir** | Paham kode yang dihasilkan, bisa debug & modifikasi manual |
| **Lanjut** | Bisa memilih kapan AI membantu vs menulis sendiri, dan mendesain prompt untuk masalah kompleks |

---

## 9. Backlog / Ide Pengembangan Kurikulum

- [ ] Materi video / screencast per lesson
- [ ] Template prompt library (cheat sheet) sebagai bonus
- [ ] Studi kasus: vibe coding untuk non-programmer (marketing, analis bisnis)
- [ ] Studi kasus: vibe coding tim (multi-agent, code review AI)
- [ ] Materi deployment: dari Termux ke VPS/cloud (Docker, serverless)
- [ ] Assessment autentik: mini-hackathon tiap akhir modul
- [ ] Daftar tool alternatif: Cursor, Windsurf, GitHub Copilot, Aider
- [ ] Lokakarya evaluasi kualitas kode AI (security review, code smells)
