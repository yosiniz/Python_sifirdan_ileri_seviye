sayilar = [1,2,3,4,5]
sayilar_str = ["1","2","3","4","5"]
isimler=["ali","yusuf","Zeynep"]
kullanicilar=[
    {"ad:":"ali","soyad:":"yılmaz"},
    {"ad:":"yusuf","soyad:":"subaşı"}
]


kareleri = [sayi **2  for sayi in sayilar]

# def kareAl(sayi):
#     return sayi ** 2

sonuc = list(map(lambda sayi: sayi **2, sayilar))
sonuc =list(map(int, sayilar_str))
sonuc= list(map(str.upper,isimler))
sonuc= list(map(lambda kisi: kisi["ad:"],kullanicilar))

print(sonuc)