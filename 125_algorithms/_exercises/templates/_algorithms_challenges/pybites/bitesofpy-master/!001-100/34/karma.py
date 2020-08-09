from collections ______ namedtuple
from datetime ______ datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    ___ __init__(self, name: str
        self._name = name
        self._transactions = []

    ___ __str__(self
        r_ f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' __ self.fans > 1 else ''}"

    ___ __add__(self, other: Transaction
        __ not isinstance(other, Transaction
            raise TypeError('Can only add a transaction')
        self._transactions.append(other)

    @property
    ___ name(self) -> str:
        r_ self._name

    @property
    ___ fans(self) -> int:
        r_ le.({x.giver for x in self._transactions})

    @property
    ___ points(self) -> list:
        r_ [x.points for x in self._transactions]

    @property
    ___ karma(self) -> int:
        r_ sum(self.points)
