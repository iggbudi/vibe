# 2.1 — Membaca Codebase

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Menemukan entry point dan memahami arsitektur aplikasi
- Teknik eksplorasi: tree, grep, baca config, jalankan test
- Membangun "peta mental" yang bisa dikomunikasikan ke AI

---

## Mulai dari mana?

Codebase orang lain terasa membingungkan karena kamu belum punya konteks. Jangan dibaca urut dari file pertama. Gunakan urutan berikut:

### 1. Baca dokumen dulu (30 detik)
```
ls
cat README.md        # apa aplikasi ini?
cat package.json / requirements.txt / pyproject.toml   # dependency apa saja?
```
Kalau tidak ada README, itu sinyal pertama: dokumentasi minim → hati-hati, AI juga akan kesulitan.

### 2. Lihat struktur folder (30 detik)
```
find . -type f -not -path './.git/*' | head -50
# atau
tree -L 2
```
Perhatikan pola: `src/`, `tests/`, `models/`, `routes/`, `config/`. Nama folder memberi petunjuk arsitektur.

### 3. Cari entry point
Entry point = file yang pertama dijalankan. Cara mencarinya:
```
# Package manifest memberi tahu perintah start:
grep -i "start\|main\|scripts" package.json
# Atau cari file dengan blok main/if __name__:
grep -rn "__main__\|app.run\|listen(" --include="*.py" --include="*.js" | head
```

### 4. Baca 1 file inti dari atas ke bawah
Pilih 1 file yang jelas penting (entry point atau model utama). Baca penuh. Ini membangun intuisi gaya kode: penamaan, struktur fungsi, pola yang dipakai.

### 5. Telusuri alur utama (satu use case)
Ambil satu use case sederhana (misal "user login"), lalu ikuti jejaknya: route → controller → service → database. Catat file yang dilalui. Ini "peta mental"mu.

## Teknik eksplorasi cepat

| Kebutuhan | Perintah |
|---|---|
| File apa saja yang menyentuh kata X | `grep -rn "X" --include="*.py" -l` |
| Fungsi X didefinisikan di mana | `grep -rn "def X\|function X" .` |
| Siapa yang memanggil fungsi X | `grep -rn "X(" .` |
| Seberapa besar file | `wc -l $(find . -name "*.py")` (urutan terbesar) |
| Test di mana & bagaimana | `ls tests/ && grep -n "def test" tests/*.py` |
| Perubahan terbaru | `git log --oneline -10` |

## Biarkan AI ikut membaca

Kamu tidak perlu membaca semua file — AI bisa meringkas. Tapi kamu harus **memverifikasi ringkasannya**:

```
[Di project ini] Jelaskan arsitektur aplikasi ini:
1. Entry point dan alur startup
2. Layer/folder apa saja dan fungsinya
3. Bagaimana data mengalir (request → response / input → output)
4. 3 file yang paling penting untuk dipahami, dan kenapa
5. Sebutkan file path yang spesifik
```

Setelah AI menjawab, **cek 1-2 klaimnya langsung** (buka file yang disebut). AI kadang salah menebak dari nama file saja.

## Peta mental minimum

Sebelum mulai mengubah apa pun, kamu harus bisa menjawab:
1. ✅ Di mana entry point-nya?
2. ✅ Di mana data disimpan (database/file/luar)?
3. ✅ File mana yang mengatur logika inti?
4. ✅ Di mana saya menambah fitur baru nanti?
5. ✅ Bagaimana cara menjalankan & men-test aplikasi ini?

## Latihan

Ambil aplikasi yang **bukan buatanmu** (rekomendasi: project open-source kecil di GitHub, atau app Modul 1 milik teman):
1. Lakukan langkah 1-5 di atas, catat peta mental di file `PETA.md`
2. Minta AI menjelaskan arsitektur → verifikasi 2 klaimnya dengan membaca file
3. Tes pemahaman: tanpa melihat kode, jelaskan alur "tambah data baru" dari input sampai tersimpan
4. Perbaiki `PETA.md` berdasarkan yang kamu temukan

**Output lesson ini**: file `PETA.md` + kemampuan menjawab 5 pertanyaan peta mental di atas.
