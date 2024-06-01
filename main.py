import os # untuk mengimport package os

pesan = True 
pesanan = [] # untuk menyimpan daftar pesanan

def daftar_pesanan():
    print('No   Item     Jumlah        Harga')
    for i in range(len(pesanan)):
        print(f'{i + 1}.    {pesanan[i][0]}     {pesanan[i][1]}x        {pesanan[i][2]}')

while pesan:
    try: # konsep nya sama try and catch untuk mencegah error
        if not pesanan: # jika belum ada pesanan 
            os.system("clear") # untuk clear terminal(bash/unix)

            print("Selamat Datang di Rumah Makan Nasi Padang\n")
            
            print("Mau Pesan Apa?")
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

        if pilihan == 1:
            os.system('clear')

            print('Pilih lauk: ')
            print('1. Ayam Goreng (Rp. 10.000,00)')
            print('2. Ayam Bakar (Rp. 10.000,00)')
            print('3. Rendang (Rp. 12.000,00)')
            print('4. Perkedel (Rp. 8.000,00)')
            print('5. Nasi (Rp. 3.000,00)')
            print('6. Telor Dadar (Rp. 9.000,00)')
            print('7. Ayam Gulai (Rp. 11.000,00)')
            print('0. Keluar')
            print()

            pilihan = int(input('Pilih: '))

            if pilihan in range(1, 8):
                if pilihan == 1:
                    item = 'Ayam Goreng'
                    harga = 10000
                elif pilihan == 2:
                    item = 'Ayam Bakar'
                    harga = 10000
                elif pilihan == 3:
                    item = 'Rendang'
                    harga = 12000
                elif pilihan == 4:
                    item = 'Perkedel'
                    harga = 8000
                elif pilihan == 5:
                    item = 'Nasi'
                    harga = 3000
                elif pilihan == 6:
                    item = 'Telor Dadar'
                    harga = 9000
                elif pilihan == 7:
                    item = 'Ayam Gulai'
                    harga = 11000


                jumlah = abs(int(input('Jumlah: ')))
                pesanan.append([item, jumlah, harga * jumlah])
        elif pilihan == 2:
            os.system('clear')

            print('Pilih minuman:')
            print('1. Air putih (Gratis)')
            print('2. Teh Manis (Rp. 5.000,00)')
            print('3. Jeruk Manis (Rp. 7.000,00)')
            print('0. Kembali')
            print()

            pilihan = int(input('Pilih: '))

            if pilihan in range(1, 4):
                if pilihan == 1:
                    item = 'Air Putih'
                    harga = 0
                elif pilihan == 2:
                    item = 'Teh Manis'
                    harga = 5000
                elif pilihan == 3:
                    item = 'Jeruk Manis'
                    harga = 7000
                
                jumlah = abs(int(input('Jumlah: ')))
                pesanan.append([item, jumlah, harga * jumlah])
        elif pilihan == 3:
            os.system('clear')

            print('Rincian Pesanan\n')
            
            daftar_pesanan()

            print('\nTekan Enter untuk melanjutkan.')
            input()
        elif pilihan == 4 and pesanan:
            os.system('clear')

            print('Ubah Pesanan\n')
            
            daftar_pesanan()

            print()
            print('0. Kembali')

            print()
            pilihan = int(input('Pilih pesanan yang mau diubah jumlahnya: ')) - 1

            if pilihan in range(len(pesanan)):
                harga_item = pesanan[pilihan][2] // pesanan[pilihan][1]
                jumlah = abs(int(input('Jumlah (Masukkan 0 untuk menghapus pesanan): ')))
                
                if jumlah == 0:
                    pesanan.pop(pilihan)
                else:
                    harga = jumlah * harga_item
                    
                    pesanan[pilihan][1] = jumlah
                    pesanan[pilihan][2] = harga
            elif pilihan == 0:
                print()
            else:
                print('\nPesanan tidak ditemukan.')
                print('\nTekan Enter untuk melanjutkan.')
                input()
        elif pilihan == 5 and pesanan:
            os.system('clear')
            print('Checkout Pesanan')
        
            daftar_pesanan()

            print()
            print('Selesaikan pesanan?')
            print('1. Ya')
            print('2. Tidak')

            pilihan = int(input('Pilihan: ')) 

            if pilihan == 1:
                exit() 
        elif pilihan == 0:
            if pesanan:
                os.system('clear')
            
                print('Selesaikan pesanan? Kamu mempunyai barang di keranjang.')
                print('1. Ya')
                print('2. Tidak')

                pilihan = int(input('Pilihan: '))

                if pilihan == 1:
                    exit()
            else:
                exit() 

    except ValueError:
        os.system("clear")

        print("Error: Pilihan tidak tersedia")
        print() # ini untuk spasi
        print("Tekan Enter untuk melanjutkan")
        input() # untuk enter
