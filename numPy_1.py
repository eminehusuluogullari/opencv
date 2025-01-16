import numpy 
print(numpy.__version__)  # numpy yukledım

# numpy nedir ?
# matematıksel hesaplama gerektıren ıslemler daha kolay ve hızlı gerceklestırılebılır

# dizi olsuturma 

import numpy
array = numpy.array([1,2,3])
print(array)

liste=[5,6,7]
dizi=numpy.array(liste)
print(dizi)

# dizimizin tam sayılardan mı kesırlı sasyılardan mı olusturgunu ogrenelım

import numpy as np
dizi2=np.array([1.5,2.6,7.8])
liste=[5,6,7]
dizi=numpy.array(liste)
print("'dizi' ismindeki degiskenin tipi: ",dizi.dtype)
print("'dizi2' ismindeki degiskenin tipi: ",dizi2.dtype)
# int 32 = 32 bıtlık verı demek

# dizilerde 4 işlem (numpy şle kolaylıkla gerceklsestırılebılıyor)

liste1=[1,2,3]
liste2=[4,5,6]
liste3=liste1+liste2 # bız burda bırsletırmıs olduk aslında tplamma yapamadık
liste3 # sonuc = [1, 2, 3, 4, 5, 6]

# dizilerde elemanları toplamayı soyle yapıyoruz

dizi1=np.array([1,2,3])
dizi2=np.array([4,5,6])
dizi3=dizi2+dizi1
print("toplama " , dizi3) # [5 7 9] 
dizi3=dizi2*dizi1
print("carpma " , dizi3) # [ 4 10 18]

# numpy ıle olsuturulmus bır dızının satır ve sutunlarını ogrenmek

import numpy as np
dizi=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(dizi)
"""
[[ 1  2  3]
 [ 4  5  6]          4 satır 3 sutundan olusuyor
 [ 7  8  9]
 [10 11 12]]
 """
dizi.shape # (4, 3)

# arange ve reshape methodu nedır ? 
# gırılen sayıya (aralık) kadar olan degrlerdedn dızı olusturur = arange
# reshape = var olan dızıyı verilen satır ve sutun degreıne gore ayırır

import numpy as np
dizi=np.arange(10) # 0 dan 10 akadar olan sayılrdan dızı olusturur
print(dizi) # [0 1 2 3 4 5 6 7 8 9]
dizi2=np.arange(3,10) # 3 den 9 a kadar olan sayılardan dızı olsuturur
dizi3=np.arange(3,9).reshape(2,3) # range ıle olusturulan dızıyı reshape ıle 2 satır 3 sutuna bol
print(dizi3)
"""
[[3 4 5]
 [6 7 8]]
"""

# tek dizide 4 işlem

import numpy as np
dizi=np.arange(1,10)
print(dizi)
# her bır elemana 5 eklemek sıtıyorsak
dizi=np.arange(1,10) + 5
print(dizi)
# karesını almak ıstıyorsak
dizi=np.arange(1,10) ** 2
print(dizi)

# zeros ones eye kavramları nelerdır ?
# zeros = elemnalrı sadece 0 olan ıstedıgın kadar elemanlı dızı olusturma
# ones = elamları sadece 1 lerden olusan dızı uertır
# eye = bırım matrıs olsururr
import numpy as np
dizi=np.zeros(10)
print(dizi) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 0 lardan olusan matrıs olusturmak ıstersek

dizi2=np.zeros((5,6))
print(dizi2)
"""
[[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
 """

dizi3=np.ones(3)
print(dizi3) # [1. 1. 1.]

dizi3=np.ones((3,4)) * 5 
print(dizi3) 
"""
[[5. 5. 5. 5.]
 [5. 5. 5. 5.]
 [5. 5. 5. 5.]]
"""

dizi5=np.eye(3)
print(dizi5)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

# olsturulacak dızının aynı elemanlardan olusması ?
# full fonksıyonu ıle bunu saglarız (satır , sutun,satır ve sutuna atanacak deger)
# gırılen parametrelere uygun bır matrıs yazaruz

import numpy as np
dizi=np.full((4,5),4.5)
print(dizi)

# maksimum ve mınımum degere nasıl ulasabılırız ?

import numpy as np
dizi=np.array([1.88,1.77,1.44,1.56,1.58,1.79])
print(dizi)

dizi.max()
dizi.min()

# soru 
"""numpy modulu ıcerısınde bulunan arange fonksıyonu ıle 5 den 25 e kadar (dahıl)
bir dizi olusturun .
olusturdugunuz dızıdekı cıft sayıları ekranda gosterın
"""
import numpy as np
dizi=np.arange(5,26)
for eleman in dizi: # dizidekı her sayıyı eleman olarak adlandırıyoruz
    if eleman %2==0:
        print(eleman)

# bir dizinin elamanlrana nasıl ulasırız ?

import numpy as np
dizi=np.array([1.88,1.77,1.44,1.56,1.58,1.79])
print(dizi)
dizi[2] # 3. elamana ulasırız
dizi[4]=5 # dıznın elemanını degıstırmıs olsuyoruz
print(dizi[4]) # degısmıs mı dıye ekrana yazdırıp kontrol edıyoruz 

dizi1=np.array([[0,1,5,9],[4,8,9,6]])
# 8 elemanuna ulasmak ıstersek
print(dizi1[1][1]) # bırıncı ındıstekı 1. elaman cunku o

# nokta carpım nedır ? 





