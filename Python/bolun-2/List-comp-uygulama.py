s1=[sayi for sayi in range(101)]

bolum12=[sayi for sayi in s1 if sayi % 12 == 0]
print(bolum12)

text ="Hello 12345  World"
rakamlar=[rakam for rakam in text if rakam.isdigit()]
print(rakamlar)

sicakliklar=[20,15,0,-5,-2]
s3=[sicaklik if sicaklik > 4 else f"Buzlanma tehlikesi Sıcaklık: {sicaklik}" for sicaklik in sicakliklar]
print(s3)

ogrenciler=["ali","ahmet","zeynep"]
notlar=[50,60,90]

liste=[(ogrenciler[i],notlar[i]) for i in range(0, len(ogrenciler))]
print(liste)

liste_dict= {key:value for (key,value) in liste if value > 50}
print(liste_dict)


s5=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(s5)

