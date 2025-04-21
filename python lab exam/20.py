# Custom Exceptions
class InvalidAccountException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

# Account Class
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient balance for withdrawal.")
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

# Create accounts
acc1 = Account(10000, 12345)
acc2 = Account(5000, 67890)
accounts = [acc1, acc2]

print("1.Debit\n2.Credit\n3.Display Balance")
choice = int(input("Enter your choice"))

if choice==1:
    self.debit=
