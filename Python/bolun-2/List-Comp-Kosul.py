# for item in liste:
#     if(kosul):
#         expression

# [exprenssion for item in liste if kosul]

sayilar=[3,5,7,6,56,34]

sonuc=[]

for sayi in sayilar:
    if(sayi % 2 == 0):
        sonuc.append(sayi)

sonuc=[sayi for sayi in sayilar if sayi % 2 == 0]    
# sonuc = [sayi if sayi % 2 == 0 else "tek sayı " for sayi in sayilar]    

# print(sonuc)

urun_fiyatrlari=[3000,1000,4000,0,5000]
vergiler=[]

vergiler=[sayi * 1.20 for sayi in urun_fiyatrlari if sayi > 0]
vergiler=[sayi * 1.20 if sayi >0 else "vergi hesaplanamadı" for sayi in urun_fiyatrlari]

print(vergiler)
