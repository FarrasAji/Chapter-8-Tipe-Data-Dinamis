listbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print ("Daftar harga buah per kilogram")
print (listbuah)
while True:
    namabuah = input ("Nama buah yang ingin dibeli : ")
    if(namabuah not in listbuah.keys()) :
        print('Buah yang dimaksud tidak ada')
        continue
    else :
        if namabuah in listbuah:
            try:
                kilo = int ( input ("jumlah kilogram             : "))
                harga = kilo * listbuah[namabuah]
                print("-------------------------------")
                print("Total harga bayar : Rp", harga)
                break
            except (ValueError):
                print ("Jumlah kilo tidak valid")
                break
