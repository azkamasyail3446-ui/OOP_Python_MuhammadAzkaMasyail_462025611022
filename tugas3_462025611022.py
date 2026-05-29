class Pesantren:
    def __init__(self, nama, stambuk, daerah, tingkatan_kelas):
        self.nama = nama
        self.stambuk = stambuk
        self.daerah = daerah
        self.tingkatan_kelas = tingkatan_kelas  # Menambahkan atribut kelas

    def tampilkan_data(self):
        print("------Data Santri------")
        print(f"Nama    = {self.nama}")
        print(f"Stambuk = {self.stambuk}")
        print(f"Daerah  = {self.daerah}")
        print()

    def tampilkan_kelas(self):
        # Menggunakan atribut self.tingkatan_kelas yang benar
        print(f"{self.nama} adalah santri kelas {self.tingkatan_kelas}")
        print()

    @staticmethod
    def Pondok():
        print("Pesantren: Al Kautsar")
        print()


# --- DI BAWAH INI DI LUAR BLOK CLASS (TANPA INDENTASI) ---

# Membuat objek santri dengan menambahkan argumen kelas di akhir
santri1 = Pesantren("azka", "84380", "Cianjur", "10 SMA")
santri2 = Pesantren("Devaleo", "64536", "Tangerang", "11 SMA")

# Memanggil method untuk santri1
santri1.tampilkan_data()
santri1.tampilkan_kelas()

# Memanggil method untuk santri2
santri2.tampilkan_data()
santri2.tampilkan_kelas()

# Memanggil static method
Pesantren.Pondok()
santri1.Pondok()