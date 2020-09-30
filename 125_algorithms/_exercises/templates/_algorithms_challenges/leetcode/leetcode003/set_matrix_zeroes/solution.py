class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    ___ setZeroes(self, matrix
        n = le.(matrix)
        m = le.(matrix[0])
        column_zero = False
        row_zero = False
        ___ i __ range(n
            ___ j __ range(m
                __ matrix[i][j] __ 0:
                    # Check whether the first row and column contain
                    # zeroes before recording
                    __ i __ 0:
                        row_zero = True
                    __ j __ 0:
                        column_zero = True
                    # Record zeroes using the first row and column
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Set zeroes except for the first row and column
        ___ i __ range(n
            ___ j __ range(m
                __ i > 0 and j > 0:
                    __ matrix[0][j] __ 0 or matrix[i][0] __ 0:
                        matrix[i][j] = 0
        # Set the first row and column
        __ row_zero:
            ___ j __ range(m
                matrix[0][j] = 0
        __ column_zero:
            ___ i __ range(n
                matrix[i][0] = 0
