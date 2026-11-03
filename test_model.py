from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku(
    "Pemrograman Python MVC", "Guido van Rossum", "2026"
)
print("Data berhasil disimpan!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    # Cetak tipe data dan isinya terlebih dahulu untuk memastikan strukturnya
    print("Tipe data:", type(buku))
    print("Isi data:", buku)
    
    # Jika hasilnya tuple (indeks angka):
    # print(f"[{buku[0]}] {buku[1]} - {buku[2]} ({buku[3]})")
    
    # Jika hasilnya dictionary (key string):
    # print(f"[{buku['id']}] {buku['judul']} - {buku['penulis']} ({buku['tahun']})")