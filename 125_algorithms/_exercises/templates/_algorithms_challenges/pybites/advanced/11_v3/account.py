c_ Account:

    ___ - , name, start_balance=0
        name = name
        start_balance = start_balance
        _transactions    # list

    $
    ___ balance
        r.. start_balance + s..(_transactions)

    ___ __len__
        r.. l..(_transactions)

    ___ __lt__  other
        __ n.. isi..(other, Account
            r.. V...()
        r.. balance < other.balance

    ___ __gt__  other
        __ n.. isi..(other, Account
            r.. V...()
        r.. balance > other.balance

    ___ __eq__  other
        __ n.. isi..(other, Account
            r.. V...()
        r.. balance __ other.balance

    ___ __le__  other
        __ n.. isi..(other, Account
            r.. V...()
        r.. balance <= other.balance

    ___ __ge__  other
        __ n.. isi..(other, Account
            r.. V...()
        r.. balance >= other.balance

    ___ __getitem__  item
        r.. _transactions[item]

    ___ __add__  other
        __ n.. isi..(other, i..
            r.. V...
        _transactions.a..(other)

    ___ __sub__  other
        __ n.. isi..(other, i..
            r.. V...
        _transactions.a..(-other)

    ___ __str__
        r.. f'{name} account - balance: {balance}'
