# 0.3 — Setup Lingkungan

**Durasi**: 1 hari (±3 jam)
**Tujuan pembelajaran**:
- Menginstall & mengkonfigurasi terminal, runtime, git, dan agent coding
- Mengetahui struktur folder project
- Verifikasi: lingkungan siap dipakai (ceklist di akhir)

---

## Yang perlu diinstall

| Komponen | Fungsi | Cara install (Termux Android) | Cara install (Desktop) |
|---|---|---|---|
| **Terminal** | Tempat menjalankan perintah | Termux (dari F-Droid) | Terminal bawaan / iTerm / Windows Terminal |
| **Python** | Runtime bahasa #1 kurikulum | `pkg install python` | python.org / `brew install python` |
| **Node.js** | Runtime alternatif (web, bot) | `pkg install nodejs` | nodejs.org |
| **Git** | Version control | `pkg install git` | git-scm.com |
| **AI agent** | Asisten coding utama | `npm install -g @earendil-works/pi-coding-agent` (pi) | sama, atau Claude Code / Cursor |

> Catatan: perintah install bisa berbeda tergantung versi tools — kalau ragu, tanyakan ke AI: *"Cara install [tool] di [platform] saya?"* — tapi verifikasi jawabannya, AI kadang mengarang.

## Verifikasi install

Setelah install, jalankan satu per satu dan pastikan semua mengeluarkan versi:
```bash
python --version        # → Python 3.x.x
node --version          # → v2x.x.x
git --version           # → git version 2.x
```
Kalau ada yang "command not found", ada 2 kemungkinan: belum terinstall, atau tidak ada di PATH. Tanyakan AI dengan error persisnya.

## Konfigurasi wajib

### 1. Git identity (sekali saja)
```bash
git config --global user.name "Nama Kamu"
git config --global user.email "email@kamu.com"
```

### 2. Setup agent coding
Agent coding (pi/Claude Code) butuh API key atau login ke penyedia model. Ikuti instruksi setup tool masing-masing. Jika pakai pi, file `AGENTS.md` di folder project bisa berisi aturan kerja untuk agent — baca dokumentasinya.

### 3. Folder project yang rapi
Buat struktur folder konsisten (ini menyelamatkanmu di modul-modul berikut):
```
projects/              # rumah semua project
├── latihan-1/         # satu folder per project
│   ├── README.md      # apa project ini?
│   └── src/           # kode
└── modul-1-catatan/   # project modul 1
```
Aturan: **satu project = satu folder = satu git repo**. Jangan taruh semua file berantakan di satu folder.

## Tes pertama: hello world dengan agent

1. Buat folder baru: `mkdir tes-pertama && cd tes-pertama`
2. Buka agent coding di folder itu
3. Kirim prompt: *"Buatkan file hello.py yang mencetak 'Halo, dunia!' lalu jalankan dan tunjukkan hasilnya"*
4. Agent akan: membuat file → menjalankan → menampilkan output
5. Kamu verifikasi: apakah file benar-benar ada? `ls` → apakah output benar?

Kalau ini berhasil, lingkunganmu siap. Kalau gagal, catat errornya dan minta bantuan agent lain / dokumentasi resmi.

## Troubleshooting umum

| Masalah | Solusi cepat |
|---|---|
| `command not found` | Belum install / PATH salah → cek perintah install, restart terminal |
| Error saat install (Android) | `pkg update && pkg upgrade` dulu |
| Agent tidak bisa menulis file | Cek izin folder (Termux: folder di dalam `~/` saja, bukan `/sdcard` langsung) |
| API key ditolak | Cek key benar, cek saldo/kuota, cek format env var |
| Internet lambat saat install | Pakai mirror/wifi, atau sabar — sekali install tidak perlu ulang |

## Ceklist Praktikum Akhir Modul 0

- [ ] Terminal berfungsi (bisa `pwd`, `ls`, `mkdir`)
- [ ] Python & Node terinstall (`--version` jalan)
- [ ] Git terinstall + identity tersetel
- [ ] Agent coding terinstall & bisa login/berfungsi
- [ ] Struktur folder `projects/` dibuat
- [ ] Tes hello world berhasil (agent bikin file + jalan)
- [ ] Kamu tahu cara memanggil agent di folder project manapun

**Output lesson ini**: lingkungan kerja lengkap yang siap dipakai di Modul 1.
