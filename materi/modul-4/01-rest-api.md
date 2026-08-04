# 4.1 — REST API & Autentikasi

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Memahami struktur REST API: endpoint, method, status code, headers
- Memanggil API dengan autentikasi (API key, Bearer token, OAuth)
- Membaca dokumentasi API dengan bantuan AI

---

## Anatomi panggilan API

```
GET https://api.weather.com/v1/weather?city=Jakarta&units=metric
│        └── base URL ──┘ └── path └── query params ─┘
└── method
```

| Method | Arti | Contoh |
|---|---|---|
| `GET` | Ambil data | Daftar cuaca kota |
| `POST` | Buat data baru | Kirim pesan |
| `PUT`/`PATCH` | Ubah data | Update profil |
| `DELETE` | Hapus | Hapus resource |

### Status code yang wajib dikenal

| Kode | Arti | Artinya untukmu |
|---|---|---|
| 200 | OK | Sukses |
| 201 | Created | Sukses buat data |
| 400 | Bad Request | Kamu kirim data salah |
| 401 | Unauthorized | API key salah / tidak ada |
| 403 | Forbidden | Key benar tapi tidak punya izin |
| 404 | Not Found | Endpoint/URL salah |
| 429 | Too Many Requests | **Rate limit** — tunggu / backoff |
| 5xx | Server Error | Server pihak ketiga bermasalah |

## Cara memanggil dari Python

```python
import requests

def get_weather(kota):
    resp = requests.get(
        "https://api.weather.com/v1/weather",
        params={"city": kota, "units": "metric"},
        headers={"X-Api-Key": os.getenv("WEATHER_API_KEY")},
        timeout=10,                      # JANGAN lupa timeout!
    )
    resp.raise_for_status()              # lempar exception jika 4xx/5xx
    return resp.json()                   # parse JSON
```

**Aturan wajib**: selalu set `timeout` — tanpa itu, request bisa menggantung selamanya dan aplikasi-mu terasa "mati".

## Tiga gaya autentikasi

| Gaya | Bentuk | Contoh |
|---|---|---|
| **API key** | Header khusus | `X-Api-Key: abc123` atau `?api_key=abc` |
| **Bearer token** | Header Authorization | `Authorization: Bearer eyJhbGci...` |
| **OAuth 2.0** | Flow: dapat token → pakai token → refresh | Google, GitHub, Stripe |

### OAuth sederhana (client credentials)
```python
# 1. Tukar client_id + client_secret dengan access token
resp = requests.post(
    "https://api.example.com/oauth/token",
    json={
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "client_credentials",
    },
)
token = resp.json()["access_token"]

# 2. Pakai token untuk panggil API
requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {token}"},
    timeout=10,
)
```
Token bisa **kedaluwarsa** (expires_in) — simpan waktu kedaluwarsa & refresh otomatis.

## Membaca dokumentasi API dengan AI

Dokumentasi API panjang dan membosankan — biarkan AI membacanya:

```
Aku mau pakai API [nama] untuk [tujuan].
1. Baca dokumentasi di [URL]
2. Jelaskan: endpoint yang relevan untuk [tujuan], format request & response,
   autentikasi yang dibutuhkan, dan batasan (rate limit, kuota)
3. Tulis contoh kode Python dengan requests yang siap dipakai
4. Sebutkan error code yang mungkin terjadi & cara menanganinya
```

**Verifikasi**: cek klaim AI ke dokumentasi asli (AI kadang mengarang endpoint). Cara tercepat: tes 1 endpoint dengan curl dulu.

## Menangani error API

```python
try:
    data = get_weather("Jakarta")
except requests.exceptions.Timeout:
    log.warning("Weather API timeout")
    return "Layanan sedang sibuk, coba lagi nanti."
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 401:
        log.error("API key salah!")
        return "Konfigurasi salah, hubungi admin."
    if e.response.status_code == 429:
        return "Terlalu banyak permintaan, tunggu sebentar."
    log.error("Weather API error: %s", e)
    return "Gagal mengambil cuaca."
except requests.exceptions.ConnectionError:
    log.error("Jaringan bermasalah")
    return "Koneksi gagal."
```

## Latihan

1. Pilih 1 API gratis (rekomendasi: Open-Meteo cuaca tanpa key, atau REST Countries)
2. Tes dengan curl → panggil dari Python dengan fungsi + timeout
3. Baca dokumentasi resminya (bisa dibantu AI) → catat: endpoint, params, response
4. Buat 3 skenario error & tangani: timeout (nonaktifkan internet), 404 (URL salah), 401 (key salah — kalau API-nya pakai key)
5. Catat pengalaman di README project-mu

**Output lesson ini**: fungsi pemanggil API yang benar (timeout, error handling) + kebiasaan baca dokumentasi.
