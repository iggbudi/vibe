# 4.2 — Webhook & Event-Driven

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Memahami konsep webhook dan kapan memakainya (vs polling)
- Membangun endpoint penerima webhook
- Memverifikasi signature webhook (keamanan wajib!)

---

## Webhook vs polling

| | Polling (kamu tanya) | Webhook (mereka kabari) |
|---|---|---|
| Arah | Kamu tarik data berkala | Mereka dorong data saat ada event |
| Contoh | Cek status order tiap 5 menit | Dapat notifikasi langsung saat order berubah |
| Biaya | Mahal (request terus-menerus) | Murah (hanya saat event) |
| Kompleksitas | Sederhana | Perlu endpoint publik + verifikasi |

Webhook cocok untuk: pembayaran, notifikasi, CI/CD, integrasi chat.

## Alur webhook

```
1. Kamu daftarkan URL ke layanan: "kirim event ke https://serverku.com/webhook/payment"
2. Layanan kirim POST ke URL itu saat event terjadi (payload JSON)
3. Server-mu menerima, memverifikasi, memproses, balas 200
4. Kalau kamu tidak balas 200 → layanan akan retry (delay bertingkat)
```

## Endpoint penerima (contoh Flask)

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook/payment", methods=["POST"])
def payment_webhook():
    # 1. Verifikasi signature DULU (lihat di bawah)
    # 2. Baru proses payload
    data = request.get_json()
    log.info("Payment event: %s", data.get("event"))
    proses_payment(data)
    return jsonify({"ok": True}), 200    # PENTING: balas 200!
```

**Aturan emas webhook**: balas `200 OK` secepat mungkin setelah data diterima & diverifikasi. Jangan proses berat di dalam handler (kirim ke antrian/thread) — layanan menunggu balasanmu dan akan retry kalau lambat.

## Verifikasi signature (WAJIB!)

⚠️ Tanpa verifikasi, **siapa pun** yang tahu URL-mu bisa mengirim webhook palsu — termasuk "payment sukses" palsu. Semua layanan serius menyediakan signature.

### Konsep
1. Layanan menghitung hash dari payload + secret (HMAC)
2. Kirim hash di header (misal `X-Signature: sha256=...`)
3. Kamu hitung ulang dengan secret yang sama → bandingkan

```python
import hmac, hashlib, os

SECRET = os.getenv("WEBHOOK_SECRET")   # rahasia, dari dashboard layanan

def verifikasi(request):
    signature = request.headers.get("X-Signature", "")
    payload = request.get_data()        # RAW body, bukan JSON hasil parse!
    expected = "sha256=" + hmac.new(
        SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)   # aman dari timing attack

@app.route("/webhook/payment", methods=["POST"])
def payment_webhook():
    if not verifikasi(request):
        log.warning("Webhook signature tidak valid!")
        return jsonify({"error": "invalid signature"}), 401
    ...
```

**Gotcha penting**: hitung HMAC dari **raw body** (byte yang diterima), bukan dari JSON yang sudah diparse — kalau format body berubah (spasi, urutan key), hash tidak cocok.

## Idempotency (webhook retry!)

Webhook dikirim ulang oleh layanan saat gagal/timeout → **event yang sama bisa tiba 2 kali**. Kalau kamu memproses 2x, user bisa ditagih 2x!

```python
def proses_payment(data):
    event_id = data["id"]                       # ID unik dari layanan
    if event_id in events_yang_sudah_diproses:  # cek dulu (di database!)
        log.info("Event %s sudah diproses, dilewati", event_id)
        return
    # ... proses ...
    simpan_event_id(event_id)                   # tandai selesai
```

Simpan event_id di database — memory tidak cukup (restart = hilang).

## Menjalankan endpoint di Termux/HP

Problem: layanan butuh URL **publik**, sedangkan kamu di HP/Termux. Solusi:
1. **Tunnel**: `cloudflared tunnel` / `ngrok` → dapat URL publik sementara yang meneruskan ke localhost
2. **VPS/server**: deploy Flask ke server (bisa juga dipelajari sebagai lanjutan)
3. Untuk praktik awal: gunakan layanan yang mendukung tes webhook tanpa URL publik (beberapa punya console yang menampilkan request)

> Catatan: tunnel adalah jembatan sementara. Untuk produksi, gunakan server permanen. Modul ini fokus pada logika webhook — tunnel cukup untuk praktik.

## Latihan

1. Buat endpoint webhook sederhana (echo: terima POST, log, balas 200)
2. Tes dengan curl: `curl -X POST http://localhost:5000/webhook/test -d '{"halo":"dunia"}'`
3. Implementasi verifikasi HMAC → tes: kirim tanpa signature (harus ditolak 401), kirim dengan signature benar (diterima)
4. Implementasi idempotency → kirim event sama 2x → proses hanya 1x
5. (Jika memungkinkan) pasang tunnel → daftarkan URL ke layanan webhook asli → terima event nyata

**Output lesson ini**: endpoint webhook dengan verifikasi signature + idempotency — pola yang sama untuk semua layanan webhook.
