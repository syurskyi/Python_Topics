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
    

    ___ __eq__(self,other):
        __ isi..(other,Account):
            r.. balance __ other.balance
    
    ___ __lt__(self,other):
        __ isi..(other,Account):
            r.. balance < other.balance
    
    

    ___ __gt__(self,other):
        __ isi..(other,Account):
            r.. balance > other.balance
    ___ __le__(self,other):
        __ isi..(other,Account):
            r.. balance <= other.balance

    ___ __ge__(self,other):
        __ isi..(other,Account):
            r.. balance >= other.balance


    ___ __getitem__(self,index):
        r.. _transactions[index]


    ___ __list__
        r.. l..(_transactions)
    

    ___ __add__(self,other):
        __ isi..(other,i..):
            _transactions.a..(other)
        ____:
            raise TypeError("can only subtract integer")
    

    ___ __sub__(self,other):
        __ isi..(other,i..):
            _transactions.a..(-other)
        ____:
            raise TypeError("can only subtract integer")

    
    ___ __str__
        r.. f"{name} account - balance: {balance}"

    # add dunder methods below
