______ threading


class BankAccount(object
    ___ __init__(self
        self.is_open = False
        self.balance = 0
        self.lock = threading.Lock()

    ___ get_balance(self
        with self.lock:
            __ self.is_open:
                r_ self.balance
            ____
                raise ValueError

    ___ open(self
        self.is_open = True

    ___ deposit(self, amount
        with self.lock:
            __ self.is_open and amount > 0:
                self.balance += amount
            ____
                raise ValueError

    ___ withdraw(self, amount
        with self.lock:
            __ self.is_open and 0 < amount <= self.balance:
                self.balance -= amount
            ____
                raise ValueError

    ___ close(self
        self.is_open = False
