# balance.py

class Balance:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def cash_deposit(self, amount):
        self.balance += amount
        return True
