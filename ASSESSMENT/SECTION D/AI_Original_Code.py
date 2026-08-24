def get_order_items():
    items = {}
    n = int(input("How many items would you like to order? "))
    for i in range(n):
        name = input("Enter item name: ")
        price = float(input(f"Enter price for {name}: "))
        if price < 0:
            print("Price cannot be negative. Please try again.")
            price = float(input(f"Enter price for {name}: "))
        items[name] = price
    return items

def calculate_bill(items, previous_orders):
    subtotal = sum(items.values())
    gst = subtotal * 0.18
    delivery_fee = 30
    total = subtotal + gst + delivery_fee

    discount = 0
    if previous_orders > 5:
        discount = total * 0.10
        total = total - discount

    return subtotal, gst, delivery_fee, discount, total

def print_receipt(items, subtotal, gst, delivery_fee, discount, total):
    print("\n----- RECEIPT -----")
    for name, price in items.items():
        print(f"{name}: Rs {price:.2f}")
    print(f"Subtotal: Rs {subtotal:.2f}")
    print(f"GST (18%): Rs {gst:.2f}")
    print(f"Delivery Fee: Rs {delivery_fee:.2f}")
    if discount > 0:
        print(f"Loyalty Discount: -Rs {discount:.2f}")
    print(f"Final Amount Payable: Rs {total:.2f}")

previous_orders = int(input("How many previous orders have you placed? "))
items = get_order_items()
subtotal, gst, delivery_fee, discount, total = calculate_bill(items, previous_orders)
print_receipt(items, subtotal, gst, delivery_fee, discount, total)