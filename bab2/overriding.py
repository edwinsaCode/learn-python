
def overriding():
    print("=== Bab 16 - Overriding ===")
    class Mahasiswa:
        def __init__(self, nama, nim, kelas):
            self.nama = nama
            self.nim = nim
            self.kelas = kelas

        def info(self):
            print(f"Nama: {self.nama}")
            print(f"NIM: {self.nim}")
            print(f"Kelas: {self.kelas}")

        def greeting(self):
            print(f"Selamat datang kepada mahasiswa baru : {self.nama}, {self.kelas}, {self.nim}")

    class MahasiswaAktif(Mahasiswa):
        def greeting(self):
            print(f"Selamat datang kepada mahasiswa aktif : {self.nama}, {self.kelas}, {self.nim}")

    mahasiswa = Mahasiswa("Ari", "12345", "Informatika")
    mahasiswa1 = MahasiswaAktif("Budi", "12345", "Informatika")

    mahasiswa.greeting()
    mahasiswa1.greeting()
