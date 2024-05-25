import os # untuk mengimport package os

pesan = True 
pesanan = [] # untuk menyimpan daftar pesanan

while pesan:
    try: # konsep nya sama try and catch untuk mencegah error
        if not pesanan: # jika belum ada pesanan 
            os.system("clear")#untuk clear terminal(bash/unix)

            print("Selamat Datang di Rumah Makan Nasi Padang")
            print()
            print("Mau Pesan Apa?")
            print()
            print("1.Pesan Makanan")
            print("2.Pesan Minuman")
            print("3.Lihat Pesanan")
            print("0.Keluar")
            print()

        else:
            os.system("clear")
            print("Mau Tambah Apa?")
            print("1.Tambah Makanan")
            print("2.Tambah Minuman")
            print("3.Lihat Pesanan")
            print("4.Ubah Pesanan")
            print("5.Check Out")
            print("0.Keluar")
            print()

        pilihan = int(input("Pilih : "))

    except ValueError:
        os.system("clear")

        print("Error: Pilihan tidak tersedia")
        print()#ini untuk spasi
        print("Tekan Enter untuk melanjutkan")
        input() #untuk enter