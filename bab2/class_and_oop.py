
def oop_dasar():
    print("=== Bab 15 - OOP Dasar ===")

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

    mahasiswa1 = Mahasiswa("Budi", "12345", "Informatika")

    mahasiswa1.info()
    mahasiswa1.greeting()