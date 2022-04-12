c_ Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    ___ setZeroes  matrix
        n l..(matrix)
        m l..(matrix 0
        column_zero F..
        row_zero F..
        ___ i __ r..(n
            ___ j __ r..(m
                __ matrix[i][j] __ 0:
                    # Check whether the first row and column contain
                    # zeroes before recording
                    __ i __ 0:
                        row_zero T..
                    __ j __ 0:
                        column_zero T..
                    # Record zeroes using the first row and column
                    matrix[i][0] 0
                    matrix[0][j] 0
        # Set zeroes except for the first row and column
        ___ i __ r..(n
            ___ j __ r..(m
                __ i > 0 a.. j > 0:
                    __ matrix[0][j] __ 0 o. matrix[i][0] __ 0:
                        matrix[i][j] 0
        # Set the first row and column
        __ row_zero:
            ___ j __ r..(m
                matrix[0][j] 0
        __ column_zero:
            ___ i __ r..(n
                matrix[i][0] 0
