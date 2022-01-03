c_ Account:

    ___ - ):
        _transactions    # list

    $
    ___ balance
        r.. s..(_transactions)

    ___ __add__(self, amount):
        _transactions.a..(amount)

    ___ __sub__(self, amount):
        _transactions.a..(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
    ___ __enter__
        _rollback = _transactions.c..
        r.. self

    ___ __exit__(self, exc_type, exc_val, exc_tb):
        __ exc_type __ n.. N.. o. balance < 0:
            _transactions = _rollback
        _rollback = N..
        r.. self
