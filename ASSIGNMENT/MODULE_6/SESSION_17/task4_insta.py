from insta_utils import format_follower_count

followers = [1500, 2300000, 850]

for count in followers:
    formatted = format_follower_count(count)
    print(count, "->", formatted)