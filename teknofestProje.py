"""
jetsonla atıs yapma emrı verme ;

import Jetson.GPIO as GPIO
import time

# GPIO pinlerini tanımla
pin = 12  # Örneğin 12 numaralı GPIO pini

# GPIO pinlerini yapılandır
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

# Atış yapma emri
GPIO.output(pin, GPIO.HIGH)  # Pini yüksek yap (açık)
time.sleep(1)                # 1 saniye bekle
GPIO.output(pin, GPIO.LOW)   # Pini düşük yap (kapalı)

# GPIO ayarlarını temizle
GPIO.cleanup()

"""

import cv2
import numpy as np

def sabit_hedef_imhasi(cap):
    alt_kirmizi1 = np.array([0, 120, 70])  # Kırmızı için ilk aralık (açık ton)
    üst_kirmizi1 = np.array([10, 255, 255])
    alt_kirmizi2 = np.array([170, 120, 70])  # Kırmızı için ikinci aralık (koyu ton)
    üst_kirmizi2 = np.array([180, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            print("kamera acilmadi")
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maske1 = cv2.inRange(hsv, alt_kirmizi1, üst_kirmizi1)
        maske2 = cv2.inRange(hsv, alt_kirmizi2, üst_kirmizi2)
        maske = maske1 + maske2
        konturlar, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for kontur in konturlar:
            alan = cv2.contourArea(kontur)
            if alan > 500:
                x, y, w, h = cv2.boundingRect(kontur)
                cx = x + w // 2
                cy = y + h // 2
                cv2.putText(frame, f"Koordinatlar: ({cx}, {cy})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow('Kamera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('x'):
            print("acil durum")
            print("sistem durduruldu..")
            break

def hareketli_hedef_imhasi(cap):
    alt_kirmizi1 = np.array([0, 120, 70])
    üst_kirmizi1 = np.array([10, 255, 255])
    alt_kirmizi2 = np.array([170, 120, 70])
    üst_kirmizi2 = np.array([180, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            print("kamera acilmadi")
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maske1 = cv2.inRange(hsv, alt_kirmizi1, üst_kirmizi1)
        maske2 = cv2.inRange(hsv, alt_kirmizi2, üst_kirmizi2)
        maske = maske1 + maske2
        konturlar, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for kontur in konturlar:
            alan = cv2.contourArea(kontur)
            if alan > 500:
                x, y, w, h = cv2.boundingRect(kontur)
                cx = x + w // 2
                cy = y + h // 2
                cv2.putText(frame, f"Koordinatlar: ({cx}, {cy})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow('Kamera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('x'):
            print("acil durum")
            print("sistem durduruldu..")
            break

def dost_dusman_hedef_imhasi(cap):
    alt_kirmizi1 = np.array([0, 120, 70])
    üst_kirmizi1 = np.array([10, 255, 255])
    alt_kirmizi2 = np.array([170, 120, 70])
    üst_kirmizi2 = np.array([180, 255, 255])
    alt_mavi = np.array([100, 150, 0])
    üst_mavi = np.array([140, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            print("kamera acilmadi")
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maske1 = cv2.inRange(hsv, alt_kirmizi1, üst_kirmizi1)
        maske2 = cv2.inRange(hsv, alt_kirmizi2, üst_kirmizi2)
        maske_kirmizi = maske1 + maske2
        maske_mavi = cv2.inRange(hsv, alt_mavi, üst_mavi)

        konturlar_kirmizi, _ = cv2.findContours(maske_kirmizi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for kontur in konturlar_kirmizi:
            alan = cv2.contourArea(kontur)
            if alan > 500:
                x, y, w, h = cv2.boundingRect(kontur)
                cx = x + w // 2
                cy = y + h // 2
                cv2.putText(frame, f"Koordinatlar: ({cx}, {cy})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.putText(frame, "dusman", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        konturlar_mavi, _ = cv2.findContours(maske_mavi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for kontur in konturlar_mavi:
            alan = cv2.contourArea(kontur)
            if alan > 500:
                x, y, w, h = cv2.boundingRect(kontur)
                cx = x + w // 2
                cy = y + h // 2
                cv2.putText(frame, "dost", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow('Kamera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('x'):
            print("acil durum")
            print("sistem durduruldu..")
            break

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("kamera acilmadi")
        return

    print("3 aşamadan oluşan yarişmamiz...")
    print("1. aşama = sabit hedef imhasi")
    print("2. aşama = hareketli hedef imhasi")
    print("3. aşama = hareketli dost-düşman hedef imhaiı")
    print("cikis yapmak için 'q' tuşuna basin")
    print("ACİL DURUM BUTONUNU AKTİF ETMEK İCİN x E BASIN")

    secim = input("Seçim yapin: ")

    if secim == "1":
        print("sabit hedefi vurmak icin program basladi....")
        sabit_hedef_imhasi(cap)
    elif secim == "2":
        print("hareketli hedefi vurmak icin program basladi....")
        hareketli_hedef_imhasi(cap)
    elif secim == "3":
        print("hareketli dost dusman ayrimiyla hedefi vurmak icin program basladi....")
        dost_dusman_hedef_imhasi(cap)
    else:
        print("hatali secim yaptiniz")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()