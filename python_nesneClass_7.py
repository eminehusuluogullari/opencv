# nesne tbanalı programlama 

class Araba():
    model="reno"
    renk="gümüş"
    beygir_gucu=110
    silindir=4
    def __init__(self):
        print("init fonksiyonu cagirildi")

class Kitap(): # kitap sinifi olusturmus olduk alta ozlleıklerı gırcez
    sayfaSayisi=250
    konu="fantastik"
    cilt=3

# sınıfı objenın ıcıne atatdık
harry_potter=Kitap()

harry_potter.sayfaSayisi # shıft enter dersek sayfa sayısı gelır 

class Kitap():  # `Kitap` adında bir sınıf tanımlanıyor.
    sayfaSayisi = 150  # Sınıf seviyesinde bir değişken tanımlanıyor. Tüm `Kitap` nesneleri için varsayılan olarak 150.
    
    def __init__(self):  # `__init__` metodu, sınıfın kurucu (constructor) metodudur. Yeni bir nesne oluşturulduğunda otomatik olarak çalışır.
        print("init cagırıldı")  # Kurucu metod çalıştığında ekrana bu mesajı yazdırır.


# Kitap adında bir sınıf tanımlanıyor.+
class Kitap():  
    # Sınıfın yapıcı (constructor) metodu tanımlanıyor. Bu metod, sınıfın yeni bir nesnesi oluşturulduğunda otomatik olarak çalışır.
    def __init__(self, sayfaSayisi, cilt, konu):
        # Nesneye ait sayfa sayısı özelliği, yapıcı metoda verilen değere ayarlanıyor.
        self.sayfaSayisi = sayfaSayisi
        # Nesneye ait konu özelliği, yapıcı metoda verilen değere ayarlanıyor.
        self.konu = konu
        # Nesneye ait cilt özelliği, yapıcı metoda verilen değere ayarlanıyor.
        self.cilt = cilt

# Kitap sınıfından harry_potter adında yeni bir nesne oluşturuluyor.
# Bu nesne, sayfa sayısı olarak 255, cilt numarası olarak 16 ve konu olarak "fantastik" değerlerini alır.
harry_potter = Kitap(255, 16, "fantastik")
harry_potter.sayfaSayisi # verir


# methot kavramı detaylıca 

class Kitap():  
    def __init__(self, isim, cilt, konu,fiyat):
        self.isim = isim
        self.konu = konu
        self.cilt = cilt
        self.fiyat=fiyat
    def zamYap(self,zam):
        self.fiyat+=zam

# harry_potter=Kitap("harry potter",3,"fantastik",56)
# harry_potter.zamYap(10)
# harry_potter.fiyat # zam yapılmıs fıyatı gosterırı
    def ciltno_guncelle(self,ciltSayisi):
        self.cilt+=ciltSayisi
    def bilgi_goster(self):
        print("""
        kitap bilgileri
        kitap ismi :{}
        kitap ciltSayisi :{}
        kitap konusu :{}
        kitap fiyat :{}
        """.format(self.isim,self.konu,self.cilt ,self.fiyat))

harry_potter = Kitap(255, 16, "fantastik")
harry_potter.bilgi_goster()

# kalitim....
class motor():
    def __init__(self,silindir_sayisi,beygir,yakit,vitesSayisi):
        self.silindir_sayisi=silindir_sayisi
        self.beygir=beygir
        self.yakit=yakit
        self.vitesSayisi=vitesSayisi

class Araba(motor): # kalitim yapmıs olduk
    pass # bunu yapmazsak alta gecerken hata verır ama boyle olursa bos gecebılır

bmw=Araba(6,190,"dizel",7) # araba sınıfının ıcınde bmv yı olusturmus olduk
bmw # gormek ıcın cıktıyı
bmw.beygir 

# ovverriding (iptal etme)
"""
mıras aldıfımız metotları aynı ısımle kendı sınıfımızda tanımlarsak , artık metodu cagırınca bızım kendı fonk. gelır mıras aldıgımız degıl 
"""
# self parametresi, sınıf içindeki değişken ve metodların hangi nesneye ait olduğunu belirtir.
#Eğer self kullanmazsak, Python hangi nesneye ait özellik veya metodu kullanacağını bilemez ve hata verir.

class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifin init fonksiyonu")

        self.isim=isim
        self.maas=maas
        self.departman=departman
    
    def bilgileriGoster(self):
        print("calisan sinifin bilgileri..")

        print("isim : {} \n maas :{} \n departman :{}\n" .format(self.isim,self.maas,self.departman))

    def departmanDegistir(self,yeniDepartman):
        self.departman=yeniDepartman

class Yonetici(Calisan):

    # init fonksıyonumuzu ovverıde etcez
    def __init__(self,isim,maas,departman,kisiSayisi):
        print("yonetici sinifin init fonksiyonu")

        self.isim=isim
        self.maas=maas
        self.departman=departman
        self.kisiSayisi=kisiSayisi

    def zamYap(self,zam_miktari):
        self.maas += zam_miktari

yonetici =Yonetici ("oguz",3500,"bilisim",10)

# ovverıde ederken aynı seylerı bu self ıle ozellık tanımlamaları tekrar tekrer yapıyoruz yaz ona gerek olmadan super ıle yapalım bıde

class YoneticiAsistani(Calisan):

    # init fonksıyonumuzu ovverıde etcez
    def __init__(self,isim,maas,departman,kisiSayisi):
        # bu super yukardakı uretteıgımız sınıftan bır fonksıyon cagırmak ıcın kullanılrı
        # initi cagırdık

        super().__init__("emine",2000,"bilisim")
        self.kisiSayisi=kisiSayisi
        print("yoneticiAsistani sinifin init fonksiyonu")

    def zamYap(self,zam_miktari):
        self.maas += zam_miktari

yonetici2 =YoneticiAsistani("oguz",4000,"siber",5) 
""" bı su usttkı satırı calsıtırınca 
calisan sinifin init fonksiyonu
yonetici sinifin init fonksiyonu
"""