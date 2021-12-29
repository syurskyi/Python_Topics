class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._length = length
        self._table =[[str(x * y) for y in range(1,length + 1)] for x in range(1,length + 1)]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""

        return self._length**2

    def __str__(self):
        """Returns a string representation of the table"""

        s = ''

        for row in self._table:
            s += (' | '.join(row)) + '\n'


        return s






    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""


        if not ((1 <= x <= self._length) and (1 <= y <= self._length)):
            raise IndexError("Invalid x and y")


        return int(self._table[x -1][y -1])

