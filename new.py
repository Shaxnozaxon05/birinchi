class ProductList:
    def __init__(self, title, *mahsulotlar):
        self.title=title
        self.mahsulotlar=list(mahsulotlar)

    def __getitem__(self, item):
        return self.mahsulotlar[item]

    def __setitem__(self, i, q):
        self.mahsulotlar[i]=q

    def __delitem__(self, key):
        del self.mahsulotlar[key]



shop = ProductList('karzinka', 'non', 'olma', 'banan', 'shakar')  # qiymatlarni yozing
shop[1] = "Noutbuk"
shop[2] = "Smartfon"
print(shop[1])
print(shop[2])
del shop[2]
print(shop[2])
print(shop.__dict__)









class BankAccount:
    def __init__(self, balance):
        self.balance=balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balans manfiy bo'lishi mumkin emas.")



account = BankAccount(1000)
print(account.balance)
account.balance = 1500
print(account.balance)







class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    @classmethod
    def from_birth_year(cls, name, birth_year):

        return



emp = Employee.from_birth_year("Ali", 1995)
print(emp.name, emp.age)
