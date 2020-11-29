try :
    listAngka = []
    i = 0
    banyakBil = int ( input ("Berapa banyak bilangan yang akan dimasukkan : "))
    while(i < banyakBil):
        angka = int ( input ("Masukkan angkanya : "))
        listAngka.append(angka)
        i+= 1
    listAngka.sort(reverse = True)
    print ("Urutan bilangan besar ke kecil dari angka yang sudah diinput yaitu : \n",listAngka)
except ValueError:
    print ("Mohon masukkan angka yang benar!")
