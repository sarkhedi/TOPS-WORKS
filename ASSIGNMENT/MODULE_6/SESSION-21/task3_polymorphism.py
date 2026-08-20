class Influencer:

    def bonus(self):
        return 2000


class BrandManager:

    def bonus(self):
        return 5000

def show_bonus(employee):

    print("Bonus:", employee.bonus())

influencer = Influencer()
brand_manager = BrandManager()

show_bonus(influencer)
show_bonus(brand_manager)