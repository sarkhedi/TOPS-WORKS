def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")

    return name

product = " oneplus-Nord "

print("Original Name :", product)
print("Clean Name    :", clean_brand_name(product))