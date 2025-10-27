import os
os.system('cls')

# Penyimpanan Data

akuns = {}
akunadmin = {}
dataparfum = {}
transaksi = 0
nama_terakhir = ''

# Fungsi Menu

def menu_utama():
    while True:
        os.system('cls')
        print(43*'=')
        print('|                                         |')
        print('|     SELAMAT DATANG DI TOKO PARFUM X     |')
        print('|     Anda ingin login sebagai siapa?     |')
        print('|                                         |') 
        print(43*'=')
        print('| 1. CUSTOMER                             |') 
        print('| 2. ADMIN                                |') 
        print('| 3. KELUAR                               |') 
        print(43*'=')
        print('')
        try:
            opsilogin = int(input('Masukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsilogin == 1:
                menu_cust1()
            elif opsilogin == 2:
                menu_admin1()
            elif opsilogin == 3:
                print('\nTerima Kasih Sudah Berkunjung :)')
                exit()
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-3')
                input('\nTekan Enter Untuk Kembali')
                continue
        except ValueError:
            print('\nPilihan Harus Berupa Angka! Silahkan Pilih Angka 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue

def menu_cust1():
    while True:
        os.system('cls')
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
        try:
            opsicust = int(input('Masukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')
            if opsicust == 1:
                register_cust()
            elif opsicust == 2:
                login_cust()
            elif opsicust == 3:
                print('\nKeluar Dari Menu Customer')
                input('Tekan Enter Untuk Melanjutkan...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-3')
                input('\nTekan Enter Untuk Kembali')
                continue
        except ValueError:
            print('Pilihan Harus Berupa Angka! Silahkan Pilih 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue

def menu_cust2():
    while True:
        os.system('cls')
        print(43*'=')
        print('|         MENU CUSTOMER TOKO PARFUM       |')
        print(43*'=')
        print('| 1. LIHAT & BELANJA                      |')
        print('| 2. KELUAR                               |')
        print(43*'=')
        try:
            opsicust = int(input('\nMasukkan Pilihan (1-2): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsicust == 1:
                belanja()
            elif opsicust == 2:
                print('\nTerima Kasih Sudah Berkunjung ke TOKO PARFUM')
                input('\nTekan Enter Untuk Kembali Ke Menu Customer...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih Angka 1-2')
                input('\nTekan Enter Untuk Kembali')
                continue
        except:
            print('\nPilihan Tidak Valid! Silahkan Pilih 1-2')
            input('\nTekan Enter Untuk Kembali...')
            continue

def menu_admin1():
    while True:
        os.system('cls')
        print(43*'=')
        print('|                                         |')
        print('|               MENU ADMIN                |')
        print('|                                         |') 
        print(43*'=')
        print('| 1. BUAT AKUN                            |') 
        print('| 2. LOGIN                                |') 
        print('| 3. KELUAR                               |') 
        print(43*'=')
        print('')
        try:
            opsiadmin = int(input('\nMasukkan Pilihan (1-3): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsiadmin == 1:
                register_admin()
            elif opsiadmin == 2:
                login_admin()
            elif opsiadmin == 3:
                print('\nKeluar Dari Menu Admin')
                input('\nTekan Enter Untuk Melanjutkan...')
                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Pilih 1-3')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nPilihan Tidak Valid! Silahkan Pilih 1-3')
            input('\nTekan Enter Untuk Kembali...')
            continue

def menu_admin2():
    while True:
        os.system('cls')
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
        try:
            opsi = int(input('\nPilih Opsi (1-5): '))
            input('\nTekan Enter Untuk Melanjutkan...')

            if opsi == 1:
                tambah()
            elif opsi == 2:
                list()
            elif opsi == 3:
                update()
            elif opsi == 4:
                hapus()
            elif opsi == 5:
                print('\nKeluar Dari Menu Admin.')
                input('\nTekan Enter Untuk Melanjutkan...')
                break
            else:
                print('Pilihan Tidak Valid! Silahkan Pilih 1-5')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('Pilihan Harus Berupa Angka! Silahkan Pilih 1-5')
            input('\nTekan Enter Untuk Kembali...')
            continue

# Fungsi Registrasi & Login

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

def login_cust():
    print('\nHalo Customer!, Silahkan Login Terlebih Dahulu.')

    usernamecust = input('Masukkan Username: ')
    passwordcust = input('Masukkan Password: ')

    input('\nTekan Enter Untuk Melanjutkan...')

    if len(akuns) == 0:
        print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')
        input('\nTekan Enter Untuk Kembali...')
    elif usernamecust in akuns and akuns[usernamecust] == passwordcust:
        menu_cust2()
    else:
        print('\nUsername atau Password Salah. Silahkan Coba Lagi')
        input('\nTekan Enter Untuk Kembali...')

def login_admin():
    print('\nHalo Admin!, Silahkan Login Terlebih Dahulu.')

    usernameadmin = input('Masukkan Username: ')
    passwordadmin = input('Masukkan Password: ')

    input('\nTekan Enter Untuk Melanjutkan...')

    if len(akunadmin) == 0:
        print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')
        input('\nTekan Enter Untuk Kembali...')
    elif usernameadmin in akunadmin and akunadmin[usernameadmin] == passwordadmin:
        menu_admin2()
    else:
        print('\nUsername atau Password Salah. Silahkan Coba Lagi')
        input('\nTekan Enter Untuk Kembali...')

# Fungsi Di Toko Parfum

def tambah():
    print('\n=== TAMBAH DATA PARFUM ===')
    nama  = input('Nama Parfum: ')
    aroma = input('Aroma Parfum: ')
    try:
        harga = int(input('Harga Parfum: Rp. '))
    except ValueError:
        print('\nHarga Harus Berupa Angka!')
        input('\nTekan Enter Untuk Kembali...')
        return
    dataparfum[nama] = {'Aroma': aroma, 'Harga': harga}
    print('\nData berhasil ditambahkan!')
    input('\nTekan Enter Untuk Kembali...')

def list():
    print('\n=== LIST DATA PARFUM ===')
    if len(dataparfum) == 0:
        print('\nData Parfum Belum Tersedia.')
        input('\nTekan Enter Untuk Kembali...')
    else:
        urutan = 1
        for nama, info in dataparfum.items():
            print(f'\nParfum Ke-{urutan}')
            print(f'Nama  : {nama}')
            print(f'Aroma : {info['Aroma']}')
            print(f'Harga : Rp. {info['Harga']}')
            urutan += 1
        input('\nTekan Enter Untuk Lanjut...')

def update():
    list()
    print('\n=== UPDATE DATA PARFUM ===')
    namasebelumnya = input('Masukkan Nama Parfum yang Ingin Diupdate: ')
    if namasebelumnya in dataparfum:
        namabaru = input('Nama baru: ')
        aromabaru = input('Aroma baru: ')
        try:
            hargabaru = int(input('Harga baru: Rp. '))
        except ValueError:
            print('\nHarga Harus Berupa Angka!')
            input('\nTekan Enter Untuk Kembali...')
            return
        dataparfum.pop(namasebelumnya)
        dataparfum[namabaru] = {'Aroma': aromabaru, 'Harga': hargabaru}
        print('\nData berhasil diupdate!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        print('\nData Tidak Ditemukan')
        input('\nTekan Enter Untuk Kembali...')

def hapus():
    list()

    print('\n=== HAPUS DATA PARFUM ===')
    hapusparfum = input('Masukkan Nama Parfum yang Ingin Dihapus: ')
    if hapusparfum in dataparfum:
        dataparfum.pop(hapusparfum)
        print('\nData berhasil dihapus!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        print('\nData Tidak Ditemukan')
        input('\nTekan Enter Untuk Kembali...')

def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_pajak(total, persen):
    persen = 5
    return total * persen / 100

def belanja():
    global transaksi, nama_terakhir
    if len(dataparfum) == 0:
        print("\nParfum Belum Tersedia, Silahkan Menunggu Admin Menambahkan Data.")
        input('\nTekan Enter Untuk Kembali...')
        return
    list()
    beli = input('\nMasukkan Nama Parfum Yang Ingin Dibeli: ')
    if beli in dataparfum:
        try:
            jumlah = int(input('Masukkan Jumlah yang Ingin Dibeli: '))
        except ValueError:
            print("\nJumlah Harus Berupa Angka!")
            input('\nTekan Enter Untuk Kembali...')
            return
        total = hitung_total(dataparfum[beli]['Harga'], jumlah)
        pajak = hitung_pajak(total, 5)
        total += pajak
        transaksi += total
        nama_terakhir = beli
        print('\n=== STRUK BELANJA ===')
        print(f'Nama Parfum              : {beli}')
        print(f'Aroma                    : {dataparfum[beli]["Aroma"]}')
        print(f'Harga Satuan             : Rp. {dataparfum[beli]["Harga"]}')
        print(f'Jumlah                   : {jumlah}')
        print(f'Total Harga + Pajak (5%) : Rp. {total}')
        print('\nTerima Kasih Sudah Berbelanja!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        print("\nNama Parfum Tidak Ditemukan")
        input('\nTekan Enter Untuk Kembali...')

# Program Utama

while True:
    menu_utama()