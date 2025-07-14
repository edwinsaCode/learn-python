# import requests

# response = requests.get("https://www.google.com")
# print(response.json())

from bab import tipe_data, if_elif_else, looping, exercise, data_structure
from bab1 import parameter_func, func_in_data_structure
from bab2 import class_and_oop, inheritance, overriding

if __name__ == "__main__":
    print("=== Menu ===")
    print("1. Bab 01 - Tipe Data")  
    print("2. Bab 02 - If, Elif, Else")
    print("3. Bab 03 - Looping")
    print("4. Bab 04 - Exercise Else If")
    print("5. Bab 05 - Exercise Looping")
    print("6. Bab 06 - Data Structure")
    print("7. Bab 07 - List Exercise")
    print("8. Bab 08 - Tuple Exercise")
    print("9. Bab 09 - Dictionary Exercise")
    print("10. Bab 10 - Function Parameters")
    print("11. Bab 11 - Function Return")
    print("12. Bab 12 - Function Return1")

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
    elif pilihan == 7:
        data_structure.list_exercise()
    elif pilihan == 8:
        data_structure.tuple_exercise()
    elif pilihan == 9:
        data_structure.dictionary_exercise()
    elif pilihan == 10:
        parameter_func.sapa("Doni")
    elif pilihan == 11:
        parameter_func.luas_persegi()
    elif pilihan == 12:
        parameter_func.keliling_persegi()
    elif pilihan == 13:
        func_in_data_structure.func_in_list()
    elif pilihan == 14:
        func_in_data_structure.func_in_dict()
    elif pilihan == 15:
        class_and_oop.oop_dasar()
    elif pilihan == 16:
        inheritance.inheritance()
    elif pilihan == 17:
        overriding.overriding()
    else:
        print("Pilihan tidak valid")