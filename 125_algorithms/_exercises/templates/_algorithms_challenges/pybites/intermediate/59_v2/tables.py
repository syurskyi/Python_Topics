c_ MultiplicationTable:

    ___ - , length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        _length = length
        _table =[[s..(x * y) ___ y __ r..(1,length + 1)] ___ x __ r..(1,length + 1)]

    ___ __len__
        """Returns the area of the table (len x* len y)"""

        r.. _length**2

    ___ __str__
        """Returns a string representation of the table"""

        s = ''

        ___ row __ _table:
            s += (' | '.j..(row)) + '\n'


        r.. s






    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""


        __ n.. ((1 <= x <= _length) a.. (1 <= y <= _length)):
            raise IndexError("Invalid x and y")


        r.. i..(_table[x -1][y -1])

