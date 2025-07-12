
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