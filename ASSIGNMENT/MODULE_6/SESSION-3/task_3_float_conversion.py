prices = ['199.99', '299.50', '150']
float_prices = []

for price in prices:
    float_price = float(price)
    float_prices.append(float_price)

total = sum(float_prices)
print("Total cart value is ₹", total)

