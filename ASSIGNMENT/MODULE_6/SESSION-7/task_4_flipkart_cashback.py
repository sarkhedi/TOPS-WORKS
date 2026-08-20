cart_value = int(input("Enter Flipkart cart value: "))

payment_method = input("Enter payment method (UPI/Card/Cash): ")

if cart_value > 1000:
    
    if payment_method == "UPI":
        print("Eligible for 10% cashback")
    
    else:
        print("Eligible for 5% cashback")

else:
    print("No cashback")