# Referensi & Riset — Vibe Coding

> Sumber bahan kurikulum. Diperbarui saat riset dilakukan.

## Definisi & Sejarah

- **Istilah diciptakan**: Andrej Karpathy (co-founder OpenAI, mantan AI lead Tesla), Februari 2025 — tweet: *"fully give in to the vibes, embrace exponentials, and forget that the code even exists"* → https://x.com/karpathy/status/1886192184808149383
- **Word of the Year 2025** (Collins English Dictionary), Nov 2025
- Definisi Merriam-Webster: *"practice of writing code, making web pages, or creating apps, by just telling an AI program what you want"*
- Latar belakang: klaim Karpathy 2023 — *"the hottest new programming language is English"*
- **Perspektif Simon Willison**: *"Jika LLM menulis semua baris kode tapi kamu me-review, men-test, dan memahaminya — itu bukan vibe coding, itu pakai LLM sebagai typing assistant"* (kunci: review & pemahaman)

## Adopsi di Industri

- 25% startup Y Combinator Winter 2025: codebase 95% AI-generated (TechCrunch, Mar 2025)
- WSJ (Jul 2025): vibe coding diadopsi developer profesional untuk kasus komersial
- Linus Torvalds vibe-code visualizer AudioNoise dengan Google Antigravity (Jan 2026)

## Kritik & Risiko (materi untuk Modul 0.4 — Etika & Keamanan)

| Risiko | Bukti/Data |
|---|---|
| **Kualitas & keamanan kode** | CodeRabbit (Des 2025): kode AI co-authored punya ~1.7x lebih banyak masalah "major", misconfiguration 75% lebih sering, security vulnerabilities 2.74x lebih tinggi |
| **Keamanan tidak membaik** | Veracode (Okt 2025): selama 3 tahun LLM makin baik menghasilkan kode fungsional, tapi keamanan tidak ikut membaik |
| **Teknikal debt** | GitClear (2025, 211 juta baris kode): refactoring turun 25%→10%, duplikasi kode naik 4x, code churn hampir 2x lipat |
| **Produktivitas** | METR (Jul 2025, RCT 16 developer): tools AI 2025 justru menambah 19% waktu di repositori mature |
| **Insiden nyata** | Replit agent menghapus database produksi (Jul 2025); kasus rsync 3.4.3 & kontroversi AI commit (2026); peringatan "vibe slop crisis" (WSJ, Zechner & Ronacher — engineer di balik pi/OpenClaw) |
| **Open source** | Paper "Vibe Coding Kills Open Source" (Jan 2026); GitHub "Eternal September": lonjakan kontribusi AI berkualitas rendah membebani maintainer |

## Best Practices (sumber: Anthropic Claude Code Engineering)

Sumber: https://code.claude.com/docs/en/best-practices

### Prinsip inti
1. **Context window = resource paling penting** — kualitas menurun saat context penuh. Kelola dengan agresif (`/clear` antar tugas).
2. **Beri AI cara memverifikasi** — tests, build, screenshot. Jangan percaya "kelihatan benar" (trust-then-verify gap).
3. **Explore → plan → code → commit** — pisahkan riset dari implementasi untuk tugas besar; untuk fix kecil langsung eksekusi.

### Menulis prompt yang baik
| Strategi | Kurang baik | Lebih baik |
|---|---|---|
| Scope task | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| Tunjuk sumber | "why does ExecutionFactory have such a weird api?" | "look through ExecutionFactory's git history and summarize how its api came to be" |
| Referensi pola existing | "add a calendar widget" | "look at how existing widgets are implemented... HotDogWidget.php is a good example. follow the pattern..." |
| Deskripsikan gejala | "fix the login bug" | "users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it" |

### Menulis file instruksi (CLAUDE.md / AGENTS.md)
- ✅ Include: bash commands yang tidak bisa ditebak AI, aturan code style yang berbeda dari default, instruksi testing, gotchas
- ❌ Exclude: yang bisa ditebak AI dari membaca kode, dokumentasi API panjang, hal yang sering berubah
- **Aturan emas**: "Apakah menghapus baris ini akan membuat AI melakukan kesalahan?" Jika tidak, potong.
- File kepanjangan → AI mengabaikan setengahnya

### Pola kegagalan yang harus dihindari
1. **Kitchen sink session** — campur banyak tugas tak terkait → fix: `/clear`
2. **Correcting over and over** — koreksi >2x pada masalah sama → fix: `/clear` + prompt lebih baik
3. **Over-specified memory file** — terlalu panjang → fix: pruning
4. **Trust-then-verify gap** — kode terlihat benar tapi edge case bocor → fix: selalu verifikasi

### Workflow lanjutan
- **Interview dulu**: minta AI mewawancarai kita sebelum fitur besar (AskUserQuestion) → spec lengkap → sesi baru untuk implementasi
- **Writer/Reviewer pattern**: sesi A menulis, sesi B fresh context mereview (bebas bias)
- **Course-correct early**: koreksi segera saat melenceng, jangan biarkan
- **Failing test dulu**: tulis test yang mereproduksi bug, baru minta fix
- **CLI tools & MCP**: `gh`, `aws`, MCP server untuk integrasi tools eksternal

## Sumber Lain yang Bisa Dieksplorasi
- IBM: "What is Vibe Coding?" → https://www.ibm.com/think/topics/vibe-coding
- Ars Technica (Mar 2025): "Will the future of software development run on vibes?" → https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/
- NYT Kevin Roose (Feb 2025): "Not a Coder? With A.I., Just Having an Idea Can Be Enough."
- METR study (Jul 2025): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Wikipedia: https://en.wikipedia.org/wiki/Vibe_coding
