import inquirer
import os
os.system('cls')
from prettytable import PrettyTable 
from belanja import belanja

def menu_cust2():
    while True:
        os.system('cls')
        menu_customer_2 = PrettyTable()
        menu_customer_2.field_names = ["No", "Pilihan Menu                    "]
        menu_customer_2.align = "l"
        menu_customer_2.hrules = 1
        menu_customer_2.add_row(['1', 'LIHAT & BELANJA'])
        menu_customer_2.add_row(['2', 'KELUAR'])
        print('Selamat Datang Di MENU CUSTOMER TOKO PARFUM X!')
        print(menu_customer_2)

        pertanyaan = [
        inquirer.List(
            'pilihan',
            message='Silahkan Pilih Opsi Yang Ada Di Menu',
            choices=[('1. Lihat & Belanja', 1), 
                    ('2. Keluar', 2) ]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers['pilihan'] == 1:
            belanja()
        else:
            answers['pilihan'] == 2
            print('\nAnda Akan Keluar Dari Menu Customer')
            input('\nTekan Enter Untuk Kembali Ke Menu...')
            break
