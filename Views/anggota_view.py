import tkinter as tk
from tkinter import ttk


class AnggotaView:

  def __init__(self, root):
    self.root = root
    self.root.title("Manajemen Anggota Perpustakaan")
    self.root.geometry("650x450")

    # Judul Form
    self.lbl_title = tk.Label(
        root, text="Form Data Anggota Perpustakaan", font=("Arial", 14, "bold")
    )
    self.lbl_title.pack(pady=10)

    # Frame Form Input
    self.frame_form = tk.LabelFrame(
        root, text="Input Data Anggota", padx=10, pady=10
    )
    self.frame_form.pack(fill="x", padx=15, pady=5)

    # Label & Entry Nama Anggota
    self.lbl_nama = tk.Label(
        self.frame_form, text="Nama Anggota:", font=("Arial", 10)
    )
    self.lbl_nama.grid(row=0, column=0, sticky="w", pady=5)
    self.txt_nama = tk.Entry(self.frame_form, width=45, font=("Arial", 10))
    self.txt_nama.grid(row=0, column=1, pady=5, padx=5)

    # Label & Entry Alamat
    self.lbl_alamat = tk.Label(
        self.frame_form, text="Alamat:", font=("Arial", 10)
    )
    self.lbl_alamat.grid(row=1, column=0, sticky="w", pady=5)
    self.txt_alamat = tk.Entry(self.frame_form, width=45, font=("Arial", 10))
    self.txt_alamat.grid(row=1, column=1, pady=5, padx=5)

    # Frame Tombol Aksi
    self.frame_btn = tk.Frame(root, pady=10)
    self.frame_btn.pack(fill="x", padx=15)

    self.btn_simpan = tk.Button(
        self.frame_btn,
        text="Simpan Data",
        bg="green",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12,
    )
    self.btn_simpan.pack(side="left", padx=5)

    self.btn_update = tk.Button(
        self.frame_btn,
        text="Perbarui Data",
        bg="blue",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12,
    )
    self.btn_update.pack(side="left", padx=5)

    self.btn_delete = tk.Button(
        self.frame_btn,
        text="Hapus Data",
        bg="red",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12,
    )
    self.btn_delete.pack(side="left", padx=5)

    # Frame Tabel Visual Anggota
    self.frame_table = tk.Frame(root, padx=10, pady=10)
    self.frame_table.pack(fill="both", expand=True, padx=15, pady=5)

    # Konfigurasi Tabel (Treeview)
    self.tree = ttk.Treeview(
        self.frame_table,
        columns=("ID", "Nama Anggota", "Alamat"),
        show="headings",
    )
    self.tree.heading("ID", text="ID")
    self.tree.heading("Nama Anggota", text="Nama Anggota")
    self.tree.heading("Alamat", text="Alamat")

    self.tree.column("ID", width=50, anchor="center")
    self.tree.column("Nama Anggota", width=220, anchor="w")
    self.tree.column("Alamat", width=300, anchor="w")

    self.tree.pack(fill="both", expand=True)


if __name__ == "__main__":
  root = tk.Tk()
  app = AnggotaView(root)
  root.mainloop()