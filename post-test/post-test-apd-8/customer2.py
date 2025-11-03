import os
os.system('cls')
from prettytable import PrettyTable 

def menu_cust2():
    while True:
        os.system('cls')
        print(43*'=')
        print('|       MENU CUSTOMER TOKO PARFUM X       |')
        print(43*'=')
        print('| 1. LIHAT & BELANJA                      |')
        print('| 2. KELUAR                               |')
        print(43*'=')
        try:
            opsicust = int(input('\nMasukkan Pilihan (1-2): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsicust == 1:
                belanja()
            elif opsicust == 2:
                print('\nTerima Kasih Sudah Berkunjung ke TOKO PARFUM')
                input('\nTekan Enter Untuk Kembali Ke Menu Customer...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-2')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nPilihan Harus Berupa Angka! Silahkan Pilih 1-2')
            input('\nTekan Enter Untuk Kembali...')
            continue
