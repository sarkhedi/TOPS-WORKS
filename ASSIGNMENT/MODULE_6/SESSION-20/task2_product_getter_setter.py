class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):

        if price < 0:
            raise ValueError("Price cannot be negative")

        self._price = price

product1 = Product(500)

print("Current Price:", product1.get_price())

product1.set_price(750)

print("Updated Price:", product1.get_price())