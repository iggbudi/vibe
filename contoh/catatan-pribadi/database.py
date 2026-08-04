"""Database layer — semua akses SQLite ada di sini.

Prinsip Modul 4.3: query selalu parameterized, koneksi ditutup setelah dipakai.
"""

import sqlite3
from datetime import datetime

DB_FILE = "catatan.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS catatan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT NOT NULL,
    isi TEXT NOT NULL DEFAULT '',
    kategori TEXT NOT NULL DEFAULT 'umum',
    tanggal_dibuat TEXT NOT NULL,
    tanggal_diubah TEXT NOT NULL
);
"""


def _koneksi():
    """Buka koneksi (row factory: akses kolom via nama, bukan index)."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Buat tabel jika belum ada. Idempotent — aman dijalankan berulang."""
    with _koneksi() as conn:
        conn.execute(SCHEMA)


def _sekarang():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def tambah_catatan(judul, isi, kategori):
    """Simpan catatan baru, kembalikan id-nya."""
    with _koneksi() as conn:
        cur = conn.execute(
            "INSERT INTO catatan (judul, isi, kategori, tanggal_dibuat, tanggal_diubah)"
            " VALUES (?, ?, ?, ?, ?)",
            (judul, isi, kategori, _sekarang(), _sekarang()),
        )
        return cur.lastrowid


def daftar_catatan():
    """Semua catatan, urut terbaru di atas."""
    with _koneksi() as conn:
        return conn.execute(
            "SELECT id, judul, kategori, tanggal_diubah FROM catatan"
            " ORDER BY tanggal_diubah DESC"
        ).fetchall()


def dapatkan_catatan(catatan_id):
    """Satu catatan lengkap, atau None jika tidak ada."""
    with _koneksi() as conn:
        return conn.execute(
            "SELECT * FROM catatan WHERE id = ?", (catatan_id,)
        ).fetchone()


def ubah_catatan(catatan_id, judul, isi, kategori):
    """Update field catatan. Return True jika ada baris yang berubah."""
    with _koneksi() as conn:
        cur = conn.execute(
            "UPDATE catatan SET judul = ?, isi = ?, kategori = ?, tanggal_diubah = ?"
            " WHERE id = ?",
            (judul, isi, kategori, _sekarang(), catatan_id),
        )
        return cur.rowcount > 0


def hapus_catatan(catatan_id):
    """Hapus catatan. Return True jika ada baris yang terhapus."""
    with _koneksi() as conn:
        cur = conn.execute("DELETE FROM catatan WHERE id = ?", (catatan_id,))
        return cur.rowcount > 0


def cari_catatan(kata_kunci):
    """Cari di judul/isi/kategori (case-insensitive)."""
    pola = f"%{kata_kunci}%"
    with _koneksi() as conn:
        return conn.execute(
            "SELECT id, judul, kategori, tanggal_diubah FROM catatan"
            " WHERE judul LIKE ? OR isi LIKE ? OR kategori LIKE ?"
            " ORDER BY tanggal_diubah DESC",
            (pola, pola, pola),
        ).fetchall()
