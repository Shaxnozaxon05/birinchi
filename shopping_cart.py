class Product:
    def __init__(self, name, price, quantity):
        if price <= 0 or quantity <= 0:
            raise ValueError("Narx va miqdor musbat bo‘lishi kerak")
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.quantity <= 0:
            raise ValueError("Mahsulot miqdori 0 bo‘lsa, qo‘shib bo‘lmaydi")
        self.items.append(product)

    def remove_product(self, product_name):
        self.items = [p for p in self.items if p.name != product_name]

    def get_total_price(self):
        return sum(p.price for p in self.items)
