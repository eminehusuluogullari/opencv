# bir goruntunun genıslık derınlık ogrenmek ıcın = shape metodu kullanılrı
#                                                       h ,derin,genis sirayla indisleri bu
import cv2 

oku=cv2.imread("cicek.jpeg")
(yukseklik,genislik,derinlik)=oku.shape
# termınale gelıyor 
print("yukseklik : {} , derinlik:{} , genislik:{}".format(yukseklik,genislik,derinlik))
cv2.imshow("resim",oku)
cv2.waitKey(0)

# bir goruntuyu boyutlandırabılmek ıcın resize fonksıyonunu kullanmamız gerek ;

resim=cv2.imread("resim.jpg")
boyut=(800,800)
boyutlandirilmis_hal=cv2.resize(resim,boyut)
cv2.imshow("orjinal",resim)
cv2.imshow("boyutlandirilmis hal",boyutlandirilmis_hal)
cv2.waitKey(0)

# piksel yogunlugu = kırmızı yesıl ve mavı rengın bellı orandakı renklerı
# icr sklasına gore olusturulmustur 
# once mavı sonra yesil en son kırmızı degerlerı gosterir

resim123=cv2.imread("resim.jpg")
(mavi,yesil,kirmizi)=resim123[125,15] # y-x eksenlri
print("kirmizi degeri : {} yesil degeri :{} mavi degeri:{}".format(kirmizi,yesil,mavi))

# belirli bolgeyı kırpma
resim=cv2.imread("resim.jpg")
kirpma=resim[60:360 , 20:360] # y eskenı 60 dan 360 a kadar 
cv2.imshow("orjinal",resim) # olusturacagımız matrısın adı orjınal
cv2.imshow("son hal",kirpma)
cv2.waitKey(0)


