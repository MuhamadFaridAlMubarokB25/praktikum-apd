import os
os.system('cls')

# Penyimpanan Data

akuns = []
dataparfum = []

# Menu Utama

while True:
    print(43*'=')
    print('|                                         |')
    print('|      SELAMAT DATANG DI TOKO PARFUM      |')
    print('|     Silahkan Pilih Menu DiBawah ini     |')
    print('|                                         |') 
    print(43*'=')
    print('| 1. REGISTRASI                           |') 
    print('| 2. LOGIN                                |') 
    print('| 3. KELUAR                               |') 
    print(43*'=')
    print('')

    opsimenu =int(input('\nPilih Opsi: '))
    
    # Proses Registrasi

    if opsimenu == 1:
        print(43*'=')
        print('|                                         |')
        print('|           SILAHKAN REGISTRASI           |')
        print('|                                         |') 
        print(43*'=')

        username = input('\nMasukkan Username: ')
        password = input('Masukkan Password: ')
        status = input('Login Sebagai (admin/customer): ')
        if status != 'admin' and status != 'customer':
            print('\nSilahkan Input Status Login dengan benar (admin/customer)')
            continue
        
        for akun in akuns:
            if akun[0] == username:
                print('Username sudah terdaftar. Silahkan Pilih Username Lain!')
                break
        akuns.append([username, password, status])
        print('\nRegistrasi Berhasil')

    # Proses Login

    elif opsimenu == 2:
        print(43*'=')
        print('|                                         |')
        print('|             SILAHKAN LOGIN              |')
        print('|                                         |') 
        print(43*'=')

        usernameinput = input('\nMasukkan Username: ')
        passwordinput = input('Masukkan Password: ')
        statusinput = (input('Login Sebagai (admin/customer): '))

        # Proses Login (Berhasil Login Sebagai Admin)

        if usernameinput == username and passwordinput == password and statusinput == 'admin':
            print('\nLogin Berhasil!, Selamat datang', username)
            print('')
            print(50*'=')
            print('|    SELAMAT DATANG DI MENU admin TOKO PARFUM    |')
            print(50*'=')
            print('| 1. TAMBAHKAN PARFUM                            |')
            print('| 2. TAMPILKAN LIST PARFUM                       |')
            print('| 3. UPDATE DATA PARFUM                          |')
            print('| 4. HAPUS DATA PARFUM                           |')
            print('| 5. KELUAR                                      |')
            print(50*'=')
            while True:
                opsi = int(input('\nPilih Opsi: '))

                # Menambahkan Parfum

                if opsi == 1:
                    print('\nSilahkan Menambahkan Data Parfum Baru')
                    nama  = input('Nama Parfum: ')
                    aroma = input('Aroma Parfum: ')
                    harga = int(input('Harga parfum: Rp. '))
                    print('\nData berhasil Ditambahkan')
                    dataparfum.append([nama, aroma, harga])

                # Membaca List Parfum

                elif opsi == 2:
                    print('\n=== LIST PARFUM ===')
                    if len(dataparfum) == 0:
                        print('\nDaftar Belum Ada, Silahkan Pilih Opsi 1 Untuk Menambahkan Data!')
                    else:
                        for i in range(len(dataparfum)):
                            print(f'\nParfum ke-{i+1}')
                            print(f'Nama Parfum : {dataparfum[i][0]}')
                            print(f'Aroma       : {dataparfum[i][1]}')
                            print(f'Harga       : Rp. {dataparfum[i][2]}')
                            print('\n===================')

                # Meng-Update Data Parfum

                elif opsi == 3:
                    updateparfum = input('\nMasukkan Nama Parfum yang ingin diupdate: ')
                    for i in range(len(dataparfum)):
                        if updateparfum == dataparfum[i][0]:
                            dataparfum[i][0] = input('Nama baru: ')
                            dataparfum[i][1] = input('Aroma baru: ')
                            dataparfum[i][2] = input('Harga baru: Rp. ')
                            print('\nData berhasil Di Update')
                            break
                        else:
                            print('\nData Tidak Ditemukan')

                # Menghapus Data Parfum

                elif opsi == 4:
                    hapusparfum = input('Masukkan Data Parfum yang ingin dihapus: ')
                    for i in range(len(dataparfum)):
                        if hapusparfum == dataparfum[i][0]:
                            del dataparfum[i]
                            print('\nData Berhasil Dihapus')

                # Keluar Dari Menu Admin

                elif opsi == 5:
                    print('\nTerima kasih sudah berkunjung ke Manajemen Data Toko Parfum')

                    break

                # Opsi Tidak Valid
                else:
                    print('\nPilihan Tidak Valid, Silahkan Pilih Opsi yang tersedia')

        # Proses Login (Berhasil Login Sebagai Customer)

        elif usernameinput == username and passwordinput == password and statusinput == 'customer':
            print('\nLogin Berhasil!')

            print(50*'=')
            print('|         SELAMAT DATANG DI TOKO PARFUM          |')
            print(50*'=')
            print('| 1. LIHAT & BELANJA                             |')
            print('| 2. KELUAR                                      |')
            print(50*'=')
            print('Silahkan Pilih Opsi!')
            while True:
                opsi = int(input('\nPilih Opsi: '))

                # Tampilan Daftar Dan Pembelian Parfum 

                if opsi == 1:
                    print('\n=== LIST PARFUM ===')
                    if len(dataparfum) == 0:
                        print('\nDaftar Parfum Belum Ada, Harap Tunggu Admin')
                        
                        continue
                    
                    for i in range(len(dataparfum)):
                        print(f'\nParfum ke-{i+1}')
                        print(f'Nama Parfum : {dataparfum[i][0]}')
                        print(f'Aroma       : {dataparfum[i][1]}')
                        print(f'Harga       : Rp. {dataparfum[i][2]}')
                        print('\n===================')

                        print('Ketentuan:')
                        print('\n- Silahkan Pilih NAMA parfum yang ingin Anda beli')
                        beli = input('Pilih Parfum: ')
                        
                        if beli == dataparfum[i][0]:
                            print('\n--- STRUK BELANJA ---')
                            print(f'Nama Parfum  : {dataparfum[i][0]}')
                            print(f'Total Harga  : {dataparfum[i][2]}')
                            print('\nTerimakasih Sudah Berbelanja')
                            print(5*'--')
                            print('\nApakah Anda Ingin Membeli parfum lagi?')
                            print('')
                            
                # Keluar ke Menu Utama
                elif opsi == 2:
                    print('Terimakasih Sudah Berkunjung ke Toko Parfum')
                    break

                # Pilihan Tidak Valid 

                else:
                    print('Pilihan Tidak Valid, Silahkan pilih Opsi yang Tersedia')
                    break

        # Status Login Salah

        elif statusinput != status:
            print('\nSilahkan Pilih Status! (admin/customer)')

        # Username Atau Input Salah

        elif usernameinput == username or passwordinput == password :
            print('\nUsername atau Password Salah, Silahkan Coba Lagi')
    
    # Keluar Dari Program

    elif opsimenu == 3:
        print('\nTerima Kasih Sudah Berkunjung')
        print('')
        exit()

    # Pilihan Tidak Valid pada Menu Utama

    else:
        print('\nPilihan Tidak Valid, Silahkan pilih Opsi yang Tersedia')

