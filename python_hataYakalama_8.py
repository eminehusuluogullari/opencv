# ! hata fırlatma

try:
    a=int("jdgsfjhs654")
    print("pragram burda")
except ValueError:
    print("bir hata olustu")
    
print("bloklar sona erdi")

# 

try:
    a=int(input("sayi1"))
    b=int(input("sayi2"))
    print(a/b)
except ValueError:
    print("lutfen inputu dogru girin")
except ZeroDivisionError :
    print("bir sayi 0 a bolunmez")
print("bloklar sona erdi")

"""
try:
............

except:
............
except:
............

finally:
! mutlaka calısması gereken bır kod varsa buraya yazcaz 

normalde ttry except kısmında excepte geldıkten sonra devam etmıyor ya
"""

# ! hata fırlatma = raise kullanırız

def tersCervir(s):
    if(type(s) != str): # tıpı sttr degılse 
        raise ValueError("lutfen dogru bir input girin")
    else:
        return s[::-1] # ters cevırmek


"""
`try-except`, programda oluşabilecek hataları yakalayıp programın durmasını engelleyerek hatayı kontrol altına alır. Öte yandan, `raise` belirli koşullarda bilinçli olarak hata fırlatmak için kullanılır ve yakalanmazsa programın durmasına neden olur. Kısacası, `try-except` hataları yönetirken, `raise` hata oluşturur.
"""