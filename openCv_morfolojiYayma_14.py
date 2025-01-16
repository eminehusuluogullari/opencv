"""
asındırmadaıkının tam tersı beyaz noktaları artırcaz
morfoljık  donusumler bınary yanı 2lık tabanda ıslemerde gercklersır 
o yuzden grı formata donusturme yaparız
"""

# yayma ıslemı ıcın kullanmamız gereken fonskıyon dılete fonksıyonu 

import cv2 as cv
import numpy as np

cekirdek=np.ones((9,9),np.uint8)
# tum elelmanları 1 olan cerkırdekk matrıs tanımlanmıs 9*9 luk
resim=cv.imread("elYazisi.png",0)
son_hal=cv.dilate(resim,cekirdek,iterations=1)
cv.imshow("orjinal",resim)
cv.imshow("yayma",son_hal)
cv.waitKey(0)