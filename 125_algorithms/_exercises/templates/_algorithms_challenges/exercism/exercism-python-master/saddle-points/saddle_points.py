"""Finds saddle points in a rectangular 2d array"""

___ saddle_points(matrix
    """Finds points that are the largest in their row
    and smallest in their column
    """
    saddles = set()
    min_col = {}
    ___ r, row __ enumerate(matrix
        max_row = ma.(row)
        ___ c __ range(le.(row)):
            __ c not __ min_col:
                try:
                    min_col[c] = min(_row[c] ___ _row __ matrix)
                except IndexError:
                    raise ValueError
            __ max_row __ min_col[c]:
                saddles.add((r, c))
    r_ saddles
