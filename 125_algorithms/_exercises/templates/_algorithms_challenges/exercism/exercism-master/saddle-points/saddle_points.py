class SaddlePoints:
    ___ __init__(self, matrix
        self.matrix = matrix
        self.columns = list(zip(*self.matrix))

    ___ get_saddle_points(self
        __ self.invalid_matrix(
            raise ValueError('Matrix has rows of unequal length')
        r_ self.saddle_points()

    ___ saddle_points(self
        saddle_points = set()
        ___ row in range(le.(self.matrix)):
            ___ col in range(le.(self.matrix[row])):
                __ self.saddle_point(row, col
                    saddle_points.add((row, col))
        r_ saddle_points

    ___ saddle_point(self, row, col
        r_ (self.matrix[row][col] __ max(self.matrix[row]) and
                self.matrix[row][col] __ min(self.columns[col]))

    ___ invalid_matrix(self
        ___ row in range(le.(self.matrix)):
            __ le.(self.matrix[row]) != le.(self.matrix[0]
                r_ True
        r_ False


___ saddle_points(inp
    r_ SaddlePoints(inp).get_saddle_points()
