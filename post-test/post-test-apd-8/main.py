import inquirer
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

        pertanyaan = [
        inquirer.List(
            "pilihan",
            message="Pilih Opsi Login",
            choices=[("1. Customer", 1), 
                    ("2. Admin", 2), 
                    ("3. Keluar", 3)]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers["pilihan"] == 1:
            menu_cust1()
        elif answers["pilihan"] == 2:
            menu_admin1()
        else:
            answers["pilihan"] == 3
            print('\nTerima Kasih Sudah Berkunjung :)')
            exit()

menu_utama()