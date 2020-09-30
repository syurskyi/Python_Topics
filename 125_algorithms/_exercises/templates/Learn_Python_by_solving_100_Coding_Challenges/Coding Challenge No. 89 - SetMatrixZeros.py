# Set Matrix Zeroes
# Question: Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place
# Solutions:

c_ Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    ___ setZeroes(self, matrix):
        m , n _ le.(matrix), le.(matrix[0])
        temp _ [[matrix[i][j] ___ j __ ra..(n)] ___ i __ ra..(m)]
        ___ i __ ra..(m):
            ___ j __ ra..(n):
                __ no. temp[i][j]:
                    setZero(i,j,n,m,matrix)

    ___ setZero(self,row,col,n,m,matrix):
        ___ i __ ra..(m):
            matrix[i][col]_0
        ___ j __ ra..(n):
            matrix[row][j]_0