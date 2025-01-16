import cv2 as cv 
import numpy as np 

resim=cv.imread("cicek.jpeg")
az=np.array([0,150,25])
cok=np.array([255,255,255])
istenen=cv.inRange(resim,az,cok)
sonuc=cv.bitwise_and(resim,resim,mask=istenen) # resımde gırsın resımden cıksın ve maskeleme ıslemısımız ıstenen dogrultusunda olsun
cv.imshow("orjinal",resim)
cv.imshow("inrange",istenen)
cv.imshow("soncu",sonuc)
cv.waitKey(0)

"""
bız burda maskeleme yapmıs oluyrouz cunku belırlı pıskel aralıgı arsındakı degerlere ulasmıs oluyoruz

bitwise_and fonksıuonu ıle bız resmı alırız ve renklı hale dnustururuz ardından ıstenmeyen bolgelerı de sılerız bu sayede sonucu ekranda gosterınce sadece ıstenen ksıımlaır gosteren bır maskleme yapmıs oluruz

"""


