def count_likes(post):

    total_likes = post["likes"]

    if "replies" in post:

        for reply in post["replies"]:
            total_likes += count_likes(reply)

    return total_likes

instagram_post = {
    "likes": 100,
    "replies": [
        {
            "likes": 50,
            "replies": [
                {
                    "likes": 20
                }
            ]
        },
        {
            "likes": 30
        }
    ]
}


total = count_likes(instagram_post)


print("Total Likes:", total)