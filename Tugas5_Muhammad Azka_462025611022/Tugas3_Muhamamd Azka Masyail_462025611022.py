class Pesantren:
    def __init__(self, nama, stambuk, daerah ):
        self.nama = nama
        self.stambuk = stambuk
        self.daerah = daerah

    def tampilkan_data(self):
        print("------Data Santri------")
        print(f"Nama    =   {self.nama}")
        print(f"stambuk    = {self.stambuk}")
        print(f"daerah  = {self.daerah}")
        print()

    def kelas(self):
        kelas = self.nama
        print(f"dia adalah santri kelas {self.kelas}")
        print()

    @staticmethod
    def Pondok():
        print("Pesantren: Al Kautsar")
        print()

    santri1 = Pesantren ("azka", "84380", "Cianjur")
    santri2 = Pesantren ("Devaleo", "64536", "Tangerang")

    santri1.tampilkan_data()
    santri1.kelas()

    santri2.tampilkan_data()
    santri2.kelas()

    Pesantren.Pondok()

    santri1.Pondok()