app_status = "Offline"

def check_status():

    user_status = "Online"

    print("Inside Function - User Status:", user_status)
    print("Inside Function - App Status:", app_status)

print("Before Function Call - App Status:", app_status)


check_status()

print("After Function Call - App Status:", app_status)