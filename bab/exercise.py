

def percabangan():
    angka = int(input("Masukkan angka: "))

    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")

    if angka != 0:
        if angka % 2 == 0:
            print("Angka genap")
        else:
            print("Angka ganjil")
    else:
        print("Angka nol")

def looping():
    angka = int(input("Masukkan angka: "))
    print(f"Tabel perkalian untuk {angka}")

    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")