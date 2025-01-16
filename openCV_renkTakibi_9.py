# inRange fonksıyonu ile belirli piksel aralgındakı degerlerı cıktı oalrak alabılırız ama goruntumuzu grı formata donustrdukten sonra

import cv2 as cv 
import numpy as np 

# renklı bır goruntu uzerınde ıslem yaptırcagımız ıcın 3 deger gırerırz
resim=cv.imread("cicek.jpeg")
az=np.array([125,150,255]) 
cok=np.array([255,255,255])
inRange=cv.inRange(resim,az,cok)
cv.imshow("orjinal",resim)
cv.imshow("inrange",inRange)
cv.waitKey(0)

# hsv formatına donsutrumeden yaptıgımzız ıcın cok saglıklı olmadı ama burda sadece pıkselı anlamak ıcın yapmısstık o yuzden