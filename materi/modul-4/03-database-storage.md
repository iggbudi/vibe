# 4.3 — Database & Storage

**Durasi**: 2 hari (±6 jam)
**Tujuan pembelajaran**:
- Menghubungkan aplikasi ke database eksternal (PostgreSQL/MySQL) atau DBaaS
- Memahami peran ORM dan kapan memakainya
- Integrasi penyimpanan file (local → cloud)

---

## Evolusi penyimpanan di kurikulum ini

```
Modul 1: SQLite (file lokal, satu pengguna)
    ↓
Modul 4: Database eksternal / DBaaS (server, banyak pengguna, akses bersama)
```

Kapan perlu pindah dari SQLite? Saat aplikasi diakses banyak orang / beberapa perangkat / perlu backup terpusat. SQLite tetap valid untuk banyak kasus — jangan over-engineer.

## Menghubungkan ke database eksternal

### SQLite → PostgreSQL (contoh konsep)

```python
# SEBELUM (SQLite):
db.execute("SELECT * FROM transaksi")

# SESUDAH (PostgreSQL via psycopg):
import psycopg2
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),   # dari .env, JANGAN hardcode
)
cur = conn.cursor()
cur.execute("SELECT * FROM transaksi")
```

**Semua kredensial database = secret**. `DB_PASSWORD` di kode = malapetaka.

### URL connection string (pola umum)
Banyak library menerima satu string:
```
postgresql://user:password@host:5432/nama_db
mysql://user:password@host:3306/nama_db
```
Simpan URL ini di `.env` (`DATABASE_URL=...`).

## ORM: kapan & kenapa

ORM (Object Relational Mapper) = library yang menerjemahkan Python object ↔ tabel database, sehingga kamu tidak menulis SQL manual.

| Tanpa ORM | Dengan ORM (contoh SQLAlchemy) |
|---|---|
| `cur.execute("INSERT INTO transaksi (tanggal,total) VALUES (?,?)")` | `db.add(Transaksi(tanggal=..., total=...))` |
| SQL string — rawan typo & injection | Object — tipe dicek, query terstruktur |

### Kapan pakai ORM
- ✅ Aplikasi dengan banyak tabel & relasi → ORM menghemat waktu & mengurangi bug
- ✅ Ingin pindah database tanpa ubah kode (SQLite ↔ PostgreSQL cukup ganti URL)
- ❌ Query kompleks/performance-critical → tulis SQL mentah (ORM bisa lebih lambat)
- ❌ Kurikulum Modul 3 → SQL sederhana sudah cukup; jangan tambah kompleksitas

**Keputusan yang baik**: mulai SQLite + SQL sederhana. Tambah ORM saat tabel mulai banyak. Minta AI menilai: *"Apakah project ini butuh ORM? Pertimbangkan jumlah tabel, relasi, dan kebutuhan pindah database."*

## Migration: mengubah skema dengan aman

Pindah ke database eksternal biasanya butuh membuat skema & mengubahnya seiring waktu. Gunakan tool migration (Alembic untuk SQLAlchemy, atau cukup script SQL):

```bash
# Ide: setiap perubahan skema = 1 file migration bernomor
migrations/
├── 001_create_transaksi.sql
├── 002_add_kategori.sql
└── 003_add_index.sql
```
- Migration idempotent: bisa dijalankan ulang tanpa merusak (`IF NOT EXISTS`)
- **Backup dulu** sebelum menjalankan migration di database yang berisi data

## File storage: local → cloud

Aplikasi yang menyimpan file (upload gambar, lampiran):

```
SEBELUM: simpan di folder /uploads lokal
SESUDAH: simpan di cloud storage (S3-compatible, Backblaze B2, dll)
```

```python
# Konsep: upload ke cloud storage
def upload_file(nama, isi):
    # boto3 untuk AWS S3 / library untuk penyedia lain
    client.upload_fileobj(isi, BUCKET_NAME, nama)
    return f"https://cdn.example.com/{nama}"   # URL publik

def download_file(nama):
    return client.download_file(BUCKET_NAME, nama)
```

**Pola penting**: database menyimpan **URL/path**, file-nya di storage. Jangan simpan blob besar di database.

## Checklist integrasi database

- [ ] Kredensial database di `.env`, tidak ada di kode/git
- [ ] Semua query parameterized (tidak ada string concatenation)
- [ ] Connection punya timeout & ditutup setelah dipakai
- [ ] Koneksi gagal → aplikasi kasih pesan jelas, bukan crash diam-diam
- [ ] Migration tersimpan & idempotent
- [ ] Backup database sebelum perubahan skema

## Latihan

1. Buat akun database gratis (Neon/Supabase untuk PostgreSQL, atau pakai Docker PostgreSQL di laptop)
2. Hubungkan aplikasi Modul 1-mu ke database itu (ganti SQLite) — pertahankan perilaku yang sama
3. Tambahkan 1 kolom baru lewat migration → verifikasi data lama tidak rusak
4. (Bonus) Upload 1 file ke cloud storage → tampilkan kembali
5. Matikan internet → pastikan aplikasi memberi pesan error yang jelas (tidak hang)

**Output lesson ini**: aplikasi yang jalan di database eksternal + migration aman.
