# 3.2 — Membangun Chat Service

**Durasi**: 3 hari (±9 jam)
**Tujuan pembelajaran**:
- Mengelola state percakapan (session & history) dengan benar
- Menambahkan tool calling / function calling untuk aksi nyata
- Mengubah chatbot pasif menjadi chatbot yang bisa BERTINDAK

---

## Dari fungsi tunggal ke chat service

Di 3.1 kamu punya `tanya_llm(messages)` — sekali panggil, sekali jawab. Chatbot sungguhan butuh:
1. **Session**: siapa yang bicara? (banyak user, jangan campur history)
2. **History**: menyimpan percakapan agar konteks berlanjut
3. **Actions**: bot bisa menjalankan perintah nyata (bukan cuma menjawab)

## 1. Session management

Setiap user punya history sendiri. Struktur sederhana:

```python
sessions = {}   # chat_id -> list of messages

def get_history(chat_id):
    if chat_id not in sessions:
        sessions[chat_id] = [{"role": "system", "content": SYSTEM_PROMPT}]
    return sessions[chat_id]

def tambah_pesan(chat_id, role, content):
    get_history(chat_id).append({"role": role, "content": content})
    # Batasi panjang history (hemat biaya & konteks):
    if len(sessions[chat_id]) > 30:
        sessions[chat_id] = [sessions[chat_id][0]] + sessions[chat_id][-20:]
```

**Aturan penting**:
- History tak terbatas = mahal + konteks penuh → **potong history lama**
- System prompt selalu di posisi pertama
- Session bisa disimpan di memory (hilang saat restart) atau database (persisten) — untuk produksi: database

## 2. Tool calling (function calling)

Tanpa tool calling, bot hanya bisa *berbicara*: "total penjualan adalah Rp X" — padahal dia tidak punya data! Bot yang berguna harus bisa **menjalankan fungsi** (query database, jalankan script, cek status).

### Cara kerja
1. Kamu definisikan fungsi + deskripsinya (dikirim ke API)
2. LLM memutuskan: jawab langsung ATAU panggil fungsi tertentu dengan argumen
3. Kode kamu menjalankan fungsi itu (dengan aman!)
4. Hasil fungsi dikirim kembali ke LLM → LLM merangkum untuk user

### Contoh definisi tool

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_penjualan",
            "description": "Query total penjualan dari database. "
                           "Parameter: tanggal (YYYY-MM-DD) atau 'kemarin'/'minggu_ini'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "periode": {"type": "string"}
                },
                "required": ["periode"],
            },
        },
    }
]
```

### Implementasi fungsi (dengan keamanan!)

```python
def query_penjualan(periode):
    # SELALU parameterized query — jangan pernah string concatenation:
    cur = db.execute(
        "SELECT SUM(total) FROM transaksi WHERE tanggal = ?",
        (periode,),
    )
    return f"Total penjualan {periode}: Rp {cur.fetchone()[0]:,}"
```

### Loop tool calling

```
user: "berapa penjualan kemarin?"
→ API: (minta panggil query_penjualan, periode="kemarin")
→ kamu: jalankan fungsi → hasil: "Rp 2.300.000"
→ API (dengan hasil): "Total penjualan kemarin adalah Rp 2.300.000."
```

## Keamanan tool calling — WAJIB

⚠️ LLM bisa memanggil fungsi dengan argumen tak terduga. **Validasi di sisi kode:**
- **Jangan pernah** mengekspos fungsi yang mengeksekusi shell bebas (`os.system`) tanpa filter ketat
- Validasi argumen: *"kalau argumen bukan tanggal valid, tolak"*
- Whitelist perintah, jangan blacklist
- Log semua pemanggilan tool (siapa, kapan, argumen apa)

```
Jangan buat tool ini:  run_command(command): os.system(command)  ❌
```
LLM akan menggunakannya dengan cara yang tidak kamu duga. Batasi ke fungsi spesifik yang kamu tulis sendiri.

## Struktur chat service lengkap

```
chat_service/
├── main.py          # loop penerima pesan → proses → balas
├── llm.py           # panggilan API (dari 3.1)
├── sessions.py      # management history
├── tools.py         # fungsi-fungsi yang bisa dipanggil LLM
├── database.py      # penyimpanan (session, data bisnis)
├── .env             # API keys (jangan di-commit!)
└── requirements.txt
```

## Latihan

1. Buat struktur folder di atas (minta AI generate kerangka dengan konteks 3.1)
2. Implementasi session management dengan batas history
3. Tambahkan 2 tool sederhana: `cek_waktu()` dan `simpan_catatan(teks)` (simpan ke file/database)
4. Tes alur: tanya bot hal yang membutuhkan `cek_waktu` → verifikasi bot memanggil tool dengan benar
5. Keamanan: tambahkan validasi argumen di tool-mu; tulis 1 contoh argumen "jahat" dan buktikan ditolak

**Output lesson ini**: chat service dengan session + 2 tool yang berfungsi — fondasi bot operasional.
