import json
import os

FILE_NAME = "orders.json"

def load_orders():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_orders(orders_list):
    with open(FILE_NAME, "w") as file:
        json.dump(orders_list, file, indent=4)

def add_new_order():
    print("\n--- Place New Order ---")
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        print("Customer name cannot be blank!")
        return

    items_raw = input("Enter food items (separated by commas): ")
    items_list = [item.strip() for item in items_raw.split(",") if item.strip()]
    if not items_list:
        print("Please enter at least one item!")
        return

    try:
        total_amount = float(input("Enter total amount: Rs "))
        if total_amount < 0:
            print("Total amount cannot be negative!")
            return
    except ValueError:
        print("Invalid amount! Please enter numbers only.")
        return

    status = input("Enter order status (e.g. Preparing / Out for Delivery / Completed): ").strip()
    if not status:
        status = "Pending"

    new_order = {
        "customer_name": customer_name,
        "items": items_list,
        "total_amount": total_amount,
        "status": status
    }

    orders = load_orders()
    orders.append(new_order)
    save_orders(orders)
    print("Order successfully saved to orders.json!")

def view_all_orders():
    orders = load_orders()
    if not orders:
        print("\nNo previous orders found in file.")
        return

    print("\n--- Past Order History ---")
    for i, order in enumerate(orders, start=1):
        print(f"\nOrder #{i}")
        print(f"  Customer : {order['customer_name']}")
        print(f"  Items    : {', '.join(order['items'])}")
        print(f"  Total    : Rs {order['total_amount']:.2f}")
        print(f"  Status   : {order['status']}")

def main():
    while True:
        print("\n=== Food Order Logger ===")
        print("1. Add New Order")
        print("2. View Past Orders")
        print("0. Exit")
        
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_new_order()
        elif choice == "2":
            view_all_orders()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option (1, 2, or 0).")

if __name__ == "__main__":
    main()