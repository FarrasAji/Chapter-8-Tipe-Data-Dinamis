try :
    status = True
    i = []
    while (status == True):
        namaMahasiswa = str ( input ("Nama mahasiswa : "))
        i.append(namaMahasiswa)
        konfirmasikan = input ("Tambah nama mahasiswa lagi? (y/n) : ")
        i.sort()
        if (konfirmasikan != 'y'):
            print()
            for datanya in i:
                    print (datanya, "(", len(tuple(datanya)), "karakter", ")")
                    status = False
except ValueError:
    print('Datanya tidak valid!')
