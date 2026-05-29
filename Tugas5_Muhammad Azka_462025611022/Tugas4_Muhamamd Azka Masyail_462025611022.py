
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    # Menampilkan informasi objek
    def __str__(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga} | Stok: {self.stok}"

    def __eq__(self, other):
        return self.harga == other.harga

    def __lt__(self, other):
        return self.harga < other.harga

    def __gt__(self, other):
        return self.harga > other.harga


# Membuat object
produk1 = Produk("Laptop", 7000000, 5)
produk2 = Produk("Mouse", 150000, 20)
produk3 = Produk("Keyboard", 150000, 10)

# __str__
print(produk1)
print(produk2)
print(produk3)

print("\n=== Perbandingan Produk ===")

# __gt__
print(f"Apakah harga {produk1.nama} > {produk2.nama}? : {produk1 > produk2}")

# __lt__
print(f"Apakah harga {produk2.nama} < {produk1.nama}? : {produk2 < produk1}")

# __eq__
print(f"Apakah harga {produk2.nama} == {produk3.nama}? : {produk2 == produk3}")