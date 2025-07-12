
def jalankan():
    print("=== Bab 06 - Data Structure ===")
    buah = ["Apel", "Jeruk", "Mangga", "Lemon"]
    buah.append("Nangka")
    buah.insert(1, "Semangka")

    for b in buah:
        print(f"Buah: {b}")

    print("\n===Contoh Tuple===")
    koordinat = (10, 20)
    print(f"Koordinat: {koordinat[0]}, {koordinat[1]}")

    print("\n===Contoh Dictionary===")
    siswa = {
        "name": "Budi",
        "class": "Informatika",
        "age": 19
    }
    siswa["alamat"] = "Jalan Tuanku"
    for key, value in siswa.items():
        print(f"{key}: {value}")
    print(f"Siswa: {siswa['name']}, {siswa['class']}, {siswa['age']}")
    print(f"Siswa: {siswa}")


def list_exercise():
    print("=== Bab 07 - List Exercise ===")
    siswa = ["Budi", "Wati", "Siti"]
    print(f"Jumlah siswa: {len(siswa)}")
    print("Daftar siswa:")
    for i, nama in enumerate(siswa,start=1):
        print(f"{i}. {nama}")


def tuple_exercise():
    print("=== Bab 08 - Tuple Exercise ===")
    koordinat_rumah = (120.12, -8.09)
    print(f"Koordinat rumah: {koordinat_rumah}")
    print(f"Data type: {type(koordinat_rumah)}")


def dictionary_exercise():
    print("=== Bab 09 - Dictionary Exercise ===")
    siswa = {
        "name": "Budi",
        "class": "Informatika",
        "age": 19
    }
    print(f"data type: {type(siswa)}")
    print(f"Biodata siswa")

    for key, value in siswa.items():
        print(f"{key.capitalize()}: {value}")