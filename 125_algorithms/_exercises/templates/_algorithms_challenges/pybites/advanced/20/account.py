c_ Account:

    ___ - ):
        _transactions    # list

    $
    ___ balance
        r.. s..(_transactions)

    ___ __add__  amount):
        _transactions.a..(amount)

    ___ __sub__  amount):
        _transactions.a..(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager


    ___ __enter__
        r.. self
    
    
    ___ __exit__ exception_type,exception_value,exception_traceback):

        


        w.... balance < 0:
            _transactions.pop()


        

