akuns = {}
akunadmin = {}


def register_cust():
    print('\nHalo Customer baru!, Silahkan Buat Akun Terlebih Dahulu.')

    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    if username in akuns:
        print('\nUsername Sudah Digunakan. Silahkan Gunakan Username Lain!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        akuns[username] = password
        print('\nAkun Berhasil Dibuat! Silakan Login.')    
        input('\nTekan Enter Untuk Kembali Ke Menu...')

def register_admin():
    print('\nHalo Admin baru!, Silahkan Buat Akun Terlebih Dahulu.')

    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    if username in akunadmin:
        print('\nUsername Sudah Digunakan. Silahkan Gunakan Username Lain!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        akunadmin[username] = password
        print('\nAkun Berhasil Dibuat! Silakan Login.')    
        input('\nTekan Enter Untuk Kembali Ke Menu...')
