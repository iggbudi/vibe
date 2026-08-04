# 3.1 — Konsep Chatbot & LLM API

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Memahami system prompt, user prompt, dan conversation context
- Memanggil API LLM dari kode: struktur request/response
- Mengelola parameter: token, temperature

---

## Anatomi percakapan dengan LLM

Setiap panggilan ke LLM adalah **list of messages**. Tiga peran:

| Peran | Arti | Contoh |
|---|---|---|
| `system` | Instruksi permanen — kepribadian & aturan bot | "Kamu asisten penjualan. Jawab singkat, bahasa Indonesia, jangan mengarang data." |
| `user` | Pesan dari user/pengguna | "Berapa total penjualan kemarin?" |
| `assistant` | Jawaban AI sebelumnya (untuk konteks percakapan) | "Total penjualan kemarin adalah Rp 2.300.000." |

**System prompt = otak bot.** Ini yang membedakan chatbot yang berguna vs chatbot generik. Ubah system prompt → ubah perilaku bot.

## Contoh system prompt yang baik

```
Kamu adalah asisten operasional "SiBudi" untuk toko online.

ATURAN:
- Jawab dalam bahasa Indonesia, singkat dan to the point
- Jika ditanya data yang tidak kamu tahu, katakan jujur "saya tidak tahu" —
  JANGAN mengarang angka
- Jika user minta aksi berbahaya (hapus data, transfer uang), minta konfirmasi
  eksplisit dulu
- Format angka: Rp 1.250.000
```

Perhatikan: aturan tentang **tidak mengarang data** adalah yang paling penting — inilah yang mencegah halusinasi merusak analitik.

## Memanggil API LLM dari kode

### Struktur dasar (contoh dengan Python + requests, tanpa SDK)

```python
import requests
import os

API_KEY = os.getenv("LLM_API_KEY")        # jangan hardcode!
API_URL = "https://api.example.com/v1/chat/completions"

def tanya_llm(messages):
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "model-name",
            "messages": messages,          # list: system + user + assistant
            "temperature": 0.3,
        },
    )
    resp.raise_for_status()                # error jika gagal
    return resp.json()["choices"][0]["message"]["content"]

# Pemakaian:
messages = [
    {"role": "system", "content": "Kamu asisten yang menjawab singkat."},
    {"role": "user", "content": "Sebutkan 3 tips belajar coding."},
]
print(tanya_llm(messages))
```

### Parameter penting

| Parameter | Fungsi | Rekomendasi untuk bot |
|---|---|---|
| `model` | Model yang dipakai | Sesuai API yang kamu punya |
| `messages` | Riwayat percakapan | Kirim hanya yang relevan (jangan seluruh history tanpa batas) |
| `temperature` | 0 = konsisten, 1+ = kreatif | **0.2-0.4** untuk bot data/analitik; lebih tinggi untuk teks kreatif |
| `max_tokens` | Batas panjang jawaban | Sesuai kebutuhan; hemat untuk menghemat biaya |
| `stream` | Jawaban bertahap vs sekaligus | `false` untuk awal (sederhana) |

## Biaya & batasan

- API LLM **bayar per token** (input + output). Semakin panjang history, semakin mahal.
- Banyak penyedia punya **rate limit** (maks panggilan per menit) — kalau bot crash dengan error 429, itu rate limit.
- Mulai dari model kecil/murah untuk development, model besar untuk produksi.
- Alternatif gratis: LLM lokal (Ollama di laptop/server) — lebih lambat tapi tanpa biaya.

## Verifikasi tanpa UI: tes dengan curl

Sebelum menulis kode penuh, tes API dengan curl (kamu bisa minta AI membuatkan perintahnya):
```bash
curl https://api.example.com/v1/chat/completions \
  -H "Authorization: Bearer $LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"model-name","messages":[{"role":"user","content":"Halo"}]}'
```
Kalau curl berhasil → API jalan → baru tulis kode Python.

## Latihan

1. Buat file `bot_test.py` dengan fungsi `tanya_llm` di atas (ganti URL/model sesuai API-mu)
2. Uji dengan 3 percakapan berbeda: pertanyaan sederhana, pertanyaan yang memancing mengarang (contoh: "sebutkan data penjualan bulan lalu" — padahal bot tidak punya datanya) → amati apakah bot mengarang
3. Eksperimen temperature: tanya hal yang sama dengan temperature 0 vs 1.2 → bandingkan variasi jawaban
4. Tulis system prompt versimu sendiri untuk "asisten operasional" (akan dipakai di 3.2)

**Output lesson ini**: fungsi `tanya_llm` yang jalan + system prompt pribadi + pengalaman langsung dengan parameter API.
