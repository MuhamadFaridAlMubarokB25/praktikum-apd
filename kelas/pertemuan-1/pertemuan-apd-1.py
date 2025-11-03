from prettytable import PrettyTable

# print(43*'=')
#         print('|                                         |')
#         print('|     SELAMAT DATANG DI TOKO PARFUM X     |')
#         print('|     Anda ingin login sebagai siapa?     |')
#         print('|                                         |') 
#         print(43*'=')
#         print('| 1. CUSTOMER                             |') 
#         print('| 2. ADMIN                                |') 
#         print('| 3. KELUAR                               |') 
#         print(43*'=')
#         print('')

menu_utama = PrettyTable()
menu_utama.field_names = ["No", "Pilihan Menu"]
menu_utama.align = "l"
menu_utama.hrules = 1
menu_utama.add_row(['1', 'CUSTOMER'])
menu_utama.add_row(['2', 'ADMIN'])
menu_utama.add_row(['3', 'KELUAR'])
print('=== SELAMAT DATANG DI TOKO PARFUM X ===')
print('Anda Login Sebagai Siapa?')
print(menu_utama)

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

menu_customer_1 = PrettyTable()
menu_customer_1.field_names = ["No", "Pilihan Menu"]
menu_customer_1.align = "l"
menu_customer_1.hrules = 1
menu_customer_1.add_row(['1', 'BUAT AKUN'])
menu_customer_1.add_row(['2', 'LOGIN'])
menu_customer_1.add_row(['3', 'KELUAR'])
print('Selamat Datang Di MENU CUSTOMER!')
print(menu_customer_1)

print(43*'=')
print('|       MENU CUSTOMER TOKO PARFUM X       |')
print(43*'=')
print('| 1. LIHAT & BELANJA                      |')
print('| 2. KELUAR                               |')

menu_customer_2 = PrettyTable()
menu_customer_2.field_names = ["No", "Pilihan Menu"]
menu_customer_2.align = "l"
menu_customer_2.hrules = 1
menu_customer_2.add_row(['1', 'LIHAT & BELANJA'])
menu_customer_2.add_row(['2', 'KELUAR'])
print('Selamat Datang Di MENU CUSTOMER TOKO PARFUM X!')
print(menu_customer_2)

# Menu admin 1

menu_admin_1 = PrettyTable()
menu_admin_1.field_names = ["No", "Pilihan Menu"]
menu_admin_1.align = "l"
menu_admin_1.hrules = 1
menu_admin_1.add_row(['1', 'BUAT AKUN'])
menu_admin_1.add_row(['2', 'LOGIN'])
menu_admin_1.add_row(['3', 'KELUAR'])
print('Selamat Datang Di MENU ADMIN!')
print(menu_admin_1)

# menu admin 2

print(43*'=')
print('|        MENU ADMIN TOKO PARFUM X         |')
print(43*'=')
print('| 1. TAMBAHKAN PARFUM                     |')
print('| 2. TAMPILKAN LIST PARFUM                |')
print('| 3. UPDATE DATA PARFUM                   |')
print('| 4. HAPUS DATA PARFUM                    |')
print('| 5. KELUAR                               |')
print(43*'=')
print('')

menu_admin_2 = PrettyTable()
menu_admin_2.field_names = ["No", "Pilihan Menu"]
menu_admin_2.align = "l"
menu_admin_2.hrules = 1
menu_admin_2.add_row(['1', 'TAMBAHKAN PARFUM'])
menu_admin_2.add_row(['2', 'TAMPILKAN LIST PARFUM'])
menu_admin_2.add_row(['3', 'UPDATE DATA PARFUM'])
menu_admin_2.add_row(['4', 'HAPUS DATA PARFUM'])
menu_admin_2.add_row(['5', 'KELUAR'])
print('Selamat Datang Di MENU ADMIN TOKO PARFUM X!')
print(menu_admin_2)