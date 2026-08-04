# 3.3 — Otomasi

**Durasi**: 3 hari (±9 jam)
**Tujuan pembelajaran**:
- Menghubungkan chat service ke platform chat nyata (Telegram/WhatsApp)
- Menjadwalkan tugas berulang (scheduler/cron)
- Membuat bot yang menjalankan aksi nyata dari perintah user

---

## Menghubungkan ke platform chat

Bot harus bisa: menerima pesan dari user, memproses, membalas. Dua pendekatan:

| Pendekatan | Cara kerja | Kapan dipakai |
|---|---|---|
| **Polling** (sederhana) | Kode bertanya ke API: "ada pesan baru?" → proses → balas | Development, bot pribadi, Termux |
| **Webhook** (production) | Platform kirim pesan ke server-mu otomatis | Skala besar, butuh URL publik |

Mulai dengan **polling** — tidak butuh server publik. (Webhook akan dibahas detail di Modul 4.)

## Telegram: langkah praktis

1. **Buat bot**: chat ke `@BotFather` di Telegram → `/newbot` → dapat **token bot** (rahasia!)
2. **Simpan token** di `.env` (bukan di kode!)
3. **Polling loop** (contoh konsep):

```python
import requests, os
from llm import tanya_llm
from sessions import tambah_pesan, get_history

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"
offset = 0

while True:
    updates = requests.get(f"{URL}/getUpdates", params={"offset": offset, "timeout": 30}).json()
    for upd in updates.get("result", []):
        offset = upd["update_id"] + 1
        chat_id = upd["message"]["chat"]["id"]
        teks = upd["message"].get("text")
        if teks:
            tambah_pesan(chat_id, "user", teks)
            jawaban = tanya_llm(get_history(chat_id))
            tambah_pesan(chat_id, "assistant", jawaban)
            requests.post(f"{URL}/sendMessage", json={"chat_id": chat_id, "text": jawaban})
```

Minta AI mengimplementasikan ini untuk platform-mu dengan konteks dari 3.2. **Jangan** copy-paste kode dari tutorial online tanpa paham alurnya — baca setiap baris.

## Scheduler: tugas terjadwal

Bot perlu bertindak **tanpa diminta**: reminder harian, laporan pagi, cek status server.

### Pendekatan: loop + pengecekan waktu

```python
import schedule, time

def laporan_harian():
    # ambil data, kirim ke chat tertentu
    ...

schedule.every().day.at("08:00").do(laporan_harian)
# atau:
schedule.every(30).minutes.do(cek_status_server)

while True:
    schedule.run_pending()
    time.sleep(1)
```

### Aturan scheduler
- Satu thread/job yang gagal **jangan** mematikan seluruh bot → bungkus dengan try/except
- Log setiap eksekusi terjadwal (berhasil/gagal + error)
- Untuk Termux: bot harus tetap jalan di background — pakai `termux-wake-lock` atau jalankan di `tmux`/`nohup`

## Bot yang menjalankan aksi nyata

Gabungkan tool calling (3.2) dengan platform chat. Contoh perintah yang harus didukung:

```
/status         → cek uptime & resource (jalankan script)
/reminder 08:00 "minum air" → jadwalkan reminder
/lapor          → jalankan laporan_harian sekarang juga
```

Perintah admin (hapus data, restart, kirim ke semua user) harus punya **guard**:
```python
ADMIN_IDS = [123456789]   # chat_id admin, dari .env

if pesan.startswith("/hapus_semua") and chat_id not in ADMIN_IDS:
    balas("Akses ditolak")
```

## Troubleshooting umum

| Gejala | Penyebab umum |
|---|---|
| Bot tidak menjawab | Token salah / bot belum di-start (`/start` di chat bot) |
| Bot crash saat dipakai banyak orang | Session/global state tidak aman → cek struktur data |
| Bot mati saat HP terkunci (Termux) | Aktifkan `termux-wake-lock` / jalankan di `tmux` |
| Error 409/conflict | Dua proses polling berjalan bersamaan → hentikan yang lama |
| Pesan terlewat | `offset` handling salah → selalu update offset SEBELUM proses |

## Latihan

1. Buat bot Telegram minimal: echo (balas pesan sama) → pastikan polling jalan
2. Sambungkan ke chat service 3.2 → bot menjawab dengan LLM + system prompt kamu
3. Tambahkan 2 perintah nyata: `/status` (informasi sistem) dan `/ingat [teks]` (simpan ke database)
4. Scheduler: kirim pesan otomatis tiap 10 menit sebagai tes (lalu ubah jadi laporan harian)
5. Guard: buat 1 perintah admin + buktikan user non-admin ditolak

**Output lesson ini**: bot Telegram polling yang menjawab via LLM + 2 perintah nyata + 1 tugas terjadwal.
