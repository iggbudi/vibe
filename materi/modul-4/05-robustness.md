# 4.5 — Robustness

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Menerapkan retry & backoff, timeout, dan idempotency
- Membangun observability: log terstruktur, health check
- Menilai ketahanan aplikasi dengan chaos test

---

## Masalah yang dipecahkan robustness

Pihak ketiga **pasti** kadang gagal: server down, timeout, rate limit, data berubah format. Aplikasi yang robust = aplikasi yang tetap berdiri & memberi pesan jelas saat itu terjadi.

## 1. Retry dengan exponential backoff

Jangan retry langsung (server masih down) dan jangan retry tanpa batas (bikin server makin down).

```python
import time

def panggil_dengan_retry(fungsi, maks_coba=4):
    for i in range(maks_coba):
        try:
            return fungsi()
        except requests.exceptions.ConnectionError:
            if i == maks_coba - 1:
                raise
            tunggu = 2 ** i          # 1s, 2s, 4s, 8s
            jitter = random.uniform(0, tunggu)   # + jitter: hindari thundering herd
            log.warning("Gagal (percobaan %d), retry dalam %ss", i+1, tunggu)
            time.sleep(tunggu + jitter)
    raise RuntimeError("Gagal setelah retry")
```

**Aturan retry**:
- Retry hanya untuk error **transien**: 429, 502, 503, 504, timeout, connection error
- **Jangan retry** 400 (request-mu yang salah — retry tidak akan membantu) dan 401 (key salah)
- Tambah jitter acak supaya banyak klien tidak menyerang server bersamaan
- Kalau ada header `Retry-After`, ikuti itu

## 2. Timeout di semua lapisan

Timeout = "saya tunggu maksimal X detik". Tanpa ini, kegagalan jaringan = aplikasi hang selamanya.

```python
requests.get(url, timeout=10)                    # timeout total
# atau terpisah:
requests.get(url, timeout=(3.05, 10))            # (connect, read)
```
- **Connect timeout**: kecil (3-5s) — koneksi macet cepat ketahuan
- **Read timeout**: lebih besar (10-30s) — server butuh waktu proses
- Juga set timeout untuk: database connection, panggilan LLM, upload file

## 3. Idempotency (sudah mulai di 4.2)

Idempotent = operasi yang bisa dijalankan berulang dengan hasil sama. Contoh: mengirim email "order dikonfirmasi" 2x itu **tidak** idempotent (user dapat 2 email).

```
Idempotent:     UPDATE status SET = 'PAID' WHERE order_id = X
Tidak:          INSERT notifikasi (order_id) — dobel
```

Pola umum: `idempotency_key` di request / cek keberadaan sebelum insert. Selalu tanyakan pada dirimu: *"kalau event ini tiba dua kali, apa yang terjadi?"*

## 4. Circuit breaker (untuk layanan yang sering gagal)

Retry melindungi satu panggilan; circuit breaker melindungi keseluruhan:

```
Normal ──> gagal 5x dalam 1 menit ──> TERBUKA (skip panggil, langsung error cepat)
              │
              └── setelah cooldown 30s ──> HALF-OPEN (coba 1x)
                     ├── sukses → NORMAL
                     └── gagal → TERBUKA lagi
```

```python
class CircuitBreaker:
    def __init__(self, batas=5, cooldown=30):
        self.batas, self.cooldown = batas, cooldown
        self.gagal = 0
        self.terbuka_sampai = 0

    def boleh_panggil(self):
        if time.time() < self.terbuka_sampai:
            return False
        return True

    def sukses(self):
        self.gagal = 0

    def gagal(self):
        self.gagal += 1
        if self.gagal >= self.batas:
            self.terbuka_sampai = time.time() + self.cooldown
```
Manfaat: layanan yang down tidak menahan request user berulang-ulang (hemat waktu & uang).

## 5. Observability: log & health check

Kamu tidak bisa memperbaiki yang tidak kamu lihat.

### Log terstruktur
```
{"time": "...", "level": "ERROR", "event": "payment.webhook.invalid_signature",
 "service": "payment", "order_id": "A123", "detail": "signature mismatch"}
```
Struktur JSON → mudah dicari & dianalisis. Log event (apa yang terjadi) + konteks (order_id) — bukan cuma pesan teks.

### Health check endpoint
```
GET /health → 200 {"status": "ok", "db": "up", "payment_api": "degraded"}
```
Satu endpoint yang melaporkan status semua dependency. Berguna untuk monitoring & debugging cepat.

## Uji ketahanan (chaos test)

1. **Matikan internet** → aplikasi harus memberi error ramah, tidak hang
2. **Matikan API pihak ketiga** (ubah URL jadi salah) → retry bekerja, aplikasi tetap hidup
3. **Kirim payload aneh** (string bukan JSON, field hilang) → ditolak dengan pesan jelas
4. **Kirim webhook ganda** → idempotency bekerja
5. **Rate limit**: kirim banyak request → circuit breaker / rate limit melindungi

Untuk tiap tes: catat apa yang terjadi, perbaiki yang tidak robust, ulangi.

## Latihan akhir (proyek modul)

Integrasikan aplikasi Modul 1/2 dengan **2+ layanan pihak ketiga** (misal: payment sandbox + notifikasi Telegram bot) dengan:
1. Semua panggilan eksternal: timeout + error handling + retry yang tepat
2. Webhook dengan verifikasi signature + idempotency
3. Tidak ada secret di repo
4. Health check endpoint + log terstruktur
5. Chaos test: buktikan kegagalan pihak ketiga tidak menjatuhkan aplikasi

## Checklist Proyek Akhir Modul 4

- [ ] 2+ integrasi berfungsi end-to-end (sandbox)
- [ ] Timeout di semua panggilan eksternal
- [ ] Retry/backoff untuk error transien; tidak retry 400/401
- [ ] Webhook: signature diverifikasi, event ganda tidak diproses 2x
- [ ] Secret 100% di env vars (audit git history!)
- [ ] Log terstruktur + health check
- [ ] Dokumentasi integrasi di README (alur, cara tes, error yang mungkin)
- [ ] Chaos test dilalui: matikan API → aplikasi tetap hidup dengan pesan jelas
