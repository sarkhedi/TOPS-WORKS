
followers = [120, 1500, 23000, 800, 45000]

for count in followers:

    if count < 1000:
        print(count, "- Micro")

    elif count >= 1000 and count <= 10000:
        print(count, "- Influencer")

    else:
        print(count, "- Celebrity")