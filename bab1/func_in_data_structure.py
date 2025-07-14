
def fungsi_1():
    print("Fungsi 1")

def fungsi_2():
    print("Fungsi 2")

def fungsi_3():
    print("Fungsi 3")

def func_in_list():
    print("=== Bab 13 - Fungsi dalam List ===")
    daftar_fungsi = [fungsi_1, fungsi_2, fungsi_3]
    for fungsi in daftar_fungsi:
        fungsi()

def func_in_dict():
    print("=== Bab 14 - Fungsi dalam Dictionary ===")
    menu = {
        "satu": fungsi_1,
        "dua": fungsi_2,
        "tiga": fungsi_3
    }
    menu["satu"]()
    for key,value in menu.items():
        print(f"{key} : {value.__name__}")

    pilihan = input("Pilih 'satu', 'dua', 'tiga': ")
    if pilihan in menu:
        menu[pilihan]()
    else:
        print("Fungsi tidak valid")