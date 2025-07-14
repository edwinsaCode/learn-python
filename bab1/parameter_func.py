
def sapa(nama):
    print(f"Selamat datang di Kampus {nama}")

def oprasi_luas_persegi(panjang, lebar):
    return panjang * lebar

def oprasi_keliling_persegi(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_persegi():
    print("=== Bab 11 - Function Return ===")
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))
    hasil = oprasi_luas_persegi(panjang, lebar)
    print(f"Luas persegi adalah {hasil}")

def keliling_persegi():
    print("=== Bab 12 - Function Return1 ===")
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))
    hasil =  oprasi_keliling_persegi(panjang, lebar)
    print(f"Keliling persegi adalah {hasil}")