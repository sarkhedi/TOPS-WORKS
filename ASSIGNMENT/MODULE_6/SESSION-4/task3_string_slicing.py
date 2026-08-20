product = "Apple iPhone 14 Pro Max"

split_index = product.find(" ")

brand = product[:split_index]
model = product[split_index + 1:]

print("Brand :", brand)
print("Model :", model)
