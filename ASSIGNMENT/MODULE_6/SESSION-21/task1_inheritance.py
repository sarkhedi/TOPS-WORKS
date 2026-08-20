class Product:

    def get_discount(self):
        return 0


class Electronics(Product):


    def get_discount(self):
        return 10

product = Product()

electronic = Electronics()


print("Product Discount:", product.get_discount(), "%")
print("Electronics Discount:", electronic.get_discount(), "%")