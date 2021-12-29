class MultiplicationTable:

    ___ __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._len = length
        self._table = [[x * y ___ x __ r..(1, length + 1)] ___ y __ r..(1, length + 1)]

    ___ __len__(self):
        """Returns the area of the table (len x* len y)"""
        r.. l..(self._table) * l..(self._table[0])

    ___ __str__(self):
        """Returns a string representation of the table"""
        r.. '\n'.join(' | '.join([str(x) ___ x __ y]) ___ y __ self._table)

    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        __ x > self._len o. y > self._len:
            raise IndexError()
        r.. self._table[x - 1][y - 1]
