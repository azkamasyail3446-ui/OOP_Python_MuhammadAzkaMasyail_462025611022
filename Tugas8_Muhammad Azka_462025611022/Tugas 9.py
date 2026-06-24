
class EmailTidakDitemukanError(Exception):
    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(self.pesan)


class PasswordSalahError(Exception):
    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(self.pesan)

class SistemLogin:
    def __init__(self):
        self.data_user = {
            "admin@gmas.com": "admin123",
            "koordinator@gmas.com": "koor123",
            "anggota@gmas.com": "anggota123"
        }

    def login(self, email, password):
        print("Memeriksa data login...")
        if email not in self.data_user:
            raise EmailTidakDitemukanError(
                "Email tidak terdaftar dalam sistem."
            )
        if self.data_user[email] != password:
            raise PasswordSalahError(
                "Password yang dimasukkan salah."
            )

        print("Login berhasil. Selamat datang di GMAS!")


sistem = SistemLogin()

try:
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    sistem.login(email, password)

except EmailTidakDitemukanError as error:
    print("ERROR:", error)

except PasswordSalahError as error:
    print("ERROR:", error)

finally:
    print("Proses pemeriksaan login telah selesai dilakukan.")