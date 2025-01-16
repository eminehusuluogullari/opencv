import cv2 as cv
import numpy as np

cv.namedWindow("Trackbar")
def fonk(sayi):
    print(sayi)

cv.createTrackbar("azM","Trackbar",0,255,fonk)
cv.createTrackbar("cokM","Trackbar",0,255,fonk)
cv.createTrackbar("azY","Trackbar",0,255,fonk)
cv.createTrackbar("cokY","Trackbar",0,255,fonk)
cv.createTrackbar("azK","Trackbar",0,255,fonk)
cv.createTrackbar("cokK","Trackbar",0,255,fonk)

# vıdyolar bırden cok kareden olustugu ıcın dongu olmak zırunda

takip=cv.VideoCapture("maviKapak.mp4")

while True:
    res = np.zeros((400, 400, 3), np.uint8)  # Görsel bir hata varsa boş bir pencere
    cv.imshow("Trackbar", res)

    kontrol,yakala =takip.read()

    if not kontrol:
        print("Video sonlandi veya okunamiyor.")
        break

    # sımdı trackbarlarımızdakı degrlerı okuyoruzz

    cv.setTrackbarPos("azM", "Trackbar", 100)
    cv.setTrackbarPos("cokM", "Trackbar", 255)
    cv.setTrackbarPos("azY", "Trackbar", 100)
    cv.setTrackbarPos("cokY", "Trackbar", 255)
    cv.setTrackbarPos("azK", "Trackbar", 100)
    cv.setTrackbarPos("cokK", "Trackbar", 255)


    # sıdmı bu azlaı ve cokları tutabılcegımız bır dızı olusturmamız gerek
    az = np.array([50, 50, 50])
    cok = np.array([255, 255, 255])


    # bu ıstenen ıslemı bınary tabanda dondurme işemi gerceklesıtırcek 
    # az cok degrlerı arasında pıksel yogunlugu hesaplayabılmemız ıcın ınRange kullanmamız gerek

    istenen=cv.inRange(yakala,az,cok) #vıyomuz ilk

    # gırıs1 ve gırıs2 vıyomuz o yuzden yakala dıcez

    son=cv.bitwise_and(yakala,yakala,mask=istenen) # istenene gore maskele

    cv.imshow("video",yakala)
    cv.imshow("istenen",istenen)
    cv.imshow("son hal",son)

    # q ya 20 mlsn basılırsa vıyodan cıkcak
    if cv.waitKey(20) & 0xFF==ord("q"):
       break; 

    cv.waitKey(1)

