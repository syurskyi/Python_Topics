c_ Account:

    ___ - , name, start_balance=0
        name name
        start_balance start_balance
        _transactions    # list

    $
    ___ balance
        r.. start_balance + s..(_transactions)
    

    ___ __len__
        r.. l..(_transactions)
    

    ___ -e other
        __ isi..(other,Account
            r.. balance __ other.balance
    
    ___ __lt__ other
        __ isi..(other,Account
            r.. balance < other.balance
    
    

    ___ __gt__ other
        __ isi..(other,Account
            r.. balance > other.balance
    ___ __le__ other
        __ isi..(other,Account
            r.. balance <_ other.balance

    ___ __ge__ other
        __ isi..(other,Account
            r.. balance >_ other.balance


    ___ __getitem__ index
        r.. _transactions[index]


    ___ __list__
        r.. l..(_transactions)
    

    ___ __add__ other
        __ isi..(other,i..
            _transactions.a..(other)
        ____
            r.. T..("can only subtract integer")
    

    ___ __sub__ other
        __ isi..(other,i..
            _transactions.a..(-other)
        ____
            r.. T..("can only subtract integer")

    
    ___ -s
        r.. f"{name} account - balance: {balance}"

    # add dunder methods below
