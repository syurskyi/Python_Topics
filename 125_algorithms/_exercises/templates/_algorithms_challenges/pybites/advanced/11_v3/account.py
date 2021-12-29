class Account:

    ___ __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    ___ balance(self):
        return self.start_balance + sum(self._transactions)

    ___ __len__(self):
        return len(self._transactions)

    ___ __lt__(self, other):
        __ not isinstance(other, Account):
            raise ValueError()
        return self.balance < other.balance

    ___ __gt__(self, other):
        __ not isinstance(other, Account):
            raise ValueError()
        return self.balance > other.balance

    ___ __eq__(self, other):
        __ not isinstance(other, Account):
            raise ValueError()
        return self.balance == other.balance

    ___ __le__(self, other):
        __ not isinstance(other, Account):
            raise ValueError()
        return self.balance <= other.balance

    ___ __ge__(self, other):
        __ not isinstance(other, Account):
            raise ValueError()
        return self.balance >= other.balance

    ___ __getitem__(self, item):
        return self._transactions[item]

    ___ __add__(self, other):
        __ not isinstance(other, int):
            raise ValueError
        self._transactions.append(other)

    ___ __sub__(self, other):
        __ not isinstance(other, int):
            raise ValueError
        self._transactions.append(-other)

    ___ __str__(self):
        return f'{self.name} account - balance: {self.balance}'
