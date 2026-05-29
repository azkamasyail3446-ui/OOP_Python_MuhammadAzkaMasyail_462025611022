class Laptop:
    # Attributes
    def __init__(self, merk, ram, storage):
        self.merk = merk
        self.ram = ram
        self.storage = storage


laptop1 = Laptop("ASUS", "8GB", "512GB SSD")

laptop2 = Laptop("Lenovo", "16GB", "1TB SSD")

print("Laptop 1")
print("Merk    :", laptop1.merk)
print("RAM     :", laptop1.ram)
print("Storage :", laptop1.storage)

print()

print("Laptop 2")
print("Merk    :", laptop2.merk)
print("RAM     :", laptop2.ram)
print("Storage :", laptop2.storage)