from config.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            # Query untuk mencocokkan username dan password dengan enkripsi SHA2 (256-bit)
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = SHA2(%s, 256)"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None