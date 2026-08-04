# 0.4 — Etika & Keamanan

**Durasi**: 1 hari (±3 jam)
**Tujuan pembelajaran**:
- Mengetahui risiko nyata kode hasil AI (dengan data, bukan fiksi)
- Melindungi secret: API key, token, password
- Menerapkan rutinitas review & verifikasi kode AI

---

## Data nyata: kenapa ini penting

Jangan percaya "AI pintar, pasti aman". Ini temuan nyata:

| Temuan | Sumber |
|---|---|
| Kode hasil AI punya **1.7x lebih banyak masalah "major"** dibanding kode manusia; security vulnerabilities **2.74x lebih tinggi**; misconfiguration 75% lebih sering | CodeRabbit (analisis 470 PR open-source, Des 2025) |
| Selama 3 tahun, LLM makin baik menghasilkan kode **fungsional**, tapi keamanan kode **tidak ikut membaik** | Veracode (Okt 2025) |
| AI agent Replit **menghapus database produksi** walau diperintahkan tidak mengubah apa pun | Insiden nyata, Jul 2025 |
| Developer yang tidak paham kode AI → bug & vulnerability lolos ke produksi | Ars Technica / diskusi industri |
| 170 dari 1.645 aplikasi buatan platform vibe coding (Lovable) punya celah yang membocorkan data pribadi | Semafor, Mei 2025 |

**Kesimpulan**: AI itu asisten yang produktif tapi **tidak bertanggung jawab**. Kamu yang bertanggung jawab atas kode yang kamu deploy. Kode AI = draft yang harus direview, bukan barang jadi.

## Bahaya #1: Secret bocor

Secret = API key, token, password, kredensial database. Masalah paling umum & paling merusak:

### Aturan mutlak
1. **Jangan pernah** menaruh secret di kode: `api_key = "sk-1234..."` di file `.py`/`.js` ❌
2. **Jangan pernah** mengirim secret ke AI: *"ini API key saya: ..., kenapa tidak jalan?"* ❌ (AI kadang menyertakannya ke file kode)
3. **Selalu** pakai environment variable / file `.env` yang diabaikan git:
   ```bash
   # .env  (jangan pernah di-commit!)
   API_KEY=sk-rahasia-saya
   ```
   ```python
   # di kode:
   import os
   key = os.getenv("API_KEY")   # ✅ baca dari environment, bukan hardcode
   ```
4. **`.gitignore` wajib**: buat file `.gitignore` berisi `.env`, `*.db`, folder `node_modules/` — minta AI membuatkannya sesuai project: *"Buatkan .gitignore untuk project Python"*
5. Kalau secret **terlanjur ter-commit**: anggap bocor → revoke/regenerate di penyedia layanan, jangan cuma hapus dari git

### Latihan cepat
Periksa project-mu: `grep -rn "sk-\|api_key\|password\|token" . --include="*.py" --include="*.js" --include="*.env*"` — kalau ada yang muncul, pindahkan ke `.env` sekarang.

## Bahaya #2: Kode yang "kelihatan benar"

AI sangat pandai menghasilkan kode yang terlihat profesional tapi salah logic-nya. Pola umum:
- Validasi yang dilewati (input kosong, angka negatif, string kosong)
- Error ditelan diam-diam (`except: pass`) — aplikasi tidak crash tapi data salah
- Library/API yang tidak ada (halusinasi) — baru ketahuan saat dijalankan
- Query SQL tanpa sanitasi (celah injection)

### Rutinitas review 3 langkah
```
1. JALANKAN: apa yang terjadi saat dijalankan? (error? output salah?)
2. UJI EDGE CASE: input kosong, nilai ekstrem, data lama — apa yang terjadi?
3. TANYA KE AI: "Review kode ini untuk masalah keamanan: injection,
   secret, validasi input. Sebutkan baris & perbaikan."
```
Untuk langkah 3, minta AI mereview dengan kacamata keamanan (lihat contoh subagent security-reviewer di referensi Anthropic).

## Bahaya #3: Terlalu percaya output AI

- AI bisa "mengaku berhasil" padahal gagal — **selalu verifikasi sendiri**: jalankan, lihat output, baca diff
- AI bisa menyarankan cara yang salah karena salah paham konteks — tanya balik: *"Kenapa pendekatan ini? Apa alternatifnya?"*
- AI bisa memproduksi **kode berlisensi bermasalah** (menyalin pola dari training data) — untuk project komersial, gunakan model dengan kebijakan lisensi jelas & review manual

## Etika penggunaan

1. **Jujur soal penggunaan AI**: di project tim/akademik, umumkan bahwa kode dibantu AI
2. **Jangan claim sebagai karya murni sendiri** tanpa pengakuan
3. **Jangan** pakai AI untuk menipu (spam, deepfake, malware) — batasan ini jelas melanggar kebijakan semua penyedia
4. **Privasi**: jangan kirim data pelanggan/rahasia perusahaan ke AI publik tanpa izin
5. **Tanggung jawab**: kode yang di-deploy = tanggung jawabmu, bukan AI-nya

## Ceklist keamanan (tempel di setiap project)

- [ ] Tidak ada secret di kode / di git history
- [ ] `.gitignore` ada & berisi `.env`, file database, dependency
- [ ] Error handling: tidak ada `except: pass` tanpa penjelasan
- [ ] Input user divalidasi (tipe, panjang, batas)
- [ ] Query database pakai parameterized query (bukan string concatenation)
- [ ] AI diminta review keamanan sebelum "selesai"
- [ ] Backup database sebelum mengubah skema

**Output lesson ini**: kebiasaan review & proteksi secret + ceklist yang bisa dipakai di semua project.
