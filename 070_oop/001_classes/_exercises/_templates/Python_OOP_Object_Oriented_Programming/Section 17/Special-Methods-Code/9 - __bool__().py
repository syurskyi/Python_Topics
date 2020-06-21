class SavingsAccount:

    def __init__(self, owner, acc_number):
        self.owner = owner
        self._acc_number = acc_number
        # The balance starts at 0
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount

    def __bool__(self):
        return self.balance > 0

