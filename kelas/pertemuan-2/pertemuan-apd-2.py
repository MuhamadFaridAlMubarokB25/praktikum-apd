from prettytable import PrettyTable
import inquirer
import os
os.system('cls')

def menu_utama():
    while True:
        menu_utama = PrettyTable()
        menu_utama.field_names = ["No", "Pilihan Menu"]
        menu_utama.align = "l"
        menu_utama.hrules = 1
        menu_utama.add_row(['1', 'CUSTOMER'])
        menu_utama.add_row(['2', 'ADMIN'])
        menu_utama.add_row(['3', 'KELUAR'])
        os.system
        print('=== SELAMAT DATANG DI TOKO PARFUM X ===')
        print('Anda Login Sebagai Siapa?')
        print(menu_utama)

        pertanyaan = [
        inquirer.List(
            "pilihan",
            message="Pilih menu",
            choices=[("1. Customer", 1), 
                    ("2. Admin", 2), 
                    ("3. Keluar", 3)]
        )
        ]

        answers = inquirer.prompt(pertanyaan)

        if answers["pilihan"] == 1:
            print('12')
        elif answers["pilihan"] == 2:
            print('32')

        input('ENTER')


menu_utama()


pertanyaan = [
inquirer.List(
    "pilihan",
    message="Silahkan Pilih Opsi Login",
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
        # try:
        #     opsilogin = int(input('Masukkan Pilihan (1-3): '))
        #     input('\nTekan Enter Untuk Melanjutkan...')

        #     if opsilogin == 1:
        #         menu_cust1()
        #     elif opsilogin == 2:
        #         menu_admin1()
        #     elif opsilogin == 3:
        #         print('\nTerima Kasih Sudah Berkunjung :)')
        #         exit()
        #     else:
        #         print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-3')
        #         input('\nTekan Enter Untuk Kembali...')
        #         continue
        # except ValueError:
        #     print('\nPilihan Harus Berupa Angka! Silahkan Pilih Angka 1-3')
        #     input('\nTekan Enter Untuk Kembali...')
        #     continue

