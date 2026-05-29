class AlatPembayaran:

    def proses_bayar(self, nominal):
        # Metode dasar yang nanti akan di-override oleh child class
        print(f"Memproses pembayaran sebesar Rp{nominal:,}")


# --- CHILD CLASS 1 ---
class KartuKredit(AlatPembayaran):

    def proses_bayar(self, nominal):
        # Overriding dengan logika tambahan biaya admin kartu kredit
        biaya_admin = 2500
        total = nominal + biaya_admin
        print("[Kartu Kredit] Menghubungkan ke jaringan bank...")
        print(
            f"[Kartu Kredit] Transaksi Berhasil! Nominal: Rp{nominal:,} + Admin: Rp{biaya_admin:,} (Total: Rp{total:,})"
        )


# --- CHILD CLASS 2 ---
class EWallet(AlatPembayaran):

    def proses_bayar(self, nominal):
        # Overriding dengan logika diskon/cashback khas e-wallet
        cashback = int(nominal * 0.05)  # Cashback 5%
        print("[E-Wallet] Memindai kode QR...")
        print(
            f"[E-Wallet] Pembayaran Sukses! Nominal: Rp{nominal:,}. Kamu mendapatkan Cashback: Rp{cashback:,}"
        )


# --- KELAS INDEPENDEN (BUKAN TURUNAN AlatPembayaran) ---
# Ini untuk membuktikan kehebatan Duck Typing!
class PembayaranAlternatif:

    def proses_bayar(self, nominal):
        print(
            f"[Metode Rahasia] Bayar pakai barter senilai Rp{nominal:,} juga bisa!"
        )


# --- FUNGSI MANDIRI (DUCK TYPING) ---
def jalankan_transaksi(objek_pembayaran, nominal):
    """Fungsi ini tidak peduli apa kelas dari 'objek_pembayaran'.

    Selama objek tersebut punya metode bernama 'proses_bayar', fungsi
    ini akan berjalan dengan aman.
    """
    objek_pembayaran.proses_bayar(nominal)


# --- DEMONSTRASI ---

# 1. Membuat objek dari berbagai kelas
dompet_digital = EWallet()
kartu_bca = KartuKredit()
metode_unik = PembayaranAlternatif()

# 2. Menjalankan fungsi mandiri dengan objek yang berbeda-beda
print("=== TRANSAKSI 1 ===")
jalankan_transaksi(dompet_digital, 50000)
print()

print("=== TRANSAKSI 2 ===")
jalankan_transaksi(kartu_bca, 150000)
print()

print("=== TRANSAKSI 3 (DUCK TYPING SEJATI) ===")
jalankan_transaksi(metode_unik, 75000)