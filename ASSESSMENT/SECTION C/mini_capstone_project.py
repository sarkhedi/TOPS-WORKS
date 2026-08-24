import json
import os

FILE_NAME = "orders.json"

class Order:
    def __init__(self, order_id, customer_name, items, total_amount, status="Pending"):
        self.order_id = str(order_id)
        self.customer_name = customer_name
        self.items = items if isinstance(items, list) else []
        self.total_amount = float(total_amount)
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amount": self.total_amount,
            "status": self.status
        }


def load_orders():
    orders = []
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            for item in data:
                order_obj = Order(
                    order_id=item["order_id"],
                    customer_name=item["customer_name"],
                    items=item["items"],
                    total_amount=item["total_amount"],
                    status=item.get("status", "Pending")
                )
                orders.append(order_obj)
    except FileNotFoundError:
       
        orders = []
    except json.JSONDecodeError:
        orders = []
    return orders


def save_all_orders(orders_list):
    data = [order.to_dict() for order in orders_list]
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def generate_next_order_id(orders_list):
    if not orders_list:
        return "ORD101"
    highest_num = 100
    for order in orders_list:
        if order.order_id.startswith("ORD"):
            try:
                num_part = int(order.order_id.replace("ORD", ""))
                if num_part > highest_num:
                    highest_num = num_part
            except ValueError:
                pass
    return f"ORD{highest_num + 1}"


def place_new_order(orders_list):
    print("\n--- Place New Order ---")

    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        print("Error: Customer name cannot be empty.")
        return

    raw_items = input("Enter food items (separated by commas): ").strip()
    items = [item.strip() for item in raw_items.split(",") if item.strip()]
    if not items:
        print("Error: You must enter at least one food item.")
        return

    try:
        total_amount = float(input("Enter total order amount: Rs "))
        if total_amount <= 0:
            print("Error: Total amount must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only.")
        return

    new_id = generate_next_order_id(orders_list)
    new_order = Order(
        order_id=new_id,
        customer_name=customer_name,
        items=items,
        total_amount=total_amount,
        status="Pending"
    )

    orders_list.append(new_order)
    save_all_orders(orders_list)
    print(f"Success: Order #{new_id} placed successfully and saved to {FILE_NAME}!")


def view_all_orders(orders_list):
    if not orders_list:
        print("\nNo orders found in the system.")
        return

    print("\n" + "=" * 78)
    print(f"{'Order ID':<12}{'Customer Name':<20}{'Item Count':<14}{'Total (Rs)':<14}{'Status':<15}")
    print("=" * 78)

    for order in orders_list:
        item_count = len(order.items)
        
    
        if order.status.lower() == "delivered":
            status_display = f"[✓ {order.status.upper()}]"
        else:
            status_display = f"- {order.status}"

        print(f"{order.order_id:<12}{order.customer_name:<20}{str(item_count):<14}{f'Rs {order.total_amount:.2f}':<14}{status_display:<15}")
    print("=" * 78)


def search_order_by_id(orders_list):
    if not orders_list:
        print("\nNo orders to search.")
        return

    search_id = input("\nEnter Order ID to search (e.g. ORD101): ").strip()
    found = False

    for order in orders_list:
        if order.order_id.lower() == search_id.lower():
            print("\n--- Order Details Found ---")
            print(f"Order ID      : {order.order_id}")
            print(f"Customer Name : {order.customer_name}")
            print(f"Items Ordered : {', '.join(order.items)} ({len(order.items)} items)")
            print(f"Total Amount  : Rs {order.total_amount:.2f}")
            print(f"Status        : {order.status}")
            
            change_status = input("Do you want to update status to 'Delivered'? (y/n): ").strip().lower()
            if change_status == "y":
                order.status = "Delivered"
                save_all_orders(orders_list)
                print(f"Order #{order.order_id} status updated to 'Delivered'!")
            
            found = True
            break

    if not found:
        print(f"Error: Order with ID '{search_id}' was not found.")


def main():
    orders = load_orders()
    
    while True:
        print("\n============================================")
        print("  Food Delivery Order Management System")
        print("============================================")
        print("1. Place New Order")
        print("2. View All Orders")
        print("3. Search Order by ID")
        print("4. Exit")
        print("--------------------------------------------")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            place_new_order(orders)
        elif choice == "2":
            view_all_orders(orders)
        elif choice == "3":
            search_order_by_id(orders)
        elif choice == "4":
            print("\nExiting Order Management System. Thank you!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()