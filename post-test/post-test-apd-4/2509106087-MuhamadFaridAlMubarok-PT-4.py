# Variabel

username = "Muhamad Farid Al Mubarok"
password = "2509106087"
maksimal_percobaan = 3
percobaan = 0

# Validasi Login

while percobaan < maksimal_percobaan:
    print()
    print('=== Selamat Datang di Toko Furnitur Infordeh ===')
    print('=== Silahkan Masukkan Username dan Password untuk Melanjutkan Pembelian Furnitur ===')
    print()
    usernameinput = input('Masukkan Username: ')
    passwordinput = input('Masukkan Password: ')
    if username == usernameinput and password == passwordinput:
        print()
        print('Login Berhasil, Silahkan Melanjutkan Pembelian Furnitur')
        print()
        print('=== Daftar Furnitur Toko Infordeh ===')
        print()
        print(46*"—")
        print("| Opsi |   Furnitur       |  Harga Per Unit  |")
        print(46*"—")
        print("| 1    |   Sofa           |  Rp.500.000      |")
        print("| 2    |   Meja Belajar   |  Rp.250.000      |")
        print("| 3    |   Rak Lemari     |  Rp.150.000      |")
        print(46*"—")
        print('''Ketentuan:
        1. Jika Sudah Memilih Furnitur, Pilih Opsi 4 untuk Melanjutkan ke Pembayaran''')

        while True:
            opsi = (input('Masukkan Opsi:'))
            if opsi == 1:
                jumlah = int(input('Masukkan Jumlah Pembelian: '))
                harga = 500000
                total = harga * jumlah
                print(f'Anda Memilih Sofa Sebanyak {jumlah} dengan Total Harga Rp.{total}')
        

    else:
        percobaan += 1
        sisa_percobaan = maksimal_percobaan - percobaan
        print('Username atau Password Salah. Percobaan Tersisa:', sisa_percobaan)
        if sisa_percobaan > 0:
            print('Username atau Password Salah. Sisa Percobaan:', sisa_percobaan)
        else:
            sisa_percobaan == 0
            print('Percobaan Anda Habis. Silahkan Coba Lagi Nanti')
            break

