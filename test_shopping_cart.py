import pytest
from shopping_cart import Product, ShoppingCart
def test_invalid_product_creation():
    with pytest.raises(ValueError):
        Product("Noto‘g‘ri", -100, 2)
    with pytest.raises(ValueError):
        Product("Noto‘g‘ri", 100, 0)

def test_add_product_total_price():
    cart = ShoppingCart()
    p1 = Product("telefon", 1000, 1)
    p2 = Product("quvvatlagich", 200, 1)
    cart.add_product(p1)
    cart.add_product(p2)
    assert cart.get_total_price() == 1200

def test_remove_product_updates_price():
    cart = ShoppingCart()
    p1 = Product("monitor", 800, 1)
    cart.add_product(p1)
    cart.remove_product("monitor")
    assert cart.get_total_price() == 0

def test_zero_quantity_product():
    with pytest.raises(ValueError):
        p = Product("kamera", 500, 0)
        cart = ShoppingCart()
        cart.add_product(p)
