import os
os.system('cls')

dataparfum = {}

def tambah():
    while True:
        os.system('cls')
        print('\n=== TAMBAH DATA PARFUM ===')
        nama  = input('Nama Parfum: ')
        if not nama:
            print('\nNama Tidak Boleh Kosong!')
            input('\nTekan Enter Untuk Kembali...')
            continue

        aroma = input('Aroma Parfum: ')
        if not aroma:
            print('\nAroma Tidak Boleh Kosong!')
            input('\nTekan Enter Untuk Kembali...')
            continue

        try:
            harga = int(input('Harga Parfum: Rp. '))
            if not harga:
                print('\nHarga Tidak Boleh Kosong!')
                input('\nTekan Enter Untuk Kembali...')
                continue
        except ValueError:
            print('\nHarga Harus Berupa Angka!')
            input('\nTekan Enter Untuk Kembali...')
            continue

        dataparfum[nama] = {'Aroma': aroma, 'Harga': harga}
        print('\nData berhasil ditambahkan!')
        input('\nTekan Enter Untuk Kembali...')
        break

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
    if len(dataparfum) == 0:
        print("\nParfum Belum Tersedia, Silahkan Pilih 1 Untuk Menambahkan Data.")
        input('\nTekan Enter Untuk Kembali...')
        return
    list()
    namasebelumnya = input('\nMasukkan Nama Parfum yang Ingin Diupdate: ')
    if namasebelumnya in dataparfum:
        while True:
            os.system('cls')
            print('\n=== UPDATE DATA PARFUM ===')
            namabaru = input('Nama baru: ')
            if not namabaru:
                print('\nNama Tidak Boleh Kosong!')
                input('\nTekan Enter Untuk Kembali...')
                continue

            aromabaru = input('Aroma Parfum: ')
            if not aromabaru:
                print('\nAroma Tidak Boleh Kosong!')
                input('\nTekan Enter Untuk Kembali...')
                continue

            try:
                hargabaru = int(input('Harga Parfum: Rp. '))
                if not hargabaru:
                    print('\nHarga Tidak Boleh Kosong!')
                    input('\nTekan Enter Untuk Kembali...')
                    continue
            except ValueError:
                print('\nHarga Harus Berupa Angka!')
                input('\nTekan Enter Untuk Kembali...')
                continue
            dataparfum.pop(namasebelumnya)
            dataparfum[namabaru] = {'Aroma': aromabaru, 'Harga': hargabaru}
            print('\nData berhasil diupdate!')
            input('\nTekan Enter Untuk Kembali...')
            break
    else:
        print('\nData Tidak Ditemukan')
        input('\nTekan Enter Untuk Kembali...')

def hapus():
    if len(dataparfum) == 0:
        print("\nParfum Belum Tersedia, Silahkan Pilih 1 Untuk Menambahkan Data.")
        input('\nTekan Enter Untuk Kembali...')
        return
    list()
    print('\n=== HAPUS DATA PARFUM ===')
    hapusparfum = input('\nMasukkan Nama Parfum yang Ingin Dihapus: ')
    if hapusparfum in dataparfum:
        dataparfum.pop(hapusparfum)
        print('\nData berhasil dihapus!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        print('\nData Tidak Ditemukan')
        input('\nTekan Enter Untuk Kembali...')