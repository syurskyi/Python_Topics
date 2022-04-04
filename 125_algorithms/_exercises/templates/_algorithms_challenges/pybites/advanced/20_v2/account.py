c_ Account:

    ___ -
        _transactions    # list

    $
    ___ balance
        r.. s..(_transactions)

    ___ __add__  amount
        _transactions.a..(amount)

    ___ __sub__  amount
        _transactions.a..(-amount)

    ___ __enter__
        r.. self

    ___ __exit__  *_
        w.... balance < 0:
            _transactions.p.. )
        r.. self
