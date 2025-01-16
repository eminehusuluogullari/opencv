# ! web cam kullanabılme 
# ! el bagnatıları takıbı tepsıtı
import cv2
import mediapipe as mp 
# modulumuzu ımport ettık el yuz vs algılama takıp etme ıcın kullanılan moduldur 

webcam=cv2.VideoCapture(0) # kamramızı acalım

""" 
min_detection_confidence=0.5: Modelin bir yüz, el veya vücut noktasını algılaması için gereken minimum güven seviyesidir (%50).

min_tracking_confidence=0.5: Tespit edilen bir hareketi takip ederken modelin güven oranıdır (%50). Daha yüksek bir değer modelin daha kesin sonuçlar vermesini sağlar, ancak performansı düşürebilir.
"""

mp_cizim=mp.solutions.drawing_utils # eger bunu cagırmazsak tespıt yanı cizim işlmerli gerceklesemez o zamada bu bır makıne ıgrebmesı dersı olmaz 
mp_butunsel=mp.solutions.holistic # holıstık butunsel demek butun bolgelere ulasabılmek ıcın vucuttakı 

with mp_butunsel.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as butun:

    #sıralı goruntu okuycaz ya
    while True: # webcam da vıyo gıbı ısledıgı ıcın donguye sokmamız gerek
        # kontrol booelan degrelrdır eger resımın ııcnde bısey yoksa bıze false dondurcektır
        kontrol,resim=webcam.read(); # goruntuyu oku

        # bgr yı rgb ye donsuturmem lazım kı daha duzgun kullanabıleyım
        resim_rgb=cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)

        sonuc=butun.process(resim_rgb)

        resim=cv2.cvtColor(resim_rgb,cv2.COLOR_RGB2BGR)

         # Sol el bağlantılarını çiz
        if sonuc.left_hand_landmarks:
            mp_cizim.draw_landmarks(resim, sonuc.left_hand_landmarks, mp_butunsel.HAND_CONNECTIONS)

        # Görüntüyü göster
        cv2.imshow("El Bağlantıları", resim)

        # ESC tuşuna basıldığında çık
        if cv2.waitKey(20) & 0xFF == 27:
            break

# Kaynakları serbest bırak
webcam.release()
cv2.destroyAllWindows()

# ! makine ogrenemsını kullanmak ııcn mediapipe modulunu kullanmamız gerek

# termınalden kusulrumu yapıyoruz; pip install mediapipe

# kullaanacagmız modul sayısınde le yuz vs dekı baglantı noktalrını bulabılırız

# bır hata mesajı duurmu var ama aynıısnı yaptım aslıdna












# ! yuzumuzu tanıtabılmek ıcın ; 

import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

mp_cizim = mp.solutions.drawing_utils
mp_butunsel = mp.solutions.holistic
# holıstık butunsel demektır butun tespıtlerı kapsar = el yuz vs.

#holsıtıc model baslatılıyor
with mp_butunsel.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as butun:
    while True:
        kontrol, resim = webcam.read()
        if not kontrol:
            print("webcam acilamadi")
            break

        # bgr yı rgb ye donusturuyoruz
        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

        # Görüntü üzerinde işlem yapılıyor
        sonuc = butun.process(resim_rgb)
        # Elleri çiz
        if sonuc.left_hand_landmarks:
            mp_cizim.draw_landmarks(resim, sonuc.left_hand_landmarks,  mp.solutions.hands.HAND_CONNECTIONS)

        # Yüzü çiz
        if sonuc.face_landmarks:
            mp_cizim.draw_landmarks(resim, sonuc.face_landmarks, mp.solutions.face_mesh.FACEMESH_TESSELATIO)

        # Görüntüyü göster
        cv2.imshow("Pencere", resim)

        # ESC tuşuna basıldığında çık
        if cv2.waitKey(20) & 0xFF == 27:
            break

        # Kaynakları serbest bırak
        webcam.release()
        cv2.destroyAllWindows()


# ! vucut modelı ve takıbı


import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

mp_cizim = mp.solutions.drawing_utils
mp_butunsel = mp.solutions.holistic

with mp_butunsel.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as butun:
    while True:
        kontrol, resim = webcam.read()
        if not kontrol:
            print("webcam acilamadi")
            break

        # bgr yı rgb ye donusturuyoruz
        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

        # Görüntü üzerinde işlem yapılıyor
        sonuc = butun.process(resim_rgb)
        
        resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

        mp_cizim.draw_landmarks(resim, sonuc.left_hand_landmarks,  mp.butunsel.hands.HAND_CONNECTIONS)

        mp_cizim.draw_landmarks(resim, sonuc.face_landmarks, mp.butunsel.face_mesh.FACEMESH_CONNECTIONS)

        mp_cizim.draw_landmarks(resim, sonuc.pose_landmarks, mp.butunsel.face_mesh.POSE_CONNECTIONS)

        if cv2.waitKey(20) & 0xFF == 27:
            break

        cv2.imshow("pencere" ,resim)

        # Kaynakları serbest bırak
        webcam.release()
        cv2.destroyAllWindows()


"""
! burda cızımın ozleıkklerını degıstrırız boyle

 mp_cizim.draw_landmarks(resim, sonuc.pose_landmarks, mp.butunsel.face_mesh.POSE_CONNECTIONS,mp_cizim.DrawingSpec((255,0,255),4,1)) 

ordakı 1 demek noktaların yarıcapı , 4 ıse cızgılerın kalınlıgı

 rengını kalınlıgını yarıcap degıtırıdk
 """

"""eger cızgılerın rengını degısrtımek ısrerk;

mp_cizim.draw_landmarks(resim, sonuc.pose_landmarks, mp.butunsel.face_mesh.POSE_CONNECTIONS,mp_cizim.DrawingSpec((255,0,255),4,1),mp_cizim.DrawingSpec((0,255,0),5,1)) 
 
 boyle yapmamız gerekuyor """

