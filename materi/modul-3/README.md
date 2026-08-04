# Modul 3 — Chatbot untuk Otomasi & Analitik

**Durasi**: 3 minggu
**Tujuan modul**: Membangun chatbot yang **benar-benar bekerja** (bukan demo): menjalankan otomasi nyata, menjawab pertanyaan dari data, dan mengirim laporan analitik — diakses lewat platform chat yang dipakai sehari-hari.

## Daftar Lesson
| # | Lesson | Fokus |
|---|---|---|
| 3.1 | [Konsep chatbot & LLM API](01-konsep-chatbot.md) | System prompt, API, request/response |
| 3.2 | [Membangun chat service](02-chat-service.md) | Session, history, tool calling |
| 3.3 | [Otomasi](03-otomasi.md) | Integrasi platform chat, scheduler |
| 3.4 | [Analitik](04-analitik.md) | Query database, RAG sederhana |
| 3.5 | [Production-readiness](05-production.md) | Logging, error handling, secret |

## Proyek Akhir Modul
**Bot Telegram "asisten operasional"** yang:
- (a) Menjalankan otomasi terjadwal (reminder, cek status, jalankan script)
- (b) Menjawab pertanyaan dari database (contoh: data penjualan)
- (c) Mengirim laporan analitik harian
- (d) Berjalan stabil (tidak crash pada input aneh)
- (e) Secret tersimpan aman (env vars, bukan hardcode)

## Prasyarat
- Modul 0-2 selesai (terutama: prompt, debugging, git, keamanan secret)
- Paham dasar Python (bisa dibantu AI, tapi harus paham alur kodenya)
- Punya akun Telegram (untuk bot platform) — atau WhatsApp/alternatif lain
- Akses ke API LLM (OpenAI/Anthropic/Gemini) atau LLM lokal

## Mindset modul ini
Chatbot adalah **aplikasi sungguhan**: ada server, database, autentikasi, kegagalan jaringan, input tak terduga. Modul 3 menggabungkan semua keterampilan sebelumnya — prompt (0.5), kode (1), integrasi (2) — plus dua hal baru: **memanggil API LLM dari kode** dan **menghubungkan ke platform eksternal**.
