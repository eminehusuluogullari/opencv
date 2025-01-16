 # w = o iismde dosya yoksa olusturuur varsa ıcını sıler tekrar getırır

open("sayilar.txt","w") # sayılar dosyası olusturuldu
# explorer dosya gezgınınde gorunutor olustu

sayilar=open("sayilar.txt","w")
sayilar.write("1 2 3 4 5") # 9 byte yer kapladı

sayilar.write("dosya islemleri")

# eger dosyayı belırlı bır konumda olusturmak ıstersen 
file=open("C:/Users/user/Desktop/bilgiler.txt","w") # konumu salladım 

# sımdıdıe okuma ıslemlerl = r

# utf-8 , en genel karater dzısı demek turkce de yazabılrıız yanı

oku = open("sayilar.txt","r",encoding="utf-8") # turkce karakter oldugu ıcın txt de bunu yazarız

# yazdıralım ekrana
for i in oku:
    print(i)
oku.close()

sayilar.close() # dosyayı kapatınca ustunde ıslem yapılmaz

# biz islem yaptıktan sonra her seferıne dosya kapat kısmını yapmak yerıne baska bır durum var ; 
# asagıdakı gıbı yazdıktan sonra bızım dosyamız otomattık kapanıyor kapatmamıza gerek yok

# dosya = islem yapacagımız dosyadakı degısken ısmıdır
with open ("sayilar.txt","r",encoding="utf-8") as dosya:
    for x in dosya:
        print(x,end="") # alt alta yazdır demek 

with open ("sayilar.txt","r",encoding="utf-8") as dosya:
    print(dosya.tell()) # doysmızın kacıncı byte de oldugunu soyle4r
# 0 mesela 0. byteden baslarak okuyor demek

with open ("sayilar.txt","r",encoding="utf-8") as dosya:
    dosya.seek(10) # 10. byte a gıt dedık ordan baslaıycaz okumaya
    print(dosya.tell())  # 10 cıkar cunku oraya seekle geldık ordan baslıycaz demek

with open ("sayilar.txt","r",encoding="utf-8") as dosya:
    dosya.seek(10) 
    for x in dosya: # dosya sonuna kadar demek ya
        print(x,end="")
# 10. indisten baslayacak ve okuycak alt alta (ilks satırda sadece şlk 10 harf yok kalanı 10.indis olmaz hep artarak gıder cunku)

with open ("sayilar.txt","r",encoding="utf-8") as dosya:
    dosya.seek(10) 
    y=dosya.read(15) # 10.byteden sonra 15 karakter okuyup dursun demek bu
    print(y)

# hem okuma hem yazma işlemi = r+ 
with open ("sayilar.txt","r+",encoding="utf-8") as isle:
    isle.seek(30) #  30.byte e gel
    isle.write("yilmaz") # 30.byteden sonrakı ılk 5 karakterı yılmaz olarak degıstır 
    # ekleme degıstır 

file= open("bilgiler.txt","r", encoding="utf-8")
for i in file:
    print(i) # satır satır okuma yapar 
file.close()

# okumanın baska yolu
file= open("bilgiler.txt","r", encoding="utf-8")
icerik=file.read()
print("dosyaniin icerigi " , icerik)

file= open("bilgiler.txt","r", encoding="utf-8")
print(file.readline()) # readline her cagırıldıgında dosyanın sadece 1 satırını okur 
# tamamını okusun ıstıyorsak alt alta bundan acıcaz  

# ! file degıskenı ımlec gorevı goruru okurekn okudukca 1 sonrakı ımlece kayar mantıgı budur hepsınde okuma yaparken 
# ! hatta file.read ile okurken bıdaha okumak ıstesek ıcerık2 dıye okuyamamzcunku metnın en sonuna gelmıstır ımleç

file= open("bilgiler.txt","r", encoding="utf-8")
print(file.readlines())
# readlines , her bır satırı okuyarak bır lısteye atar 
"""
['ali bey'
'murat'
'su'] boyle
"""

# istediğimiz indexe ekeleme yapmak için
with open("bilgiler.txt","r",encoding="utf-8") as file :
    liste=file.readlines() # okuduklarını lısteye at 
    liste.insert(3,"ahmet baltaci\n") # 3.indexe bu ısmı ekle
    file.seek(0) # lıstenın en basına don
    for i in liste:
        file.write(i) # lsıteye yazıyoruz

# a kıpıyle dosya actıgımızda append , dosya yoksa olusturulur eger mevcutsa tekrar olusturulmaz ve dosya ımlecı dosyanınsonuna gıderek ekleme yapmayı saglar 

# en alta metnın devamı olarak bunu ekler
with open ("sayilar.txt","a",encoding="utf-8") as isle:
    isle.write("\n bugun hava cok guzel")