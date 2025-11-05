from crud import dataparfum
from crud import list
from datetime import datetime

transaksi = 0
nama_terakhir = ''

def hitung_total(harga, jumlah):
    return harga * jumlah

def hitung_pajak(total, persen):
    persen = 5
    return total * persen / 100

def waktu():
    print(datetime.now())

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
        print(f'Tanggal Pembelian        : '), waktu()
        print('\nTerima Kasih Sudah Berbelanja!')
        input('\nTekan Enter Untuk Kembali...')
    else:
        print("\nNama Parfum Tidak Ditemukan")
        input('\nTekan Enter Untuk Kembali...')
