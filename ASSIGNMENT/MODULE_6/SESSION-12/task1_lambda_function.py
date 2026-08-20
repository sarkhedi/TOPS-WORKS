gst_price = lambda price: price + (price * 18 / 100)

price1 = 100
price2 = 250
price3 = 500

print("Original Price:",price1,"Final Price:",gst_price(price1))

print("Original Price:",price2,"Final Price:",gst_price(price2))

print("Original Price:",price3,"Final Price:",gst_price(price3))