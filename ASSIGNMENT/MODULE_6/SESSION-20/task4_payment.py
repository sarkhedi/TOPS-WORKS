from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")

class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}")

upi_payment = UPI()
card_payment = CreditCard()

upi_payment.pay(500)
card_payment.pay(1000)