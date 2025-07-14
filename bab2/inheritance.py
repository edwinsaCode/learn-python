
def inheritance():
    print("=== Bab 16 - Inheritance ===")
    
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
        def __init__(self,nama,nim,kelas,prodi):
            super().__init__(nama,nim,kelas)
            self.prodi = prodi

        def tampilkan_prodi(self):
            print(f"Prodi: {self.prodi}")

    mahasiswa1 = MahasiswaAktif("Budi", "12345", "Informatika", "Teknik Informatika")
    mahasiswa1.info()
    mahasiswa1.greeting()
    mahasiswa1.tampilkan_prodi()