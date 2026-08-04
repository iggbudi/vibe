# 3.5 — Production-Readiness

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Menerapkan logging, error handling, retry, dan rate limit
- Konfigurasi via environment variables
- Menilai apakah bot "layak dipakai 24 jam"

---

## Bot yang "jalan di laptop" vs "layak produksi"

| Aspek | Demo (laptop) | Produksi |
|---|---|---|
| Error | Crash → user tidak dapat apa-apa | Error tercatat, bot tetap hidup |
| Secret | Hardcode di kode | Environment variables |
| API LLM down | Bot mati | Retry + fallback |
| User spam | Bot kewalahan | Rate limit |
| Restart | History hilang | Session di database |
| Debug | Print di terminal | Log terstruktur dengan waktu & konteks |

Modul ini mengubah bot demomu menjadi tahan banting.

## 1. Logging

Ganti `print()` dengan logging terstruktur:

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    filename="bot.log",          # simpan ke file
)
log = logging.getLogger("bot")

log.info("Pesan diterima dari chat %s: %s", chat_id, teks[:50])
log.warning("LLM timeout untuk chat %s", chat_id)
log.error("Tool gagal: %s", e, exc_info=True)   # exc_info = traceback
```

**Aturan**: log *apa yang terjadi* (pesan, keputusan, error) — bukan data sensitif (jangan log isi password/token).

## 2. Error handling berlapis

```
LAYER 1 (per pesan):  satu pesan error JANGAN mematikan loop
while True:
    try:
        proses_pesan(upd)          # satu update gagal → lewati, lanjut
    except Exception as e:
        log.error("Gagal proses update: %s", e, exc_info=True)

LAYER 2 (per panggilan API): retry transien
for percobaan in range(3):          # retry 3x dengan backoff
    try:
        return tanya_llm(messages)
    except RateLimitError:
        time.sleep(2 ** percobaan)  # 2s, 4s, 8s — exponential backoff
    except TimeoutError:
        time.sleep(1)

LAYER 3 (paling dalam): tool
def tool_wrapper(func):
    def aman(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log.error(...)
            return {"error": f"Gagal: {e}"}   # dikembalikan ke LLM → LLM bilang ke user dengan sopan
    return aman
```

**Poin penting**: hasil error tool *dikirim kembali ke LLM* — bot bisa menjelaskan kegagalan ke user dengan bahasa manusia, bukan crash.

## 3. Rate limit (lindungi dirimu sendiri)

Bot melayani banyak user → biaya API LLM & rate limit penyedia. Sederhana:

```python
from collections import defaultdict
import time

batas = defaultdict(list)          # chat_id -> [timestamps]
MAKS_PER_MENIT = 10

def boleh_proses(chat_id):
    kini = time.time()
    batas[chat_id] = [t for t in batas[chat_id] if kini - t < 60]
    if len(batas[chat_id]) >= MAKS_PER_MENIT:
        return False
    batas[chat_id].append(kini)
    return True
```
Kalau melebihi batas → balas "Mohon tunggu sebentar 🙏" → jangan panggil LLM.

## 4. Konfigurasi via environment

Semua hal yang bisa berubah (token, ID admin, model, threshold) → `.env`:

```bash
# .env — JANGAN di-commit!
TELEGRAM_BOT_TOKEN=123:abc
ADMIN_IDS=111111,222222
LLM_MODEL=model-name
MAX_HISTORY=30
RATE_LIMIT=10
```

```python
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
```

**Aturan**: kode tidak boleh berisi nilai yang berbeda antar lingkungan (laptop vs server). Semua lewat env.

## 5. Session persisten (database)

Memory (`sessions = {}`) hilang saat restart → user kehilangan konteks. Pindah ke SQLite:

```python
CREATE TABLE sessions (
    chat_id INTEGER PRIMARY KEY,
    history TEXT,            -- JSON dari list messages
    updated_at TIMESTAMP
);
```
Simpan history saat selesai proses, muat saat user kirim pesan. Sederhana & persisten.

## Ceklist "layak produksi"

- [ ] Tidak ada secret di kode / git history
- [ ] Logging ke file (bukan cuma terminal)
- [ ] Error handling 3 lapis (per-update, retry API, tool aman)
- [ ] Rate limit aktif
- [ ] Session persisten di database
- [ ] Bot tetap hidup walau 1 pesan gagal (uji: kirim pesan aneh / API mati)
- [ ] Restart bot → history user tidak hilang
- [ ] `requirements.txt` lengkap (bisa dijalankan orang lain)

## Latihan akhir (proyek modul)

Gabungkan semuanya — **Bot Telegram "asisten operasional"**:

1. **Otomasi** (3.3): `/status`, 1 perintah admin dengan guard, 1 tugas terjadwal (laporan harian 08:00)
2. **Analitik** (3.4): 3 tool query data + anti-halusinasi ("tidak tahu" saat data tidak ada)
3. **Production** (3.5): logging, retry, rate limit, session di database, semua di `.env`
4. **Uji ketahanan**: kirim 30 pesan cepat → rate limit bekerja; matikan API LLM → bot tetap hidup & memberi pesan error sopan; restart → history tersimpan
5. Dokumentasikan di README: cara setup, cara menjalankan, daftar perintah

## Checklist Proyek Akhir Modul 3

- [ ] Bot menjawab pertanyaan dengan LLM (system prompt pribadi)
- [ ] Minimal 2 perintah nyata via tool calling (bukan cuma ngobrol)
- [ ] 1 otomasi terjadwal berjalan
- [ ] Analitik: jawaban akurat, tidak mengarang, terverifikasi
- [ ] Rate limit & error handling berfungsi
- [ ] Tidak ada secret di repo
- [ ] README lengkap (orang lain bisa menjalankan bot-mu)
