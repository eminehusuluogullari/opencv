# JSON = verileri tutmak için kullandiğimiz yapıdır
# ornEk kullanımı ; 
"""
# anahtarlar 
# hep strıng

"isim" : "yilmaz"
"yas" : 19

"arabalar" : { "marka1" : "ford" , "marka2" : "seat"}

"evlilik" : false

"""
isim ={"isim":"yilmaz"} # sözlük
isim["isim"] # ciktisi yılmaz dir

import json # json u dahıl etmıs olduk

kullanici = '{"isim":"ali" , "soyisim":"aslan" , "yas":16}' # sozluk olusturmus olduk dısına tırnak koyunca json oldu
bilgileri_cek=json.loads(kullanici) 
bilgileri_cek # {"isim":"ali" , "soyisim":"aslan" , "yas":16} burayı verıır
# sozluge donusturulmus oldu bilgileri_cek

kullanici=json.dump(bilgileri_cek) # gerı jsona donusturmus olduk sozlugu
kullanici # shıft enter yapınca json gorunur 

# json dosyamızı olusturmustuk acalım
import json
with open ("yol.json","r",encouding="utf-8") as dosya:
    print(dosya.read())

""" boyle okur 
{
    "isim":"ali",
    "yas":19
}
"""

# ornek
# bır json uzantılı dosya olusturmak ve buradaı bılgıyı oraya yazdırmaya calısaz
import json
bilgi = '{"isim":"ali" , "yas": 19}'
sozluk = json.loads(bilgi) # bilgi jsonu , sozluge donusecektır 
print(sozluk) # {'isim': 'ali', 'yas': 19}

# w = olustur ve ıcıne yazcaz demek
with open("veri.json","w",encoding="utf-8") as yazdir:
    json.dump(sozluk,yazdir)

# proje 
#aynı yazdıma ama bır hata vvar

"""
import json 
import time 

print("\nkullanici bilgi sistemine hosgeldiniz\n")

while True:
    islem=input("lutfen yapmak istediginiz islmei girin\n kullanici bilgisi icin 1 \nkullanici maasina zam yapmak icin 2\ncikmak icin 3 e bas ")

    if islem=="3":
        break

    elif islem=="2":
        #sadece okumak yetemz zam yapcaz r+
        with open("veriler.json","r+",encoding="utf-8") as oku:
        veri_oku=json.load(oku)
        zam= int(input("zam miktari girin..."))
        veri_oku["maas"]+=zam
        oku.seek(33) # zamlı maası en sona degılde olmadı gereken yere eklesın dıye seek yaptık
        json.dump(veri_oku["maas"],oku)

    elif islem=="1":
        with open("veriler.json","r",encoding="utf-8") as oku:
        veri_oku=json.load(oku)

        print("suanda veriler okunuyor....")
        time.sleep(2)

        print("kullanici adi:" ,veri_oku["isim"])
        print("kullanici yasi:" ,veri_oku["yas"])
        print("kullanici maas:" ,veri_oku["maas"])
        time.sleep(2)
        if verileri_oku["medenihal"]==False:
            print("bekar")
            time.sleep(2)
        else:
            print("evli")
            time.sleep(2)
"""










