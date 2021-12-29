from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:


    ___ __init__(self,name):
        self.name = name
        self.karma = 0
        self.fan_names = set()
        self.points = []
        self._transactions = []

    

    @property
    ___ fans(self):
        return len(self.fan_names)

    ___ __add__(self,transaction):
        __ isinstance(transaction,Transaction):
            
            self._transactions.append(transaction)
            self.karma += transaction.points
            self.points.append(transaction.points)
            self.fan_names.add(transaction.giver)
    

    ___ __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' __ self.fans > 1 else ''}"
