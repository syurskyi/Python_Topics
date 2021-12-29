# source: https://dbader.org/blog/python-dunder-methods
____ functools _______ total_ordering


@total_ordering
class Account:
    'A simple account class'

    ___ __init__(self, owner, amount=0):
        'This is the constructor that lets us create objects from this class'
        self.owner = owner
        self.amount = amount
        self._transactions    # list

    ___ __repr__(self):
        r.. 'Account({!r}, {!r})'.f..(self.owner, self.amount)

    ___ __str__(self):
        r.. 'Account of {} with starting amount: {}'.f..(self.owner,
                                                               self.amount)

    ___ add_transaction(self, amount):
        __ n.. isi..(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.a..(amount)

    @property
    ___ balance(self):
        r.. self.amount + s..(self._transactions)

    ___ __len__(self):
        r.. l..(self._transactions)

    ___ __getitem__(self, position):
        r.. self._transactions[position]

    ___ __eq__(self, other):
        r.. self.balance __ other.balance

    ___ __lt__(self, other):
        r.. self.balance < other.balance

    ___ __add__(self, other):
        owner = '{}&{}'.f..(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        ___ t __ l..(self) + l..(other):
            acc.add_transaction(t)
        r.. acc