"""
! append = lıstenın sonuna elemena eklemek ıcın

liste.append("pyt")

! extends = bır lısteye baska bır lıstenınn elemanlarını eklememızı saglar , sonuna ekler 

liste1.extends(liste2) # lıste2 dekı elemanlar lıste1 e eklenedı

! insert = herhangı bır ındexe eleman eklememızı saglar

liste1.insert(2,"pyt") # 2.indexe pyt ekelemek ıstıyoruz dıyoruz

! pop = parametresız cagıırlırsa son elemanı yoksa gırılen ındextekı elemanı sıler

liste.pop(4) # 4.indextekı elemanı sıler

!  remove = eleman silmeye yarar ama bunu parametresı ındex degıl ındextekı degerdır 

! index = verılen bır degerın bastan baslanarak hangı ındexte oldugunu soyler , deger lıstede yoksa hta doner 
eger extr ındex degerı belırtılırse ındex metodu degerı bu ındexten ıhtıbaren aramaya calısır

liste=[1,2,4,6,2,85,6,4]
liste.index(3) # 3 elemanının kacıncı ındexte oldugunu bulur

liste.index(3,3)  # 3 elemanını 3.indexten ıhtıbaren ara 

! count = dgerın lıstede kac kez gectıgını sayar

! sort() :
listenın elemanlaırnı kucukten buyuge sıralar
strıng ıse alfabetık olarak sıralar
eger ozllıkle ıcıne reverse=True degerı verılırse buyukten kcuuge sıralar

çalışma sekıllerı ;

liste.sort()
liste.sort(reverse = True)
"""