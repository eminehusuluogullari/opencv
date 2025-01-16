
95 in [1, 2, 56, 95]  # cikti = true (bu lıstede 95 var cunku)
# bunu yaz boyle sonra sec bu satırı
# shıft + enter bu kodun cıktısını termısnalde verir
 
liste = [1,2,3,7]
95 in liste

"ahmet" in ("ali","veli")

# for dongusu ;

for  x in [1,4,5,6,9,8,7,2]:
    print(x) # sırayla yazdııryor

sayilar =[1,4,5,6,9,8,7,2]
for  x in sayilar:
    print(x) # sırayla yazdııryor

isim = "yilmaz"
for harf in isim: # harfın ıcerısıne ıısm degıskenındekı degerler tek tek atandı
    print(harf) # harfi yazdiriyor

# for harf in isim = burda ismin icindeki harfleri sirayla alıyor

isim = "yilmaz"
for harf in isim: # burda ismin icindeki harfleri sirayla alıyor
    print(isim) # ismi yazdiriyor

sayilar = [1,4,5,6,9,8]
for x in sayilar:
    print(x)

"""
bırden fazla  degerleri bulunan ddemetlerin içine nasıl ulasırız ;
sadece demet olmka zorunda degıl lısteler uzerınden de yapabılırız
"""

demet = ((1,2,3),(4,5,6,),("ali","veli","ayse"))
for i in demet:
    print(i)

liste1 = [[1,2,],[4,5]]
for i, j in liste1 :# i 1.elemana j 2.elemana ulasacak orda
    print("i: {} , j: {}".format(i,j))

# while dongusu ;

# bı hata var anlamadım
sayi=int(input("sayi girin..."))
while sayi>0 :
    print("sayi : ",sayi)
    sayi-=1 
print("donguden cikildi")

#calısmaıd hata verıyor aynısını yazdım vıdyonun ama
i=0
while(i<20):
    print("i degeri : " , i)
    i+=1

#range fonksıyonu = belırlı aralıktakı deglerı dondurmemmıze olanak saglayan fonksıyondur ;
range(5) # range(0,5) yanı 0 la 5 aralıgınfakı degerlerı bana donduurur
#eger usttekı gıbı tek eleman gırersek ılkını kendısıı otomatık 0 alıyor
# 5 dahil degildir 
#range fonksıyonunu yazdırmak ıcın basına * koymak gerekır
print(*range(5))

range(5,10) # 5 den 10 a kadar 10 dahıl degıl yazdırı
print(*range(5,10))

range(0,51,2) # 0 dan 51 e kadar saysın ve 2 ser artırarak gıtsın
print(*range(2,51,2))

# soylede kullanabılırız ;
for x in range (5):
    print(x)

# break ,contınue ogrenleım ;

sayi=15
while(0<sayi):
    print(sayi)
    sayi-=1
    if(sayi==5):
        break      # -----------> tamamen cikar tum dongulerden

sayi=20
while(0<sayi):
    print(sayi)
    sayi-=1
    if(sayi % 2 ==0):
         continue     # -------------> sadece en ıctekı mevcut oldugu donguden cıkar
         
# buda hata verıyor whıle lerde oluyor bu 
x= int(input("eger hesap makinesini aktif etmek istersen 1 e bas"))
while(x==1):
    islem=int(input("1-toplama\n2-cikarma\n3-carpma\n4bolme \ncikis icin 5 e bas"))
    if(islem==1):
        a=float(input("ilk dgeri girin..."))
        b =float(input("ikinci dgeri girin..."))
        print("toplami : " ,a+b)
        a=0
        b=0 # bunları 0 a esıtlıyoruz cunku bu bı sonsuz dongu ve 1 kere kullanılmayack
    elif(islem==2):
        a=float(input("ilk dgeri girin..."))
        b =float(input("ikinci dgeri girin..."))
        print("cikarmasi : " ,a-b)
        a=0
        b=0
    elif(islem==3):
        a=float(input("ilk dgeri girin..."))
        b =float(input("ikinci dgeri girin..."))
        print("carpimi : " ,a*b)
        a=0
        b=0
    elif(islem==4):
        a=float(input("ilk dgeri girin..."))
        b =float(input("ikinci dgeri girin..."))
        if(b==0):
            print("payda sifira esit olamaz") 
        print("bolmesi : " ,a/b)
        a=0
        b=0
    elif(islem==5):
        print("cikis yapiliyor...")
        break
    else:
        print("hatali giris..")

# soru
faktoriyel = 1
print("Faktoriyel bulma programını girin...")
while True:
    deger =input("Lütfen bir sayı girin..(Çıkmak için 'e' ye basın)")
    if(deger=="e" or deger=="E"):
        break
    k = int(deger)
    while(k > 0):
        faktoriyel *= k
        k -= 1
    print(deger, "faktöriyeli:", faktoriyel)
    faktoriyel = 1  # faktöriyel başlatılacak yer burada olmalı

# soru
"""
belirli deger araliğinda verilen syaılaarımıızn cift degerlrini
kendi aaralarında tek degerlerini kendıı aralrında 
toplayalım
"""
ciftToplam = 0
tekToplam =0
for x in range(10) : # 0dan 10 kadarı
    if(x %2 ==0):
        ciftToplam +=x
    else:
        tekToplam +=x

print("tek sayilar toplami : " ,tekToplam , "cift tplmai : ",ciftToplam)

# Metotlaar ;

isim = ["ali","veli","ayse"]
isim.append("fatma") # ıcıne yazılan sayısal yada karaktersel metodu lıstenın sonuna ekler
isim.insert(1,"gul") # hangı ındısın yerıne ne eklenecegını gırerız bunada
isim.clear() # isim listesini bosaltir içini siler
isim.pop(1) # içine gırılen ındıstekı verıyı sıler

sayilar1 = [1,2,1,2,1,2,3,4,5,6,1]
sayilar1.count(1) # ıcıne gırelıen eleman degerınden kac tane oldugunu sorgulamaya yarar

# Fonksiyonlar ;
"""
deger dondurebılen ornek fonksıyon kalıbı ;

def sayi(x):
    return x+2

fonksıyondan cıkıp degerıyazdırısak;

print(sayi(5)) -----> cıktı = 7
"""

# parametresiz fonksıyon 
def fonksıyon1():
    print("fonksiyon cagırıldı")

#fonksıyonu cagıralım
fonksıyon1()

#-----------------------

#2 parametrelı fonksıyon ;
def toplama (x,y):
    print("toplami : " ,x+y)

# fonksıyonu cagıralım
toplama(7,5)

#soru
def sayi(x):
    return x

print("sonuc :" ,sayi(2)) # sonuc : 2 ,cıktısı gelır

# soru
def cift_kontrol(x):
    if(x %2 ==0 ):
        return True
    else:
        return False

cift_kontrol(5) 

# soru
# bır sayının asal olup olmama durumuna bakalım 

def asal_kontrol(x):
    for x in range(2,x):
        if(x%i == 0):
            print(x , " degeri asal degildir")
            break
        else:
            print(x , " degeri asal sayidir")
            break

asal_kontrol(12)

# soru
# args = esneklık saglar eleman sayısı belırtmeden

def toplama(*args):
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

print(toplama(1, 2, 3))  # 6
print(toplama(5, 10, 15, 20))  # 50

# soru
def topla(x,y):
    return x+y
def carpma(x,y):
    return x*y
def cikarma(x,y):
    return x-y
def bolme(x,y):
    if(y != 0):
        return x/y
    else:
        print("payda 0 a esit")

while(True):
    print("hesap makinesine hos geldiniz..")
    islem =input("toplama icin 1 e , carpma icin 2 ye , cikarma icin 3 e bolme icin 4 e basin")
    if(islem == "q"):
        break
    k=int(islem)

    if(k==1):
        x=float(input("lutfen ilk sayiyi girin.."))
        y=float(input("lutfen ilk sayiyi girin.."))
        print(topla(x,y))
    elif(k==2):
        x=float(input("lutfen ilk sayiyi girin.."))
        y=float(input("lutfen ilk sayiyi girin.."))
        print(carpma(x,y))
    elif(k==3):
        x=float(input("lutfen ilk sayiyi girin.."))
        y=float(input("lutfen ilk sayiyi girin.."))
        print(cikarma(x,y))
    elif(k==4):
        x=float(input("lutfen ilk sayiyi girin.."))
        y=float(input("lutfen ilk sayiyi girin.."))
        print(bolme(x,y))

# lambda  ifadesi bir fonksıyonu tek bır satırda yazmamıza olanak saglar

# 2 dereceden kok almak demek 1/2 dreceden us almak demektır
def karekok(x):
    return x**0.5
karekok(4) # 2

# lambda halını gosterelım
karekok = lambda x : x**0.5
karekok(4) # 2

# ters cevırme fonksıyou
def ters(x):
    return x[::-1]
print(ters(Ali)) # ilA

# liste okuma fonksıyonla
def liste_oku(liste_adi):
    for i in liste_adi:
        print(i)
isim = ["yilmaz","veli","ahmet","seyma"]
liste_oku(isim) # listenin ismini gonderdik okuma yappcak orda 

# end komutu alt ata yazılmıs olan prınt komutlarını alt alta yazdırmaya yarar
print("merhaba ",end =" ")
print("ali")   #  cıktı = merhaba ali

# enumerate fonksyonu nedir 
# indexleme islmelrini daha kolat gerceklestırırız

#yenı soru
liste =["GTA V" ,"valorant","CS"]
# 1 gts , 2 valorant dye yazdır 

sayi=1
for oyun in liste:
    print(sayi,oyun)
    sayi+=1

# bunu daha kısa 2 satırda gerceklestırmenın yolu = enumarate fonksıyonu 

liste =["GTA V" ,"valorant","CS"]

for index,oyun in enumarate (liste,start=1): # 1 ile naslayıp artırcak
    print(index,oyun)

# map fonksıyonu = bır lısteyı kullanark yenı bır lısste olusturmadır
# listedkı elemanlerın 4. ussunu alarak bu elemanlari bos lısteye doldurma ıslemı yapcagaız

liste =[2,4,6]
bos=[]
def dorduncu(sayi):
    return sayi ** 4 
for sayi in liste:
    bos.append(dorduncu(sayi))

# aynı seyı daha kısa kod yazarak map ıle yapacagız 

liste =[2,4,6]
def dorduncu(sayi):
    return sayi ** 4 # buraya kadar aynı zaten

sayilar = map (dorduncu,liste) # dorduncu fonkıyonunu cagırıp listeyı ıcıne attık
sayilar=list(sayilar)
print(list(sayilar))

# bırden fazla degıkene aynı anda ınput fonksıyonuyla girdiler 
# atamak ıstersek nasıl yaparız ? 

# split metofu kullanılmak zorundadır

x,y =input ("x ve y degerini girin..").split()
# deger gırerken x ı gırınce enter deme 1 bolsuk bırak 2. degerı gır enter de

print(x)
print(y)