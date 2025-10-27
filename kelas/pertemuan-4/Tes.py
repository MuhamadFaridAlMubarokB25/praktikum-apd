import os
import sys

jenis_senjata = ("Rifle", "SMG", "Shotgun", "LMG", "Marksman Rifle", "Sniper Rifle", "Pistol", "Senjata khusus")

model_senjata = [
    ["M4A1", "AKM", "K416", "M7", "SG552", 'AK-12', 'SCAR-H', 'PTR-32', 'AS VAL', 'CI-19', 'K437', 'KC17'],  # Rifle
    ['MP5', 'P90', 'VECTOR', 'UZI', 'BIZON', 'SMG-45', 'SR-3M', 'VITYAZ', 'QCQ171', 'MP7'],  # SMG
    ['M1014', 'S12K', 'M870', '725 DOUBLE'],  # Shotgun
    ['PKM', 'M249', 'M250', 'QCB-201'],  # LMG
    ['MINI-14', 'VSS', 'SVD', 'M14', 'SKS', 'SR-25', 'SR-9', 'PSG-1', 'MARLIN LEVER'],  # Marksman
    ['SV-98', 'R93', 'M700', 'AWM'],  # Sniper
    ['M1911', 'DESERT EAGLE', 'QSZ-92G', 'G18', '93R', '357 REVOLVER'],  # Pistol
    ['COMPOUND BOW']  # Senjata khusus
]

# === Statistik tiap jenis ===
statistik_rifle = [
    ['Damage   : 42', 'Fire Rate: 750', 'Accuracy : 70', 'Mobility : 60', 'Range    : 600'],
    ['Damage   : 49', 'Fire Rate: 600', 'Accuracy : 65', 'Mobility : 55', 'Range    : 550'],
    ['Damage   : 45', 'Fire Rate: 700', 'Accuracy : 68', 'Mobility : 58', 'Range    : 580'],
    ['Damage   : 44', 'Fire Rate: 720', 'Accuracy : 69', 'Mobility : 59', 'Range    : 590'],
    ['Damage   : 46', 'Fire Rate: 680', 'Accuracy : 67', 'Mobility : 57', 'Range    : 570'],
    ['Damage   : 47', 'Fire Rate: 660', 'Accuracy : 66', 'Mobility : 56', 'Range    : 560'],
    ['Damage   : 48', 'Fire Rate: 640', 'Accuracy : 64', 'Mobility : 54', 'Range    : 540'],
    ['Damage   : 50', 'Fire Rate: 620', 'Accuracy : 63', 'Mobility : 53', 'Range    : 530'],
    ['Damage   : 43', 'Fire Rate: 730', 'Accuracy : 71', 'Mobility : 61', 'Range    : 610'],
    ['Damage   : 41', 'Fire Rate: 760', 'Accuracy : 72', 'Mobility : 62', 'Range    : 620'],
    ['Damage   : 44', 'Fire Rate: 710', 'Accuracy : 68', 'Mobility : 59', 'Range    : 590'],
    ['Damage   : 45', 'Fire Rate: 700', 'Accuracy : 67', 'Mobility : 58', 'Range    : 580'],
]

statistik_smg = [
    ['Damage   : 30', 'Fire Rate: 900', 'Accuracy : 60', 'Mobility : 80', 'Range    : 300'],
    ['Damage   : 28', 'Fire Rate: 950', 'Accuracy : 58', 'Mobility : 82', 'Range    : 280'],
    ['Damage   : 32', 'Fire Rate: 850', 'Accuracy : 62', 'Mobility : 78', 'Range    : 320'],
    ['Damage   : 29', 'Fire Rate: 920', 'Accuracy : 59', 'Mobility : 81', 'Range    : 290'],
    ['Damage   : 27', 'Fire Rate: 970', 'Accuracy : 57', 'Mobility : 83', 'Range    : 270'],
    ['Damage   : 31', 'Fire Rate: 880', 'Accuracy : 61', 'Mobility : 79', 'Range    : 310'],
    ['Damage   : 33', 'Fire Rate: 840', 'Accuracy : 63', 'Mobility : 77', 'Range    : 330'],
    ['Damage   : 26', 'Fire Rate: 980', 'Accuracy : 56', 'Mobility : 84', 'Range    : 260'],
    ['Damage   : 34', 'Fire Rate: 830', 'Accuracy : 64', 'Mobility : 76', 'Range    : 340'],
    ['Damage   : 25', 'Fire Rate: 990', 'Accuracy : 55', 'Mobility : 85', 'Range    : 250'],
]

statistik_shotgun = [
    ['Damage   : 70', 'Fire Rate: 300', 'Accuracy : 50', 'Mobility : 40', 'Range    : 100'],
    ['Damage   : 75', 'Fire Rate: 280', 'Accuracy : 48', 'Mobility : 38', 'Range    : 90'],
    ['Damage   : 80', 'Fire Rate: 260', 'Accuracy : 46', 'Mobility : 36', 'Range    : 80'],
    ['Damage   : 85', 'Fire Rate: 240', 'Accuracy : 44', 'Mobility : 34', 'Range    : 70'],
]

statistik_lmg = [
    ['Damage   : 55', 'Fire Rate: 600', 'Accuracy : 60', 'Mobility : 50', 'Range    : 400'],
    ['Damage   : 50', 'Fire Rate: 650', 'Accuracy : 58', 'Mobility : 52', 'Range    : 380'],
    ['Damage   : 52', 'Fire Rate: 620', 'Accuracy : 59', 'Mobility : 51', 'Range    : 390'],
    ['Damage   : 54', 'Fire Rate: 610', 'Accuracy : 57', 'Mobility : 53', 'Range    : 370'],
]

statistik_marksman = [
    ['Damage   : 60', 'Fire Rate: 500', 'Accuracy : 75', 'Mobility : 45', 'Range    : 500'],
    ['Damage   : 58', 'Fire Rate: 520', 'Accuracy : 77', 'Mobility : 44', 'Range    : 520'],
    ['Damage   : 65', 'Fire Rate: 480', 'Accuracy : 80', 'Mobility : 43', 'Range    : 550'],
    ['Damage   : 62', 'Fire Rate: 510', 'Accuracy : 76', 'Mobility : 46', 'Range    : 510'],
    ['Damage   : 59', 'Fire Rate: 530', 'Accuracy : 78', 'Mobility : 44', 'Range    : 530'],
    ['Damage   : 64', 'Fire Rate: 490', 'Accuracy : 79', 'Mobility : 45', 'Range    : 540'],
    ['Damage   : 61', 'Fire Rate: 505', 'Accuracy : 74', 'Mobility : 46', 'Range    : 505'],
    ['Damage   : 66', 'Fire Rate: 475', 'Accuracy : 81', 'Mobility : 42', 'Range    : 560'],
    ['Damage   : 63', 'Fire Rate: 495', 'Accuracy : 73', 'Mobility : 47', 'Range    : 495'],
]

statistik_sniper = [
    ['Damage   : 90', 'Fire Rate: 200', 'Accuracy : 90', 'Mobility : 30', 'Range    : 800'],
    ['Damage   : 95', 'Fire Rate: 180', 'Accuracy : 92', 'Mobility : 28', 'Range    : 850'],
    ['Damage   : 100', 'Fire Rate: 160', 'Accuracy : 94', 'Mobility : 27', 'Range    : 900'],
    ['Damage   : 110', 'Fire Rate: 150', 'Accuracy : 95', 'Mobility : 25', 'Range    : 950'],
]

statistik_pistol = [
    ['Damage   : 35', 'Fire Rate: 400', 'Accuracy : 65', 'Mobility : 70', 'Range    : 200'],
    ['Damage   : 45', 'Fire Rate: 350', 'Accuracy : 60', 'Mobility : 68', 'Range    : 180'],
    ['Damage   : 33', 'Fire Rate: 420', 'Accuracy : 66', 'Mobility : 72', 'Range    : 210'],
    ['Damage   : 30', 'Fire Rate: 450', 'Accuracy : 67', 'Mobility : 73', 'Range    : 220'],
    ['Damage   : 28', 'Fire Rate: 480', 'Accuracy : 68', 'Mobility : 74', 'Range    : 230'],
    ['Damage   : 50', 'Fire Rate: 300', 'Accuracy : 55', 'Mobility : 65', 'Range    : 170'],
]

statistik_khusus = [
    ['Damage   : 25', 'Fire Rate: 100', 'Accuracy : 85', 'Mobility : 90', 'Range    : 150'],
]

semua_statistik = [statistik_rifle, statistik_smg, statistik_shotgun, statistik_lmg, statistik_marksman, statistik_sniper, statistik_pistol, statistik_khusus]

# === Rekomendasi ===
rekomendasi_list = [
    ['M4A1', 'AKM', 'K416'],
    ['MP5', 'P90', 'VECTOR'],
    ['M1014', 'S12K'],
    ['PKM', 'M249'],
    ['MINI-14', 'VSS'],
    ['SV-98', 'R93'],
    ['M1911', 'DESERT EAGLE'],
    ['COMPOUND BOW']
]
data_user = [
    ["Aditya", "2202", "admin"],
    ["ForReal", "1608", "user"]
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LOGIN DELTA FORCE ARMORY ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih_login = input("Pilih menu (1-3): ")

    if pilih_login == '1':
        username = input("Username: ")
        password = input("Password: ")
        status = ""

        for data in data_user:
            if data[0] == username and data[1] == password:
                status = data[2]
                break

        if status == "":
            print("Username atau password salah!")
            input("Enter untuk ulang")
        else:
            print(f"Login berhasil sebagai {status}!")
            input("Enter untuk lanjut")

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== Delta Force Armory ===")
                print("1. Rekomendasi Senjata")
                print("2. Update Rekomendasi Senjata")
                print("3. Kelola Model & Statistik Senjata")
                print("4. Keluar")
                menu = input("Pilih opsi (1-4): ")


                if menu == '1':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('=== REKOMENDASI SENJATA ===')
                        for i in range(len(jenis_senjata)):
                            print(str(i+1) + ". " + jenis_senjata[i])
                        print(str(len(jenis_senjata)+1) + ". Kembali ke menu utama")
                        pilih_jenis = int(input("Pilih jenis senjata: ")) - 1

                        if pilih_jenis == len(jenis_senjata):
                            break

                        elif pilih_jenis < len(jenis_senjata):
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("=== Rekomendasi " + jenis_senjata[pilih_jenis] + " ===")
                                for j in range(len(rekomendasi_list[pilih_jenis])):
                                    print(str(j+1) + ". " + rekomendasi_list[pilih_jenis][j])
                                print(str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali")

                                pilih_model = int(input("Pilih senjata untuk lihat statistik: ")) - 1
                                if pilih_model == len(rekomendasi_list[pilih_jenis]):
                                    break
                                elif pilih_model < len(rekomendasi_list[pilih_jenis]):
                                    nama_senjata = rekomendasi_list[pilih_jenis][pilih_model]
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("=== Statistik Senjata", nama_senjata, "===")
                                    if nama_senjata in model_senjata[pilih_jenis]:
                                        index = model_senjata[pilih_jenis].index(nama_senjata)
                                        statistik = semua_statistik[pilih_jenis][index]
                                        for s in statistik:
                                            print(s)
                                        input("\nEnter untuk kembali")
                                    else:
                                        print("Statistik tidak ditemukan.")
                                        input("\nEnter untuk kembali")
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Pilihan tidak valid!")
                                    input("\nEnter untuk ulangi")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Pilihan tidak valid!")
                            input("\nEnter untuk ulangi")


                elif menu == '2':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== KELOLA REKOMENDASI SENJATA ===")
                        print("1. Tambah Rekomendasi Senjata")
                        print("2. Hapus Rekomendasi Senjata")
                        print("3. Kembali")
                        pilih = input("Pilih opsi: ")

                        if pilih == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== TAMBAH REKOMENDASI SENJATA ===")
                            for i in range(len(jenis_senjata)):
                                print(str(i+1) + ". " + jenis_senjata[i])
                            print(str(len(jenis_senjata)+1) + ". Kembali")
                            pilih_jenis = int(input("Pilih jenis: ")) - 1

                            if pilih_jenis == len(jenis_senjata):
                                continue

                            elif pilih_jenis < len(jenis_senjata):
                                baru = input("Masukkan nama senjata yang direkomendasikan: ").upper()
                                rekomendasi_list[pilih_jenis].append(baru)
                                print("Berhasil menambahkan rekomendasi baru!")
                                input("Enter untuk lanjut")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Pilihan tidak valid!")
                                input("Enter untuk ulangi")

                        elif pilih == '2':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== HAPUS REKOMENDASI SENJATA ===")
                            for i in range(len(jenis_senjata)):
                                print(str(i+1) + ". " + jenis_senjata[i])
                            print(str(len(jenis_senjata)+1) + ". Kembali")
                            pilih_jenis = int(input("Pilih jenis: ")) - 1  

                            if pilih_jenis == len(jenis_senjata):
                                continue
                            
                            elif pilih_jenis < len(jenis_senjata):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Rekomendasi " + jenis_senjata[pilih_jenis] + ":")
                                for j in range(len(rekomendasi_list[pilih_jenis])):
                                    print(str(j+1) + ". " + rekomendasi_list[pilih_jenis][j])
                                hapus = int(input("Pilih yang ingin dihapus: ")) - 1
                                if hapus < len(rekomendasi_list[pilih_jenis]):
                                    print(f"{rekomendasi_list[pilih_jenis].pop(hapus)} dihapus dari rekomendasi.")
                                    input("Enter untuk lanjut")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Pilihan tidak valid!")
                                input("Enter untuk ulangi")

                        elif pilih == '3':
                            break
                    
                        else:
                            print("Pilihan tidak valid!")
                            input("Enter untuk ulangi")

                elif menu == '3':
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== KELOLA MODEL & STATISTIK SENJATA ===")
                        print("1. Tambah Model + Statistik Baru")
                        print("2. Hapus Model + Statistik")
                        print("3. Update Statistik (Buff/Nerf)")
                        print("4. Kembali")
                        pilih = input("Pilih opsi: ")

                        if pilih == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== TAMBAH MODEL + STATISTIK ===")
                            for i in range(len(jenis_senjata)):
                                print(str(i+1)+". "+jenis_senjata[i])
                            print(str(len(jenis_senjata)+1)+". Kembali")
                            jenis = int(input("Pilih jenis: ")) - 1

                            if jenis == len(jenis_senjata):
                                continue

                            nama = input("Nama senjata baru: ").upper()
                            dmg = input("Damage   : ")
                            rate = input("Fire Rate: ")
                            acc = input("Accuracy : ")
                            mob = input("Mobility : ")
                            rng = input("Range    : ")
                            model_senjata[jenis].append(nama)
                            semua_statistik[jenis].append([
                                f"Damage   : {dmg}",
                                f"Fire Rate: {rate}",
                                f"Accuracy : {acc}",
                                f"Mobility : {mob}",
                                f"Range    : {rng}"
                            ])
                            print("Model & statistik baru ditambahkan!")
                            input("Enter untuk lanjut")

                        elif pilih == '2':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== HAPUS MODEL + STATISTIK ===")
                            for i in range(len(jenis_senjata)):
                                print(str(i+1)+". "+jenis_senjata[i])
                            print(str(len(jenis_senjata)+1)+". Kembali")
                            jenis = int(input("Pilih jenis: ")) - 1

                            if jenis == len(jenis_senjata): 
                                continue

                            for j in range(len(model_senjata[jenis])):
                                print(str(j+1)+". "+model_senjata[jenis][j])
                            hapus = int(input("Pilih yang dihapus: ")) - 1

                            if hapus < len(model_senjata[jenis]):
                                model_senjata[jenis].pop(hapus)
                                semua_statistik[jenis].pop(hapus)
                                print("Model & statistik berhasil dihapus!")
                            input("Enter untuk lanjut")

                        elif pilih == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("=== UPDATE STATISTIK (BUFF/NERF) ===")
                            for i in range(len(jenis_senjata)):
                                print(str(i+1)+". "+jenis_senjata[i])
                            print(str(len(jenis_senjata)+1)+". Kembali")
                            jenis = int(input("Pilih jenis: ")) - 1

                            if jenis == len(jenis_senjata): 
                                continue

                            for j in range(len(model_senjata[jenis])):
                                print(str(j+1)+". "+model_senjata[jenis][j])
                            pilih_model = int(input("Pilih model: ")) - 1

                            if pilih_model < len(model_senjata[jenis]):
                                dmg = input("Damage baru   : ")
                                rate = input("Fire Rate baru: ")
                                acc = input("Accuracy baru : ")
                                mob = input("Mobility baru : ")
                                rng = input("Range baru    : ")
                                semua_statistik[jenis][pilih_model] = [
                                    f"Damage   : {dmg}",
                                    f"Fire Rate: {rate}",
                                    f"Accuracy : {acc}",
                                    f"Mobility : {mob}",
                                    f"Range    : {rng}"
                                ]
                                print("Statistik berhasil diperbarui!")
                            input("Enter untuk lanjut")

                        elif pilih == '4':
                            break
                        else:
                            print("Pilihan tidak valid!")
                            input("Enter untuk ulangi")

                elif menu == '4':
                    print("Terima kasih dan sampai jumpa lagi!")
                    sys.exit()

                else:
                    print("Pilihan tidak valid!")
                    input("Enter untuk ulangi")
    
    elif pilih_login == '2':
        username = input("Buat username baru: ")
        password = input("Buat password baru: ")

        duplikat = False
        for user in data_user:
            if user[0] == username:
                duplikat = True
                break
        if duplikat:
            print("Username sudah digunakan!")
        else:
            data_user.append([username, password, "user"])
            print("Akun berhasil dibuat! Silakan login.")
        input("Enter untuk lanjut")

    elif pilih_login == '3':
        print("Yahh, gak jadi mampir :(")
        sys.exit()

    else:
        print("Input tidak valid!")
        input("Enter untuk ulang")