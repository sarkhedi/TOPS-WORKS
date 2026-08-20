import os

files = os.listdir()

for file in files:

    if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
        print(file)