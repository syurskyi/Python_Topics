class SaddlePoints:
    ___ __init__(self, matrix):
        self.matrix = matrix
        self.columns = l..(zip(*self.matrix))

    ___ get_saddle_points(self):
        __ self.invalid_matrix():
            raise ValueError('Matrix has rows of unequal length')
        r.. self.saddle_points()

    ___ saddle_points(self):
        saddle_points = set()
        ___ row __ r..(l..(self.matrix)):
            ___ col __ r..(l..(self.matrix[row])):
                __ self.saddle_point(row, col):
                    saddle_points.add((row, col))
        r.. saddle_points

    ___ saddle_point(self, row, col):
        r.. (self.matrix[row][col] __ max(self.matrix[row]) and
                self.matrix[row][col] __ m..(self.columns[col]))

    ___ invalid_matrix(self):
        ___ row __ r..(l..(self.matrix)):
            __ l..(self.matrix[row]) != l..(self.matrix[0]):
                r.. True
        r.. False


___ saddle_points(inp):
    r.. SaddlePoints(inp).get_saddle_points()
