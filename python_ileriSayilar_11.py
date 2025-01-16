"""
! Taban: 10
İnsanlar tarafından en yaygın kullanılan sayı sistemidir. Her basamak, 10'un kuvvetleriyle çarpılarak ifade edilir.

123₁₀ = 1×10² + 2×10¹ + 3×10⁰ = 100 + 20 + 3 = 123

! Taban: 2 (bınary )
Bilgisayarların temel çalışma mantığıdır. Elektronik cihazlarda yalnızca 0 (kapalı) ve 1 (açık) değerleri kullanılır. Sayılar 2'nin kuvvetleriyle ifade edilir.

1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀

! Taban: 16
Genellikle bilgisayar sistemlerinde (örneğin bellek adreslemesi, renk kodları vb.) kullanılır. A-F harfleri 10-15 değerlerini temsil eder. Sayılar 16'nın kuvvetleriyle ifade edilir.

1A3₁₆ = 1×16² + 10×16¹ + 3×16⁰ = 256 + 160 + 3 = 419₁₀

!  10 ----------> 2     bin() fonksıyonu kullanılır
Onluk'tan İkilik'e (45₁₀):
45'i 2'ye bölerek kalanları yaz

45 ÷ 2 = 22 kalan 1
22 ÷ 2 = 11 kalan 0
11 ÷ 2 = 5  kalan 1
5 ÷ 2  = 2  kalan 1
2 ÷ 2  = 1  kalan 0
1 ÷ 2  = 0  kalan 1

bin(4) = 0b100 = b orda 2 lık taban oldugunu gosterır ,100 da 2lik halı
bin(10) = 0b10011 


! 10 ------------>16    hex() fonksiyonu kullanılır

Onluk'tan 16'lık'a (255₁₀):
255'i 16'ya bölerek kalanları yaz

255 ÷ 16 = 15 kalan 15 → F
15 ÷ 16  = 0  kalan 15 → F

hex(20) = 0x14  , xhexx oldugu ıcın 16*1 + 16 üzeri 0 dan da 4 

"""

# abs(x) = sayının mutlak degerını alamamızı saglar 
# round(x) = sayıllaır gercek hayatta nasıl yuvarlıyorsak onu yapar
# max(x,y,z....) = max sayıyı dondurur , mın de aynsıı
# sum(x,y,z....) = içindekı sayıları toplar , sadece sayı gonderılır
# pow(2,4) = 16 , üst alma fonksıyonu 2**4 de aynısı
# ! pow(64,0.5) = 8 , karekokonu alıyor 



