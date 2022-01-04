c_ Account:

    ___ - , name, start_balance=0):
        name = name
        start_balance = start_balance
        _transactions    # list

    $
    ___ balance
        r.. start_balance + s..(_transactions)

    ___ __len__
        r.. l..(_transactions)

    ___ __lt__(self, other):
        __ n.. isi..(other, Account):
            raise ValueError()
        r.. balance < other.balance

    ___ __gt__(self, other):
        __ n.. isi..(other, Account):
            raise ValueError()
        r.. balance > other.balance

    ___ __eq__(self, other):
        __ n.. isi..(other, Account):
            raise ValueError()
        r.. balance __ other.balance

    ___ __le__(self, other):
        __ n.. isi..(other, Account):
            raise ValueError()
        r.. balance <= other.balance

    ___ __ge__(self, other):
        __ n.. isi..(other, Account):
            raise ValueError()
        r.. balance >= other.balance

    ___ __getitem__(self, item):
        r.. _transactions[item]

    ___ __add__(self, other):
        __ n.. isi..(other, i..):
            raise ValueError
        _transactions.a..(other)

    ___ __sub__(self, other):
        __ n.. isi..(other, i..):
            raise ValueError
        _transactions.a..(-other)

    ___ __str__
        r.. f'{name} account - balance: {balance}'
