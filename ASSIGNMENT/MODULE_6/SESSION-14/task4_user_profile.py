import json

with open("user_profile.json","r") as file:

    data = json.load(file)

print("Username:",data["username"])

print("Followers:",data["followers"])