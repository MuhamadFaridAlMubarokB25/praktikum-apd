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

# menu_utama = PrettyTable()
# menu_utama.field_names = ["No", "Pilihan Menu"]
# menu_utama.align = "l"
# menu_utama.hrules = 1
# menu_utama.add_row(['1', 'CUSTOMER'])
# menu_utama.add_row(['2', 'ADMIN'])
# menu_utama.add_row(['3', 'KELUAR'])
# print(menu_utama)

tabel_admin = PrettyTable()
tabel_admin.field_names = ["No", "Pilihan Menu"]
tabel_admin.align = "l"
tabel_admin.hrules = 2
tabel_admin.add_row(["1", "Lihat Semua Properti"])
tabel_admin.add_row(["2", "Tambah Properti"])
tabel_admin.add_row(["3", "Update Properti"])
tabel_admin.add_row(["4", "Hapus Properti"])
tabel_admin.add_row(["5", "Logout"])
print(tabel_admin)