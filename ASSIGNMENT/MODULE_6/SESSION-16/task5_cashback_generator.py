def cashback_generator(transactions):
    for amount in transactions:

        cashback = amount * 5 / 100

        yield cashback


transactions = [
    1000,
    500,
    2000,
    750,
    1200
]

cashback = cashback_generator(transactions)

for value in cashback:
    print("Cashback: ₹", value)