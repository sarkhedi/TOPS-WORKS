order_price = input("Enter Zomato order price: ")
order_price = float(order_price)
gst = order_price * 18 / 100

final_amount = order_price + gst

print("Final bill amount is ₹", final_amount)
