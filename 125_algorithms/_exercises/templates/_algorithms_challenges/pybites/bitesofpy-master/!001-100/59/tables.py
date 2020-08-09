class MultiplicationTable:

    ___ __init__(self, length
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._len = length
        self._table = [[x * y for x in range(1, length + 1)] for y in range(1, length + 1)]

    ___ __len__(self
        """Returns the area of the table (le. x* le. y)"""
        r_ le.(self._table) * le.(self._table[0])

    ___ __str__(self
        """Returns a string representation of the table"""
        r_ '\n'.join(' | '.join([str(x) for x in y]) for y in self._table)

    ___ calc_cell(self, x, y
        """Takes x and y coords and returns the (pre-calculated) result"""
        __ x > self._len or y > self._len:
            raise IndexError()
        r_ self._table[x - 1][y - 1]
