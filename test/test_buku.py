from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku():
    # Inisialisasi Model
    model = BukuModel()

    # Mock koneksi database dan cursor
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menentukan nilai kembalian tiruan (mock return value) dari database fetchall
    mock_cursor.fetchall.return_value = [
        (1, "Algoritma Pemrograman", "Penulis A", 2025),
        (2, "Struktur Data", "Penulis B", 2026)
    ]

    # Eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()

    # Verifikasi hasil pengujian
    assert isinstance(hasil, list)
    assert len(hasil) == 2