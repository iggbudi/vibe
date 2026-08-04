# 2.5 — Fitur Besar & Refactoring Aman

**Durasi**: 4 hari (±12 jam)
**Tujuan pembelajaran**:
- Memecah fitur besar menjadi milestone kecil
- Refactoring dengan safety net: test sebelum & sesudah
- Strategi branch & rollback yang benar

---

## Kenapa fitur besar berbahaya?

Fitur besar menyentuh banyak file, mengubah alur, dan memberi AI "ruang" untuk membuat keputusan yang tidak kamu sadari. Best practices Anthropic: **explore → plan → code → commit** — pisahkan riset dan perencanaan dari implementasi.

## Workflow fitur besar (4 fase)

### Fase 1: Explore (jangan ubah apa pun)
```
[Baca dulu] Aku mau menambah fitur "export laporan bulanan ke PDF".
Jangan ubah apa pun. Jelaskan:
1. File mana yang terlibat (routes, model, template)
2. Alur data yang ada sekarang untuk laporan
3. Risiko apa saja yang kamu lihat
4. Usulan pendekatan: library apa, atau tanpa library
```

### Fase 2: Plan
```
Berdasarkan eksplorasi tadi, buat rencana implementasi:
1. Urutan langkah (milestone) — tiap langkah bisa diverifikasi & di-commit terpisah
2. File yang akan diubah/dibuat di tiap milestone
3. Apa yang TIDAK akan kamu sentuh
4. Cara verifikasi tiap milestone
```
**Review rencana ini bersama AI** sebelum lanjut. Ini "kontrak" implementasi. Simpan sebagai `PLAN.md`.

### Fase 3: Implementasi per milestone
Kerjakan SATU milestone per sesi, urut dari yang paling berisiko rendah:
```
[Milestone 1/3] Kerjakan bagian X dari PLAN.md:
[tempel bagian rencana]
Ikuti PLAN.md — jangan menambah di luar rencana. Verifikasi sesuai cara yang
tertulis di plan, laporkan hasilnya.
```
Satu milestone selesai → commit → lanjut milestone berikutnya.

### Fase 4: Review menyeluruh
Setelah semua milestone:
```
Review seluruh diff fitur ini terhadap PLAN.md:
1. Semua requirement terpenuhi?
2. Ada perubahan di luar scope?
3. Edge case yang belum ditangani?
Laporkan gaps, bukan preferensi gaya.
```

## Refactoring dengan safety net

Refactoring = mengubah struktur tanpa mengubah perilaku. Aturan emas: **perilaku sama, kode lebih baik**. Kalau perilaku berubah, itu bukan refactoring — itu perubahan fitur (dan perlu approval).

```
Sebelum refactor: pastikan ada test yang mencakup perilaku saat ini
(pytest / test suite / atau tulis dulu test smoke manual).

Refactor: gabungkan logika duplikat di [file A] dan [file B] menjadi satu
fungsi di [file C]. JANGAN ubah perilaku apa pun — hanya pindahkan/menyatukan.

Setelah: jalankan semua test. Semua harus lolos tanpa mengubah test apa pun.
```
**Indikator sukses refactoring**: test suite lolos **tanpa ada test yang diubah**.

## Branch & rollback

| Situasi | Perintah |
|---|---|
| Mulai fitur besar (isolasi) | `git checkout -b fitur-export-pdf` |
| Kembali ke kondisi aman | `git checkout main` |
| Batalkan milestone yang jelek | `git revert <commit-id>` |
| Buang branch yang gagal total | `git branch -D fitur-export-pdf` |
| Lihat perubahan sejak main | `git diff main...HEAD` |

Kenapa branch: kalau fitur gagal total, `main` tetap bersih dan jalan. Jangan pernah mengerjakan fitur besar langsung di `main`.

## Kapan fitur "cukup"?

- Semua milestone selesai & terverifikasi
- Tidak ada perubahan di luar scope
- Fitur lama masih berfungsi (regression pass)
- Kamu bisa menjelaskan keputusan desain utama

Kalau sudah: merge branch → `git checkout main && git merge fitur-export-pdf` → hapus branch.

## Latihan (proyek akhir modul)

Kerjakan 1 fitur besar di aplikasi 2.1 dengan workflow 4 fase:
1. **Explore** → minta AI analisis tanpa mengubah (documented)
2. **Plan** → tulis PLAN.md, diskusikan dengan AI
3. **Implement** → 2-3 milestone, commit per milestone, di branch terpisah
4. **Review** → review diff terhadap plan
5. **Refactor bonus**: minta AI cari duplikasi kode → refactor dengan safety net → semua test lolos tanpa mengubah test
6. **Merge** ke main setelah semua beres

## Checklist Proyek Akhir Modul 2

- [ ] 2 fitur kecil (2.4) + 1 bugfix (2.3) + 1 fitur besar (2.5) selesai
- [ ] Fitur lama tidak rusak (regression verified)
- [ ] Git log: commit per fitur/milestone dengan pesan jelas
- [ ] Kamu bisa menjelaskan arsitektur app (PETA.md) & alasan tiap keputusan
- [ ] Punya pengalaman rollback: pernah revert/branch dan berhasil kembali ke kondisi aman
