class User:

    def get_status(self):
        return "active"


class PremiumUser(User):

    def get_status(self):
        return "premium"


user1 = User()
premium_user1 = PremiumUser()

print("User Status:", user1.get_status())
print("Premium User Status:", premium_user1.get_status())