import os # untuk mengimport package/modul os
import qrcode #untuk menampilkan qrcode
import numpy as np #untuk menghitung ascii



pesan = True # membuat variabel pesan menjadi true
pesanan = [] # untuk menyimpan daftar pesanan

def daftar_pesanan():
    print('No   Item     Jumlah        Harga')
    for i in range(len(pesanan)):
        print(f'{i + 1}.    {pesanan[i][0]}     {pesanan[i][1]}x        {pesanan[i][2]}')

    total_harga = 0

    for i in range(len(pesanan)):
        total_harga = total_harga + pesanan[i][2]

    print('\nTotal harga:', total_harga)

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

        pilihan = int(input("Pilih (berupa angka): "))
#
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

            pilihan = int(input('Pilih (berupa angka): '))

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
                elif pilihan == 0:
                    print()
                
                if pilihan:
                    jumlah = abs(int(input('Jumlah: ')))

                    if jumlah > 0:
                        pesanan.append([item, jumlah, harga * jumlah])
        elif pilihan == 2:
            os.system('clear')

            print('Pilih minuman:')
            print('1. Air putih (Gratis)')
            print('2. Teh Manis (Rp. 5.000,00)')
            print('3. Jeruk Manis (Rp. 7.000,00)')
            print('0. Kembali')
            print()

            pilihan = int(input('Pilih (berupa angka): '))

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
                elif pilihan == 0:
                    print()
                
                if pilihan:
                    jumlah = abs(int(input('Jumlah: ')))

                    if jumlah > 0:
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

            print('\n0. Kembali\n')
            
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
            elif pilihan == -1:
                print()
            else:
                print('\nPesanan tidak ditemukan.')
                print('\nTekan Enter untuk melanjutkan.')
                input()
        elif pilihan == 5 and pesanan:
            os.system('clear')

            print('Checkout Pesanan\n')
        
            daftar_pesanan()

            print('\nMetode pembayaran:')
            print('1. Cash')
            print('2. Non Cash(Dana)'),
            print('0. Kembali')
            print()

            pilihan = int(input('Pilih (berupa angka): '))

            if pilihan == 1:
                print('\nTerima kasih atas kunjungannya.')
                exit()
            elif pilihan == 2:
                print("\n")
                # Link yang akan dijadikan barcode
                link = "https://qr.dana.id/v1/281012012023033112307249"

                # Buat QR code dengan ukuran yang lebih kecil
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=1,
                    border=1,
                )
                qr.add_data(link)
                qr.make(fit=True)

                # Buat gambar QR code
                img = qr.make_image(fill_color="black", back_color="white")

                # Konversi gambar ke numpy array
                img_array = np.array(img)

                # Konversi ke bentuk ASCII
                ascii_art = []
                for i in range(0, len(img_array), 2):
                    upper_row = img_array[i]
                    lower_row = img_array[i + 1] if i + 1 < len(img_array) else np.zeros_like(upper_row)
                    ascii_row = ""
                    for upper_pixel, lower_pixel in zip(upper_row, lower_row):
                        if upper_pixel and lower_pixel:
                            ascii_row += "█"  # Full block
                        elif upper_pixel and not lower_pixel:
                            ascii_row += "▀"  # Upper half block
                        elif not upper_pixel and lower_pixel:
                            ascii_row += "▄"  # Lower half block
                        else:
                            ascii_row += " "  # Space
                    ascii_art.append(ascii_row)

                # Gabungkan baris-baris ASCII
                ascii_art_str = "\n".join(ascii_art)

                # Cetak QR code di terminal
                print(ascii_art_str)

                print('\nTekan Enter untuk melanjutkan.')
                input()

                os.system("clear")
                print('\nTerima kasih atas kunjungannya.')
                exit()
        elif pilihan == 0:
            if pesanan:
                os.system('clear')
            
                print('Yakin mau keluar? Kamu mempunyai barang di keranjang.')
                print('1. Ya')
                print('2. Tidak')

                pilihan = int(input('Pilih (berupa angka): '))

                if pilihan == 1:
                    print('\nTerima kasih atas kunjungannya.')
                    exit()
            else:
                print('\nTerima kasih atas kunjungannya.')
                exit() 

    except ValueError:
        os.system("clear")

        print("Error: Pilihan tidak tersedia\n") # \n untuk spasi
        print("Tekan Enter untuk melanjutkan")
        input() # untuk enter
