# Bu uygulamada amaç başka bir modül içindeki sınıf yapılarından fonksiyonları çekmek.
# HesapProgrami.py isimli dosya istediğiniz geometrik cisimler ile ilgili hesap yapmanızı sağlayacak.
# Program hesapları yaparken buradaki fonksiyonları kullanacak.

# Alan Hesaplarının Bulunduğu Class
class Alan:
    def KareAlan(self, x):
        return x * x

    def DikdortgenAlan(self, x, y):
        return x * y

    def UcgenAlan(self, a, h):
        return (a * h) / 2

    def CemberAlan(self, r):
        return 3.14 * r * r

# Çevre Hesaplarının Bulunduğu Class
class Cevre:
    def KareCevre(self, a):
        return 4 * a

    def DikdortgenCevre(self, a, b):
        return (2 * a) + (2 * b)

    def UcgenCevre(self, a, b, c):
        return a + b + c

    def CemberCevre(self, r):
        return 2 * 3.14 * r

# Hacim Hesaplarının Bulunduğu Class
class Hacim:
    def DikdortgenPrizmaHacim(self, a, b, h):
        return a * b * h

    def KupHacim(self, a):
        return a ** 3

    def UcgenPrizmaHacim(self, a, b, h):
        return 0,5 * a * b * h

    def SilindirHacim(self, r, h):
        return 3.14 * r * r * h

    def PiramitHacim(self, a, b, h):
        return (1/3) * a * b * h