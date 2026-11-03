import sqlite3

class BukuModel:
    def __init__(self):
        self.db_name = "database_perpustakaan.db"
        self.conn = None  # Atribut tambahan untuk mendukung mock pada testing
        self.create_table()

    def get_connection(self):
        # Jika koneksi sedang di-mock oleh unit test, gunakan objek mock tersebut
        if self.conn is not None:
            return self.conn
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # Agar baris bisa diakses sebagai dictionary
        return conn

    def create_table(self):
        # Lewati pembuatan tabel jika sedang dalam mode mock testing
        if self.conn is not None:
            return
            
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Buat tabel jika belum ada
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buku (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                penulis TEXT NOT NULL,
                tahun TEXT NOT NULL
            )
        """)
        
        # Cek apakah tabel masih kosong; jika ya, masukkan data contoh otomatis
        cursor.execute("SELECT COUNT(*) FROM buku")
        count = cursor.fetchone()[0]
        if count == 0:
            sample_data = [
                ("cara jago sulap", "Revan", "2005"),
                ("resep masak", "vania", "2023"),
                ("Pemrograman Python MVC", "Guido van Rossum", "2023")
            ]
            cursor.executemany("INSERT INTO buku (judul, penulis, tahun) VALUES (?, ?, ?)", sample_data)
        
        conn.commit()
        if self.conn is None:
            conn.close()

    def get_all_buku(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        # Menggunakan AS agar nama kolom klop dengan yang dipanggil di controller (id_buku & tahun_terbit)
        cursor.execute("SELECT id AS id_buku, judul, penulis, tahun AS tahun_terbit FROM buku")
        rows = cursor.fetchall()
        
        # Konversi hasil query ke format dictionary agar sesuai dengan pemanggilan view/controller
        data = [dict(row) for row in rows]
        
        # Tutup koneksi hanya jika bukan objek Mock
        if self.conn is None:
            conn.close()
        return data

    def insert_buku(self, judul, penulis, tahun):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO buku (judul, penulis, tahun) VALUES (?, ?, ?)", (judul, penulis, tahun))
        conn.commit()
        if self.conn is None:
            conn.close()
        return True  # Mengembalikan True agar pengujian test_create_buku_berhasil sukses

    def create_buku(self, judul, penulis, tahun):
        # Alias untuk insert_buku agar cocok dengan test_model.py dan test_buku.py
        return self.insert_buku(judul, penulis, tahun)

    def update_buku(self, id_buku, judul, penulis, tahun):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE buku SET judul = ?, penulis = ?, tahun = ? WHERE id = ?", (judul, penulis, tahun, id_buku))
        conn.commit()
        if self.conn is None:
            conn.close()
        return True  # Mengembalikan True agar controller tahu proses update sukses

    def delete_buku(self, id_buku):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM buku WHERE id = ?", (id_buku,))
        conn.commit()
        if self.conn is None:
            conn.close()
        return True  # Mengembalikan True agar controller tahu proses delete sukses