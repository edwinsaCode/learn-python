# import requests

# response = requests.get("https://www.google.com")
# print(response.json())

from bab import tipe_data, if_elif_else, looping, exercise, data_structure

if __name__ == "__main__":
    print("=== Menu ===")
    print("1. Bab 01 - Tipe Data")  
    print("2. Bab 02 - If, Elif, Else")
    print("3. Bab 03 - Looping")
    print("4. Bab 04 - Exercise Else If")
    print("5. Bab 05 - Exercise Looping")
    print("6. Bab 06 - Data Structure")

    pilihan = int(input("Pilih bab: "))
    if pilihan == 1:
        tipe_data.jalankan()
    elif pilihan == 2:
        if_elif_else.jalankan()
    elif pilihan == 3:
        looping.jalankan()
    elif pilihan == 4:
        exercise.percabangan()
    elif pilihan == 5:
        exercise.looping()
    elif pilihan == 6:
        data_structure.jalankan()
    else:
        print("Pilihan tidak valid")