# Variabel

username = "Muhamad Farid Al Mubarok"
password = "2509106087"
maksimal_percobaan = 3
percobaan = 0

# Validasi Login

print()
print('Selamat Datang di Toko Furnitur Infordeh')
print('Silahkan Masukkan Username dan Password untuk Melanjutkan Furnitur Furnitur')
print()

while percobaan < maksimal_percobaan:
    usernameinput = input('Masukkan Username: ')
    passwordinput = input('Masukkan Password: ')
    if username == usernameinput and password == passwordinput:
        print()
        print('Login Berhasil, Silahkan Melanjutkan Pembelian Furnitur')
        print()
        

# Pembelian Furnitur

        opsi = True
        while opsi == True:
            print('Daftar Furnitur Toko Infordeh')
            print()
            print(46*"—")
            print("| Opsi |   Furnitur       |  Harga Per Unit  |")
            print(46*"—")
            print("| 1    |   Sofa           |  Rp.500.000      |")
            print("| 2    |   Meja Belajar   |  Rp.250.000      |")
            print("| 3    |   Rak Lemari     |  Rp.150.000      |")
            print(46*"—")
            print('Ketentuan:')
            print('1. Pilih Opsi 4 untuk membatalkan pembelian.')
            print("2. Jika Total bayar mencapai Rp.700.000 atau lebih, Anda mendapatkan diskon 20%.")
            print("3. Jika Total bayar mencapai Rp.500.000 atau Rp.699.000, Anda mendapatkan diskon 8%.")
            print('4. Jika Total bayar mencapai Rp.150.000 sampai Rp.499.000, Anda mendapatkan Kitchen Set.')
            print()
            opsi = int(input('Masukan opsi: '))
            if opsi == 1:
                furnitur = 'Sofa'
                jumlah_unit = int(input('Masukkan Jumlah Furnitur: '))
                harga = 500000

                total = 0
                for i in range(jumlah_unit):
                    total += harga
                if total >= 700000:
                    total_bayar = total - (0.20 * total)
                    diskon = '20%'
                elif total >= 500000 and total < 700000:
                    total_bayar = total - (0.08 * total)
                    diskon = '10%'
                else:
                    total >= 150000 and total < 500000
                    diskon = 'kitchen set'
                print()
                print('Terima Kasih Telah Berbelanja di Toko Furnitur Infordeh')
                print(20*"_")
                print()
                print('Struk Pembayaran')
                print('Jenis Furnitur:', furnitur)
                print('Jumlah Unit:', jumlah_unit)
                print('Total Harga: Rp.', total_bayar)
                print('Diskon/Bonus:', diskon)
                print(20*"_")
                print()
            elif opsi == 2:
                furnitur = 'Meja Belajar'
                jumlah_unit = int(input('Masukkan Jumlah Furnitur: '))
                harga = 250000
                
                total = 0
                for i in range(jumlah_unit):
                    total += harga
                if total >= 700000:
                    total_bayar = total - (0.20 * total)
                    diskon = '20%'
                elif total >= 500000 and total < 700000:
                    total_bayar = total - (0.08 * total)
                    diskon = '10%'
                else:
                    total >= 150000 and total < 500000
                    diskon = 'kitchen set'
                print()
                print('Terima Kasih Telah Berbelanja di Toko Furnitur Infordeh')
                print(20*"_")
                print()
                print('Struk Pembayaran')
                print('Jenis Furnitur:', furnitur)
                print('Jumlah Unit:', jumlah_unit)
                print('Total Harga: Rp.', total_bayar)
                print('Diskon/Bonus:', diskon)
                print(20*"_")
                print()
            elif opsi == 3:
                furnitur = 'Rak Lemari'
                jumlah_unit = int(input('Masukkan Jumlah Furnitur: '))
                harga = 150000
                
                total = 0
                for i in range(jumlah_unit):
                    total += harga
                if total >= 700000:
                    total_bayar = total - (0.20 * total)
                    diskon = '20%'
                elif total >= 500000 and total < 700000:
                    total_bayar = total - (0.08 * total)
                    diskon = '10%'
                else:
                    total >= 150000 and total < 500000
                    diskon = 'kitchen set'
                print()
                print('Terima Kasih Telah Berbelanja di Toko Furnitur Infordeh')
                print(20*"_")
                print()
                print('Struk Pembayaran')
                print('Jenis Furnitur:', furnitur)
                print('Jumlah Unit:', jumlah_unit)
                print('Total Harga: Rp.', total)
                print('Diskon/Bonus:', diskon)
                print(20*"_")
                print()
            elif opsi == 4:
                print()
                print('Anda Membatalkan Pembelian')
                print()
                opsi = False
            else:
                print('Opsi Tidak Tersedia, Silahkan Pilih Opsi yang Tersedia')
                break
    else:
        percobaan += 1
        sisa_percobaan = maksimal_percobaan - percobaan
        if sisa_percobaan > 0:
            print()
            print('Username atau Password Salah. Sisa Percobaan:', sisa_percobaan)
            print()
        else:
            sisa_percobaan == 0
            print()
            print('Percobaan Anda Habis. Silahkan Coba Lagi Nanti')
            print()
            break

