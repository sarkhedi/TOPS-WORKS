followers = int(input("Enter number of followers: "))

if followers < 10000:
    print("Micro Influencer")

elif followers >= 10000 and followers <= 100000:
    print("Rising Star")

else:
    print("Celebrity")