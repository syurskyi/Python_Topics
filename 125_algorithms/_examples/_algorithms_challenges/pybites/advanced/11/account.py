class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)
    

    def __len__(self):
        return len(self._transactions)
    

    def __eq__(self,other):
        if isinstance(other,Account):
            return self.balance == other.balance
    
    def __lt__(self,other):
        if isinstance(other,Account):
            return self.balance < other.balance
    
    

    def __gt__(self,other):
        if isinstance(other,Account):
            return self.balance > other.balance
    def __le__(self,other):
        if isinstance(other,Account):
            return self.balance <= other.balance

    def __ge__(self,other):
        if isinstance(other,Account):
            return self.balance >= other.balance


    def __getitem__(self,index):
        return self._transactions[index]


    def __list__(self):
        return list(self._transactions)
    

    def __add__(self,other):
        if isinstance(other,int):
            self._transactions.append(other)
        else:
            raise TypeError("can only subtract integer")
    

    def __sub__(self,other):
        if isinstance(other,int):
            self._transactions.append(-other)
        else:
            raise TypeError("can only subtract integer")

    
    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"

    # add dunder methods below
