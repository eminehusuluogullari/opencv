""""
Gradyan yayilma ve asindirmanin farkidir.  
Yani biz gradyan kullanarak bir goruntunun iskeletlerini cikartabiliriz.  
Mesela 'J' harfi var, siyah ekranin uzerinde beyaz olarak. Burada beyaz harfin ortasindan cizgiler olacak.  
Yani iskeletini cikaracak."
 """

import cv2 as cv
import numpy as np

# 5x5 bir kernel matrisi oluştur (morfolojik işlemler için kullanılacak)

cekirdek=np.ones((5,5),np.uint8)
resim=cv.imread("elYazisi.png",0) # morfolıjıkler bınary yanı grı

gradient=cv.morphologyEx(resim,cv.MORPH_GRADIENT,cekirdek)
cv.imshow("orjinal",resim)
cv.imshow("gradient",gradient)
cv.waitKey(0)