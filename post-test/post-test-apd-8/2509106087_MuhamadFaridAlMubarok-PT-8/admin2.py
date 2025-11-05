import inquirer
import os
os.system('cls')
from prettytable import PrettyTable
from crud import tambah, list, update, hapus

def menu_admin2():
    while True:
        os.system('cls')
        menu_admin_2 = PrettyTable()
        menu_admin_2.field_names = ["No", "Pilihan Menu                    "]
        menu_admin_2.align = "l"
        menu_admin_2.hrules = 1
        menu_admin_2.add_row(['1', 'TAMBAHKAN PARFUM'])
        menu_admin_2.add_row(['2', 'TAMPILKAN LIST PARFUM'])
        menu_admin_2.add_row(['3', 'UPDATE DATA PARFUM'])
        menu_admin_2.add_row(['4', 'HAPUS DATA PARFUM'])
        menu_admin_2.add_row(['5', 'KELUAR'])
        print('Selamat Datang Di MENU ADMIN TOKO PARFUM X!')
        print(menu_admin_2)

        pertanyaan = [
        inquirer.List(
            'pilihan',
            message='Silahkan Pilih Opsi Yang Ada Di Menu',
            choices=[('1. TAMBAH', 1),
                    ('2. LIST', 2),
                    ('3. UPDATE', 3),
                    ('4. HAPUS', 4),
                    ('5. KELUAR', 5), ]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers['pilihan'] == 1:
            tambah()
        elif answers['pilihan'] == 2:
            list()
        elif answers['pilihan'] == 3:
            update()
        elif answers['pilihan'] == 4:
            hapus()
        else:
            answers['pilihan'] == 5
            print('\nAnda Akan Keluar Dari Menu Admin')
            input('\nTekan Enter Untuk Kembali Ke Menu...')
            break