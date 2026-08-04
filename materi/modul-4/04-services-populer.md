# 4.4 — Services Populer

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Mengenal pola integrasi layanan populer: payment, email/SMS, messaging
- Memahami alur pembayaran (client → backend → gateway → webhook)
- Mengenali pola umum yang berulang di semua integrasi

---

## Peta layanan populer

| Kategori | Contoh | Event penting |
|---|---|---|
| **Payment** | Midtrans, Xendit, Stripe, PayPal | `payment.success`, `payment.failed` |
| **Email** | SendGrid, Resend, Brevo | Pengiriman / bounce |
| **SMS/WA** | Twilio, Fonnte, WhatsApp Business API | Terkirim / gagal |
| **Messaging** | Telegram Bot API (sudah di Modul 3) | Pesan masuk |
| **Cloud** | Cloudflare, AWS, Vercel | Deploy, DNS, fungsi serverless |

Kabar baik: **pola integrasinya sama** untuk semua. Kuasai satu → sisanya tinggal baca dokumentasi.

## Studi kasus: alur payment (paling penting)

```
1. USER klik "Bayar" di aplikasi
2. BACKEND buat transaksi di payment gateway
   → dapat payment_token / URL pembayaran
3. USER diarahkan ke halaman gateway → bayar
4. GATEWAY kirim webhook ke server-mu: payment.success (dengan signature!)
5. BACKEND verifikasi signature → update status transaksi → kirim notifikasi
6. USER dapat konfirmasi (email/WA/bot)
```

### Langkah 2 — buat transaksi
```python
def buat_pembayaran(order_id, jumlah):
    resp = requests.post(
        f"{PAYMENT_URL}/v1/charges",
        json={
            "order_id": order_id,
            "amount": jumlah,
            "payment_type": "bank_transfer",
        },
        headers={"Authorization": f"Basic {BASE64_AUTH}"},  # atau API key
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()   # berisi payment_url untuk user
```

### Langkah 5 — terima webhook (kombinasi 4.2 + 4.3)
```python
@app.route("/webhook/payment", methods=["POST"])
def webhook():
    if not verifikasi_signature(request):      # 4.2
        return jsonify({"error": "invalid"}), 401
    data = request.get_json()
    if not idempotent(data["transaction_id"]): # 4.2
        return jsonify({"ok": True}), 200
    if data["status"] == "success":
        update_status_order(data["order_id"], "PAID")   # 4.3
        kirim_notifikasi_user(order_id)                  # 4.4: email/WA
    return jsonify({"ok": True}), 200
```

### Aturan payment yang tidak boleh dilanggar
1. **Jangan pernah percaya harga dari client** — harga harus dihitung ulang di backend (user bisa mengubah payload!)
2. **Jangan pernah** set status "lunas" tanpa verifikasi webhook/signature
3. Simpan `transaction_id` dari gateway untuk audit & refund
4. Gunakan **sandbox/test mode** dulu — jangan langsung uang asli!

## Pola umum semua integrasi (template yang sama)

```
1. SETUP    : akun layanan → dapat API key/secret → simpan di .env
2. DOKUMENTASI: minta AI baca docs → catat endpoint & format
3. IMPLEMENTASI: fungsi pemanggil (timeout + error handling — 4.1)
4. EVENT    : daftarkan webhook/URL callback + verifikasi signature (4.2)
5. PROSES   : update data + efek samping (4.3)
6. NOTIFIKASI: kabari user (email/WA/bot)
7. FAILOVER : error → retry/backoff, log, pesan ramah (4.5)
```

## Sandbox vs produksi

| Layanan | Sandbox | Produksi |
|---|---|---|
| Payment | Test mode, uang virtual | Uang asli, butuh approval |
| Email | Bisa kirim ke email sendiri | Domain terverifikasi, rate lebih tinggi |
| SMS/WA | Nomor terdaftar saja | Nomor bebas (berbayar) |

**Aturan**: semua latihan pakai sandbox. Pindah ke produksi hanya setelah flow terbukti di sandbox + kamu paham konsekuensinya.

## Latihan

Pilih **1 layanan** (rekomendasi: payment sandbox — paling kaya pelajaran):
1. Buat akun sandbox, dapat API key, simpan di `.env`
2. Implementasi alur 6 langkah di atas (bisa sebagian: buat transaksi → simulasi bayar → webhook → update status)
3. Tes skenario: pembayaran sukses, gagal, signature salah (harus ditolak)
4. Pastikan tidak ada secret bocor & ada log tiap langkah
5. Dokumentasikan integrasi di README: endpoint yang dipakai, alur, cara tes

**Output lesson ini**: 1 integrasi payment sandbox end-to-end + pola yang bisa dipakai ulang untuk layanan lain.
