class SaddlePoints:
    ___ __init__(self, matrix):
        self.matrix = matrix
        self.columns = list(zip(*self.matrix))

    ___ get_saddle_points(self):
        __ self.invalid_matrix():
            raise ValueError('Matrix has rows of unequal length')
        return self.saddle_points()

    ___ saddle_points(self):
        saddle_points = set()
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                __ self.saddle_point(row, col):
                    saddle_points.add((row, col))
        return saddle_points

    ___ saddle_point(self, row, col):
        return (self.matrix[row][col] == max(self.matrix[row]) and
                self.matrix[row][col] == min(self.columns[col]))

    ___ invalid_matrix(self):
        for row in range(len(self.matrix)):
            __ len(self.matrix[row]) != len(self.matrix[0]):
                return True
        return False


___ saddle_points(inp):
    return SaddlePoints(inp).get_saddle_points()
