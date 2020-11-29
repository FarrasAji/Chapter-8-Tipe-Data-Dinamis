listbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("Daftar harga buah per kilogram")
print (listbuah, "\n")
while (status == True):
    print ("Menu :\nA. Beli buah \nB. Tambah daftar harga buah \nC. Selesai")
    pilihan = input ("\nPilihan Anda (A,B,C,D) : ")
    print() 
    harga = []
    if (pilihan == 'A' or pilihan == 'a'):
        while True :
            namabuah = input("Nama buah yang ingin dibeli : ")
            if namabuah in listbuah:
                try:
                    kilo = int(input ("Jumlah Kg             : "))
                    harga1 = kilo * listbuah[namabuah]
                    harga.append(harga1)
                    konfirmasi = input ("\nIngin beli buah lagi? (y/n) : ")
                    if (konfirmasi != 'y'):
                        print("-------------------------------")
                        print("Total harga                 : Rp", sum(harga), "\n")
                        break    
                except (ValueError):
                    print ("Masukkan jumlah kilogram yang valid")
            
            elif (namabuah == '') or (namabuah not in listbuah):
                print ("Buah yang ingin Anda beli tidak ada di daftar")
            
    elif (pilihan == 'B' or pilihan =='b'):
        i = True
        while (i == True) :
            buah_baru = input ("Nama buah yang ingin dijual :")
            if buah_baru in listbuah:
                print (buah_baru, "sudah ada ")
            elif buah_baru not in listbuah:    
                try:
                    harga_baru = int(input("Harga per kilogram : "))
                    listbuah[buah_baru] = harga_baru
                    print (buah_baru, "berhasil ditambahkan\n")
                    print ("Daftar harga baru \n")
                    for data in listbuah:
                        print (data, "( Harga Rp",buah.get(data),")")
                        i = False
                    print()
                except ValueError:
                    print ("Masukkan harga yang valid")
    elif (pilihan == 'C' or pilihan =='c'):
        break
