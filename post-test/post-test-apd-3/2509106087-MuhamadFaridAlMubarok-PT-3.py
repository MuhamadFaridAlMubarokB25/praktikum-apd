# ariabel

nama = "Muhamad Farid Al Mubarok"
nim = "2509106087"
UKT = 6000000

# input nama dan nim

print()
print("=== Masukkan Nama dan NIM untuk Melanjutkan ke Opsi Pembayaran UKT ===")
print()
namapengguna = input("Masukkan nama lengkap: ")
nimpengguna = input("Masukkan NIM: ")

# proses login dan pembayaran UKT

if nama == namapengguna and nim == nimpengguna:
    print("Login berhasil, Silahkan lanjut Opsi Pembayaran")
    print()
    print("=== Pembayaran UKT ===")
    print()
    print("Total UKT adalah Rp", UKT)
    print()
    print(48*"—")
    print("| Opsi |   Metode Pembayaran   |  Biaya Admin  |")
    print(48*"—")
    print("| 1    |   Lunas               |  1%           |")
    print("| 2    |   Cicilan 2x          |  5%           |")
    print("| 3    |   Cicilan 4x          |  8%           |")
    print("| 4    |   Cicilan 6x          |  12%          |")
    print(48*"—")
    print()

    pembayaran = int(input("Masukkan opsi pembayaran : "))



    if pembayaran == 1:
        biaya_admin = UKT * 0.01
        total_bayar = UKT + biaya_admin
        print()
        print(f"Pembayaran Lunas dengan Total Rp{total_bayar} dengan biaya admin Rp{biaya_admin}")
        print()
    elif pembayaran == 2:
        biaya_admin = UKT * 0.05
        total_bayar = UKT + biaya_admin
        cicilan = total_bayar / 2
        print()
        print(f"Pembayaran Cicilan 2x dengan Total Rp{total_bayar} dengan biaya admin Rp{biaya_admin} per cicilan Rp{cicilan}")
        print()
    elif pembayaran == 3:
        biaya_admin = UKT * 0.08
        total_bayar = UKT + biaya_admin
        cicilan = total_bayar / 4
        print()
        print(f"Pembayaran Cicilan 4x dengan Total Rp{total_bayar} dengan biaya admin {biaya_admin} per cicilan {cicilan}")
        print()
    elif pembayaran == 4:
        biaya_admin = UKT * 0.12
        total_bayar = UKT + biaya_admin
        cicilan = total_bayar / 6
        print()
        print(f"Pembayaran Cicilan 2x dengan Total {total_bayar} dengan biaya admin {biaya_admin} per cicilan {cicilan}")
        print()
    else:
        print("Pembayaran tidak valid")
else:
    print("Login gagal")
