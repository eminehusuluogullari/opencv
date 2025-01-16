"""
Top hat = açma işleminden orijinal görüntünün çıkarılması işlemidir.

Black hat = kapatma işleminden orijinal görüntünün çıkarılması işlemidir.
"""

import cv2 as cv
import numpy as np

cekirdek = np.ones((7, 7), np.uint8)
resim = cv.imread("elYazisi.png", 0)
top_hat = cv.morphologyEx(resim, cv.MORPH_TOPHAT, cekirdek)
black_hat = cv.morphologyEx(resim, cv.MORPH_BLACKHAT, cekirdek)

cv.imshow("orjinal", resim)
cv.imshow("tophat", top_hat)
cv.imshow("blackhat", black_hat)
cv.waitKey(0)

# herssye dogru ama boyel ahat verıyro bosluktan falandır bakamam kac kere baktım
