class Santri:

    def __init__(self, nama):
        self.nama = nama

    def identitas(self):
        print(f"[*] {self.nama} adalah seorang Santri.")


class PengurusAsrama(Santri):

    def identitas(self):
        # super() dihapus
        print(f"[+] Tugas Tambahan: Mengurus ketertiban kamar asrama.")


class PengajarAlquran(Santri):

    def identitas(self):
        # super() dihapus
        print(f"[+] Tugas Tambahan: Mengajar kelas tajwid dan tahfidz.")


class KetuaPondok(PengurusAsrama, PengajarAlquran):

    def identitas(self):
        print(f"=== Profil Ketua Pondok ===")
        # super() dihapus
        print(f"[>] Peran Utama: Mengkoordinasi seluruh kegiatan pesantren.")
