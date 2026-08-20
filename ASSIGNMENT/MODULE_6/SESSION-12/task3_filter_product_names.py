products = [
    "Samsung Mobile",
    "Apple iPhone",
    "Sony TV",
    "Boat Earbuds",
    "samsung Watch"
]

filtered_products = list(
    filter(lambda product: product.lower().startswith("s"), products)
)

print(filtered_products)