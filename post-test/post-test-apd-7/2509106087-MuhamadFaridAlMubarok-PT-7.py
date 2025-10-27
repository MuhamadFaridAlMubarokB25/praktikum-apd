import os
os.system('cls')

# Penyimpanan Data
akuns = {}
akunadmin = {}
dataparfum = {}

# Menu Utama
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

    opsilogin = int(input('\nMasukkan Pilihan: '))

    input('\nTekan Enter Untuk Melanjutkan...')

    # Menu Customer
    if opsilogin == 1:
        while True:
            os.system('cls')
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
    
            opsicust = int(input('\nMasukkan Pilihan: '))

            input('\nTekan Enter Untuk Melanjutkan...')
    
            # Buat Akun Customer

            if opsicust == 1:
                os.system('cls')
                print('\nHalo Customer baru!, Silahkan Buat Akun Terlebih Dahulu.')

                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')

                if username in akuns:
                    print("Username Sudah Digunakan. Silahkan Gunakan Username Lain!")

                    input('\nTekan Enter Untuk Kembali...')

                else:
                    akuns[username] = password
                    print("Akun Berhasil Dibuat! Silakan Login.")    

                    input('\nTekan Enter Untuk Kembali Ke Menu...')
                    continue

            # Login Customer

            elif opsicust == 2:
                os.system('cls')
                print('\nHalo Customer baru!, Silahkan Login Terlebih Dahulu.')

                usernamecust = input('Masukkan Username: ')
                passwordcust = input('Masukkan Password: ')

                input('\nTekan Enter Untuk Melanjutkan...')

                if len(akuns) == 0:
                    print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')

                    input('\nTekan Enter Untuk Kembali...')

                elif usernamecust in akuns and akuns[usernamecust] == passwordcust:
                    while True:
                        os.system('cls')
                        print(43*'=')
                        print('|         MENU CUSTOMER TOKO PARFUM       |')
                        print(43*'=')
                        print('| 1. LIHAT & BELANJA                      |')
                        print('| 2. KELUAR                               |')
                        print(43*'=')

                        opsi = int(input('\nPilih Opsi: ')) 

                        input('\nTekan Enter Untuk Melanjutkan...')

                        # LIHAT & BELANJA

                        if opsi == 1:
                            if len(dataparfum) == 0:
                                print('\nDaftar Parfum Belum Ada, Harap Tunggu Admin Menambahkan Data.')

                                input('\nTekan Enter Untuk Kembali...')

                                continue
                            else:
                                print('\n=== LIST PARFUM ===')
                                urutan = 1
                                for nama, info in dataparfum.items():
                                    print(f'\nParfum Ke-{urutan}')
                                    print(f'Nama  : {nama}')
                                    print(f'Aroma : {info["Aroma"]}')
                                    print(f'Harga : Rp. {info["Harga"]}')
                                    urutan += 1

                                beli = input('\nMasukkan Nama Parfum Yang Ingin Dibeli: ')

                                if beli in dataparfum:
                                    jumlah = int(input('Masukkan Jumlah Yang Ingin Dibeli: '))

                                    input('\nTekan Enter Untuk Membeli...')

                                    total = jumlah * dataparfum[beli]['Harga']

                                    print('\n=== STRUK BELANJA ===')
                                    print(f'Nama Parfum  : {beli}')
                                    print(f'Aroma        : {dataparfum[beli]["Aroma"]}')
                                    print(f'Harga Satuan : Rp. {dataparfum[beli]["Harga"]}')
                                    print(f'Jumlah       : {jumlah}')
                                    print(f'Total Harga  : Rp. {total}')
                                    print('Terima Kasih Sudah Berbelanja!\n')

                                    input('\nTekan Enter Untuk Kembali...')

                                else:
                                    print('\nParfum Tidak Ditemukan')

                                    input('\nTekan Enter Untuk Kembali...')
                        
                        # KELUAR

                        elif opsi == 2:
                            print('\nTerima Kasih Sudah Berkunjung ke TOKO PARFUM')

                            input('\nTekan Enter Untuk Kembali Ke Menu Utama...')
                            break
                        
                        else:
                            print('Pilihan Tidak Valid, Silahkan pilih opsi yang tersedia')

                            input('\nTekan Enter Untuk Kembali...')

                else:
                    print('\nUsername atau Password Salah. Silahkan Coba Lagi')

                    input('\nTekan Enter Untuk Kembali...')

            elif opsicust == 3:
                print('\nTerima Kasih Sudah Berkunjung, Silahkan Datang Lagi.')

                input('\nTekan Enter Untuk Keluar...')

                break
            else:
                print('\nPilihan Tidak Valid! Silahkan Masukkan Pilihan yang Tersedia Di Menu.')

                input('\nTekan Enter Untuk Kembali...')


    # Menu Utama Admin

    elif opsilogin == 2:
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

            opsiadmin = int(input('Masukkan Pilihan: ')) 

            input('\nTekan Enter Untuk Melanjutkan...')

            # Buat Akun Admin

            if opsiadmin == 1:
                os.system('cls')
                print('\nHalo Admin baru!, Silahkan Buat Akun Terlebih Dahulu.')

                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                
                if username in akunadmin:
                    print("Username sudah digunakan. Silahkan Gunakan Username Lain!")

                    input('\nTekan Enter Untuk Kembali...') 
                else:
                    akunadmin[username] = password
                    print("Akun berhasil dibuat! Silakan login.") 

                    input('\nTekan Enter Untuk Kembali Ke Menu...')   
                    continue

            # Login Admin

            elif opsiadmin == 2:
                os.system('cls')
                print('\nHalo Admin baru!, Silahkan Login Terlebih Dahulu.')

                usernameadmin = input('Masukkan username: ')
                passwordadmin = input('Masukkan password: ')

                input('\nTekan Enter Untuk Melanjutkan...')

                if len(akunadmin) == 0:
                    print('\nAnda Belum Memiliki Akun. Silahkan Buat Akun Untuk Login!')

                    input('\nTekan Enter Untuk Kembali Ke Menu...')  

                elif usernameadmin in akunadmin and akunadmin[usernameadmin] == passwordadmin:
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

                        opsi = int(input('\nPilih Opsi: '))

                        input('\nTekan Enter Untuk Melanjutkan...') 

                        # Tambah Data Parfum

                        if opsi == 1:
                            os.system('cls')
                            print('\n=== TAMBAH DATA PARFUM ===')
                            
                            nama  = input('Nama Parfum: ')
                            aroma = input('Aroma Parfum: ')
                            harga = int(input('Harga parfum: Rp. '))

                            dataparfum[nama] = {
                                'Aroma': aroma,
                                'Harga': harga
                            }
                            print('\nData berhasil ditambahkan!')

                            input('\nTekan Enter Untuk Kembali Ke Menu...')

                        # Lihat List Parfum

                        elif opsi == 2:
                            print('\n=== LIST PARFUM ===')
                            if len(dataparfum) == 0:
                                print('Daftar belum ada, silahkan tambah data dulu!')

                                input('\nTekan Enter Untuk Kembali Ke Menu...')

                            else:
                                urutan = 1
                                for nama, info in dataparfum.items():
                                    print(f'\nParfum Ke-{urutan}')
                                    print(f'Nama  : {nama}')
                                    print(f'Aroma : {info["Aroma"]}')
                                    print(f'Harga : Rp. {info["Harga"]}')
                                    urutan += 1

                                input('\nTekan Enter Untuk Kembali Ke Menu...')



                        # Update Data Parfum

                        elif opsi == 3:
                            os.system('cls')
                            print('\n=== UPDATE DATA PARFUM ===')
                            
                            namasebelumnya = input('Masukkan Nama Parfum yang Ingin Diupdate: ')
                            if namasebelumnya in dataparfum:
                                namabaru = input('Nama baru: ')
                                aromabaru = input('Aroma baru: ')
                                hargabaru = int(input('Harga baru: Rp. '))
                                dataparfum.pop(namasebelumnya)
                                dataparfum[namabaru] = {'Aroma': aromabaru, 'Harga': hargabaru}
                                print('\nData berhasil diupdate!')

                                input('\nTekan Enter Untuk Kembali Ke Menu...')

                            else:
                                print('\nData Tidak Ditemukan')

                                input('\nTekan Enter Untuk Kembali Ke Menu...')

                        # Hapus Data Parfum

                        elif opsi == 4:
                            os.system('cls')
                            print('\n=== HAPUS DATA PARFUM ===')

                            hapusparfum = input('Masukkan Nama Parfum yang Ingin Dihapus: ')
                            if hapusparfum in dataparfum:
                                dataparfum.pop(hapusparfum)
                                print('\nData berhasil dihapus!')

                                input('\nTekan Enter Untuk Kembali Ke Menu...')

                            else:
                                print('\nData Tidak Ditemukan')

                                input('\nTekan Enter Untuk Kembali...')

                        # Keluar Menu Admin Toko Parfum

                        elif opsi == 5:
                            print('\nKeluar dari menu admin.')

                            input('\nTekan Enter Untuk Keluar Dari Menu...')
                            break

                        # Pilihan Tidak Valid

                        else:
                            print('\nPilihan Tidak Valid!')

                            input('\nTekan Enter Untuk Kembali...')

                # User atau Pass Salah

                else:
                    print('\nUsername atau Password Salah. Silahkan Coba Lagi')

                    input('\nTekan Enter Untuk Kembali...')

            # Keluar Menu admin

            elif opsiadmin == 3:
                print('\nTerima Kasih Sudah Berkunjung.')

                input('\nTekan Enter Untuk Keluar Dari Program...')
                break

            else:
                print('\nPilihan Tidak Valid!')

                input('\nTekan Enter Untuk Kembali...')

    # Keluar Program

    elif opsilogin == 3:
        print('\nTerima Kasih Sudah Berkunjung :).')
        exit()
    
    # Pilihan Tidak Valid

    else:
        print('\nPilihan Tidak Valid, Silahkan Pilih Opsi yang tersedia')

        input('\nTekan Enter Untuk Kembali...')

