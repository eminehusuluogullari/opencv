# mesela asagıdakı modulu yazarsak matematıksel formullerı kullanabırıır
import math # shift + enter deyınce dosyanın ıcıne ındıırlmıs vazıyette olacaktır 

#modullerın ıcındekı fonksıyonları nasıl kullanabılırız
factoriyel=math.factorial(7) # dıye kullanırız
faktoriyel # boylede sonuuc yazdırırız

# eger bu math bızım ıngılızce oldugu ıcın aklımıa gemezse onu soyle mat dıye
# degıstırebılırız ve adı artık mat dıye kullanılır
import math as mat # modulu farklı ısımde kullanma
karekok= mat.sqrt(4)
karekok # boylede sonuuc yazdırırız

# bellekten tasarruf
# bır modulun tum fonksıyonları yer kaplasın ıstemıyoolrsk 
from math import pow # math dan pow u kullancaz demek (for dan den demek)

# tarıh modulu
import datetime 
dir(datetime) # hangı fonksıyonları kapsadıgımızı gormek ıcın

help(datetime) # ılgılı modulun fonksıyonalrı hakkında bılgı verır

datetime.datetime.now() # bugunun tarıh saat bılgılerınıı verır

# 

import time 

print("selam")
time.sleep(4) # 4 sn sonraa alt satura gec
print("selam2")