liste=[]

for i in range(5):
    liste.append(i*2)
print(liste)

liste2=[i for i in range(5)]    
print(liste2)

kurum="Btk Akademi"

for i in kurum:
    print(i.upper())

sonuc=[i.upper() for i in kurum]    
print(sonuc)