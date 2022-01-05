c_ MultiplicationTable:

    ___ - , length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        _len = length
        _table = [[x * y ___ x __ r..(1, length + 1)] ___ y __ r..(1, length + 1)]

    ___ __len__
        """Returns the area of the table (len x* len y)"""
        r.. l..(_table) * l..(_table[0])

    ___ __str__
        """Returns a string representation of the table"""
        r.. '\n'.j..(' | '.j..([s..(x) ___ x __ y]) ___ y __ _table)

    ___ calc_cell  x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        __ x > _len o. y > _len:
            r.. IndexError()
        r.. _table[x - 1][y - 1]
