# 2 boyutlu goruntuyu belli bir konumda dondurme ;

import cv2 as cv

resim=cv.imread("resim.jpg") # burası 500x500 dur
genislik=500
yukseklik=500
merkez_nokta=(genislik/2,yukseklik/2) # tam orta noktayı merkez nokta almıs oldukk
# donudremek ıcın kulladıgımız sey ;
d=cv.getRotationMatrix2D(merkez_nokta,-30,1.0) # -30= acı , 1 = seklın carpılacagı katsayı 
dondurme=cv.warpAffine(resim,d,(genislik,yukseklik))
cv.imshow("dondurme",dondurme)
cv.imshow("orjinal",resim)

cv.waitKey(0)

# x eksini y ekseni veya xy eksenınde dondurme
# flip fonksıyonu kullanılr 


import cv2 as cv

resim=cv.imread("resim.jpg",0) # grı resım uzerıjnde  calıslaım
dikine_dondurme=cv.flip(resim,0) # donduurelecek resım , 0 =  x eksnınde donmesı ıcın
yatay_dondurme=cv.flip(resim,1) # donduurelecek resım , 1 =  y eksnınde donmesı ıcın
tum_dondurme=cv.flip(resim,-1) # donduurelecek resım , -1 =  hem x hem y eksnınde donmesı ıcın
cv.imshow("orjinal",resim)
cv.imshow("dikine",dikine_dondurme)
cv.imshow("yatay",yatay_dondurme)
cv.imshow("tum islemler",tum_dondurme)

cv.waitKey(0)

# degıısk bır dondurme methodu = rotate ( icine dondumre kodunu yazarız pythonda tanımlı )

import cv2 as cv

resim=cv.imread("resim.jpg",0) 
dondurme=cv.rotate(resim,cv.ROTATE_180) # saat yonunun terısnde 180 dercelık dondurme ıselmı yapacak demek
dondurme2=cv.rotate(resim,cv.ROTATE_90_CLOCKWISE) # saat yonunde 90
cv.imshow("180",dondurme)
cv.imshow("90",dondurme2) # tınak ıcınde yazanlar acılan pencerelı anlamakmaız ıcın ustunde yazrıyor hangısının sonucu oldugunu

cv.waitKey(0)




