"""
! map fonksıyonu 
 map() fonksiyonu, Python'da bir liste veya başka bir iterable (yinelenebilir) veri yapısının her bir elemanına belirli bir işlev uygulamak için kullanılır.

map(fonksiyon,iterasyon yapılabılcek verı tıpı (liste,demek vb))

soncuları map objesı olarak oarak doner 
"""

def double(x):
    return x*2

map(double,[1,2,3,4,5,6,7,8,9]) # butun degerlerı alıp double foksıyonu ıcıne atıyor aslında ana mantık bu

list(map(lambda x : x**2,(1,2,3,4,5,6,7,8,9))) # lamdbda tek satırda yazar fonksıyonu map da ona degrleır tek tek atıyor

list1= [1,2,3,4]
list2= [5,6,7,8]
list3= [9,10,11,12,13]

list(map(lambda x,y : x*y, list1,list2)) # listelerı sırasyıyla x ve y ye gonderıyro 

"""
! reduce fonksıyonu 
reduce() fonksiyonu, Python'da bir liste veya iterable (yinelenebilir) üzerindeki elemanları ikişer ikişer işleyerek tek bir sonuç döndüren bir fonksiyondur.

Bu fonksiyon, functools modülü içinde yer alır ve toplama, çarpma, maksimum değeri bulma gibi işlemler için idealdir.

calisma mantıgı ;
deger olarak aldıgı fonksıyonu soldan bsalayararak lıstenın ılk 2 elemanına uygular ve daha sonra cıkan soncuu lıstenın 3. elemanına uygular ve bu sekılde devam ederek lıste bıtınce bır tane deger doner 

"""
# modul ve yenı python suurmunde olan modul
from functools import reduce 

def toplama(x,y):
    return x+y

reduce(toplama,[12,18,20,10]) # sonuc 60 , ilk 2 sını topladı sonra 3. ile topladı onuda 4. ile 

# faktorıyel bulalum
reduce(lambda x,y : x*y ,[1,2,3,4,5])

# ! filter fonksıyonu 
"""
filter() fonksiyonu, Python'da bir iterable (liste, demet, set vb.) üzerindeki elemanları belirli bir koşula göre süzmek (filtrelemek) için kullanılır.

functıon kısmı dıgerlınden farklı olarak true veya false degerı dondurmelıdır 
"""
# tek cıft sorusu

filter (lambda x : x % 2 ==0, [1,2,3,4,5,6,7,8,9])  # x ın 2 ıle bolumunden kalan 0 dır , boyle oursa true yoksa false 
# bu fonksıyon gıırlen o sayılar uzerımde uygulanacaktır 
list(filter (lambda x : x % 2 ==0, [1,2,3,4,5,6,7,8,9]) ) # bunu lsıteye attık ve 2,4,6,8 cıktılarını verdıı 

# asal bulma sousu
def asal_mi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(x>i):
            if(x%i==0):
                return False
            i+=1
        return True

# fıltermız yanı burdakı bılgı suzgecımız asallık
list(filter(asal_mi,range(1,100))) # asal olanları bıze lıset olarak yazdırır

# ! zip fonksıyonu 
"""
zip() fonksiyonu, Python’da iterasyon işlemlerini kolaylaştıran yerleşik bir fonksiyondur. Birden fazla liste, demet (tuple) veya diğer iterasyon yapılabilir (iterable) nesneleri eşleştirerek tek bir iterasyon yapılabilir nesne oluşturur.

Her bir iterable’daki aynı indeksli elemanları birleştirerek tuple'lar oluşturur ve bu tuple'lardan oluşan bir zip objesi döndürür."""

# yapmaya calsıtııgımız sey =(1,6),(2,7),..(5,10)
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]

i=0
sonuc=list()
# bu asagıdakı sart sayesınde 11 bosta kalcak cunku yanına  gelcek bısye yok 
while(i<len(liste1) and i<len(liste2)): # 2 lıstenınde boyu i yı gecmeden 
    sonuc.append((liste1[i],liste2[i])) # sonuc lıstemıze atıyoruz 
    i +=1
    print(sonuc) # sonuc listesını basar
    # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# sımdı bu yaptıgımızın aynısını ıste kolay yolla zıp fonk ile yapabılırz
zip(liste1,liste2) #3 parametrelı de yaparsın veya x parametrelı 

sozluk1={"elma":1 , "armut":2 ,"kiraz":3}
sozluk2={"sifir" :0, "bir":1 ,"iki":2}

zip(sozluk1,sozluk2)  # bu sınıfarken elma,sıfır ... dıye yaprık degelrı de almak ıcın ;;

zip(sozluk1.values(),sozluk2.values()) 
list(zip(sozluk1.values(),sozluk2.values()) ) # lısteye atıp yazdırdık suan 

# ! enumarate fonkısyonu 
"""
elemanlarımıza numara verır
Python'da enumerate fonksiyonu, bir iterasyon sırasında elemanlara ve bu elemanların indekslerine aynı anda erişim sağlamak için kullanılır. Genellikle listeler, tuple'lar veya diğer iteratif veri yapıları üzerinde çalışırken kullanılır."""

# yapmak ıstedıgımız = [(0,elma),(1,armut),(...)]
liste=["elma","armut","muz","kiraz"]
sonuc=list()
i=0
while(i<len(liste)):
    sonuc.append((i,liste[i])) # index ve idexin o ankı degeri
print(sonuc)

# işte bu ıslemlerı daha kolay sekılde yapanılmek ıcın enumarate fonksıyonunu kullanırız

list(enumerate(liste)) # list sonucu gormeke ıcın 

liste=["a","b","c","d","e","f","g"]
for i,j in enumerate(liste):
    if (i%2 == 0):
        print(j)

"""a
c
e
g"""

# ! all any fonksıyonları
"""
all, bir iteratif veri yapısındaki tüm öğelerin True olması durumunda True döner. Eğer bir öğe bile False ise, sonuç False olur.

any, bir iteratif veri yapısındaki en az bir öğenin True olması durumunda True döner. Eğer tüm öğeler False ise, sonuç False olur
"""
# mesela any olmasa kulanılcak yapıyı yazayım

def herhangi (liste):
    for i in liste:
        if i:
            return True # herpsı true ıse treu don yoksa false don
    return False

liste=[True,True,False,False]
herhangi(liste)
#  any ıle yappalım 2 yol var ;
any(liste) 
any([True,True,False,False])

# sayılrdakı 0 degrerı mantıksal olraak false harıcı true degerıne esıttır