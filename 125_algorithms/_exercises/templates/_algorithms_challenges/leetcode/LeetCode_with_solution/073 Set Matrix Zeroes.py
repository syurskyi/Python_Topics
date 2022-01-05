"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
__author__ = 'Danyang'
c_ Solution:
    ___ setZeroes_error  matrix):
        """
        store the zero at the head

        constant space, O(2)
        :param matrix: a list of lists of integers
        :return: NOTHING, MODIFY matrix IN PLACE.
        """
        __ n.. matrix:
            r..

        m = l..(matrix)
        n = l..(matrix[0])

        ___ row __ xrange(m):
            ___ col __ xrange(n):
                __ matrix[row][col]__0:
                    matrix[0][col]=0  # previously scanned, safe to modify
                    matrix[row][0]=0  # previously scanned, safe to modify

        ___ row __ xrange(m):
            __ matrix[row][0]__0:
                ___ col __ xrange(n):
                    matrix[row][col] = 0

        ___ col __ xrange(n):
            __ matrix[0][col]__0:
                ___ row __ xrange(m):
                    matrix[row][col] = 0


    ___ setZeroes  matrix):
        """
        store the zero at the head
        constant space
        :param matrix: a list of lists of integers
        :return: NOTHING, MODIFY matrix IN PLACE.
        """
        __ n.. matrix:
            r..

        m = l..(matrix)
        n = l..(matrix[0])

        # special treatment for row and col 
        clear_first_row = F..
        clear_first_col = F..
        ___ row __ xrange(m):
            __ matrix[row][0]__0:
                clear_first_col = T..
        ___ col __ xrange(n):
            __ matrix[0][col]__0:
                clear_first_row = T..

        ___ row __ xrange(1, m):
            ___ col __ xrange(1, n):
                __ matrix[row][col]__0:
                    matrix[0][col] = 0  # previously scanned, safe to modify
                    matrix[row][0] = 0  # previously scanned, safe to modify

        ___ row __ xrange(1, m):  # avoid 0 at (0, 0) affect the entire matrix
            __ matrix[row][0]__0:
                ___ col __ xrange(n):
                    matrix[row][col] = 0

        ___ col __ xrange(1, n):  # avoid 0 at (0, 0) affect the entire matrix
            __ matrix[0][col]__0:
                ___ row __ xrange(m):
                    matrix[row][col] = 0

        __ clear_first_row:
            ___ col __ xrange(n):
                matrix[0][col] = 0
        __ clear_first_col:
            ___ row __ xrange(m):
                matrix[row][0] = 0



