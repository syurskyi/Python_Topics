class Account:

    ___ __init__(self):
        self._transactions = []

    @property
    ___ balance(self):
        return sum(self._transactions)

    ___ __add__(self, amount):
        self._transactions.append(amount)

    ___ __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager


    ___ __enter__(self):
        return self
    
    
    ___ __exit__(self,exception_type,exception_value,exception_traceback):

        


        while self.balance < 0:
            self._transactions.pop()


        

