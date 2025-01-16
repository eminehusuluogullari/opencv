# bir matrıste okumus oldugumuz goruntuyu baska matrıse atama

import cv2
resim=cv2.imread("resim.jpg")
kopya = resim.copy()

cv2.imshow("kopya",kopya)
cv2.imshow("orjinal",resim)
cv2.waitKey(0)