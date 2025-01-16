"""
kümeler bır elemandan sadece 1 tane tutan verı tipidir 
küme = set
"""
x={1,2,3} # bır kumem

liste=[1,2,3,4,2,5,3,6,5,1,2,6]
x=set(liste) # verı tıpı donusturme yapılıyor ve her elamdan sadece 1 tanesı alınır 

# ! difference metodu = 2 kumenın farkını almamızı saglıyor 

kume1={1,2,3,10,34,100,-2}
kume2={1,2,23,34,-1}

kume1.difference(kume2)

# kume1 ın kume2 den farkını kume1 e ata
kume1.difference_update(kume2)

# ! discard = içine verilen degerı kumeden cıkarır , eger o deger yoksa hıc bısey olmaz

kume2={1,2,23,34,-1}
kume2.discard(1)

# ! intersection = ortak elemanları bulmak ıcım kullanılır
kume1={1,2,3,10,34,100,-2}
kume2={1,2,23,34,-1}

kume1.intersection(kume2)

# ! intersection_update = kume kesısımlerı ve guncelleme
# ! indisjoint = ayrık kume mı dıye bakıyoruz , ortak elemnarı varmı dıye

kume1={1,2,3,10,34,100,-2}
kume2={1,2,23,34,-1}
kume3={30,40,50}

kume1.isdisjoint(kume2) # 1 ıle 2 ayrık mı dıyoruz sonrada bakıyoruz ortak eleman var yanı false

# ! issubset = alt kumesı mı kontrolu ıcın

kume1={1,2,3,10,34,100,-2}
kume2={1,2,3,23,34,-1}
kume3={30,40,50}
kume1.issubset(kume2) # kume1 kume2 nın alt kumesı mı evet truee

# ! union = bırlesım kumesı

kume1={1,2,3,10,34,100,-2}
kume2={1,2,23,34,-1}
kume1.union(kume2) # 2 kumeyı bırlstır ama kume ya o yuzden aynı elemandan sadece 1 kere bulunabılır

# ! update = bırlesım kummsını kume 1 e atamak ıcın kullanılır

kume1.update(kume2) # kume bırın ıcı artık guncellendı butun elamanlar var ıcınde 