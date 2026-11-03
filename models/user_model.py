import hashlib
import sqlite3

class UserModel:
    def __init__(self):
        # Sesuaikan dengan koneksi database Anda (misal: 'database.db')
        self.conn = sqlite3.connect("database.db")

    @staticmethod
    def hash_password(password):
        """Mengubah password plain text menjadi hash SHA-256 yang konsisten"""
        return hashlib.sha256(password.encode()).hexdigest()

    def autentikasi(self, username, password):
        """Melakukan autentikasi pengguna berdasarkan username dan password"""
        cursor = self.conn.cursor()
        password_hashed = self.hash_password(password)
        
        cursor.execute(
            "SELECT id_user, username, role FROM users WHERE username = ? AND password = ?",
            (username, password_hashed)
        )
        row = cursor.fetchone()
        
        if row:
            # Mendukung tuple maupun dict dari mock/database
            if isinstance(row, dict):
                return row
            elif hasattr(row, "keys"):
                return dict(row)
            else:
                return {
                    "id_user": row[0],
                    "username": row[1],
                    "role": row[2]
                }
        return None