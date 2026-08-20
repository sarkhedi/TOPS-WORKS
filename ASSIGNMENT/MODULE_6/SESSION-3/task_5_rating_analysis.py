ratings = ['4.5', '3.0', '5', '4.2']

float_ratings =[]

for rating in ratings:
    float_rating = float(rating)
    float_ratings.append(float_rating)

highest_rating = max(float_ratings)

print("Highest rating is:",highest_rating)