#hiding the complex information
from abc import ABC, abstractmethod
class Phonepay(ABC):
    def senderinfo(self):
        print("You can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need to enter the pin")
    @abstractmethod
    def transaction(self):
        pass
class HDFC(Phonepay):
    def transaction(self):
        print("Payment using HDFC bank")
class SBI(Phonepay):
    def transaction(self):
        print("Payment using SBI bank")
class UNION(Phonepay):
    def transaction(self):
        print("Payment using UNION bank")
class AXIS(Phonepay):
    def transaction(self):
        print("Payment using AXIS bank")
class ICICI(Phonepay):
    def transaction(self):
        print("Payment using ICICI bank")