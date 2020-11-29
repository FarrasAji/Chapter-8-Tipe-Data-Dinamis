def kuadrat(bil):
        hasil = []
        for data in range(len(bil)):
            perkalian = bil[data]**2
            hasil.append(perkalian)
        return hasil
bil = [2, 4, 5, 6]
hasilperhitungan = kuadrat(bil)
print(hasilperhitungan)
