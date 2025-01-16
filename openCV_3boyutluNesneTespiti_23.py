"""
2 boyutlu goruntu uzeırnde 3 byutlu goruntu tespıtı
kupamızı ve ayakkabımızı tespıt etmeye caslıcaz

burdada medıapay kullanılır

with objectıron ısımlı dosyadakı sınıfımızı acmmaızı saglar 

static_image_mod=false // anlık olarak tespıt yapabllmemı saglar
ama eger =true dersem // normal onceden cekılmısgoruntuler uzzerınden tesspıt ıslemını gerceklestırmemı saglar

max_num_objects = goruntu yzerunde maxısmum kac adet tespıt ıslemı gercekelstırecegımızı yazarız

min_detection_confıdence=tespıt guvenlırlıgı

mın_tarcakıng_confıdence= takıp guvenırlırlıgı

modal_name= hangı model uzerınden ıslem gerceklestırecegımızdır

jdsfhgsjdfgj as nesne3d = jhfgjhdgf dekı sınıfımızı nesne3d olarak kullancaz demek

ımport cv2 as cv gıbı aaynıs sey

! medıapıa modleınde goruntu ıslemı gerceklestırırken goruntumuzu rgb ye cevırmemız gerekıyor = cvtColor ile gerceklesır 

rgb ye donsuturebılme parametresı = cv2.COLOR_BGR2RGB 

.process etmek = Mediapipe kütüphanesinde .process() fonksiyonu, bir görüntüyü veya video karesini işleyerek, belirli özelliklerin (örneğin yüz, el, vücut işaretleri gibi) tespit edilmesini sağlar.

"""
import cv2 
import mediapipe as mp

mp_3d=mp.solutions.objectron
mp_3d_cizim=mp.solutions.drawing_utils
resim=cv2.imread("ayakkabi.png")

with mp_3d.Objectron(static_image_mode= True , max_num_objects=1 , min_detection_confidence=0.3 , min_tracking_confidence=0.3 , model_name= "Shoe") as nesne_3d:
    rgb=cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)
    sonuc=nesne_3d.process(rgb)  # rgb ye donsuturme
    if sonuc.detected_objects: # nesnelrer tespıt edılıyorsa
        #  3 boyuutlu tespıt ıslemımızı gerceklestırecgız kı hatalrımızı cızdırelım (for ile)
        for tespit in  sonuc.detected_objects:  
            # ilk basta 3 boyutlu hatlarımızı cızdırıoruz
                                                                       # baglantı nokalarımızı safglaıycaz bununla
            mp_3d_cizim.draw_landmarks( # hat cızdırmek ıcın landmraks
                resim,
                tespit.landmarks_2d,
                mp_3d.Objectron.BOX_CONNECTIONS  # Doğru bağıntı tanımlaması
            ) # 2 boyutlu hatlarımızı cızdııryotuz
            # 2 boyutlu hatlarımızı da cızdırgımızıe gore artık bu resmı dıkdortgen prızması ıcıne almamız gerekır 
            """      
       +--------+
      /        /|
     /        / |
    +--------+  |     burdakı / ler varya onalrla da bu 2 dıkadortgen 
    |        |  +            /  basglnatı kurup olsturumasını saglıyor 
    |        | /
    |        |/
    +--------+
            """
    cv2.imshow("3D Detection" , resim)
    cv2.waitKey(0)










    # 1 hata verıyor 