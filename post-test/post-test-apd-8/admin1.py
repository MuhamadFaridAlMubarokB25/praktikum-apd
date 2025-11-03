import os
os.system('cls')
from prettytable import PrettyTable 
from registrasi import register_admin

def menu_admin1():
    while True:
        os.system('cls')
        menu_admin_1 = PrettyTable()
        menu_admin_1.field_names = ["No", "Pilihan Menu"]
        menu_admin_1.align = "l"
        menu_admin_1.hrules = 1
        menu_admin_1.add_row(['1', 'BUAT AKUN'])
        menu_admin_1.add_row(['2', 'LOGIN'])
        menu_admin_1.add_row(['3', 'KELUAR'])
        print('Selamat Datang Di MENU ADMIN!')
        print(menu_admin_1)
        try:
            opsiadmin = int(input('\nMasukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsiadmin == 1:
                register_admin()
            elif opsiadmin == 2:
                login_admin()
            elif opsiadmin == 3:
                print('\nAnda Akan Keluar Dari Menu Admin')
                input('\nTekan Enter Untuk Melanjutkan...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih 1-3')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nPilihan Harus Berupa Angka! Silahkan Pilih 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue