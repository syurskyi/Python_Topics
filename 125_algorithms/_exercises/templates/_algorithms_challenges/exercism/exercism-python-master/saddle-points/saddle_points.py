"""Finds saddle points in a rectangular 2d array"""

___ saddle_points(matrix
    """Finds points that are the largest in their row
    and smallest in their column
    """
    saddles = set()
    min_col = {}
    ___ r, row in enumerate(matrix
        max_row = max(row)
        ___ c in range(le.(row)):
            __ c not in min_col:
                try:
                    min_col[c] = min(_row[c] ___ _row in matrix)
                except IndexError:
                    raise ValueError
            __ max_row __ min_col[c]:
                saddles.add((r, c))
    r_ saddles
