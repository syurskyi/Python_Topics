class Account:

    ___ __init__(self, name, start_balance=0
        self.name = name
        self.start_balance = start_balance
        self._transactions =   # list

    @property
    ___ balance(self
        r_ self.start_balance + su.(self._transactions)

    ___ __len__(self
        r_ le.(self._transactions)

    ___ __lt__(self, other
        __ not isinstance(other, Account
            raise ValueError()
        r_ self.balance < other.balance

    ___ __gt__(self, other
        __ not isinstance(other, Account
            raise ValueError()
        r_ self.balance > other.balance

    ___ __eq__(self, other
        __ not isinstance(other, Account
            raise ValueError()
        r_ self.balance __ other.balance

    ___ __le__(self, other
        __ not isinstance(other, Account
            raise ValueError()
        r_ self.balance <= other.balance

    ___ __ge__(self, other
        __ not isinstance(other, Account
            raise ValueError()
        r_ self.balance >= other.balance

    ___ __getitem__(self, item
        r_ self._transactions[item]

    ___ __add__(self, other
        __ not isinstance(other, int
            raise ValueError
        self._transactions.append(other)

    ___ __sub__(self, other
        __ not isinstance(other, int
            raise ValueError
        self._transactions.append(-other)

    ___ __str__(self
        r_ f'{self.name} account - balance: {self.balance}'
