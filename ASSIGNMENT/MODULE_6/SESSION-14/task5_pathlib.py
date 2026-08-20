from pathlib import Path

file_path = Path("zomato_orders.json")

if file_path.exists():
    print("zomato_orders.json file found!")
else:
    print("zomato_orders.json file not found!")