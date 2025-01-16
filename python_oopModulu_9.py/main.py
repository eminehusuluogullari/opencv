import school # olusturdugumuz modulu buraya dahıl etmemız gerek

Ogrenci1= school.Okul.Ogrenci("yilmaz","alaca",150,"11-a",100)
# Ogrenci1.disiplin()
# Ogrenci1.goruntule()    # sirayla calistırıp deneyebılırısın
# Ogrenci1.puan_degis()

Ogrenci1.school.Okul.Ogretmen("ahmet","siyah",4614148)
sifre=int(input("sifreyi giirn.."))
if sifre == Ogretmen.sifre:
    Ogrenci1.disiplin()
else:
    print("boyle bir yetkiniz yoktur")


# Ogrenci1.hoca_yakalama()
# Ogrenci1.goruntule() 

# ıgretmen objemızı olusturduk
Ogretmen=school.Okul.Ogretmen("ali","akca",124578)
Okul=school.Okul("vefa okulu")

while True:
    print("""
    sevgili {} sakinleri , okulumuza hosgeldiniz
   """.format(Okul.isim))

    islem=input("ogrenci islemi icin 1 e , ogretmen islmei icin 2 ye , cikis ici '*' a basin")
    if islem=="1":
        print("ogrenci sistemindesniz")
        islem2=input("puan goruntulemek icin 1 e ogrenci bilgisi goruntulemek icin 2 ye basin")
        if islem2=='1':
            if Ogrenci1.disiplin_puani!=None:
                Ogrenci1.puan_goruntule()
        elif islem2=='2':
            Ogrenci1.goruntule()
        else:
            print("hataali deger girdiniz , sistemi mesgul ettiniz ogrtemene bilgi verildi")
            Ogrenci1.hoca_yakalama()
    elif islem=="2":
        print("ogretmen bilgi sistemindesniz")
        islem3=input("""
        yapabileceginiz islemler ,
        disiplin icin 1,
        ders notu icin 2
        ogretmen bilgisi icin 3 e basin
        """)
        if islem3=="1":
            sifre==int(input("lutfen ogretmen sifrenizi girinn"))
            if sifre==Ogretmen.sifre:
                Ogrenci1.disiplin()
            elif sifre!= Ogretmen.sifre:
                print("yanlis sifre girdiniz hocaya haber veriliyor")
                Ogretmen.hoca_yakalama()
        elif islem3=="2":
            sifre==int(input("lutfen ogretmen sifrenizi girinn"))
            if sifre==Ogretmen.sifre:
                if Ogrenci1.disiplin_puani!=None:
                    Ogrenci1.puan_degis()
            elif sifre!= Ogretmen.sifre:
                print("yanlis sifre girdiniz hocaya haber veriliyor")
                Ogretmen.hoca_yakalama()
        elif islem3=="3":
            Ogretmen.ogretmen_bilgi()
    elif islem=="*":
        break



