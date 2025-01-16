print(alaca) # bunu yazdık try except olmadan asagıda name error verdı 
# bıdaha boyle hata cıkarsa dıye excepte yazdık hata nameerror olursa o prıntı yazdıracak

try:
    print(alaca)
    print("jsdhfjfg")
except NameError:
    print("boyle bir degisken onceden tanimlanmamis")
except : # baska bır herhangıı hatadada bu kısıma gelır dıye bunu yazdiriyoruz
    print("bir hata olustu") 