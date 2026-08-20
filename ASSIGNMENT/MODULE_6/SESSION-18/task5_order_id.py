import re

pattern = r"OD\d{18}"

orders = [
    "OD123456789012345000",
    "Order ID is OD987654321098765432",
    "OD12345",
    "ABC123456789012345678"
]

for order in orders:
    result = re.search(pattern, order)
    
    if result:
        print("Match found:", result.group())
    else:
        print("No match:", order)