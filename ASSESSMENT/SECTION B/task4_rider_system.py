import csv
import os

CSV_FILE = "riders.csv"

class Rider:
    def __init__(self, rider_id, name, status="Available", total_deliveries=0):
        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = int(total_deliveries)

    def assign_order(self, order_id):
        self.status = "On Delivery"
        print(f"Order #{order_id} assigned to rider {self.name} (ID: {self.rider_id}). Status is now 'On Delivery'.")

    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print(f"Delivery completed by {self.name}! Total completed: {self.total_deliveries}. Status reset to 'Available'.")

    def display_info(self):
        print(f"ID: {self.rider_id} | Name: {self.name:<12} | Status: {self.status:<12} | Total Deliveries: {self.total_deliveries}")


def load_riders():
    riders_list = []
    if os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rider = Rider(
                        rider_id=row["rider_id"],
                        name=row["name"],
                        status=row["status"],
                        total_deliveries=int(row["total_deliveries"])
                    )
                    riders_list.append(rider)
        except Exception:
            riders_list = []

    if not riders_list:
        riders_list = [
            Rider("R101", "Rahul Sharma"),
            Rider("R102", "Amit Patel"),
            Rider("R103", "Priya Shah")
        ]
    return riders_list


def save_riders(riders_list):
    with open(CSV_FILE, mode="w", newline="") as file:
        fieldnames = ["rider_id", "name", "status", "total_deliveries"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for r in riders_list:
            writer.writerow({
                "rider_id": r.rider_id,
                "name": r.name,
                "status": r.status,
                "total_deliveries": r.total_deliveries
            })
    print("Rider data saved to riders.csv.")


def main():
    riders = load_riders()
    
    while True:
        print("\n=== Delivery Rider Management ===")
        print("1. View All Riders")
        print("2. Assign Order to Rider")
        print("3. Mark Delivery Complete")
        print("0. Save & Exit")
        
        choice = input("Enter option: ").strip()

        if choice == "1":
            print("\n--- Rider Details ---")
            for r in riders:
                r.display_info()

        elif choice == "2":
            rid_input = input("Enter Rider ID to assign order: ").strip()
            found = False
            for r in riders:
                if r.rider_id.lower() == rid_input.lower():
                    order_num = input("Enter Order ID to assign: ").strip()
                    r.assign_order(order_num)
                    found = True
                    break
            if not found:
                print("Rider ID not found!")

        elif choice == "3":
            rid_input = input("Enter Rider ID to complete delivery: ").strip()
            found = False
            for r in riders:
                if r.rider_id.lower() == rid_input.lower():
                    r.complete_delivery()
                    found = True
                    break
            if not found:
                print("Rider ID not found!")

        elif choice == "0":
            save_riders(riders)
            print("Exiting system. Have a great day!")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()