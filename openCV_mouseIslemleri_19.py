"""opencv modulumuzde bulununnan mouse harekterlrını nasıl kullnacagımız hakkıdna bılgı sahıbı olacagız"""

import cv2 as cv
import numpy as np

# x goruntunun x uzerındekı dusum noktası y de aynı
def mouse(etkinik,x,y,flags,param): # son 2 sıne suan takılma
    if(etkinik==cv.EVENT_MOUSEMOVE):
        print("mouse resim uzerinde")
    elif(etkinik==cv.EVENT_LBUTTONDOWN):
        print("sol tika basildi")
    elif(etkinik==cv.EVENT_RBUTTONDOWN):
        print("sag tika basişdi")

resim=np.zeros((400,400,3),np.uint8)
# gosterecegı cerceveyı orjınal boyutunda kednı ayarlasın dıye
cv.namedWindow("Mouse",cv.WINDOW_AUTOSIZE)

# mouse işlemlerini kontrol etme fonksıynu 
# once perncere adı , sonra olusturdugumuz fonk adi
cv.setMouseCallback("Mouse",mouse)

# ekeranin uzerınde ısteduguımız  kadar 0 matrısını goruntuleleyebılmek ıcım
cv.imshow("Mouse",resim)
cv.waitKey(0)

"""run edınce calsımıor ama tammanını secıp shıft+enter deyınce oluyor"""


# MOUSE İLE CİZİM YAPMAK(DAİRE VE YAZI YAZDIRALIM)
"""ben bır resım okuyyayım ve resımden ıcktı alayım , resımden cıktıı aldıktan sornna mousemın sol tıkına bastıgım zaman bır tane daıre olsutursun ve daırenın ust kısmına gelsın ve deısn kı ;
ben daire olsturdum """

# circle() fonksiyonu, bir görüntü üzerinde bir daire çizmek için kullanılır. 

import cv2

# bu goruntuyu okuyalım
resim=cv2.imread("yesillikCocouk.jpg")

def daire_ciz(etkinlik,x,y,f,p):# flags,param o 2 sı az oncekı gıbı
    if etkinlik==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(resim,(x,y),35,(255,0,0)) # son 2 sı yarıcap , renk
        
# bıze bır perncere olustursun kı o oencere uzerınden yuruyebılbeyım