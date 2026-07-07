import re
class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance   # Encapsulation

    def withdraw(self, amount):
        self.__balance -= amount
        print("Balance =", self.__balance)

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def withdraw(self, amount):
        print("Savings Account")
        super().withdraw(amount)

class CurrentAccount(Account):
    def withdraw(self, amount):
        print("Current Account")
        super().withdraw(amount)

#validate account no. (6 digits)
acc = input("Enter Account Number: ")

if re.fullmatch(r"\d{6}", acc):
    s = SavingsAccount(acc, 10000)
    s.withdraw(2000)
else:
    print("Invalid Account Number")