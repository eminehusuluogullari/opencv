"""
acma işlemini yapınca once asındırma sonra yayma ıslemı yapılır
"""

# acmada ve kapamada kullanılan fonskıyon = morphologyEx

# resımdekı puantıyeleı sılcez

import cv2 as cv
import numpy as np

cekirdek=np.ones((9,9),np.uint8)
resim=cv.imread("puantiye.png",0)
acma=cv.morphologyEx(resim,cv.MORPH_OPEN,cekirdek)
cv.imshow("acma",acma)
cv.imshow("orjinal",resim)
cv.waitKey(0)


"""
acma kod satırı yerıne once asındırma sonra yayma yaparsakta aynıs olur 2 satır halıdne 
"""

# SIMDIDE KAPAMA ISLEMINI YAPACAGIZ
# burdada sıyahlaır beyazlara yaklastırıyor

import cv2 as cv
import numpy as np

cekirdek=np.ones((9,9),np.uint8)
resim2=cv.imread("tersPuantiye.png",0)
kapama=cv.morphologyEx(resim2,cv.MORPH_CLOSE,cekirdek)
cv.imshow("acma",kapama)
cv.imshow("orjinal",resim2)
cv.waitKey(0)

