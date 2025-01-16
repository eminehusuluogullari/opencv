ad = input("lutfen isminizi girin...")
soyad = input("lutfen soyadinizi girin...")
not1 = float(input("lutfen notunuzu girin(1.)"))
not2 = float(input("lutfen notunuzu girin(2.)"))
ort = (not1+not2)/2
veri =[ad,soyad,not1,not2,ort] # listemize ekkliyoruz
print("ismi {} olan soyismi {} olan ogrencimizin 1.ders notu {} olan\n 2.ders notu {} olan ogrencimizin ortalamasi {}".format(veri[0],veri[1],veri[2],veri[3],veri[4]))

bool(71) # true

x = "yilmaz"
print("blok1")
if(x == "yilmaz"): 
    print("blok2")
else:
    print("blok3")

"""
cikti : 
blok1
blok2
"""
x=input("lutfen x i girin..")
y=input("lutfen y yi girin..")
if(x < y):
    print("y buyuktur")
else:
    print("x buyuktur")

# soru
x = float(input("x girin..."))
y = float(input("y girin..."))
if(x < y):
    print("y x ten buyuktur")
elif(y < x):
    print("x y den buyuktur")
else:
    print("sayilar esittir")

#soru
tc = int(input("tc no girin.."))
isim = (input("isim girin.."))
soyisim = (input("soyiism girin.."))
if(tc == 123456 and isim == "yilmaz" and soyisim == "alaca"):
    print("bilgiler dogrudur")
elif(tc != 123456 and isim == "yilmaz" and soyisim == "alaca"):
    print("tc no hatalidir")
else:
    print("hatai giris")

#soru
x = float(input("1.sayisyi girin..."))
y = float(input("2.sayisyi girin..."))
islem = int(input("yapmak istediginiz islmei secin \n 1-toplama\n 2-carpma\n 3-bolme \n 4-cikarma\n "))
if islem == 1 :
    print("toplama sonucu " , (x+y))
elif islem == 2 :
    print("carpma sonucu " , (x*y))
elif islem == 3 :
    print("bolme sonucu " , (x/y))
elif islem == 4:
    print("cikarma sonucu " , (x-y))
else:
    print("hatali giris")

#soru
sayi = int(input("sayi giirn..."))
if(sayi < 0):
    print("negatiftir")
elif(sayi > 0):
    print("pozitiftir")
else:
    print("sifira esittir")

# ic ice kosullar
x= int(input("sayi girin.."))
if x==5 :
    y= int(input("sayi girin.."))
    if y==10 :
        print("x : {} y : {}".format(x,y))
print("kosullardan cikalim")