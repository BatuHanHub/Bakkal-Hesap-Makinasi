print ( """
   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/                                                 
       
Bakkal Hesap Makinası, sürüm 3.2 -sürüm (x86_x64)
Lisans GPLv3+ : GNU GPL sürüm 3 <https://www.gnu.org/licenses/gpl-3.0.html>
telif hakkı (C) 2022 BatuHanHub 

Bu ücretsiz bir yazılımdır; değiştirmekte ve yeniden dağıtmakta özgürsünüz.
Yasaların izin verdiği ölçüde HİÇBİR GARANTİ YOKTUR.\n""" )

#ürün adı
urun = str(input("Sattığınız ürünün adı nedir?:"))

while True:
 
 #kutu miktarı

 Kutu = int(input(f"\nKac tane {urun} kutusu var? : ")) #kullanıcıdan kutu miktarını istiyor.
 
 if Kutu > 0:
   pass
   
 elif Kutu < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz\n")  
   continue 

#biri koli içindeki ürün

 KutuUrun = int(input(f"bir {urun} kutusunda kaç tane {urun} var? : ")) #1 kolideki ürün miktarını istiyor
 
 if KutuUrun > 0:
   pass
   
 elif KutuUrun < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz\n")
   continue

#bütün kolideki su hesaplanıyor

 ToplamUrun = Kutu * KutuUrun #işlem1:toplam koli sayısı ile 1 kolide olan su miktarını çarpıyor.
 print(f"*toplam kutulardaki {urun} miktarı :{ToplamUrun}")

#alışfiyatı

 AlisFiyati = float(input("Alısfiyatınızı giriniz: ")) #suyun alış fiyatını soruyor.
 
 if AlisFiyati > 0:
   pass
   
 elif AlisFiyati < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz örneğin x.y yapınız\n")   
   continue

 UrunAlis = AlisFiyati / ToplamUrun
 print(f"*bir {urun} alısfiyatı:{UrunAlis}")

#Kâr marjı

 Kar = float(input("kâr marjınızı giriniz: ")) #sudan kazanılan parayı soruyor

 if Kar > 0:
   pass
   
 elif Kar < 0:
   print("\nhatalı sayı gidiniz lütfen düzeltiniz x.y yapınız\n")
   continue
 
#ürünün toplam satış fiyatı
 print("\n SONUCLAR")

 Toplam = UrunAlis + Kar

 print(f"\nsatıs fiyatınız: {Toplam}")

#toplam kutulardaki ürün fiyatı

 Islem1 = Toplam * ToplamUrun

 print(f"Toplam kolideki su fiyatınız: {Islem1}")

#toplam ürün fiyatı ile Kâr hesaplanıyor

 ToplamKar = ToplamUrun * Kar

 print(f"toplam {urun} kazandıgınız kâr: {ToplamKar}")
 
 break

print("\ndiğer projelerim için: <https://github.com/BatuHanHub>")

input("\nbir tusa basarak pencereyi kapatabilirsiniz...")
