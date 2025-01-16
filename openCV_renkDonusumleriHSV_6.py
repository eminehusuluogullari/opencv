# grı formatta goruntu olusturma kullanılan fonk. = cvtColor
# donsuturme kodu : cv.COLOR_BGR2GRAY 

"""
grı formata donusturme onelıdır neden ?
renkli yaoarken renk skalsında bırden falza deger tutuluyordu 
eger grı formatta yaparsak tek bır deger alacagından ve alacagı degeler sıyahla beyaz arasında olacagından ;
bu makıne ogrenmesı kısmında ısımızı kolaylastırır
"""
import cv2 as cv 

resim=cv.imread("resim.jpg")
gri_format=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
cv.imshow("orjinal",resim)
cv.imshow("son hal",gri_format)
cv.waitKey(0)

# daha kısa kodla daha kolay yapımı 

import cv2 as cv 

resim=cv.imread("resim.jpg",0)
cv.imshow("orjinal",resim)
cv.waitKey(0)

# HSV goruntu formatına donusturme ,
"""
acv renk skalasına gore kyaslanınca renk doygunlugu daha bellı olan formatır
eger renk takıbı gereckelstırecek olursak hsv formatını kullanmamız gerek
"""

import cv2 as cv 

resim= cv.imread("renk.jpg")
hsv=cv.cvtColor(resim,cv.COLOR_BGR2HSV)
cv.imshow("gercek:",resim)
cv.imshow("HSV",hsv)
cv.waitKey(0)

# bir goruntunun binary hali = binary renk donusumu
# kullanılan fonksıyon = threshold

"""Eşikleme (thresholding), bir görüntüyü segmentlere ayırmak için kullanılan bir tekniktir. Piksel değerleri belirli bir eşik değerin üstünde veya altında olup olmamasına göre sınıflandırılır. Genelde, eşik değerinin üzerindeki pikseller beyaz, altındaki pikseller siyah olarak belirlenir."""

# ( , burası eısk deger 0 dan 255 e kadar verikir eger 126 verırısen mesela 125 olan degerı sıyah olarak alcak ustunu ebyaz alcak)
# cv.THRESH_BİNARY = INV tam tersi
# CV.THRESH_BİNARY_INV =S siyahlar beyaz oluyor beyazlar sıyah

# obje tespıtınde kullanır ya tam sıyah ya tam beyazdır bınary goruntu 
# bınary e donsuturmek ıcın once grıye donsuturme yapılır

# kontrol degıskenı ne ıse yarıyor anlamadım
import cv2 as cv 

resim= cv.imread("resim.jpg",0) # grı formmata otomatık burda donustsurme yaptık
kontrol,binary=cv.threshold(resim,150,255,cv.THRESH_BINARY)
kontrol,binary2=cv.threshold(resim,150,255,cv.THRESH_BINARY_INV)
cv.imshow("binary1:",binary)
cv.imshow("binary2:",binary2)
cv.waitKey(0)