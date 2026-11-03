import sqlite3

class BukuModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.create_table() # Otomatis membuat tabel jika belum ada

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buku (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                penulis TEXT NOT NULL,
                tahun TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def get_connection(self):
        return self.conn

    def create_buku(self, judul, penulis, tahun):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO buku (judul, penulis, tahun) VALUES (?, ?, ?)",
            (judul, penulis, tahun)
        )
        conn.commit()
        return True

    def get_all_buku(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id AS id_buku, judul, penulis, tahun AS tahun_terbit FROM buku")
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            if isinstance(row, dict):
                data.append(row)
            elif hasattr(row, "keys"):
                data.append(dict(row))
            elif isinstance(row, (list, tuple)) and len(row) >= 4:
                data.append({
                    "id_buku": row[0],
                    "judul": row[1],
                    "penulis": row[2],
                    "tahun_terbit": row[3]
                })
            else:
                data.append(row)
        return data