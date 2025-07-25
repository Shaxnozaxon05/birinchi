
import matematik
a = 10
b = 4
print("Yig'indisi:", matematik.summa(a, b))
print("Ayirmasi:", matematik.ayirma(a, b))




import math
import datetime

son = 25
ildiz = math.sqrt(son)  # 25 ning ildizi
burchak = math.radians(60)  # 60 gradusni radianlarga aylantirish
kosinus = math.cos(burchak)  # kosinus(60°)

print("1. Math modulidan foydalanish:")
print(f"{son} ning kvadrat ildizi: {ildiz}")
print(f"60 gradusning kosinusi: {kosinus:.4f}")

# sana va vaqt
hozirgi_vaqt = datetime.datetime.now()

print("\n2. Datetime modulidan foydalanish:")
print("Hozirgi sana va vaqt:", hozirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S"))


