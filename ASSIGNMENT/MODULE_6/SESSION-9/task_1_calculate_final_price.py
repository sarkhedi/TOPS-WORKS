
def calculate_final_price(price, discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price

price = 1200
discount_rate = 0.15

result = calculate_final_price(price, discount_rate)

print("Final Price:", result)