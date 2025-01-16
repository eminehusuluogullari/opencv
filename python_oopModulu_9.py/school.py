import random # sayı degıskenı ıcın olusturduk

class Okul:
    def __init__(self,isim):
        self.isim=isim
    
    class Ogrenci:
        def __init__(self,isim,soyisim,no,sinif,disiplin_puani,ders={"turkce":0 , "matematik":0}):
            self.isim=isim
            self.soyisim=soyisim
            self.no=no
            self.sinif=sinif
            self.disiplin_puani=disiplin_puani
            self.ders=ders

        def disiplin(self):
            disiplin=input("ogrenci disipline gittimi (evet hayur)")

            if disiplin=="evet":
                self.disiplin_puani-=10
                if self.disiplin_puani<=0:
                    print("ogrenci kaydi silinir")
                    self.isim=None
                    self.soyisim=None
                    self.no=None
                    self.sinif=None
                    self.disiplin_puani=None
                else:
                    print("ogrenci disiplin puani 10 puan dusuruldu", self.disiplin_puani)
            elif(disiplin != "evet" or disiplin=="hayir"):
                print("mesgul etme")
        def goruntule (self):
            print("""
            isim:{}
            soyisim:{}
            no:{}
            sinif:{}
            disiplin puani:{}
            """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplin_puani))
        def puan_degis(self):
            girdi=input("puanini degistirmek istediginiz dersi girin..")
            if girdi=="turkce":
                self.ders["turkce"]=int(input("puani girin.."))
                if 0<=self.ders["turkce"]<=100:
                    print("puan degişti : ", self.ders["turkce"])
                else:
                    print("puan degismedi")
                    self.ders["turkce"]=0

            elif girdi=="matematik":
                self.ders["matematik"]=int(input("puani girin.."))
                if 0<=self.ders["matematik"]<=100:
                    print("puan degişti : ", self.ders["matematik"])
                else:
                    print("puan degismedi")
                    self.ders["matematik"]=0

            else:
                print("boyle bir ders yok")

        def puan_goruntule(self):
            print("""
            matematik not:{}
            turkce not:{}
            """.format(self.ders["matematik"],self.ders["turkce"]))

        def hoca_yakalama(self):
            sayi=random.randint(1,2) # random olarak ya 1 ya 2 olsuturacak demdk
            if sayi==1:
                print("hocaya yakalandik")
                self.disiplin_puani-=2
            elif sayi==2:
                print("yanlis alarm")

class Ogretmen: # disipiline gondermeyı hoca yapabıır (sifreyle giriiş yapcakı)
    def __init__(self,isim,soyisim,sifre="123456"):
        self.isim=isim
        self.soyisim=soyisim
        self.sifre=sifre
    def ogretmen_bilgi(self):
        print("""
        isim:{}
        soyisim:{}
       """.format(self.isim,self.soyisim))















