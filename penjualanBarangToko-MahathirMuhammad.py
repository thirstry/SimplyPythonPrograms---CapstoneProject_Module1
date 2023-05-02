# Penjualan barang Toko Pak Aji

from prettytable import PrettyTable

sembako= {
    'Minyak goreng':[ 20, 20000,"Bimoli"],
    'Mie instan':[50, 3500,"Indomie"],
    'Gula':[30,15000,"Gulaku"]
}
peralatan_mandi= {
        'Odol':[30,10000,"Pepsodent"],
        'Shampoo':[25,25000,"Clear"],
        'Sabun mandi':[35, 20000,"Lux"]
}

def barangPrintInv() :
    print('Daftar Barang:')
    print('\nSembako:\n')
    tabel_sembako = PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
    for i in sembako:
        tabel_sembako.add_row([i, sembako[i][0], sembako[i][1], sembako[i][2]])
    print(tabel_sembako)

    print('\nPeralatan Mandi:\n')
    tabel_pmandi= PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
    for j in peralatan_mandi:
        tabel_pmandi.add_row([j,peralatan_mandi[j][0],peralatan_mandi[j][1],peralatan_mandi[j][2]])
    print(tabel_pmandi)

def pilihMenu():
    print('Pilihlah Menu yang mau ditampilkan')
    while True:
        pilihan=input('1. Sembako\n2. Peralatan Mandi\n')
        if pilihan == '1':
            tabel_sembako = PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
            for i in sembako:
                tabel_sembako.add_row([i, sembako[i][0], sembako[i][1], sembako[i][2]])
            print(tabel_sembako)
            break            

        elif pilihan =='2':
            tabel_pmandi= PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
            for j in peralatan_mandi:
                tabel_pmandi.add_row([j,peralatan_mandi[j][0],peralatan_mandi[j][1],peralatan_mandi[j][2]])
            print(tabel_pmandi)
            break
        
def sembakoSaja():
    tabel_sembako = PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
    for i in sembako:
        tabel_sembako.add_row([i, sembako[i][0], sembako[i][1], sembako[i][2]])
    print(tabel_sembako)

def pMandiSaja():
    tabel_pmandi= PrettyTable(['Nama Barang', 'stok', 'Harga', 'Merek'])
    for j in peralatan_mandi:
        tabel_pmandi.add_row([j,peralatan_mandi[j][0],peralatan_mandi[j][1],peralatan_mandi[j][2]])
    print(tabel_pmandi)

def errorIntMessage() :
    print('Masukan hanya angka!')

# APPS START

while True :

    print('''
Selamat Datang di Toko Pak Aji!

List Menu :
1. Menampilkan daftar barang yang ada di Toko Pak Aji
2. Menambah barang di Toko Pak Aji
3. Menghapus barang di Toko Pak Aji
4. Mengubah barang di Toko Pak Aji
5. Exit
''')
    try : # error handling untuk non int di menu
        menuInput = int(input('Masukan angka Menu yang ingin dijalankan :'))
        if menuInput == 1 :
            while True:
                Menu1 = input('''
1. Tampilkan seluruh barang yang tersedia
2. Tampilkan barang dengan jenis tertentu (sembako / peralatan mandi)
3. Kembali ke menu utama
Silahkan pilih sub-menu bagian daftar penjualan (1-3): ''')
                
                if Menu1 == '1': #cuman nampilin menu tabel doang
                    barangPrintInv()
                    continue
                elif Menu1 == '2':#nampilin menu pilihan doang
                    pilihMenu()
                    continue
                elif Menu1 =='3':#buat balik ke menu utama kalo ga mau
                    break
        elif menuInput == 2 : #cuman masukin ke dictionary doang
            barangPrintInv()
            while True :
                namabarang = input('Masukan nama barang : ')
                stokbarang= int(input('Masukan stok barang :'))
                hargabarang = int(input('Masukan harga barang :'))
                merekbarang = input('Masukkan merek barang :')
                print('1. Sembako \n2. Peralatan Mandi\n')
                jenisbarang= input('Masukan jenis Barang: ')
                if jenisbarang =='1':
                    sembako[namabarang]=stokbarang,hargabarang,merekbarang
                    print('Barang telah ditambahkan dalam tabel Sembako')
                    break
                elif jenisbarang =='2':
                    peralatan_mandi[namabarang]=stokbarang,hargabarang,merekbarang
                    print('Barang telah ditambahkan dalam tabel Peralatan Mandi')
                    break
                elif jenisbarang != '1' or jenisbarang !='2':
                    print('Masukkan nomor barang yang benar!')
        elif menuInput == 3 : #cmn delete key value
            while True :
                print('1. Sembako \n2. Peralatan Mandi\n')
                jenisbarang= input('Masukan nomor jenis barang yg mau dihapus:')
                if jenisbarang =='1':
                    sembakoSaja()               
                    hapusbarang = input('Masukan nama barang yang ingin di hapus :').capitalize()
                    del sembako[hapusbarang]
                    print('Barang telah terhapus')
                    break
                elif jenisbarang=='2':
                    pMandiSaja()
                    hapusbarang = input('Masukan nama barang yang ingin di hapus :').capitalize()
                    del peralatan_mandi[hapusbarang]
                    print('Barang telah terhapus')
                    break
        elif menuInput == 4 : #intinya dapetin inputan baru, abis itu timpa ke dictionary
            while True:
                print('1. Menambah/mengurang stok\n2. Mengubah Jumlah stok/harga/nama barang\n')
                pilihubah=input('Pilihlah nomor yang diinginkan: ')
                if pilihubah=='1':##buat nambah/kurang stok
                    print('1. Sembako\n2. Peralatan Mandi')
                    pilihjenis=input('Pilihlah jenis barang yang mau diubah: ')
                    if pilihjenis=='1':
                        sembakoSaja()
                        pilihbrg=input('Pilihlah nama barang yang ingin diubah: ').capitalize()
                        if pilihbrg in sembako: ##buat sembako
                            print('1. Menambah Stok\n2. Mengurangi Stok')
                            tmbhkrg=input('Pilihlah pilihan: ')
                            if tmbhkrg=='1':
                                tmbh=int(input('Masukkan jumlah tambahan barang: '))
                                stokbaru=int(sembako[pilihbrg][0])+tmbh
                                sembako[pilihbrg][0]=stokbaru
                                print('Stok telah berhasil tertambahkan sebagai berikut: ')
                                sembakoSaja()
                                break
                            elif tmbhkrg=='2':
                                krg=int(input('Masukkan jumlah barang yang ingin dikurangi: '))
                                stokbaru=int(sembako[pilihbrg][0])-krg
                                sembako[pilihbrg][0]=stokbaru
                                print('Stok telah berhasil terkurang sebagai berikut: ')
                                sembakoSaja()
                                break
                        else: ##ini kalo usernya iseng
                            print('Tolong masukkan nama yang benar!')                    
                    elif pilihjenis=='2':
                        pMandiSaja()
                        pilihbrg=input('Pilihlah nama barang yang ingin diubah: ').capitalize()
                        if pilihbrg in peralatan_mandi: ##alat mandi
                            print('1. Menambah Stok\n2. Mengurangi Stok')
                            tmbhkrg=input('Pilihlah pilihan: ')
                            if tmbhkrg=='1':
                                tmbh=int(input('Masukkan jumlah tambahan barang: '))
                                stokbaru=int(peralatan_mandi[pilihbrg][0])+tmbh
                                peralatan_mandi[pilihbrg][0]=stokbaru
                                print('Stok telah berhasil tertambahkan sebagai berikut: ')
                                pMandiSaja()
                                break
                            elif tmbhkrg=='2':
                                krg=int(input('Masukkan jumlah barang yang ingin dikurangi:'))
                                stokbaru=int(peralatan_mandi[pilihbrg][0])-krg
                                peralatan_mandi[pilihbrg][0]=stokbaru
                                print('Stok telah berhasil terkurang sebagai berikut: ')
                                pMandiSaja()
                                break
                        else:
                            print('Tolong masukkan nama yang benar!')   
                elif pilihubah=='2':
                    print('1. Sembako\n2. Peralatan Mandi')
                    pilihjenis=input('Masukkan nomor yang ingin diubah: ')
                    if pilihjenis =='1':
                        print('Berikut adalah menu untuk sembako: ')
                        sembakoSaja()
                        while True:
                            pilihnama=input('Masukkan nama barang yang ingin diubah: ').capitalize()
                            if pilihnama in sembako:
                                print('1. Ubah total stok\n2. Ubah Harga\n3. Ubah Merek barang')
                                ubahan=input('Pilihlah nomor pilihan yang inginkan: ')
                                if ubahan=='1':
                                    ubahstok=input('Masukkan stok baru: ')
                                    sembako[pilihnama][0]=ubahstok
                                    print('Berikut adalah daftar sembako yang baru: ')
                                    sembakoSaja()
                                    break
                                elif ubahan=='2':
                                    ubahharga=input('Masukkan harga baru: ')
                                    sembako[pilihnama][1]=ubahharga
                                    print('Berikut adalah daftar sembako yang baru: ')
                                    sembakoSaja()
                                    break
                                elif ubahan=='3':
                                    ubahmerek=input('Masukkan merek baru: ')
                                    sembako[pilihnama][2]=ubahmerek
                                    print('Berikut adalah daftar sembako yang baru: ')
                                    sembakoSaja()
                                    break
                            else:
                                print('Masukkan nama yang benar!')
                    elif pilihjenis=='2':
                        print('Berikut adalah menu untuk peralatan mandi: ')
                        pMandiSaja()
                        while True:
                            pilihnama=input('Masukkan nama barang yang ingin diubah: ').capitalize()
                            if pilihnama in peralatan_mandi:
                                print('1. Ubah total stok\n2. Ubah Harga\n3. Ubah Merek barang')
                                ubahan=input('Pilihlah nomor pilihan yang inginkan: ')
                                if ubahan=='1':
                                    ubahstok=input('Masukkan stok baru: ')
                                    peralatan_mandi[pilihnama][0]=ubahstok
                                    print('Berikut adalah daftar Peralatan Mandi yang baru: ')
                                    pMandiSaja()
                                    break
                                elif ubahan=='2':
                                    ubahharga=input('Masukkan harga baru: ')
                                    peralatan_mandi[pilihnama][1]=ubahharga
                                    print('Berikut adalah daftar Peralatan Mandi yang baru: ')
                                    pMandiSaja()
                                    break
                                elif ubahan=='3':
                                    ubahmerek=input('Masukkan merek baru: ')
                                    peralatan_mandi[pilihnama][2]=ubahmerek
                                    print('Berikut adalah daftar Peralatan Mandi yang baru: ')
                                    pMandiSaja()
                                    break
                            else:
                                print('Masukkan nama yang benar!')
                                            
                        



                    
                    
            # jenisubah=input('Pilihlah jenis barang yang mau diubah: ')
            #     if jenisubah=='1':
        elif menuInput == 5 :
            print('Program telah tertutup.')
            break # break untuk menu 5
    except ValueError : # error handling untuk nomor di menu
        errorIntMessage()