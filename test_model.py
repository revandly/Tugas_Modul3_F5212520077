from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku(
    "Pemrograman Python MVC", "Guido van Rossum", "2026"
)  # Sesuaikan tahun jika diperlukan
print("Data berhasil disimpan!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    # Menggunakan indeks angka (tuple) karena mengambil dari SQLite langsung:
    # buku[0] = id, buku[1] = judul, buku[2] = penulis, buku[3] = tahun
    print(f"[{buku[0]}] {buku[1]} - {buku[2]} ({buku[3]})")