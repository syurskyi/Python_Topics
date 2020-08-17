class Account:

    ___ __init__(self
        self._transactions = []

    @property
    ___ balance(self
        r_ su.(self._transactions)

    ___ __add__(self, amount
        self._transactions.append(amount)

    ___ __sub__(self, amount
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    ___ __enter__(self
        self._rollback = self._transactions.copy()
        r_ self

    ___ __exit__(self, exc_type, exc_val, exc_tb
        __ exc_type pa__ not None or self.balance < 0:
            self._transactions = self._rollback
        self._rollback = None
        r_ self
