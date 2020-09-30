# Rotate Image
# Question: You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Solutions:


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix


Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])