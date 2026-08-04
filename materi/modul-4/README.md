# Modul 4 — Integrasi dengan Tools Existing & Third Party

**Durasi**: 2 minggu
**Tujuan modul**: Menghubungkan aplikasi dengan ekosistem layanan nyata — API pihak ketiga, webhook, database eksternal, dan services populer — dengan error handling yang benar.

## Daftar Lesson
| # | Lesson | Fokus |
|---|---|---|
| 4.1 | [REST API & autentikasi](01-rest-api.md) | Request, headers, API key, baca dokumentasi |
| 4.2 | [Webhook & event-driven](02-webhook.md) | Endpoint penerima, signature verification |
| 4.3 | [Database & storage](03-database-storage.md) | DB eksternal, ORM, file storage |
| 4.4 | [Services populer](04-services-populer.md) | Payment, email, cloud — pola umum |
| 4.5 | [Robustness](05-robustness.md) | Retry, timeout, idempotency, observability |

## Proyek Akhir Modul
Aplikasi dari Modul 1/2 diintegrasikan dengan **2+ layanan pihak ketiga**, misalnya:
- Notifikasi via bot Telegram (Modul 3) saat terjadi sesuatu
- Payment gateway untuk pembayaran
- Penyimpanan file di cloud / database eksternal
- Email/SMS otomatis

Kriteria:
- (a) Integrasi berfungsi end-to-end
- (b) Kegagalan API pihak ketiga **tidak menjatuhkan aplikasi**
- (c) Secret tidak bocor (env vars)
- (d) Ada log & dokumentasi integrasi

## Prasyarat
- Modul 0-3 selesai (terutama: keamanan secret, debugging, error handling)
- Paham konsep HTTP dasar (request/response) — bisa dibantu AI
- Punya minimal 1 akun layanan pihak ketiga gratis (Telegram bot sudah punya dari Modul 3)

## Mindset modul ini
Integrasi adalah tempat paling banyak "hal tak terduga": server pihak lain down, rate limit, format data berubah, timeout. Skill utama bukan *menghubungkan* — itu mudah — tapi **menangani kegagalan dengan anggun**. Modul 4 melatih itu.
