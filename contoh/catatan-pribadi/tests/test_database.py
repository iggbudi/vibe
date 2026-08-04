"""Test sederhana untuk layer database (Modul 2.3: failing test dulu).

Jalankan: python tests/test_database.py
Menggunakan database sementara agar tidak mengotori data asli.
"""

import os
import sys
import tempfile

# Arahkan database ke file sementara sebelum import
TMP_DIR = tempfile.mkdtemp()
os.environ.setdefault("DB_FILE", os.path.join(TMP_DIR, "test.db"))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Patch DB_FILE di modul database agar test tidak menyentuh data asli
import database  # noqa: E402

database.DB_FILE = os.path.join(TMP_DIR, "test.db")

LULUS = 0
GAGAL = 0


def cek(nama, kondisi):
    global LULUS, GAGAL
    if kondisi:
        LULUS += 1
        print(f"  ✅ {nama}")
    else:
        GAGAL += 1
        print(f"  ❌ {nama}")


def test_crud():
    print("\n— CRUD dasar —")
    database.init_db()

    # Tambah
    catatan_id = database.tambah_catatan("Belajar Python", "Latihan Modul 1", "belajar")
    cek("tambah catatan menghasilkan id", isinstance(catatan_id, int) and catatan_id > 0)

    # Baca (daftar)
    daftar = database.daftar_catatan()
    cek("daftar berisi catatan baru", any(c["id"] == catatan_id for c in daftar))

    # Baca (detail)
    detail = database.dapatkan_catatan(catatan_id)
    cek("detail judul benar", detail["judul"] == "Belajar Python")
    cek("detail kategori benar", detail["kategori"] == "belajar")
    cek("tanggal_dibuat terisi", bool(detail["tanggal_dibuat"]))
    cek("tanggal_diubah terisi", bool(detail["tanggal_diubah"]))

    # Edit
    berubah = database.ubah_catatan(catatan_id, "Belajar Python Lanjutan", "Latihan", "belajar")
    cek("edit mengembalikan True", berubah is True)
    detail = database.dapatkan_catatan(catatan_id)
    cek("judul berubah setelah edit", detail["judul"] == "Belajar Python Lanjutan")

    # Hapus
    terhapus = database.hapus_catatan(catatan_id)
    cek("hapus mengembalikan True", terhapus is True)
    cek("catatan tidak ditemukan setelah hapus", database.dapatkan_catatan(catatan_id) is None)


def test_edge_case():
    print("\n— Edge cases —")
    # Hapus id yang tidak ada → False (bukan error)
    cek("hapus id tak ada → False", database.hapus_catatan(99999) is False)
    # Edit id yang tidak ada → False
    cek("edit id tak ada → False", database.ubah_catatan(99999, "x", "x", "x") is False)
    # Detail id yang tidak ada → None (bukan error)
    cek("detail id tak ada → None", database.dapatkan_catatan(99999) is None)
    # Cari tanpa hasil → list kosong
    cek("cari tanpa hasil → list kosong", database.cari_catatan("zzz-tidak-ada-zzz") == [])
    # Isi kosong diperbolehkan
    catatan_id = database.tambah_catatan("Judul saja", "", "umum")
    cek("isi kosong diperbolehkan", database.dapatkan_catatan(catatan_id)["isi"] == "")


def test_pencarian():
    print("\n— Pencarian —")
    database.tambah_catatan("Resep Nasi Goreng", "Bahan: nasi, telur, kecap", "makanan")
    database.tambah_catatan("List Belanja", "Telur 1 kg", "belanja")

    hasil = database.cari_catatan("telur")
    cek("cari 'telur' dapat 2 hasil", len(hasil) == 2)
    hasil = database.cari_catatan("RESEP")  # case-insensitive
    cek("cari case-insensitive", len(hasil) == 1)
    hasil = database.cari_catatan("makanan")  # cari di kategori
    cek("cari di kategori", len(hasil) == 1)


def test_persistensi():
    print("\n— Persistensi (data tahan setelah koneksi ditutup) —")
    database.tambah_catatan("Catatan persisten", "Harus tetap ada", "test")
    daftar = database.daftar_catatan()
    cek("data tersimpan di file database", any(c["judul"] == "Catatan persisten" for c in daftar))


if __name__ == "__main__":
    test_crud()
    test_edge_case()
    test_pencarian()
    test_persistensi()
    print(f"\n=== HASIL: {LULUS} lulus, {GAGAL} gagal ===")
    sys.exit(1 if GAGAL else 0)
