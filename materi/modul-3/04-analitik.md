# 3.4 — Analitik

**Durasi**: 3 hari (±9 jam)
**Tujuan pembelajaran**:
- Membangun chatbot yang menjawab pertanyaan dari data (database)
- RAG sederhana: dokumen → chunking → retrieval
- Memastikan jawaban akurat (anti-halusinasi data)

---

## Pola inti: LLM + database

Bot analitik = **LLM yang pandai bicara + kode yang memegang data**. Aturan emas: *LLM tidak pernah menyentuh data mentah langsung — dia hanya merangkum hasil query yang dibuat kode.*

### Alur yang benar
```
user: "penjualan tertinggi minggu ini?"
→ LLM: (pilih tool query_penjualan dengan periode tepat)
→ kode: SELECT ... FROM transaksi WHERE ...   (parameterized!)
→ hasil: [{tanggal, total}]
→ LLM: "Penjualan tertinggi minggu ini: Sabtu, Rp 850.000"
```

### Alur yang SALAH
```
user: "penjualan tertinggi minggu ini?"
→ LLM: "Penjualan tertinggi minggu ini adalah Rp 5.000.000"  ❌
      (LLM MENGARANG karena tidak punya akses data)
```

## Kapan LLM membuat query vs kode yang membuat query?

| Strategi | Cara | Risiko |
|---|---|---|
| **Kode menulis query** (aman, direkomendasikan) | Tool punya query tetap; LLM hanya pilih & isi parameter | Rendah — query terkontrol |
| **LLM menulis SQL bebas** | LLM generate SQL dari natural language | **Tinggi** — SQL salah, SQL injection, query mahal |

Untuk kurikulum ini: **pakai strategi pertama**. Buat 3-5 query siap pakai, LLM memilih:
```
Tools yang tersedia:
- total_penjualan(periode)          → SELECT SUM(total) ...
- penjualan_per_hari(periode)       → SELECT tanggal, SUM(total) GROUP BY tanggal
- produk_terlaris(limit)            → SELECT produk, SUM(qty) ORDER BY ... LIMIT ?
- cek_stok(produk)                  → SELECT stok FROM produk WHERE nama = ?
```

## Contoh implementasi tool analitik

```python
def penjualan_per_hari(periode):
    """Return ringkasan penjualan per hari untuk periode tertentu."""
    # periode: 'hari_ini' | 'kemarin' | '7_hari' | '30_hari'
    mapping = {
        "hari_ini": "date('now')",
        "kemarin": "date('now','-1 day')",
        "7_hari": "date('now','-7 day')",
        "30_hari": "date('now','-30 day')",
    }
    if periode not in mapping:
        return {"error": f"Periode tidak dikenal: {periode}. Pilih: {list(mapping)}"}

    cur = db.execute(f"""SELECT tanggal, SUM(total) AS total
                        FROM transaksi WHERE tanggal >= {mapping[periode]}
                        GROUP BY tanggal ORDER BY tanggal""")
    baris = cur.fetchall()
    return [{"tanggal": r[0], "total": r[1]} for r in baris]
```

Perhatikan: periode di-*whitelist* (bukan string user langsung) → tidak ada injection.

## RAG sederhana (retrieval-augmented generation)

RAG = biarkan bot menjawab berdasarkan **dokumenmu** (manual, kebijakan, FAQ) tanpa melatih ulang model. Empat langkah:

### 1. Chunking — potong dokumen
Dokumen panjang tidak muat di konteks → potong jadi potongan kecil:
```python
def chunk(teks, ukuran=500):
    # potong per paragraf/kalimat, simpan dengan id & sumber
    ...
```

### 2. Embedding — ubah jadi vektor
Setiap chunk diubah jadi angka (vektor) oleh model embedding:
```python
vektor = embedding_model.encode(chunk_teks)
```

### 3. Retrieval — cari yang relevan
Saat user bertanya, ubah pertanyaan jadi vektor → cari chunk dengan jarak terdekat (cosine similarity):
```python
q_vec = embedding_model.encode(pertanyaan)
terdekat = sorted(chunks, key=lambda c: cosine(c.vec, q_vec), reverse=True)[:3]
```

### 4. Generation — jawab dengan konteks
Kirim chunk terpilih sebagai konteks:
```
[SYSTEM] Jawab pertanyaan HANYA berdasarkan konteks berikut. Jika konteks
tidak menjawab, katakan "informasi tidak ditemukan di dokumen".
[KONTEKS]
<chunk 1>
<chunk 2>

[PERTANYAAN USER]
Apa kebijakan refund?
```

> 📌 RAG penuh (vector database, chunking pintar) adalah topik lanjutan — untuk kurikulum ini, RAG sederhana di atas sudah cukup untuk bot yang menjawab dari dokumen. Kalau data tinggal 1-2 dokumen kecil, alternatif paling sederhana: masukkan langsung ke system prompt.

## Memastikan akurasi (anti-halusinasi)

1. **System prompt wajib**: *"Jangan pernah mengarang data. Jika tidak ada di hasil query/konteks, katakan tidak tahu."*
2. **Perlihatkan sumber**: minta bot menyebutkan angka yang diambil dari query, bukan kata-kata sendiri
3. **Verifikasi silang**: bandingkan 3 jawaban bot dengan query manual langsung di database
4. **Log pertanyaan & jawaban** — audit kalau ada jawaban aneh

## Latihan

1. Siapkan data: buat tabel transaksi dengan 20+ baris data contoh (minta AI generate script seeding)
2. Implementasi 3 tool analitik (total, per-hari, produk terlaris) dengan whitelist periode
3. Tes: tanya bot 5 pertanyaan berbeda → verifikasi tiap jawaban dengan query manual
4. Tanyakan pertanyaan yang datanya TIDAK ada → pastikan bot menjawab "tidak tahu", bukan mengarang
5. (Bonus) RAG sederhana: buat dokumen FAQ 2 halaman → bot menjawab dari dokumen

**Output lesson ini**: bot yang menjawab pertanyaan data dengan akurat & tidak mengarang.
