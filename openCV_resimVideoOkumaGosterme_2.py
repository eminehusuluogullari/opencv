import cv2

# fotografı ac

# imread = goruntuyu okuyabılmek ıcın gereklı fonksıyon

resim=cv2.imread("resim.jpg") # matrıssel oldu degıskene atamamız gerek
cv2.imshow("Resim",resim) # resmi goruntuler 
cv2.waitKey(0) # sonsuza kadar goruntu ekranda kalır , herhangı bır tusa basınca otomatık kapanır
# cv2.waitKey(2000)  # 2 sn ekranda gosterırı

# Tüm pencereleri kapatın
# cv2.destroyAllWindows()


# vidyoyu ac

# web cam uzerınden okuma da yapabılır = videocapture
video=cv2.VideoCapture("video.mp4")
#video sirali fotograf oldugu ıcın dongu gerek
while True:
    kontrol,yakala=video.read() # kontrol video varmı dıye true false 
    if not kontrol: # kontrol basarısız ıse
        print("video okuma basarisiz")
    cv2.imshow("goruntu",yakala)
    if cv2.waitKey(20) & 0xFF==ord('p'):# p tusuna 20mlsn basarak bu kod sonlancak ve vıdyo kapanacak bu zorunlu
        break








