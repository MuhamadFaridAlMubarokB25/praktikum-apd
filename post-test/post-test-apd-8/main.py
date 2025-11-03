import os
os.system('cls')
from prettytable import PrettyTable
from customer1 import menu_cust1
from admin1 import menu_admin1

def menu_utama():
    while True:
        menu_utama = PrettyTable()
        menu_utama.field_names = ["No", "Pilihan Menu"]
        menu_utama.align = "l"
        menu_utama.hrules = 1
        menu_utama.add_row(['1', 'CUSTOMER'])
        menu_utama.add_row(['2', 'ADMIN'])
        menu_utama.add_row(['3', 'KELUAR'])
        os.system('cls')
        print('=== SELAMAT DATANG DI TOKO PARFUM X ===')
        print('Anda Login Sebagai Siapa?')
        print(menu_utama)
        try:
            opsilogin = int(input('Masukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsilogin == 1:
                menu_cust1()
            elif opsilogin == 2:
                menu_admin1()
            elif opsilogin == 3:
                print('\nTerima Kasih Sudah Berkunjung :)')
                exit()
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-3')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nPilihan Harus Berupa Angka! Silahkan Pilih Angka 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue