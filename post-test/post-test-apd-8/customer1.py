import os
os.system('cls')
from prettytable import PrettyTable
from registrasi import register_cust
from login import login_cust

def menu_cust1():
    while True:
        os.system('cls')
        menu_customer_1 = PrettyTable()
        menu_customer_1.field_names = ["No", "Pilihan Menu"]
        menu_customer_1.align = "l"
        menu_customer_1.hrules = 1
        menu_customer_1.add_row(['1', 'BUAT AKUN'])
        menu_customer_1.add_row(['2', 'LOGIN'])
        menu_customer_1.add_row(['3', 'KELUAR'])
        print('Selamat Datang Di MENU CUSTOMER!')
        print(menu_customer_1)
        try:
            opsicust = int(input('Masukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')
            if opsicust == 1:
                register_cust()
            elif opsicust == 2:
                login_cust()
            elif opsicust == 3:
                print('\nAnda Akan Keluar Dari Menu Customer')
                input('\nTekan Enter Untuk Melanjutkan...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-3')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nPilihan Harus Berupa Angka! Silahkan Pilih 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue