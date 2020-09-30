# Set Matrix Zeroes
# Question: Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place
# Solutions:

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m , n = len(matrix), len(matrix[0])
        temp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not temp[i][j]:
                    self.setZero(i,j,n,m,matrix)

    def setZero(self,row,col,n,m,matrix):
        for i in range(m):
            matrix[i][col]=0
        for j in range(n):
            matrix[row][j]=0