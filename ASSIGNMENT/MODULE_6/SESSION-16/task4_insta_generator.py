def insta_posts_generator(posts):
    
    for post in posts:
       
        yield post

posts = [
    "Good vibes only!",
    "Weekend memories ",
    "Learning Python!",
    "Coffee and coding ",
    "Keep growing!"
]


post_generator = insta_posts_generator(posts)


try:
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))

except StopIteration:
    print("All posts have been printed.")