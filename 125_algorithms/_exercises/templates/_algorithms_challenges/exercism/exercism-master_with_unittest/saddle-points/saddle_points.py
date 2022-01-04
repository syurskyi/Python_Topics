c_ SaddlePoints:
    ___ - , matrix):
        matrix = matrix
        columns = l..(z..(*matrix))

    ___ get_saddle_points
        __ invalid_matrix
            r.. ValueError('Matrix has rows of unequal length')
        r.. saddle_points()

    ___ saddle_points
        saddle_points = set()
        ___ row __ r..(l..(matrix)):
            ___ col __ r..(l..(matrix[row])):
                __ saddle_point(row, col):
                    saddle_points.add((row, col))
        r.. saddle_points

    ___ saddle_point(self, row, col):
        r.. (matrix[row][col] __ max(matrix[row]) a..
                matrix[row][col] __ m..(columns[col]))

    ___ invalid_matrix
        ___ row __ r..(l..(matrix)):
            __ l..(matrix[row]) != l..(matrix[0]):
                r.. T..
        r.. F..


___ saddle_points(inp):
    r.. SaddlePoints(inp).get_saddle_points()
