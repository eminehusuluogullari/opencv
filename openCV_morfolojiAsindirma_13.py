# morfolojı = bicim biirmi 

"""bir cervceve dusun içinde karamalaı bır kısım var aradakı boslukları asındırıp kalan karalamalı kısma benzetmek  ııcn yapılır 

sıyahla beyazın bulundugu gosrsellerde yapılan buu ıslemde sıyah ıle beyazın kesıtıgıı bırlestırgı yerlerde asındırma ıslemı yapar
"""

# 1 lerden ollusan degrelr ııcn ones fonksyonu kullanılır

import cv2 as cv
import numpy as np
# 5 e 5 olan cekırek matısıne baglı bıde
# 1 e 1 olsa cok sılmez degımmez ama rttıkca sılınen de artıyor 
cekirdek =np.ones((5,5),np.uint8)
# rresım bızım ıslem yapacagımız matrıs
resim=cv.imread("elYazisi.png",0) # 0 = grı formata donusturmek demek(binary uzerınde ıslem yapacagımız ıcın)

# iterations = asındırma ıllemının kac kere yapılcagı 
asindirma=cv.erode(resim,cekirdek,iterations=1)
# iterasyonu artırısak her seferınde beyazları dahada sılcek ve kaybolcak bı srue sonra 
cv.imshow("orjinal",resim)
cv.imshow("erozyon",asindirma)
cv.waitKey(0)

# sıyah ve beyaz varya gordugu beyazı asındırıyor 