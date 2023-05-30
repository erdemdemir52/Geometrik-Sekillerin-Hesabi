# HesapModulu.py dosyası yaptığımız hesapların formüllerini barındıran dosyadır.
# Çevre, Alan, Hacim formülleri HesapModulu.py dosyasında girilmiştir ve bu dosya ya import edilmiştir.
# Hem modüllerin hem de sınıf yapısının iyi anlaşılması için böyle bir uygulama yapılmıştır.

# HesapModulu.py dosyasını aşağıdaki gibi dosyamıza tanıtıyoruz.
from HesapModulu import *

# Modül içindeki sınıflardan yeni nesneler türetiyoruz.
# Modülün içindeki sınıflardan böylece fonksiyonları çağırabiliriz.
cevreHesaplama = Cevre()
alanHesaplama = Alan()
hacimHesaplama = Hacim()
# DipNot: Sınıf oluşturmadan direk fonksiyonlar üzerinden de işlemleri yapabiliriz.
# Lakin hem formüllerin düzenli olması hem de sınıf yapısını öğrenmek için böyle bir sistem kurayım dedim.

sistemDurum = True

# ilk çalıştırdığımızda aktif olacak olan fonksiyon.
def menuBaslat():
    menuSecim = int(input("Yapmak istediğiniz işlem nedir? \n1-Çevre\n2-Alan\n3-Hacim\n"))

    # 1 ile 3 arasında başka bir sayı girilirse döngüye alacak işlemi.
    while menuSecim < 1 or menuSecim > 3:
        menuSecim = int(input("1 ile 3 arasında sayı giriniz: \n1-Çevre\n2-Alan\n3-Hacim\n"))

    if menuSecim == 1:
        CevreIslem()

    if menuSecim == 2:
        AlanIslem()

    if menuSecim == 3:
        HacimIslem()

# Geometrik şekillerin çevre bilgilerinin girildiği fonksiyon
def CevreIslem():
    menuSecim = int(input("Geometrik şekli belirtin:\n1-Kare\n2-Dikdörtgen\n3-Üçgen\n4-Çember\n"))

    # 1-4 arasından başka bir sayı girilmesi durumunda başka sayı isteyecek.
    while menuSecim < 1 or menuSecim > 4:
        menuSecim = int(input("Lütfen 1-4 arası sayı giriniz:\n1-Kare\n2-Dikdörtgen\n3-Üçgen\n4-Çember\n"))

    if menuSecim == 1:
        a = int(input("Lütfen kareninin bir kenarını (a) giriniz: "))
        cevre = cevreHesaplama.KareCevre(a)
        print("Karenin Çevresi: {}".format(cevre))

    if menuSecim == 2:
        a = int(input("Lütfen ilk kenarın ölçüsünü (a) giriniz: "))
        b = int(input("Lütfen diğer kenarın ölçüsünü (b) giriniz: "))
        cevre = cevreHesaplama.DikdortgenCevre(a, b)
        print("Dikdörtgenin Çevresi: {}".format(cevre))

    if menuSecim == 3:
        a = int(input("Lütfen üçgenin birinci kenar ölçüsünü (a) girin: "))
        b = int(input("Lütfen üçgenin ikinci kenar ölçüsünü (b) girin: "))
        c = int (input("Lütfen üçgenin üçüncü kenar (c) ölçüsünü girin: "))
        cevre = cevreHesaplama.UcgenCevre(a, b, c)
        print("Üçgenin Çevresi: {}".format(cevre))

    if menuSecim == 4:
        r = int(input("Lütfen çemberin yarıçapını girin: "))
        cevre = cevreHesaplama.CemberCevre(r)
        print("Çemberin Çevresi: {}".format(cevre))

# Geometrik şekillerin alan bilgilerinin girildiği fonksiyon.
def AlanIslem():
    menuSecim = int(input("Geometrik şekli belirtin:\n1-Kare\n2-Dikdörtgen\n3-Üçgen\n4-Çember\n"))

    # 1-4 arasından başka sayı girilmesi durumunda tekrar değer isteyecek.
    while menuSecim < 1 or menuSecim > 4:
        menuSecim = int(input("Lütfen 1-4 arasında sayı giriniz:\n1-Kare\n2-Dikdörtgen\n3-Üçgen\n4-Çember\n"))

    if menuSecim == 1:
        a = int(input("Lütfen kareninin bir kenarını (a) giriniz: "))
        alan = alanHesaplama.KareAlan(a)
        print("Karenin Alanı: {}".format(alan))

    if menuSecim == 2:
        a = int(input("Lütfen ilk kenarın ölçüsünü (a) giriniz: "))
        b = int(input("Lütfen diğer kenarın ölçüsünü (b) giriniz: "))
        alan = alanHesaplama.DikdortgenAlan(a, b)
        print("Dikdörtgenin Alanı: {}".format(alan))

    if menuSecim == 3:
        a = int(input("Lütfen üçgenin birinci kenar ölçüsünü (a) girin: "))
        h = int(input("Lütfen üçgenin yüksekliğini (h) girin: "))
        alan = alanHesaplama.UcgenAlan(a, h)
        print("Üçgenin Alanı: {}".format(alan))

    if menuSecim == 4:
        r = int(input("Lütfen çemberin yarıçapını girin: "))
        alan = alanHesaplama.CemberAlan(r)
        print("Çemberin Çevresi: {}".format(alan))

# Geometrik şekillerin hacim bilgilerinin girildiği fonksiyon.
def HacimIslem():
    menuSecim = int(input("Lütfen Geometrik Şekli Seçiniz:\n1-Dikdörgen Prizma\n2-Küp\n3-Üçgen Prizma\n4-Silindir\n5-Piramit\n"))

    # 1-5 arasından başka sayı girilmesi durumunda tekrar değer isteyecek.
    while menuSecim < 1 or menuSecim > 5:
        menuSecim = int(input("Lütfen 1-5 arasında sayı girin:\n1-Dikdörgen Prizma\n2-Küp\n3-Üçgen Prizma\n4-Silindir\n5-Piramit\n"))

    if menuSecim == 1:
        a = int(input("Birinci kenar (a) ölçüsünü giriniz: "))
        b = int(input("İkinci kenar (b) ölçüsünü giriniz: "))
        h = int(input("Prizmanın yüksekliği (h) giriniz: "))
        hacim = hacimHesaplama.DikdortgenPrizmaHacim(a, b, h)
        print("Dikdörtgen Prizmanın Hacmi: {}".format(hacim))

    if menuSecim == 2:
        a = "Bir kenar uzunluğunu (a) giriniz: "
        hacim = hacimHesaplama.KupHacim(a)
        print("Küpün Hacmi: {}".format(hacim))

    if menuSecim == 3:
        a = int(input("Birinci kenar uzunluğunu (a) giriniz: "))
        b = int(input("İkinci kenar uzunluğunu (b) giriniz: "))
        h = int(input("Prizmanın yükseliğini (h) giriniz: "))
        hacim = hacimHesaplama.UcgenPrizmaHacim(a, b, h)
        print("Üçgen Prizmanın Hacmi: {}".format(hacim))

    if menuSecim == 4:
        r = int(input("Silindirin yarıçapını (r) giriniz: "))
        h = int(input("Silindirin yükseliğini (h) giriniz: "))
        hacim = hacimHesaplama.SilindirHacim(r, h)
        print("Silindirin Hacmi: {}".format(hacim))

    if menuSecim == 5:
        a = int(input("Birinci kenarın (a) ölçüsünü girin: "))
        b = int(input("İkinci kenarın (b) ölçüsünü girin: "))
        h = int(input("Piramitin yüksekliğini (h) girin: "))
        hacim = hacimHesaplama.PiramitHacim(a, b, h)
        print("Piramitin Hacmi: {}".format(hacim))

# Sistemimizi bir döngü içinde başlatıyoruz. Biz sistemden çıkmadan hiçbir şekilde program kapanmayacak.
while sistemDurum:
    # aşağıdaki fonksiyon ile programı direk çalıştırmış oluyoruz.
    menuBaslat()