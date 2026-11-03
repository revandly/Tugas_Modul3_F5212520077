import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x500")
        self.resizable(False, False)

        # Konfigurasi Tema
        ctk.set_appearance_mode("Dark")

        # Frame Kiri (Form Input & Tombol)
        self.frame_form = ctk.CTkFrame(self, width=350)
        self.frame_form.pack(side="left", fill="y", padx=20, pady=20)

        self.label_title = ctk.CTkLabel(self.frame_form, text="Form Data Buku", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=20)

        self.entry_judul = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Judul Buku", width=280)
        self.entry_judul.pack(pady=10)

        self.entry_penulis = ctk.CTkEntry(self.frame_form, placeholder_text="Masukkan Nama Penulis", width=280)
        self.entry_penulis.pack(pady=10)

        self.entry_tahun = ctk.CTkEntry(self.frame_form, placeholder_text="Tahun Terbit (Misal: 2024)", width=280)
        self.entry_tahun.pack(pady=10)

        # Tombol-tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_form, text="Simpan Data", fg_color="green", hover_color="darkgreen", width=280)
        self.btn_simpan.pack(pady=15)

        self.btn_update = ctk.CTkButton(self.frame_form, text="Perbarui Data (Update)", fg_color="blue", hover_color="darkblue", width=280)
        self.btn_update.pack(pady=5)

        self.btn_hapus = ctk.CTkButton(self.frame_form, text="Hapus Data (Delete)", fg_color="red", hover_color="darkred", width=280)
        self.btn_hapus.pack(pady=5)

        # Frame Kanan (Tabel / Treeview)
        self.frame_tabel = ctk.CTkFrame(self)
        self.frame_tabel.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.label_tabel = ctk.CTkLabel(self.frame_tabel, text="Daftar Koleksi Buku", font=("Arial", 18, "bold"))
        self.label_tabel.pack(pady=10)

        # Setup Treeview
        columns = ("ID", "Judul Buku", "Penulis", "Tahun")
        self.tabel = ttk.Treeview(self.frame_tabel, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, width=110, anchor="center")
        
        self.tabel.column("ID", width=40)
        self.tabel.column("Judul Buku", width=180)
        
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)