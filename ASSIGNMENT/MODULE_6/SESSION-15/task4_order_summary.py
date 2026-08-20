try:
   
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    
    total_price = price * quantity

except ValueError:
   
    print("Error: Please enter valid numbers.")

else:
   
    print("Total Price:", total_price)

finally:
   
    print("Thank you for shopping!")