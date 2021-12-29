class Account:

    ___ __init__(self):
        self._transactions    # list

    @property
    ___ balance(self):
        r.. s..(self._transactions)

    ___ __add__(self, amount):
        self._transactions.a..(amount)

    ___ __sub__(self, amount):
        self._transactions.a..(-amount)

    ___ __enter__(self):
        r.. self

    ___ __exit__(self, *_):
        w.... self.balance < 0:
            self._transactions.pop()
        r.. self
