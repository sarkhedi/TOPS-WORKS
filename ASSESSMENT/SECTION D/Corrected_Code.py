def get_int_input(prompt):
    """Keeps asking until the user enters a valid whole number (no crash)."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number (digits only).")

def get_positive_float(prompt):
    """Keeps asking until the user enters a valid, non-negative price."""
    while True:
        value = input(prompt)
        try:
            price = float(value)
        except ValueError:
            print("Please enter a valid number for the price.")
            continue
        if price < 0:
            print("Price cannot be negative. Please try again.")
            continue
        return price

def get_order_items():
    items = {}
    n = get_int_input("How many items would you like to order? ")
    for i in range(n):
        name = input("Enter item name: ")
        price = get_positive_float(f"Enter price for {name}: ")
        items[name] = price
    return items

def calculate_bill(items, previous_orders):
    subtotal = sum(items.values())

    discount = 0
    if previous_orders > 5:
        discount = subtotal * 0.10

    discounted_subtotal = subtotal - discount
    gst = discounted_subtotal * 0.18
    delivery_fee = 30
    total = discounted_subtotal + gst + delivery_fee

    return subtotal, gst, delivery_fee, discount, total

def print_receipt(items, subtotal, gst, delivery_fee, discount, total):
    print("\n----- RECEIPT -----")
    for name, price in items.items():
        print(f"{name}: Rs {price:.2f}")
    print(f"Subtotal: Rs {subtotal:.2f}")
    if discount > 0:
        print(f"Loyalty Discount (10%): -Rs {discount:.2f}")
    print(f"GST (18%): Rs {gst:.2f}")
    print(f"Delivery Fee: Rs {delivery_fee:.2f}")
    print(f"Final Amount Payable: Rs {total:.2f}")

previous_orders = get_int_input("How many previous orders have you placed? ")
items = get_order_items()
subtotal, gst, delivery_fee, discount, total = calculate_bill(items, previous_orders)
print_receipt(items, subtotal, gst, delivery_fee, discount, total)