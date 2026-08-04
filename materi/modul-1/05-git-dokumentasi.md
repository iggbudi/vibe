# 1.5 — Version Control & Dokumentasi

**Durasi**: 1 hari (±3 jam)
**Tujuan pembelajaran**:
- Git dasar: init, add, commit, branch, revert
- Menulis README yang baik (dengan bantuan AI)
- Memahami kenapa git penting untuk vibe coding

---

## Kenapa git wajib untuk vibe coder?

1. **Rollback**: AI mengubah sesuatu dan merusak aplikasi → `git checkout` kembali ke versi yang jalan. Ini **jaring pengaman** utama vibe coding.
2. **Diff review**: `git diff` menunjukkan persis apa yang AI ubah — cara mengecek "trust-then-verify".
3. **History sebagai dokumentasi**: commit per fitur = catatan perkembangan.
4. **Kolaborasi AI**: Modul 2 akan bekerja di codebase existing — AI perlu membaca history.

## Perintah git dasar

```bash
git init                    # mulai repo di folder project
git add .                   # stage semua perubahan
git commit -m "Fitur: tambah catatan"   # simpan snapshot
git log --oneline           # lihat history commit
git diff                    # lihat perubahan yang belum di-commit
git checkout -- app.py      # batalkan perubahan app.py (rollback!)
git revert <commit-id>      # buat commit baru yang membatalkan commit lama
```

## Workflow commit yang disarankan

```
1. Fitur selesai & sudah dites manual
2. git add . && git commit -m "Fitur: tambah catatan"
3. (opsional) git diff sebelum commit untuk review
```

**Satu commit = satu fitur**. Bukan "update 1", "update 2" — pesan commit harus menjelaskan **apa** yang berubah.

## Biarkan AI membantu git

AI bisa melakukan git untukmu. Prompt yang berguna:

```
Aku baru selesai implementasi fitur edit. 
1. Jalankan git diff dan review perubahan yang sudah dibuat
2. Buatkan pesan commit yang deskriptif
3. Commit dengan pesan itu
```

Tapi kamu **wajib** bisa menjalankan sendiri — jangan pernah tergantung 100% pada AI untuk hal yang melindungi pekerjaanmu.

## Menulis README dengan AI

README yang baik menjawab 3 pertanyaan:
1. **Apa ini?** — satu kalimat + screenshot/demo (opsional)
2. **Cara install?** — perintah lengkap dari nol
3. **Cara pakai?** — fitur utama + contoh

Template:
```markdown
# Nama Aplikasi

Deskripsi satu kalimat: aplikasi catatan pribadi sederhana berbasis terminal.

## Cara Install
```bash
git clone <url-repo>
cd <folder>
pip install -r requirements.txt
```

## Cara Pakai
```bash
python app.py
```
Fitur: tambah, lihat, edit, hapus, cari catatan.

## Struktur Project
- `app.py` — menu utama
- `database.py` — penyimpanan SQLite
```

Prompt ke AI: *"Baca kode project ini lalu tuliskan README.md menggunakan template yang aku berikan. Jelaskan cara install dan pakai berdasarkan kode yang sebenarnya."* — selalu minta AI **membaca kode dulu**, jangan mengarang.

## Latihan

1. `git init` di project catatanmu (kalau belum)
2. Buat commit per fitur yang sudah kamu kerjakan (jika belum, pisahkan sekarang)
3. Minta AI review `git diff` terakhir → perbaiki kalau ada yang aneh
4. Tulis README.md dengan bantuan AI (minta baca kode dulu)
5. Simulasikan bencana: minta AI mengubah sesuatu sampai rusak → `git checkout` → beres

**Output lesson ini**: project dengan history git rapi + README yang bisa dibaca orang lain.

---

## Checklist Proyek Akhir Modul 1

- [ ] Aplikasi todo + catatan berfungsi (tambah/lihat/edit/hapus)
- [ ] Data persisten setelah restart (SQLite/JSON)
- [ ] README lengkap (install + pakai)
- [ ] History git: commit per fitur, pesan jelas
- [ ] Kamu bisa menjelaskan setiap bagian kode ke orang lain
- [ ] Backlog fitur lanjutan tercatat di README
