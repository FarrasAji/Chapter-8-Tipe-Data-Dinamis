def nilaitertinggi(nilaimahasiswa):
    X = 0
    
    for r in nilaimahasiswa:
        MID = r.get('mid')
        UAS = r.get('uas')
        Akhir = (MID + 2*UAS)/3
        
        if(Akhir > X):
            X = Akhir
            data= {}
            data['nim'] = r.get('nim')
            data['nama'] = r.get('nama')
    return data

nilaimahasiswa = [{'nim' : 'A01','nama': 'Amir','mid' : 50,'uas' : 80},
                  {'nim' : 'A02','nama': 'Budi','mid' : 40,'uas' : 90},
                  {'nim' : 'A03','nama': 'Cici','mid' : 50,'uas' : 50},
                  {'nim' : 'A04','nama': 'Dedi','mid' : 20,'uas' : 30},
                  {'nim' : 'A05','nama': 'Fifi','mid' : 70,'uas' : 40}]

tinggi = nilaitertinggi(nilaimahasiswa)
print('nilai akhir tertinggi adalah {0} dengan NIM {1} '.format(tinggi['nama'], tinggi['nim']))
