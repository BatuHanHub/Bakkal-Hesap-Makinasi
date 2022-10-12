print("""Bakkal Hesap Makinası, version 3.0 -release (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2022 BatuHanHub Software 

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""")

while True:

##########################################################################################################

#koli miktarı

 Box = int(input("\nKac tane koliniz var? : ")) #kullanıcıdan koli miktarını istiyor.
 
 if Box > 0:
   pass
   
 elif Box < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz\n")  
   continue 

#########################################################################################################

#biri koli içindeki su

 BoxWater = int(input("bir kolide kaç tane su var? : ")) #1 kolideki su miktarını istiyor
 
 if BoxWater > 0:
   pass
   
 elif BoxWater < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz\n")
   continue

#bütün kolideki su hesaplanıyor

 TotalWater = Box * BoxWater #işlem1:toplam koli sayısı ile 1 kolide olan su miktarını çarpıyor.
 print("*toplam kolilerdeki su miktarı :",TotalWater)

##########################################################################################################

#alışfiyatı

 PurchasePrice = float(input("Alısfiyatınızı giriniz: ")) #suyun alış fiyatını soruyor.
 
 if PurchasePrice > 0:
   pass
   
 elif PurchasePrice < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz örneğin x.y yapınız\n")   
   continue

 Water = PurchasePrice / TotalWater
 print("*bir suyun alısfiyatı:", Water)

###########################################################################################################

#Kâr marjı

 Gain = float(input("kâr marjınızı giriniz: ")) #sudan kazanılan parayı soruyor

 if Gain > 0:
   pass
   
 elif Gain < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz x.y yapınız\n")
   continue

###########################################################################################################
 
#suyun toplam satış fiyatı
 print("\n SONUCLAR")

 Total = Water + Gain

 print("\nsatıs fiyatınız: ", Total)

#toplam kolilerdeki su fiyatı

 Process1 = Total * TotalWater

 print("Toplam kolideki su fiyatınız: ", Process1)

#toplam su fiyatı ile Kâr hesaplanıyor

 TotalGain = TotalWater * Gain

 print("toplam sudan kazandıgınız kâr: ", TotalGain)


############################################################################################################

print("\ndiğer projelerim için: <https://github.com/BatuHanHub>")

input("\nbir tusa basarak pencereyi kapatabilirsiniz...") #ekranın hemen kapanmasını engelliyor.
