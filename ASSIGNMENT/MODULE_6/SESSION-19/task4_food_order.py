class FoodOrder:

    def __init__(self, restaurant_name):

        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):

        self.items.append(item)

        self.total_price += price


order = FoodOrder("La Pino's Pizza")

order.add_item("Farmhouse Pizza", 300)
order.add_item("Garlic Bread", 150)

print("Restaurant:", order.restaurant_name)
print("Items:", order.items)
print("Total Price:", order.total_price)