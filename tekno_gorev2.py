import cv2
import numpy as np

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



def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("kamera acilmadi")
        return       

    hareketli_hedef_imhasi(cap)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()