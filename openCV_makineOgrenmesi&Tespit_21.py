"""Makine ogrenmeıs nedır ?

elde bulunna herhangı bır verı kumseıne,matematıksel ve cesıtlı ıstatıslıksel ıslemler yaparak , elde ettıgı tahmınlerı de bır cıktı olarak veren bılgısayar modellemsıdır

goruntu ıslemede de makıne ogrenmeıs ıslemı pozıfı ve negatıf ıslmelere baglı olarak yapılmaktadır

pozitif resim ; 
(bak buna benzer dıyecegımız)
tespiti yapılacak goruntu 

negtıaf resım ; 
(bak buna benzemıyor dıyecegımız goruntu)
tespıtı yapılacak goruntu ile uyusmayan goruntulerdır
""" 

# ! yuz tespıtı ıslemı 

"""
haarcascade nedır ?

opencv ıcınde bulunun haarcascade sınıfını kullanarak cesıtlı tanıma ıslemlerını gerceklestırırız 

haarcascade_fonk.xml -----> .xml olarak kullanırız

xml verılerı tutan dosyadır 

örn;
// goruntunun uzeınde goz resmı varmı yokmu kontrolu ıcın kullanılrı

haarcascade_eye.xml

// opencv klasorunu ac 
sources kısmına gel
data
haarcascade
burdakılerden kullanacgını 
kes ve burda fotograflları kullanırken yapıstırıdgın gıbı yapıstır 
"""
import cv2

# nesne tanımlayalım
# yuz tanıma ıcın greklı modulu yukluoyoruzz
yuz_tanima= cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # yuztanımanın ıcıne bunu dahıl etmıs olduk

# bu kosula gırmez cunku goruntu okuma yapılıyor burda zaten 
if yuz_tanima.empty(): # bos ıse
    print("veri okunamdi")

# yuz dıye bır matrıs olusturlaım , grı yap

yuz=cv2.imread("emineYuz.jpg")
gri=cv2.cvtColor(yuz,cv2.COLOR_BGR2GRAY)

# artık tespıtı yaptırlaım
# tespıt ıcın greklı fonksıyon;
yuzSonuc=yuz_tanima.detectMultiScale(gri,1.5,4)
# yuzumuuzn uzerıne dıkdortgen cızdırmeyıı yapcaz (for ıle)
# x,y,genislik,yukseklik parametrelerımz
# x ve y ilk bastakı konumalır yanı alt kosler dıkdortgendekı 
# genıslık ve yukseklıkte eklıycez ustune kı ust noktalrı bulalım

for( x,y,genislik,yukseklik) in yuzSonuc:
    cv2.rectangle(yuz, (x, y), (x + genislik, y + yukseklik), (255, 0, 0), 3)

    # son 2 si= renk,kalınlık

cv2.imshow("yuz tanitma",yuz) # pencere adı yuz tanıtma 
cv2.waitKey(0)


# ! goz tespıt ıslemııı
# tespıt edılern yuz ıcınde bunuda tespıt etez gıbı dusun

import cv2

yuz_tanima = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz_tanima=cv2.CascadeClassifier("haarcascade_eye.xml")

if yuz_tanima.empty():
    print("veri okunamadi")

yuz = cv2.imread("emineYuz.jpg")
gri = cv2.cvtColor(yuz, cv2.COLOR_BGR2GRAY)

# eger yanlıs seylerı de aranan nesne gıbı tespıt ederse 1.5 varya onu artır o zaman ortadan kaybolur
yuzSonuc = yuz_tanima.detectMultiScale(gri, 1.5, 4)

for (x, y, genislik, yukseklik) in yuzSonuc:
    cv2.rectangle(yuz, (x, y), (x + genislik, y + yukseklik), (255, 0, 0), 3)
    gozSonuc= goz_tanima.detectMultiScale(gri,1.1,4)
    # forun ıcınde bakmamız gerek goze cunku oce yuzu bulca sonra ııcnden gozu 
    # sımdı dıdortgenı cızdırmem gerek bunu da frda yapmam lazım 
    for(gx,gy,goz_genislik,goz_yukseklik) in gozSonuc:
        cv2.rectangle(yuz,(gx,gy),(gx+goz_genislik,gy+goz_yukseklik),(0,0,255),5)
        
cv2.imshow("yuz tanitma", yuz)
cv2.waitKey(0)

