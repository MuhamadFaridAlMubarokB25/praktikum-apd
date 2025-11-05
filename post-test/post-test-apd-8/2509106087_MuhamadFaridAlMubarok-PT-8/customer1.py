import inquirer
import os
os.system('cls')
from prettytable import PrettyTable
from registrasi import register_cust
from login import login_cust

def menu_cust1():
    while True:
        os.system('cls')
        menu_customer_1 = PrettyTable()
        menu_customer_1.field_names = ["No", "Pilihan Menu                    "]
        menu_customer_1.align = "l"
        menu_customer_1.hrules = 1
        menu_customer_1.add_row(['1', 'BUAT AKUN'])
        menu_customer_1.add_row(['2', 'LOGIN'])
        menu_customer_1.add_row(['3', 'KELUAR'])
        print('Selamat Datang Di MENU CUSTOMER!')
        print(menu_customer_1)

        pertanyaan = [
        inquirer.List(
            'pilihan',
            message='Silahkan Pilih Opsi Yang Ada Di Menu',
            choices=[('1. Buat Akun', 1),
                    ('2. Login', 2),
                    ('3. Keluar', 3)]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers['pilihan'] == 1:
            register_cust()
        elif answers['pilihan'] == 2:
            login_cust()
        else:
            answers['pilihan'] == 3
            print('\nAnda Akan Keluar Dari Menu Customer')
            input('\nTekan Enter Untuk Kembali Ke Menu...')
            break

