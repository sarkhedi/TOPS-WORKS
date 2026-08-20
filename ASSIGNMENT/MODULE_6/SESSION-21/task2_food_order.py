class FoodOrder:

    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_total(self):
        return self.base_price


class ZomatoOrder(FoodOrder):

    def calculate_total(self):

        delivery_charge = self.base_price * 0.05

        total = self.base_price + delivery_charge

        return total

order1 = FoodOrder(1000)

order2 = ZomatoOrder(1000)

print("Food Order Total:", order1.calculate_total())
print("Zomato Order Total:", order2.calculate_total())