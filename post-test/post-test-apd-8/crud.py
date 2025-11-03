dataparfum = {}

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
    if len(dataparfum) == 0:
        print("\nParfum Belum Tersedia, Silahkan Pilih 1 Untuk Menambahkan Data.")
        input('\nTekan Enter Untuk Kembali...')
        return
    list()

    print('\n=== UPDATE DATA PARFUM ===')
    namasebelumnya = input('\nMasukkan Nama Parfum yang Ingin Diupdate: ')
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