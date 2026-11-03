Python
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # 1. Inisialisasi Model dan View untuk Anggota
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # 2. Binding tombol simpan di View Anggota
        self.view.btn_simpan.configure(command=self.simpan_anggota)

        # 3. Memuat data ke tabel anggota saat pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari AnggotaModel
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke dalam tabel View
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['email']))

    def simpan_anggota(self):
        # Mengambil input dari form anggota
        nama = self.view.entry_nama.get()
        email = self.view.entry_email.get()

        # Validasi form kosong
        if not nama or not email:
            messagebox.showwarning("Peringatan", "Semua kolom form anggota harus diisi!")
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_anggota(nama, email)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            # Bersihkan form input
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_email.delete(0, 'end')
            # Muat ulang tabel
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data anggota.")

    # Fungsi untuk menjalankan view anggota
    def run(self):
        self.view.mainloop()