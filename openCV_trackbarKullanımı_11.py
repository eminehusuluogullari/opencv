"""
tarckbar sayesınde bızler pıksel yogunlugu ıle ılgılı degrlerı kolaylıkla degıstırebılrız

trackbar sadece bu ıse yaramaz kullanıcı arayuz işlevlrinde bı cok seyde kullanılır

tarckbar aslında bır guı dır 
grafıcsel user interface = grafıksle kullanıcı arayuz
bu tarckbar garfıksel kullanıcı arayuzuu olarak kullanılabılmektedır 
"""

import cv2 as cv
import numpy as np # sıfır matrısı(sıyah bır goruntudur) olusturmak ıcın bunu dahıl ettım 

# zeros fonksıyonu matrıstekı degrlere 0 verır
siyah=np.zeros((480,640,3),np.uint8) # x eksını , y eksenı , kac kanlalı olacagı, kac bıtlık olacagı 

def fonk(x):
    print(x)


# trackbarı olusturlaım
# adi , hangı pencerede goruntulenmek ıstendıgı , deger (kactan baslasın) ,deger(kacta bıtsın) , fonkısyon adı(bu treackbarın ne ıse yarayacagını soyleyen)

# Pencereyi oluşturuyoruz
#cv.namedWindow("pencere")

cv.createTrackbar("Ali","pencere",0,255,fonk) # bız burda degere 0 dedık ama ılerde renk tabıkı yaparken bunu ona gore ayarlarız

# bu tarckbar oldu bıtıye gelmemlı 0-255 deger aralıgı arsında gıdıp gelcek cunku sureklı yanı donguye sokmalıyız
while True:

    # bız trackbarımızı alı degıskenıne atadık ve ıslemlerımzı bunun uzerınde gerckelstırcez
    ali=cv.getTrackbarPos("Ali","pencere") # tarckbar ısmı , goruntulemek ıstedıgım pencere ısmı 
    cv.imshow("pencere",siyah)
    cv.waitKey(1) #her 1 mılı sanıeyede gostersın


# trackbar yardımıyla bır goruntunun oıksellerıyle nasıl oynarız skla gelıyor ordan ayarlıyoruz 

import cv2 as cv
import numpy as np

cv.namedWindow("Goruntu") 

# sımdı 3 kanallı bır zeros olusturusak mantık ;[0,0,0]

goruntu=np.zeros((450,495,3),np.uint8)

def fonk(sayi):
    print(sayi)

# 3 tane tarckbar olsuturmammız gerek cunku mavı yesıl ve kırmızıyı kontrol etmek ııvn
#tarckbar adı , penvcere adi
cv.createTrackbar("mavi","Goruntu",0,255,fonk) # 
cv.createTrackbar("yesil","Goruntu",0,255,fonk) # 
cv.createTrackbar("kirmizi","Goruntu",0,255,fonk) # 

while True:
    cv.imshow("Goruntu",goruntu)
    mavi=cv.getTrackbarPos("Mavi","Goruntu")
    yesil=cv.getTrackbarPos("Yesil","Goruntu")
    kirmizi=cv.getTrackbarPos("Kirmizi","Goruntu")

    # ama bunalrı matrıse aayalım kı sıkladan renk degısımı olabilsin
    goruntu[:]=[mavi,yesil,kirmizi] # ıga sklasında renk sısrası boyle o yuzden 

    cv.waitKey(1)


