dataSayur = ['bayam', 'kangkung', 'wortel', 'selada']
print ("Sayuran yang ada : ", dataSayur)
print ("\nSilahkan memilih menu dibawah")
while True :
    print('Menu Pilihan:')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur')
    print('D. Selesai')
    pilihan = input ("Pilihan Anda (A,B,C,D) : ")
    if (pilihan == 'A' or pilihan =='a'):
        tambahdata = str (input("Nama sayur yang ingin ditambahkan : "))
        print (tambahdata, "sudah dimasukkan dalam keranjang\n")
        dataSayur.append (tambahdata)
    elif (pilihan == 'B' or pilihan =='b'):
        i = True
        while (i == True):
            try:
                hapusdata = str(input("Nama sayuran yang ingin anda hapus : "))
                dataSayur.remove(hapusdata)
                print(hapusdata, "telah dihapus \n")
                i = False
            except (ValueError):
                print ("Tidak ditemukan")
    
    elif (pilihan == 'C' or pilihan =='c') :
        print("isi sayuran sekarang : ", dataSayur, "\n")
    elif (pilihan == 'D' or pilihan =='d'):
        keluar = input ("Anda ingin keluar dari program? (y/n) : ")
        if keluar == 'y':
            break
