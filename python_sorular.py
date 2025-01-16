# soru 

print("km yi mile donusturen programa hos geldiniz....\n")
km=float(input("lutfen kac km oldugunu girin.."))
mil=0.6452548554*km
print("girilen km:" , km , "esit oldugu mil:" ,mil)

# soru
# matematıksel formulu pyton da nasıl kullanabılcegeımız ;
# silindiirn yuzey alanıı ve hacmını hesaplayacagız 

import math

r = float(input("yaricap degerini girin: "))  
h = float(input("yukseklik degerini girin: ")) 
yuzeyAlani = 2 * math.pi * r * r + 2 * math.pi * r * h
print("Yuzey alani: ", yuzeyAlani)
hacim = math.pi * r * r * h
print("Hacim: ", hacim)


# soru
# bır sayının kendınden kucuk bolenlerının toplamını bulma 

def bolenler(sayi):
    liste=[1] # her sayı 1 e bolunur fıye
    for tara in range(2,sayi): # 2 den gırılen sayıya kadarkı sayılara bolmeyı denesın
        if(sayi%tara==0):
            liste.append(tara) # bolen sayılrımızı lısteye eklıyoruz
    return sum(liste) # toplma ıslemını yapıyor 

print(bolenler(12))

# soru
# verilen belirli bir aralıktakı tek sayıları bulma fonkısyonu

def tekSayi(sayi1,sayi2):
    for tek in range(sayi1,sayi2+1): # son dege dahıl degıldı ya olsun dıye +1 dedık
        if(tek%2!=0):
            print(tek,end="-")

print(tekSayi(12,36))

#soru
#input ıcın gırıs yaptımadı calsıımıyor aynı yazdım ama
takimAdi = input("Takim adi gir: ")
macSayisi = int(input("Kac mac oynansin: "))
toplamSkor = 0

while macSayisi > 0:
    macKontrol = int(input("Kazandiysa 1, berabereyse 2, maglubiyetse 3'e basin: "))
    if macKontrol == 1:
        toplamSkor += 3
    elif macKontrol == 2:
        toplamSkor += 1
    elif macKontrol == 3:
        toplamSkor += 0
    macSayisi -= 1

with open("arsenal.txt","w",encoding="utf-8") as dosya:
    dosya.write("arsenal takiminin toplam skoru:")
    dosya.write(str(toplamSkor))

with open("arsenal.txt","r",encoding="utf-8") as dosya:
   print(dosya.read())

# soru
# eger o gun calsımıyorsak uyuyabılırız
#caslima durumu true veya false gır kafandan dene
# and 2 sıde 1 ıse , 1 olur

def uyku(calismaDurumu , tatil):
    if not calismaDurumu and tatil: # calismiyorsam ve tatil = uyku
        return True
    else :
        return False

print(uyku(true,false)) # ornek deneme

# soru 
# olumsuz yapma fonksıyonu

def olumsuzluk(string):
    if len(string)>0 and "degil" in string: # degil strınge dahılse ıcınde varsa
        return string
    else:
        return string + "degil"

print(olumsuzluk("mukemmel"))  

# soru

"""
mahmut a ulkesinde yasamaktadır , a ülkesinde toplam 4 cesıt para bonknotu
bulunmaktadır ve bu paraların degerleri sirasıyla 
100 50 10 1 a banknotudur.
yazılacak programda istenen mahmutun parasına gore en az sayıda banknot kullanılsın ve hangı banknottan kac adet
gerektıgını yazan kodu gıırn
"""

while True:
    para=int(input("para miktarini girinn ve cikis icin 0 a basin"))
    yuzluk=int(para/100)
    ellilik=int(para-(yuzluk*100))/50
    onluk=int(para-(yuzluk*100)-(ellilik*50))/10
    birlik=int(para-(yuzluk*100)-(ellilik*50)-(onluk*10))/1
    toplamBnaknot=yuzluk+ellilik+onluk+birlik
    print("toplam yuzluk : " , yuzluk)
    print("toplam ellilik : " , ellilik)
    print("toplam onluk : " , onluk)
    print("toplam birlik : " , birlik)
    print("toplam banknot : " , toplamBnaknot)
    
    if para==0:
        print("gule gule")
        break

# soru
def unluHArfSayisiniBul(metin ="",sayi=0): # ilk basta metın yokyabos aldık ve bulunan harf sayısıda 0 suan
    unluHarfler="aeiıüöou"
    for tara in metin:
        if tara in unluHarfler:
            sayi+=1
    return sayi

yazi="dfjlkhbgnücooujfdc"
print(unluHArfSayisiniBul(yazi))

# soru
# metın yazma hızı hesaplama uygulaması

import datetime

baslangic=datetime.datetime.now()

metin= "bugun hava cok guzeldi . ama ben ısınamadım"
if(metin==input("metni yazin")):
    son=datetime.datetime.now()
    hesap=son-baslangic
    saniye_bul=hesap.total_seconds()
    print(saniye_bul, " sn de yazdiniz")

#soru
# kullanıcıdan zar atıs tahmını

import random

print("merhaba zar atma oyununa hosgeldiniz")
min=1
max=6
while True:
    deger=int(input("1-6 araliginda bir deger girin (cikis icin 9 a basin)"))
    if deger==9:
        break
    elif 1<=deger<=6:
        x=random.randint(min,max)
        if x==deger:
            print("tebrikler kazandiniz")
        else:
            print("kaybettiniz , pc tahmini : ", x)
    else:
        print("eksik veya hatali tuslama yaptiniz")


# soru
# adam asamaca oyunu

isim=input("isminizi girin..")
print("sevgili " , isim, " toplam yanilma hakkiniz 5 dir")
tahmin="" #dogru bır tahmın olursa buraya ekleyecegız sımdı bos
hak=5

#birden fazla harf deneyecegımız ıcın bunu donguye sokuyoruz
kelime="python"

while hak>0:
    hata=0
    for harf in kelime:
        if harf in tahmin:
            print(harf)
        else:
            print("-")
            hata+=1
    if(hata==0):
        print("kazandiniz")
        break
    tahmin_harf=input("lutfen bir harf girin")
    tahmin+=tahmin_harf
    if tahmin_harf not in kelime: # kelimenın ıcınde bu harf yoksa
        hak-=1
        print("yanlis harf sectiniz kalan hakkiniz " , hak , " tir")

# soru (1-40 arasında sayıyı tahmın edın)
import random 
import time

rasgele_sayi =random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("tahmininizzz"))

    if(tahmin< rasgele_sayi):
        print("bilgiler sorgulaniyorrr")
        time.sleep(1)

        print("daha yüksek bir sayi söyleyin")
        tahmin_hakki-=1

    elif(tahmin> rasgele_sayi):
        print("bilgiler sorgulaniyorrr")
        time.sleep(1)

        print("daha dusuk bir sayi söyleyin")
        tahmin_hakki-=1   

    else: # sayının dogru tahmın edılme durumu
        print("bilgiler kontrol ediliyor")
        time.sleep(1)
        print("tebriklerrr sayimiz = " , rasgele_sayi)
        break

    if(tahmin_hakki==0):
        print("tahmin hakkiniz bitti")
        break

# not heaplama sıstemı yapalım dosya.txt okuyarak
"""her bır satırı tek tek oyuyup hespalama yaparak 
hangı ogrencının hangı karf notunu aldıgını bulucaz"""

def not_hesapla(satir):
    satir=satir[:-1] # satırları okurken hep 1 satır bolsuk bırakıyror sistem \n var orda gggorunmeyen
    # bızde onu yoketmek ıcın :-1 yapıyoruz 

    print(satir)
    liste=satir.split(",") # virgullere gore ayırıyoruz

    """  boyle okyuyor 
    [
        'ali','50','50'
    ]
    [
        'verli','45','45'
    ]
    """
    isim=satir.split(",")
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=not1*0.3 + not2*0.3 + not3*0.4 

    if(son_not >= 90):
        harf="AA"
    elif(son_not >= 85):
        harf="BA"
    elif(son_not >= 80):
        harf="BB"
    elif(son_not >= 75):
        harf="CB"
    elif(son_not >= 70):
        harf="CC"
    elif(son_not >= 65):
        harf="DC"
    elif(son_not >= 60):
        harf="DD"
    elif(son_not >= 55):
        harf="FD"
    else:
        harf="FF"

    return isim + "---------------->" + harf + "\n"



with open("dosya.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi=[]

    for i in file: # her bır satırı okumak ıstıyoruz dıycez
        eklenecekler_listesi.append(not_hesapla(i))
        
    # yenı bır dosyaya yazcaz sımdı 
    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)

""""futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe"""

with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()
    
    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")

        else:
            bjk.append(satır + "\n")
    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
            
            

    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)

# ssoru

""" map kullanın
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]
"""
liste=[(3,4),(10,3),(5,6),(1,9)]
sonuc =list(map(lambda x: x[0]*x[1] , liste))
print(sonuc)

#  soru

"""Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. 
"""

liste=[(3,4,5),(6,8,10),(3,10,7)]

def ucgenmi(liste):
    return liste[0] + liste[1] > liste[2] and liste[0] + liste[2] > liste[1] and liste[2] + liste[1] > liste[0]

sonuc=list(filter(ucgenmi,liste))
print(sonuc)

# soru

"""Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*

reduce kullanmak ıcn functoolsu ıcerı aktarmak laazım
"""
from functools import reduce

liste=[1,2,3,4,5,6,7,8,9,10]

def ciftMi(x):
    return x % 2 == 0
    
cift_sayilar = filter(ciftMi, liste)
toplam = reduce(lambda x, y: x + y, cift_sayilar)

print(toplam)

# soru 
"""Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

*Not: zip() fonksiyonunu kullanmaya çalışın. *
"""

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)


# soru
# metın uzerınde ıslemler

class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi = file.read() # tekte dosyayı okuyoruz
            print(dosya_icerigi)

            kelimeler =dosya_icerigi.split() # bosluga gore ayır
            self.sade_kelimeler = list()

            for i in kelimeler :
                i=i.strip("\n")
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")

                self.sade_kelimeler.append(i)


    def tum_kelimeler(self):

        kelimeler_kumesi=set() # kume olusturduk

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)

            print("tum kelimeler.....")

            for i in kelimeler_kumesi :
                print(i)
                print("************************")

    def kelime_frekansi(self): # her bır kelımenın kac defa gectıgını bulmak ııcın
        kelime_sozluk = dict()

        for i in self.sade_kelimeler:
            if ( i in kelime_sozluk): # sozlukte o kelımeden varmı demek ıstıyoruz
                kelime_sozluk[i] += 1 # aynı kelımeden 1 tane daha gelınce saysıını artırıyoruz
            else :# onceden o kelıme yoksa
                kelime_sozluk[i] = 1   # ekledik
# ! items() metodu, Python'da sözlük (dictionary) veri tipinde kullanılır. Bu metod, sözlükteki tüm anahtar-değer (key-value) çiftlerini döndürür.
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geciyor".format(kelime,sayi))

dosya=Dosya()
dosya.tum_kelimeler()

"""self Ne İşe Yarar?
Sınıf içinde tanımlanan değişkenleri ve metotları sınıfın örneğine (nesnesine) bağlar.
Python'da sınıf metotlarında ilk parametre olarak otomatik geçer, fakat biz bunu yazmak zorundayız."""

# soru
"""Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın."""

s =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for karakter in s:
    if (karakter in frekans):
        frekans[karakter] += 1
    else:
        frekans[karakter] = 1
for i,j in frekans.items():
    
    print(i,":",j)

# items() metodu, Python'da sözlük (dictionary) veri tipinde kullanılır ve sözlükteki anahtar-değer (key-value) çiftlerini döndürür.

# soru
"""şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece 
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
"""
bas_harfler= ""

with open ("siir.txt","r" , encoding="utf-8") as file:
    for satir in file:
        bas_harfler += satir[0]
print(bas_harfler)

# soru

"""Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com
                           //
                           //

*İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.*"""

with open("mailler.txt","r" ,encoding="utf-8")  as file:
    for satir in file:
        satir=satir[:-1] # son karaketerı yanı \n yı sılmek ıcın kullanılır
        if (satir.endswith(".com") and satir.find("@") != -1):
            print(satir[i])
        else:
            print("uygun degildir")


# soru
"""Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]"""

liste1=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
liste2=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste=list(zip(liste1,liste2))
liste.sort()

for i,j in liste:
    print(i,j)

