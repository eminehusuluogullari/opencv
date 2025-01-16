"""
! veritabanı nedır ?
uygulamalarımızda websıtelerımızde veya en genel anlamda programlarımızda gerekli olan bilgileri depoladıgımız yapıdır

SQL veritabanı sunucu kurmaya gerek kalmayan verı tabannıdır 

"""
import sqlite3 # sqlite yi dahil ediyoruz
com=sqlite3.connect("kütüphane.db") # tabloya baglanıyoruz
cursor=con.cursor() # cursor isimli degişken vertabanı uzerınde ıslem yapmak ıcın kullanacagımız imlec olacak
con.close() # bagantıyı koparıoruz

"""
veritabanını kalsore olsturunca bı py yı acarken 
sag tık 
open with brackets ile ac i sec
"""