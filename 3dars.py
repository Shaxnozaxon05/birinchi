narx = float(input("Mahsulot narxi: "))
foizi = float(input("Chegirma foizi: "))
chegirma = narx * foizi / 100
yangi_narx = narx - chegirma
print(f"Chegirma: {chegirma}")
print(f"Yangi narx: {yangi_narx}")




import math
a = float(input("Tomon a: "))
b = float(input("Tomon b: "))
c = float(input("Tomon c: "))
perimetr = a + b + c
s = perimetr / 2
yuza = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Perimetr: {perimetr}")
print(f"Yuza: {yuza:.4f}")






kredit = float(input("Kredit miqdori: "))
foiz_stavkasi = float(input("Yillik foiz stavkasi (%): "))
muddat = int(input("Kredit muddati (yil): "))
yillik_foiz = kredit * foiz_stavkasi / 100
umumiy_qarz = kredit + (yillik_foiz * muddat)
print(f"Yillik foiz: {yillik_foiz}")
print(f"Umumiy qarz miqdori: {umumiy_qarz}")





