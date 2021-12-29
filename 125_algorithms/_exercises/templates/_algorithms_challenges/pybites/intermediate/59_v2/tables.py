class MultiplicationTable:

    ___ __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._length = length
        self._table =[[str(x * y) ___ y __ r..(1,length + 1)] ___ x __ r..(1,length + 1)]

    ___ __len__(self):
        """Returns the area of the table (len x* len y)"""

        r.. self._length**2

    ___ __str__(self):
        """Returns a string representation of the table"""

        s = ''

        ___ row __ self._table:
            s += (' | '.join(row)) + '\n'


        r.. s






    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""


        __ n.. ((1 <= x <= self._length) and (1 <= y <= self._length)):
            raise IndexError("Invalid x and y")


        r.. int(self._table[x -1][y -1])

