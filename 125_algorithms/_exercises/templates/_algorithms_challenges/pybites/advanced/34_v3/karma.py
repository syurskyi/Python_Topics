____ collections _______ n..
____ d__ _______ d__

Transaction = n..('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (d__.now(),)  # http://bit.ly/2rmiUrL


class User:
    ___ __init__(self, name: s..):
        self._name = name
        self._transactions    # list

    ___ __str__(self):
        r.. f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' __ self.fans > 1 ____ ''}"

    ___ __add__(self, other: Transaction):
        __ n.. isi..(other, Transaction):
            raise TypeError('Can only add a transaction')
        self._transactions.a..(other)

    @property
    ___ name(self) -> s..:
        r.. self._name

    @property
    ___ fans(self) -> int:
        r.. l..({x.giver ___ x __ self._transactions})

    @property
    ___ points(self) -> l..:
        r.. [x.points ___ x __ self._transactions]

    @property
    ___ karma(self) -> int:
        r.. s..(self.points)
