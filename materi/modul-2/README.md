# Modul 2 — Menambah Fitur di Aplikasi yang Sudah Jalan

**Durasi**: 3 minggu
**Tujuan modul**: Bekerja di codebase yang *bukan* buatan sendiri tanpa merusaknya. Ini keterampilan paling bernilai di dunia nyata — sebagian besar pekerjaan developer adalah mengubah sistem yang sudah ada.

## Daftar Lesson
| # | Lesson | Fokus |
|---|---|---|
| 2.1 | [Membaca codebase](01-membaca-codebase.md) | Navigasi, entry point, peta mental |
| 2.2 | [Memberi konteks ke AI](02-konteks-ke-ai.md) | Prompt untuk codebase besar |
| 2.3 | [Bugfix](03-bugfix.md) | Reproduksi, isolasi, regression |
| 2.4 | [Menambah fitur kecil](04-fitur-kecil.md) | CRUD baru, validasi, trade-off |
| 2.5 | [Fitur besar & refactoring aman](05-refactoring-aman.md) | Migration, safety net, rollback |

## Proyek Akhir Modul
Pada aplikasi yang **diberikan** (bukan buatan sendiri — bisa app open-source kecil atau app Modul 1 milik teman):
- (a) Tambah **2 fitur baru**
- (b) Perbaiki **1 bug** yang ada
- (c) Fitur lama tidak rusak (regression test / verifikasi manual)
- (d) Perubahan terdokumentasi di git log
- (e) Kamu bisa menjelaskan ulang konteks prompt yang kamu pakai

## Prasyarat
- Modul 1 selesai (bisa baca kode sendiri, git lancar)
- Paham struktur prompt: konteks → instruksi → constraints → acceptance criteria

## Mindset modul ini
> **"Vibe coding your way to a production codebase is clearly risky. Most of the work we do involves evolving existing systems, where the quality and understandability of the underlying code is crucial."** — Simon Willison

Modul 2 melatih kebalikan dari asal-generate: **membaca sebelum mengubah**. AI tetap yang menulis, tapi kamu yang tahu *di mana, mengapa, dan apa risikonya*.
