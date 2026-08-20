from datetime import datetime
date_input = input("Enter date (YYYY-MM-DD): ")

date = datetime.strptime(date_input, "%Y-%m-%d")

day = date.strftime("%A")
print("Day:", day)