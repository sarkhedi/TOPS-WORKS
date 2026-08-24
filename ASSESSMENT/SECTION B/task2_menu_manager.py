menu = {
    "Paneer Butter Masala": {"price": 240, "category": "Main Course"},
    "Veg Biryani": {"price": 180, "category": "Rice"},
    "Masala Dosa": {"price": 90, "category": "Breakfast"},
    "Garlic Naan": {"price": 50, "category": "Breads"},
    "Paneer Tikka": {"price": 210, "category": "Starters"},
    "Gulab Jamun": {"price": 70, "category": "Dessert"}
}

def view_all_items():
    print("\n--- Current Menu ---")
    print(f"{'No.':<5}{'Dish Name':<25}{'Category':<15}{'Price (Rs)':<10}")
    print("-" * 55)
    for idx, (dish, details) in enumerate(menu.items(), start=1):
        print(f"{idx:<5}{dish:<25}{details['category']:<15}{details['price']:<10}")

def filter_by_category():
    cat_input = input("\nEnter category name to filter (e.g. Starters, Main Course): ").strip()
    found = False
    print(f"\n--- Items in '{cat_input}' ---")
    for dish, details in menu.items():
        if details["category"].lower() == cat_input.lower():
            print(f"- {dish}: Rs {details['price']}")
            found = True
    if not found:
        print("No items found in this category.")

def search_dish_price():
    dish_name = input("\nEnter dish name to search: ").strip()
    for dish, details in menu.items():
        if dish.lower() == dish_name.lower():
            print(f"Found: {dish} costs Rs {details['price']} (Category: {details['category']})")
            return
    print(f"Sorry, '{dish_name}' is not in the menu.")

def main():
    while True:
        print("\n=== Restaurant Menu System ===")
        print("1. View all items")
        print("2. Filter items by category")
        print("3. Search for a dish by name")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_all_items()
        elif choice == "2":
            filter_by_category()
        elif choice == "3":
            search_dish_price()
        elif choice == "0":
            print("Exiting Menu Manager. Thank you!")
            break
        else:
            print("Invalid option! Please enter 1, 2, 3 or 0.")

if __name__ == "__main__":
    main()