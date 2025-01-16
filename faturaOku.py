import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def find_text_in_image(image_path, search_text):
   
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

   
    custom_config = r'--oem 3 --psm 6'  

    boxes = pytesseract.image_to_data(binary_image, lang='eng', config=custom_config, output_type=pytesseract.Output.DICT)

    fatura_ort_degeri = None
    for i, word in enumerate(boxes['text']):
           # print(f"kWh metni bulundu: {word}")
            
            if i + 1 < len(boxes['text']):
                sonraki_kelime = boxes['text'][i + 1]
                try:
                    fatura_ort_degeri = float(sonraki_kelime)  

                    print(f"Bulunan kWh değeri: {fatura_ort_degeri}")

                    print("Birim Fiyatı : 2TL\nOdenecek tutar = " ,(fatura_ort_degeri*2) )
                    break
                except ValueError:
                    pass  
    image_resized = cv2.resize(image, (800, 600))  # Görüntüyü boyutlandırma
    cv2.imshow("Görüntüdeki Metin", image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
    if fatura_ort_degeri is not None:
        print(f"FATURA ORT. değeri: {fatura_ort_degeri}")
    else:
        print("FATURA ORT. değeri bulunamadı.")
"""


image_path = "fatura10.jpg"  # Değiştirilebilir
search_text = "kWh"  # Aranacak metin: "FATURA ORT."

find_text_in_image(image_path, search_text)
