print("""Bakkal Hesap Makinası, version 3.0 -release (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2022 BatuHanHub Software 

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""")


##########################################################################################################

#koli miktarı

koli=(int(input("\nKac tane koliniz var? : "))) #kullanıcıdan koli miktarını istiyor.

#########################################################################################################

#biri koli içindeki su

koli_su=(int(input("bir kolide kaç tane su var? : "))) #1 kolideki su miktarını istiyor

#bütün kolideki su hesaplanıyor

Toplam_Su = koli * koli_su #işlem1:toplam koli sayısı ile 1 kolide olan su miktarını çarpıyor.
print("*toplam kolilerdeki su miktarı :",Toplam_Su)

##########################################################################################################

#alışfiyatı

Alis_fiyatı=(float(input("Alısfiyatınızı giriniz: "))) #suyun alış fiyatını soruyor.
Bir_su= Alış_fiyatı / Toplam_Su
print("*bir suyun alısfiyatı:",Bir_su)

###########################################################################################################

#Kâr marjı

Kar=(int(input("kâr marjınızı giriniz: "))) #sudan kazanılan parayı soruyor

###########################################################################################################

#suyun toplam satış fiyatı
print("\n SONUCLAR")

Toplam = Bir_su + Kar

print("\nsatıs fiyatınız: ", Toplam)

#toplam kolilerdeki su fiyatı

işlem2 = Toplam * Toplam_Su

print("Toplam kolideki su fiyatınız: ", işlem2)

#toplam su fiyatı ile Kâr hesaplanıyor

TopKar = Toplam_Su * Kar

print("toplam sudan kazandıgınız kâr: ", TopKar)

############################################################################################################

print("\ndiğer projelerim için: <https://github.com/BatuHanHub>")

input("\nbir tusa basarak pencereyi kapatabilirsiniz...") #ekranın hemen kapanmasını engelliyor.
