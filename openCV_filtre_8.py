# canny kenar uygulamsı= kenaar tespıt ıslemını gerceklestırır
# acıklan bır resmın , goruntunun kenarlarını bulamamızı saglar 
# canney ı kullanabılmek ıcın once kendısı bı bınary donusum yapacaktır o yuzden resmı grı hale cevırmelıyız 

import cv2 as cv 

# esik deger = kenalraı tespıt etmek ıcın gereklı pıksel yogunlugu
resim=cv.imread("resim.jpg",0) # grı tonlama kenar bulma ıslemınde daha verımlıdır
kenar=cv.Canny(resim,45,150) # degeler esik degelerdır
cv.imshow("resim",resim)
cv.imshow("kenar bulma ",kenar)
cv.waitKey(0)

# NEGATIF GORUNTUYE ULASMAK (goruntuyu tersıne cevırmektır)
# (telefonda olan)
import cv2 as cv 

resim1=cv.imread("resim.jpg")
negatif=cv.bitwise_not(resim1)
cv.imshow("resim",resim1)
cv.imshow("negatif",negatif)

cv.waitKey(0)

# GAUSS FİLTRESİ (GORUNTU BULANIKLASTIRMA) ????????

import cv2 as cv
resim=cv.imread("resim.jpg")
# 7 ,7 yazan yer kernael sıze dır ve tek sayı gırılmezse calısmaz
# kernel size = filtre boyutu
bulanik=cv.GaussianBlur(resim,(7,7),0) # 7 7 bulanıklastırma 
cv.imshow("resim",resim)
cv.imshow("gauss",bulanik)
cv.waitKey(0)

# MEDYAN FİLTRESİ (GURULTU TEMZIZLER)

import cv2 as cv
isim="kadin.jpg"
resim=cv.imread(isim)
medyan=cv.medianBlur(resim,3) # 3= filtre boyutu
cv.imshow("orjinal",resim)
cv.imshow("medyanlanmis hali",medyan)
cv.waitKey(0)

# bileteral filtre (gurultuyu azaltır yumusaklıgı artırır)
# nasil işler ;
# biz filtre boyutunu gırdıkten sonra bu fıltre boyutları arsındakı degelrrın
# agırdık ortalamsını alıyor , bu ortalama deger goruntumuze pıksel yogunlugu olarak atanır 

import cv2 as cv
resim=cv.imread("kadin.jpg")
bileteral=cv.bilateralFilter(resim,15,93,43)
# biz burdakı dgerlerı ne kadar fazla verırısek o kadar 1 piksel daha uzaktakı bır pıkselle etkılesım halıne girebilir
# ona gorede bır yogunluk hesabı ortaya cıkartabılır 
cv.imshow("orjinal",resim)
cv.imshow("bileteral",bileteral)
cv.waitKey(0)


