def format_coupon_message(username, discount=10):
    return f"Hi {username}, you get {discount}% off!"


print(format_coupon_message("Rahul", 20))

print(format_coupon_message("Mahek"))