# source: https://dbader.org/blog/python-dunder-methods
from functools import total_ordering


@total_ordering
class Account:
    'A simple account class'

    ___ __init__(self, owner, amount=0):
        'This is the constructor that lets us create objects from this class'
        self.owner = owner
        self.amount = amount
        self._transactions = []

    ___ __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    ___ __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner,
                                                               self.amount)

    ___ add_transaction(self, amount):
        __ not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    ___ balance(self):
        return self.amount + sum(self._transactions)

    ___ __len__(self):
        return len(self._transactions)

    ___ __getitem__(self, position):
        return self._transactions[position]

    ___ __eq__(self, other):
        return self.balance == other.balance

    ___ __lt__(self, other):
        return self.balance < other.balance

    ___ __add__(self, other):
        owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc