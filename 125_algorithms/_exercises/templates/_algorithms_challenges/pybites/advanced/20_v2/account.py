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

    ___ __enter__
        r.. self

    ___ __exit__(self, *_):
        w.... balance < 0:
            _transactions.pop()
        r.. self
