class Product:

    def __init__(self, price):

        self._price = price

    def display_price(self):
        print("Product Price:", self._price)

product1 = Product(500)

product1.display_price()