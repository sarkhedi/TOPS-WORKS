# Movies =[
#     "Dhurandhar",
#     "Avatar",
#     "War 2",
#     "Stree 2",
#     "Spider-Man: Brand New Day"
# ]

# movie_iterator = iter(Movies)

# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))
# print(next(movie_iterator))

#While Loops 

movies = [
    "Dhurandhar",
    "Avatar",
    "War 2",
    "Stree 2",
    "Pushpa 2"
]

movie_iterator = iter(movies)

while True:
    try:
        movie = next(movie_iterator)
        print(movie)

    except StopIteration:
        break