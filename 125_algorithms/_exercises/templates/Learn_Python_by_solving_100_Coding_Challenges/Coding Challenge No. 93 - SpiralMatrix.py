# Spiral Matrix
# Question: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# For example:
# Given the following matrix:
# [ [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ] ]
# You should return [1,2,3,6,9,8,7,4,5].
# Solutions:


c_ Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    ___ spiralOrder(self, matrix):
        __ matrix __   # list:
            r_   # list
        res _   # list
        maxUp _ maxLeft _ 0
        maxDown _ le.(matrix) - 1
        maxRight _ le.(matrix[0]) - 1
        direct _ 0 # 0 go right, 1 go down, 2 go left, 3 go up
        w___ T..:
            __ direct __ 0: # go right
                ___ i __ ra..(maxLeft, maxRight + 1):
                    res.ap..(matrix[maxUp][i])
                maxUp +_ 1
            ____ direct __ 1: # go down
                ___ i __ ra..(maxUp, maxDown + 1):
                    res.ap..(matrix[i][maxRight])
                maxRight -_ 1
            ____ direct __ 2: # go left
                ___ i __ reversed(ra..(maxLeft, maxRight + 1)):
                    res.ap..(matrix[maxDown][i])
                maxDown -_ 1
            ____ # go up
                ___ i __ reversed(ra..(maxUp, maxDown + 1)):
                    res.ap..(matrix[i][maxLeft])
                maxLeft +_ 1
            __ maxUp > maxDown or maxLeft > maxRight:
                r_ res
            direct _ (direct + 1) % 4


Solution().spiralOrder([ [ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ] ])