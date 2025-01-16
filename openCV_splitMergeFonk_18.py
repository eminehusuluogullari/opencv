"""
split ayirmak 
merge bırlestırmek demektır 

bizim renklı goruntulerımız 3 kanaldan olusuyor , eger herhangı bır kanalı gosermek ıstıyorusak  
dıger 2 kanalı 0 lar yerlestırcez kı gostermek ıstedıgımız regı daha net gosterelım bunun ıcınde bıze 0 matrısler gerekıyor 

"""
import cv2 as cv
import numpy as np # 0 matrısını kullanmak ıcın
sifir=np.zeros(resim.shape[:2],np.uint8)

"""resim.shape[:2]: Bu, resim adlı görüntünün yüksekliğini (height) ve genişliğini (width) alır. resim.shape genellikle (yükseklik, genişlik, kanal_sayısı) şeklinde bir tuple döner. Burada [:2] dilimi, sadece yükseklik ve genişlik bilgilerini alır, kanal bilgisi hariç tutulur."""


""" birelsime yapacaksan burası olcak 
        # sımdı bu merge satırlaarı harıc ayrıstırma yapıyorduk
        mavi=cv.merge([b,sifir,sifir])
       # bırelsırme yaparken mavı rengı dırket 
       # vercez ama dıger renklerı 0 olarak vercez

        yesi=cv.merge([sifir,g,sifir])
        kirmizi=cv.merge([sifir,sifir,r])
        cv.imshow("orjınal",resim)
        cv.imshow("b",mavi)
        cv.imshow("g",yesil)
        cv.imshow("r",kirmizi)
"""


# 3 kanllı bır gggoruntu uzerınde ıslem yaptıgımızda 
# b g r ye gore , bu sırayla ılerlememız gerek
b,g,r= cv.split(resim) # resmı bunlrar gore ayırcaz
cv.imshow("orjınal",resim)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)
cv.waitKey(0)
