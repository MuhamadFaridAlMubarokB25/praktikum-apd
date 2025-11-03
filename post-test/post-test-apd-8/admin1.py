import inquirer
import os
os.system('cls')
from prettytable import PrettyTable 
from registrasi import register_admin
from login import login_admin

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

        pertanyaan = [
        inquirer.List(
            'pilihan',
            message='Silahkan Pilih Opsi Login',
            choices=[('1. Buat Akun', 1), 
                    ('2. Login', 2), 
                    ('3. Keluar', 3)]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers['pilihan'] == 1:
            register_admin()
        elif answers['pilihan'] == 2:
            login_admin()
        else:
            answers['pilihan'] == 3
            print('\nAnda Akan Keluar Dari Menu Login')
            input('\nTekan Enter Untuk Kembali Ke Menu Utama...')
            break