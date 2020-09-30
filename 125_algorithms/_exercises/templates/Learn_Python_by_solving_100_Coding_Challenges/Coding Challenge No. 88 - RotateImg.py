# Rotate Image
# Question: You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Solutions:


c_ Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    ___ rotate(self, matrix):
        n _ le.(matrix)
        ___ i __ ra..(n):
            ___ j __ ra..(i+1, n):
                matrix[i][j], matrix[j][i] _ matrix[j][i], matrix[i][j]
        ___ i __ ra..(n):
            matrix[i].reverse()
        r_ matrix


Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])