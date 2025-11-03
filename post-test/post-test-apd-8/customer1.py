import os
os.system('cls')
from prettytable import PrettyTable
from 

def menu_cust1():
    while True:
        os.system('cls')
        print('')
        print(43*'=')
        print('|                                         |')
        print('|              MENU CUSTOMER              |')
        print('|                                         |') 
        print(43*'=')
        print('| 1. BUAT AKUN                            |') 
        print('| 2. LOGIN                                |') 
        print('| 3. KELUAR                               |') 
        print(43*'=')
        print('')
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