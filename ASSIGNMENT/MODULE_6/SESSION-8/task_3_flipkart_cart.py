item_prices = [299, 499, 199, 999, 149]

total = 0

for price in item_prices:

    if price < 200:
        continue

    total += price

print("Total Cart Value:", total)