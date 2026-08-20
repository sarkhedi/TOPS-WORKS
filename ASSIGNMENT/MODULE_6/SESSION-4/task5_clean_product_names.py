products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']
clean_products = []

for product in products:

    product = product.strip()

    product = product.replace("-", " ")
    product = product.title()
    clean_products.append(product)

print(clean_products)