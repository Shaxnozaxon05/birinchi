class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def harakatlan(self):
        print(f"{self.model} harakatlanmoqda!")

class Elektromobil(Avtomobil):
    def __init__(self, model, yil, tezlik, batareya_quvvati):
        super().__init__(model, yil, tezlik)
        self.batareya_quvvati = batareya_quvvati

    def harakatlan(self):
        print(f"{self.model} elektromobili harakatlanmoqda! Batareya: {self.batareya_quvvati}")


a1 = Elektromobil("Tesla", 2023, 150, "100 kWh")
a1.harakatlan()







import math

class Shakl:
    def yuza(self):
        pass

class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return round(math.pi * self.radius ** 2, 1)

class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

figuralar = [Doira(5), Kvadrat(5)]

for figura in figuralar:
    print(f"{figura.__class__.__name__} yuzi:", figura.yuza())










class BankHisobi:
    def __init__(self):
        self.__balans = 0

    def deposit(self, summa):
        self.__balans += summa
        print(f"Hisobga {summa} qo‘shildi.")

    def withdraw(self, summa):
        if summa <= self.__balans:
            self.__balans -= summa
            print(f"{summa} so‘m yechildi. Yangi balans: {self.__balans}")
        else:
            print("Yetarli mablag‘ mavjud emas.")

    def get_balans(self):
        return self.__balans

class BiznesHisob(BankHisobi):
    def withdraw(self, summa):
        komissiya = summa * 0.05
        jami = summa + komissiya
        if jami <= self.get_balans():
            # balansni yangilash uchun super().withdraw() emas, private atributga to‘g‘ridan-to‘g‘ri kira olmaymiz
            self._BankHisobi__balans -= jami
            print(f"{summa} so‘m yechildi (komissiya bilan {int(jami)}). Yangi balans: {int(self.get_balans())}")
        else:
            print("Yetarli mablag‘ mavjud emas.")

hisob = BiznesHisob()
hisob.deposit(1000)
hisob.withdraw(100)


