def calculate_cashback(amount, cashback_rate=0.05):

    cashback = amount * cashback_rate

    return cashback

zomato_cashback = calculate_cashback(500)

flipkart_cashback = calculate_cashback(2000, 0.07)


print("Zomato Cashback:", zomato_cashback)
print("Flipkart Cashback:", flipkart_cashback)