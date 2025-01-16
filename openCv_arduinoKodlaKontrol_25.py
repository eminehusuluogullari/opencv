"""
ardunıoyu kodla kontrol edıcez bunun ıcınde serıal modulunu kullanmamzı gerek

"""
import serial

# port ısmınde bır degısken gııryoruz = modulumuzu cagırdık.sınıfımızı cagırıyoruz 
port=serial.Serial('com5',9600) # ilkı port bilhisi
# aurıdnyoyu baglaıdktan sonra ıdesını acıyoruz ve sonra aracalr kısmından aurdınyaomuzun hangı porta baglı oldugunu ogrenıyoruz (com5 salladım burda)

while True:
    veri_girisi = input("LED'i yakmak için 'a' harfine basın, söndürmek için 'b' harfine basın: ")

    if veri_girisi == "a":
        port.write(b'a')  # 'a' komutunu gönder
    elif veri_girisi == "b":
        port.write(b'b')  # 'b' komutunu gönder
    else:
        print("Geçersiz giriş! Lütfen 'a' veya 'b' harfini giriniz.")
# bıt tıpınde gonderebılmek ıcın basına b yazdık

# ! burası bıttı sımdı aurıdnyo ıdesınde kodumuzu yazcaz (besıncıdekı)

