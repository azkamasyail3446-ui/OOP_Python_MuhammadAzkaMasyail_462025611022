# File: main.py

class DompetDigital:
    # Constructor
    def __init__(self, nama_pengguna, pin, saldo):
        self.__nama_pengguna = nama_pengguna
        self.__pin = pin
        self.__saldo = saldo

    def get_nama_pengguna(self):
        return self.__nama_pengguna

    def cek_saldo(self, pin):
        if pin == self.__pin:
            return f"Saldo anda: Rp{self.__saldo}"
        else:
            return "PIN salah! Akses ditolak."


dompet1 = DompetDigital("Azka", "1234", 500000)

# Menampilkan nama pengguna menggunakan getter
print("Nama Pengguna:", dompet1.get_nama_pengguna())


print("\n=== Pengujian Validasi PIN ===")

print(dompet1.cek_saldo("1234"))

print(dompet1.cek_saldo("0000"))
