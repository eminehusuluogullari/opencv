# dikdortgen cizdirelim kullanılan fonk. = rectangle
# rectangle =degisken ad,baslangıc konum,b,t,s konum,renk(skalsı),kalinilk

# resmin uzerıne dıkdortgen cızdık
import cv2

oku=cv2.imread("resim.jpg")
cv2.rectangle(oku,(12,12),(155,180),(255,0,0),2) # mavi kalınlık 2
cv2.imshow("pencere",oku)
cv2.waitKey(0)

# daire cizimi kullanılan fonk = circle
# giris cikis matisi , merkez noktasi , yarıcap , renk , kalinil
# kaliniliga -1 dersen dairenin ,c,ni boyuyor

# nıye calısmadı bılmıyorum aynı yazdım ama
import cv2

oku=cv2.imread("resim.jpg")
merkez=(125,480)
renk=(125,150,12)
cv2.circle(oku,merkez,70,renk,4)
cv2.imshow("pencere",oku)
cv2.waitKey(0)

# dogru arcası cızme kullanılan fonk=line 

import cv2
res=cv2.imread("resim.jpg") # res bızım matrısımız okumnın yapıldıgı
nok1=(150,95)
nok2=(400,295)
renk=(55,152,255)
kalinlik=6
cv2.line(res,nok1,nok2,renk,kalinlik)
cv2.imshow("pencere",res)
cv2.waitKey(0)

# resim ustune yazı yazdırma fonksıyonu putText (en sonkı kalınlık)

import cv2
resim=cv2.imread("resim.jpg") 
renk=(255,0,0)
# kalınlık 2 olsun
resim=cv2.putText(resim,"husulu",(50,50),cv2.FONT_ITALIC,1,renk,2) # resmın ustune yazacagzımız ıcın bu adrese ataamamız gerek bu fonku
cv2.imshow("pencere",resim)
cv2.waitKey(0)

