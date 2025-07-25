class Talaba:
    def __init__(self, ism, yosh, fakultet):
        self.ism = ism
        self.yosh = yosh
        self.fakultet = fakultet

    def talaba_malumotlari(self):
        print(f"Ismi: {self.ism}, Yoshi: {self.yosh}, Fakulteti: {self.fakultet}")

talaba1 = Talaba("Ali", 20, "Dasturlash")
talaba1.talaba_malumotlari()







class Tortburchak:
    def __init__(self, uzunlik, eni):
        self.uzunlik = uzunlik
        self.eni = eni

    def yuza(self):
        return self.uzunlik * self.eni

    def perimetr(self):
        return 2 * (self.uzunlik + self.eni)


t1 = Tortburchak(4, 5)
print("Yuza:", t1.yuza())
print("Perimetr:", t1.perimetr())










class Hisoblagich:
    def __init__(self):
        self.qiymat = 9

    def oshirish(self):
        self.qiymat += 10

    def kamaytirish(self):
        self.qiymat -= 1

    def qaytar(self):
        return self.qiymat

h = Hisoblagich()
h.oshirish()
h.oshirish()
h.kamaytirish()
print("Hozirgi qiymat:", h.qaytar())
