listbuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print ("Daftar Buah :")
print (listbuah)
total = 0
lanjutkan = 'y'
while lanjutkan == 'y':
    try:
        pilihan = input("Nama buah yang ingin dibeli : ")
        if(pilihan in listbuah):
            kg = float(input('Berapa Kg             : '))
            total += (listbuah[pilihan] * kg)
            lanjutkan = input("Beli buah yang lain (y/n) ? ")
        else:
            print('tidak ada dalam Daftar buah'.format(pilihan))
        
    except ValueError:
        print('Data Tidak Valid')
print("Total harga           :",total)
