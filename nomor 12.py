listbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("Daftar harga buah")
print (listbuah)
while (status == True):
    print ("Menu pilihan : ")
    print ("A. Beli buah")
    print ("B. Tambah daftar harga")
    print ("C. Hapus buah dari daftar")
    print ("D. Selesai")
    pilihan = input ("Pilihan Anda (A,B,C,D) : ")
    print() 
    harga = []
    if (pilihan == 'A' or pilihan == 'a'):
        while True :
            beli = input ("Nama buah yang ingin dibeli : ")
            if (beli in listbuah):
                try:
                    jmlkilo = int(input("jumlah kilogram             : "))
                    harga1 = jmlkilo * listbuah[beli]
                    harga.append(harga1)
                    konfirmasi = input("\nIngin beli buah lagi? (y/n) : ")
                    if (konfirmasi != 'y'):
                        print("-------------------------------")
                        print("Total harga                 : Rp", sum(harga), "\n")
                        break    
                except (ValueError):
                    print ("Masukkan jumlah kilogram yang valid")
            
            elif (beli == '') or (beli not in listbuah):
                print ("Buah yang ingin Anda beli tidak ada di daftar")
            
    elif (pilihan == 'B' or pilihan =='b'):
        j = True
        while (j == True) :
            buah_baru = input ("Masukkan nama buah baru yang ingin dijual :")
            if (buah_baru in listbuah):
                print (buah_baru, "sudah ada dalam daftar")
            elif (buah_baru not in listbuah):    
                try:
                    harga_baru = int ( input ("Harga per kilogram : Rp"))
                    listbuah[buah_baru] = harga_baru
                    print (buah_baru, "berhasil ditambahkan\n")
                    print ("Daftar harga saat ini \n")
                    for data in listbuah:
                        print (data, "( Harga Rp",buah.get(data),")")
                        j = False
                    print()
                except (ValueError):
                    print ("Masukkan harga yang valid")
    elif (pilihan == 'C' or pilihan =='c'):
        i = True
        while (i == True):
            hapus = input ("Ketikkan nama buah yang akan dihapus : ")
            if (hapus not in listbuah):
                print ("Buah", hapus, "tidak ada dalam daftar")
            elif (hapus in listbuah):
                del listbuah[hapus]
                print (hapus, "telah dihapus dari daftar\n")
                print ("Daftar harga saat ini\n")
                for data in listbuah:
                        print (data, "( Harga Rp",listbuah.get(data),")")
                i = False
    elif (pilihan == 'D' or pilihan =='d'):
        break
