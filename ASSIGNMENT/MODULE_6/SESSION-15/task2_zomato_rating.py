try:

    reviews = int(input("Enter number of reviews: "))
    
    stars = int(input("Enter total stars: "))
    average_rating = stars / reviews

    print("Average Rating:", average_rating)

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Number of reviews cannot be zero.")