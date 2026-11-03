from models.user_model import UserModel

model = UserModel()
# Uji coba autentikasi secara langsung lewat kode
hasil = model.autentikasi("petugas", "admin123")

print("Hasil autentikasi:", hasil)
if hasil:
    print("STATUS: BERHASIL LOGIN!")
else:
    print("STATUS: GAGAL / PASSWORD TIDAK COCOK!")