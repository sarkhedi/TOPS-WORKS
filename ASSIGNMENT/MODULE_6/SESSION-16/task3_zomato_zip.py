foods = [
    "Pizza",
    "Burger",
    "Pasta",
    "Sandwich"
]

prices = [
    250,
    150,
    200,
    120
]

for food, price in zip(foods, prices):
    print(f"{food} - ₹{price}")