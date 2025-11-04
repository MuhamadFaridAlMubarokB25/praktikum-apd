import pwinput
from registrasi import akuns
from registrasi import akunadmin
from admin2 import menu_admin2
from customer2 import menu_cust2

def login_cust():
    print('\nHalo Customer!, Silahkan Login Terlebih Dahulu.')

    usernamecust = input('Masukkan Username: ')
    passwordcust = pwinput.pwinput(prompt='Masukkan Password: ', mask='*')

    if len(akuns) == 0:
        print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')
        input('\nTekan Enter Untuk Kembali...')
    elif usernamecust in akuns and akuns[usernamecust] == passwordcust:
        print('\nLogin Berhasil!')
        input('\nTekan Enter Untuk Melanjutkan...')
        menu_cust2()
    else:
        print('\nUsername atau Password Salah. Silahkan Coba Lagi')
        input('\nTekan Enter Untuk Kembali...')

def login_admin():
    print('\nHalo Admin!, Silahkan Login Terlebih Dahulu.')

    usernameadmin = input('Masukkan Username: ')
    passwordadmin = pwinput.pwinput(prompt='Masukkan Password: ', mask='*')

    if len(akunadmin) == 0:
        print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')
        input('\nTekan Enter Untuk Kembali...')
    elif usernameadmin in akunadmin and akunadmin[usernameadmin] == passwordadmin:
        print('\nLogin Berhasil!')
        input('\nTekan Enter Untuk Melanjutkan...')
        menu_admin2()
    else:
        print('\nUsername atau Password Salah. Silahkan Coba Lagi')
        input('\nTekan Enter Untuk Kembali...')