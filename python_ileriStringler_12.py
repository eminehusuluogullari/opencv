"""
# ! upper
"pyTHon".upper() = tum karakterlerı buyuk harf yapar

# ! lower
kucuk harf yapar

# ! replace ( 1 er parametre almak orunda degıl (xhg,ghd)) olarak da cevrıme yapabılır
guncelliyor dıyleım

"herkes ana baci gardas".replace("a","o") # a yı o yap
" jhdfg hgf hj ".replace(" ","-") # bolsukları tre yap

# ! starswith() = true false ıle anıt verırı onunla baslıyor mu ıdye bakar

"python".starswith("py") # true

# ! endswith = aynısının bıtme durumu

# ! split = ayırmma

liste = "jhdsgfjgsd jhdsf fhjds".split(" ") # bolsuklara gore ayır

# ! strip(x) = strıngın basında ve sonunda bulunan x dgerlerını sıler

# ! istrip(x) = sadece basındakı x lerı ssıler 
# ! rstrip(x) = sadece sonundaki x degerlerini siler

"<<<<<<<<<<<<<<<<<<<<hdghdfghdg<<<<<<<<<<<<<<".strip("<")

#! join = listenın elemanlarını bır strıng dgerıyle bırlestırmeye yarar

liste= ["21","78","2016"]
"/".join(liste) # 21/78/2016

# ! count(x) = strıng ıcındekı x degerını sayar

" ada kapisi acildi".count("a") # 4

# ! find = buldugu ındexı bıze dondurur

"araba".find("a") # 0
"""