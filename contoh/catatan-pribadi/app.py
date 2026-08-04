"""Catatan Pribadi — aplikasi CLI untuk mengelola catatan (project Modul 1).

Entry point & menu utama. Logika data ada di database.py.
Run: python app.py
"""

import sys

import database

MENU = """
=== CATATAN PRIBADI ===
1. Tambah catatan
2. Lihat daftar catatan
3. Lihat detail catatan
4. Edit catatan
5. Hapus catatan
6. Cari catatan
0. Keluar
Pilih (0-6): """


def input_teks(prompt, wajib=True):
    """Input dengan validasi: wajib diisi & tidak hanya spasi."""
    while True:
        nilai = input(prompt).strip()
        if nilai or not wajib:
            return nilai
        print("⚠️  Tidak boleh kosong. Coba lagi.")


def konfirmasi(prompt):
    """Konfirmasi y/n yang aman (input apapun selain y → tidak)."""
    jawaban = input(prompt).strip().lower()
    return jawaban in ("y", "ya", "yes")


def pilih_id(action):
    """Baca id catatan + cek keberadaan. Return id atau None (batal)."""
    try:
        catatan_id = int(input(f"Id catatan yang ingin di-{action}: "))
    except ValueError:
        print("❌ Id harus angka.")
        return None
    if database.dapatkan_catatan(catatan_id) is None:
        print(f"❌ Catatan id {catatan_id} tidak ditemukan.")
        return None
    return catatan_id


def fitur_tambah():
    judul = input_teks("Judul: ")
    isi = input_teks("Isi (boleh kosong): ", wajib=False)
    kategori = input_teks("Kategori (default: umum): ", wajib=False) or "umum"
    catatan_id = database.tambah_catatan(judul, isi, kategori)
    print(f"✅ Catatan tersimpan (id {catatan_id}).")


def fitur_daftar():
    catatan = database.daftar_catatan()
    if not catatan:
        print("📭 Belum ada catatan. Tambahkan yang pertama!")
        return
    print(f"\n{len(catatan)} catatan:")
    print("-" * 60)
    for c in catatan:
        print(f"  [{c['id']:>3}] {c['judul']}  ({c['kategori']})  — {c['tanggal_diubah']}")


def fitur_detail():
    catatan_id = pilih_id("lihat")
    if catatan_id is None:
        return
    c = database.dapatkan_catatan(catatan_id)
    print(f"\n📝 {c['judul']}  [{c['kategori']}]")
    print(f"   dibuat: {c['tanggal_dibuat']} | diubah: {c['tanggal_diubah']}")
    print("-" * 60)
    print(c["isi"] or "(kosong)")


def fitur_edit():
    catatan_id = pilih_id("edit")
    if catatan_id is None:
        return
    c = database.dapatkan_catatan(catatan_id)
    # Tampilkan nilai lama, user bisa tekan Enter untuk mempertahankan
    judul = input_teks(f"Judul [{c['judul']}]: ", wajib=False) or c["judul"]
    isi = input_teks(f"Isi [{c['isi'][:30]}{'...' if len(c['isi']) > 30 else ''}]: ", wajib=False)
    kategori = input_teks(f"Kategori [{c['kategori']}]: ", wajib=False) or c["kategori"]
    database.ubah_catatan(catatan_id, judul, isi, kategori)
    print("✅ Catatan diperbarui.")


def fitur_hapus():
    catatan_id = pilih_id("hapus")
    if catatan_id is None:
        return
    c = database.dapatkan_catatan(catatan_id)
    if not konfirmasi(f"Yakin hapus \"{c['judul']}\"? (y/n): "):
        print("↩️  Dibatalkan.")
        return
    database.hapus_catatan(catatan_id)
    print("🗑️  Catatan dihapus.")


def fitur_cari():
    kata_kunci = input_teks("Kata kunci: ")
    hasil = database.cari_catatan(kata_kunci)
    if not hasil:
        print(f"🔍 Tidak ada hasil untuk \"{kata_kunci}\".")
        return
    print(f"\n{len(hasil)} hasil untuk \"{kata_kunci}\":")
    print("-" * 60)
    for c in hasil:
        print(f"  [{c['id']:>3}] {c['judul']}  ({c['kategori']})")


ACTIONS = {
    "1": fitur_tambah,
    "2": fitur_daftar,
    "3": fitur_detail,
    "4": fitur_edit,
    "5": fitur_hapus,
    "6": fitur_cari,
}


def main():
    database.init_db()
    while True:
        pilihan = input(MENU).strip()
        if pilihan == "0":
            print("Sampai jumpa! 👋")
            sys.exit(0)
        aksi = ACTIONS.get(pilihan)
        if aksi is None:
            print("❌ Pilihan tidak valid. Pilih 0-6.")
            continue
        try:
            aksi()
        except KeyboardInterrupt:
            print("\n↩️  Dibatalkan.")
        except Exception as e:  # jaring pengaman: satu error tidak boleh crash app
            print(f"❌ Terjadi error: {e}")


if __name__ == "__main__":
    main()
