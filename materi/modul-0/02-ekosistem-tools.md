# 0.2 — Ekosistem Tools

**Durasi**: 1 hari (±2 jam)
**Tujuan pembelajaran**:
- Membedakan AI assistant, AI agent, dan IDE berbasis AI
- Memahami konsep dasar LLM: konteks, token, halusinasi
- Memilih tool yang sesuai kebutuhan & budget

---

## Peta tools

```
┌─────────────────────────────────────────────────┐
│ 1. AI ASSISTANT (chatbot)                       │
│    ChatGPT, Claude, Gemini, Grok, DeepSeek      │
│    Kamu: tempel kode/error → AI jawab → salin   │
│    Terbaik untuk: tanya konsep, review kode     │
├─────────────────────────────────────────────────┤
│ 2. AI AGENT (coding agent)                      │
│    pi, Claude Code, Codex, Cursor Agent, Aider  │
│    AI: baca file, ubah kode, jalankan perintah  │
│    Terbaik untuk: kerja nyata di project        │
├─────────────────────────────────────────────────┤
│ 3. AI IDE (editor + AI)                         │
│    Cursor, Windsurf, VS Code + Copilot          │
│    Autocomplete + chat + agent dalam 1 editor   │
│    Terbaik untuk: yang suka GUI & visual        │
├─────────────────────────────────────────────────┤
│ 4. NO-CODE / APP BUILDER                        │
│    Replit, Lovable, Bolt, v0, Antigravity       │
│    Deskripsi → website/aplikasi langsung        │
│    Terbaik untuk: non-programmer, landing page  │
└─────────────────────────────────────────────────┘
```

**Rekomendasi kurikulum ini**: pakai **AI agent** (level 2) sebagai tool utama — karena kamu tetap belajar melihat file, menjalankan perintah, dan membaca hasil. Agent = asisten yang bekerja, bukan sekadar menjawab.

## Konsep dasar LLM yang wajib dipahami

### Konteks (context window)
AI hanya "melihat" sejumlah teks tertentu dalam satu sesi (ribuan–jutaan token). Semua yang kamu kirim + semua yang AI baca + semua jawaban memenuhi konteks ini. **Semakin penuh konteks, semakin buruk performanya** — AI mulai "lupa" instruksi awal. Karena itu: sesi pendek & fokus lebih baik dari sesi panjang campur aduk.

### Token
Unit teks yang diproses AI (1 token ≈ 3/4 kata dalam bahasa Inggris, lebih mahal untuk beberapa bahasa lain). Token = biaya & kapasitas. File besar = banyak token = konteks cepat penuh.

### Halusinasi
AI bisa menghasilkan hal yang terdengar masuk akal tapi salah — termasuk **kode yang tidak ada, API yang tidak pernah ada, atau file yang tidak ada**. AI tidak "tahu" — ia memprediksi kata berikutnya. Verifikasi selalu diperlukan.

### Suhu & model
- Model dasar (base) vs reasoning (berpikir lebih lama, lebih baik untuk logika/debug)
- Parameter "temperature": tinggi = lebih kreatif/acak, rendah = lebih konsisten. Untuk kode, umumnya rendah lebih baik.

## Model & API

- **Model populer**: Claude (Anthropic), GPT (OpenAI), Gemini (Google), DeepSeek, Qwen
- **Cara akses**: web app (berbayar/subscription), API (bayar per token, untuk membangun aplikasi yang memanggil AI sendiri — dipakai di Modul 3), atau via agent yang mengelola sendiri
- **API**: nanti di Modul 3 kamu akan memanggil API LLM langsung untuk membangun chatbot

## Memilih tool (tabel keputusan)

| Kondisi kamu | Rekomendasi |
|---|---|
| Punya HP Android, mau murah & praktis | Termux + pi (seperti setup lesson 0.3) |
| Punya laptop, suka editor visual | Cursor / VS Code + Copilot |
| Non-programmer murni, mau cepat tampil | Replit / Lovable / v0 |
| Ingin belajar paling dalam | Agent CLI (pi / Claude Code) — dipaksa paham terminal & file |

## Latihan

1. Tulis perbedaan assistant vs agent vs IDE dalam 3 kalimat
2. Buka 2 tool berbeda (misal ChatGPT web + agent coding) untuk tugas yang sama: *"Tulis fungsi Python untuk menghitung rata-rata dari list angka"* → bandingkan pengalamannya
3. Cari tahu: berapa context window model yang kamu pakai? Berapa harga/langganannya?
4. Identifikasi tool utama yang akan kamu pakai sepanjang kurikulum ini — catat alasannya

**Output lesson ini**: keputusan tool utama + pemahaman konsep konteks/token/halusinasi.
