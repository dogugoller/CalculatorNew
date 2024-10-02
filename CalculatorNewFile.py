import math

class Hesapmakinesi:
    def __init__(self):
        self.hafiza = 0


    def toplama(self, sayi):
        self.hafiza += sayi
        return self.hafiza

    def cikarma(self, sayi):
        self.hafiza -= sayi
        return self.hafiza

    def carpma(self, sayi):
        self.hafiza *= sayi
        return self.hafiza

    def bolme (self, sayi):
        if sayi == 0:
            return "Sayı sıfıra bölünemez."
        self.hafiza /= sayi
        return self.hafiza

    def karekok_al (self):
        if self.hafiza < 0:
            return "Negatif sayının karekökü alınamaz."
        self.hafiza = math.sqrt(self.hafiza)
        return self.hafiza

    def yuzde (self,sayi):
        self.hafiza = self.hafiza * (sayi / 100)
        return self.hafiza

    def grand_total(self):
        return self.hafiza

    def reset(self):
        self.hafiza = 0

if __name__ == "__main__":
    hesapmakinesi = Hesapmakinesi()
    while True:
        try:
            secim = int(input("Lütfen bir işlem seçin: "))
        except ValueError:
            print("Yanlış bir işlem tuşladınız.")
            continue

        if secim == 9:
            break

        if secim in [1, 2, 3, 4, 6]:
            sayi = float(input("Bir sayı girin : (Çıkan sonuç üzerinden işlem yapılacak.) "))

        if secim in [5] :
            sayi = float(input("Sayıyı girin."))

        try:
            if secim == 1:
                result = hesapmakinesi.toplama(sayi)
            elif secim == 2:
                result = hesapmakinesi.cikarma(sayi)
            elif secim == 3:
                result = hesapmakinesi.carpma(sayi)
            elif secim == 4:
                result = hesapmakinesi.bolme(sayi)
            elif secim == 5:
                result = hesapmakinesi.karekok_al(sayi)
            elif secim == 6:
                result = hesapmakinesi.yuzde(sayi)
            elif secim == 7:
                result = hesapmakinesi.grand_total()
            elif secim == 8:
                hesapmakinesi.reset()
                print("Hesap makinesi sıfırlandı.")
                continue
            else:
                print("Geçersiz seçim.")
                continue

            print("Sonuç", result)
        except ValueError:
            print("Geçersiz Giriş.")
        except ZeroDivisionError:
            print("Sıfıra Bölme Hatası.")
        except:
            print("Bir Hata Oluştu.")