____ collections _______ namedtuple
____ datetime _______ datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:


    ___ __init__(self,name):
        self.name = name
        self.karma = 0
        self.fan_names = set()
        self.points    # list
        self._transactions    # list

    

    @property
    ___ fans(self):
        r.. l..(self.fan_names)

    ___ __add__(self,transaction):
        __ isi..(transaction,Transaction):
            
            self._transactions.a..(transaction)
            self.karma += transaction.points
            self.points.a..(transaction.points)
            self.fan_names.add(transaction.giver)
    

    ___ __str__(self):
        r.. f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' __ self.fans > 1 ____ ''}"
