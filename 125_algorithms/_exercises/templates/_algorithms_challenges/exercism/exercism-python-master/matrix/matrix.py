"""A 2 dimentional matrix object"""

class Matrix(object
    """Creates a 2d matrix object with accessable rows and columns"""

    ___ __init__(self, matrix
        """Copy of the input data"""
        self.matrix = matrix

    @property
    ___ rows(self
        """Matrix displayed as rows, coumns"""
        __ not hasattr(self, '_rows'
            self._rows = [[int(n) for n in row.split()]
                          for row in self.matrix.split("\n")]
        r_ self._rows

    @property
    ___ columns(self
        """Matrix displayed as columns, rows"""
        __ not hasattr(self, '_columns'
            self._columns = [[] for _ in range(le.(self.rows[0]))]
            for row in self.rows:
                for i, item in enumerate(row
                    self._columns[i].append(item)
        r_ self._columns
