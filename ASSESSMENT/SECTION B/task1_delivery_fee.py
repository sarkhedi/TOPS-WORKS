def calculate_delivery_bill():
    print("--- Food Delivery Fee Calculator ---")
    
    try:
        order_value = float(input("Enter order value (in Rs): "))
        distance = float(input("Enter delivery distance (in km): "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    if order_value < 0 or distance < 0:
        print("Error: Order value and distance cannot be negative numbers.")
        return
    
    if order_value >= 500:
        delivery_fee = 0
    elif distance <= 5:
        delivery_fee = 30
    else:
        delivery_fee = 60

    final_amount = order_value + delivery_fee

    print("\n--- Bill Summary ---")
    print(f"Item Total    : Rs {order_value:.2f}")
    print(f"Delivery Fee  : Rs {delivery_fee:.2f}")
    print(f"Final Payable : Rs {final_amount:.2f}")

if __name__ == "__main__":
    calculate_delivery_bill()