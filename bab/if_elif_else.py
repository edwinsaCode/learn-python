
def jalankan():
    print("=== Bab 02 - Tipe Data ===")
    nilai = int(input("Masukan nilai kamu: "))

    if nilai >= 90:
        print("Nilai kamu A/sangat baik")
    elif nilai >= 75:
        print("Nilai kamu B/cukup baik")
    elif nilai >= 60:
        print("Nilai kamu C/cukup")
    else:
        print("Nilai kamu D/kurang")