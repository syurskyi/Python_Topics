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
            self._rows = [[int(n) ___ n in row.split()]
                          ___ row in self.matrix.split("\n")]
        r_ self._rows

    @property
    ___ columns(self
        """Matrix displayed as columns, rows"""
        __ not hasattr(self, '_columns'
            self._columns = [[] ___ _ in range(le.(self.rows[0]))]
            ___ row in self.rows:
                ___ i, item in enumerate(row
                    self._columns[i].append(item)
        r_ self._columns
