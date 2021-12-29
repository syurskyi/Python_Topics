"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
__author__ = 'Danyang'


class Solution:
    ___ generateMatrix(self, n):
        """
        algorithm: array, simulation
        :param n: Integer
        :return: a list of lists of integer
        """
        left = 0
        right = n - 1 # [0, n)
        top = 0
        bottom = n - 1  # [0, n)

        result = [[-1 ___ _ __ xrange(n)] ___ _ __ xrange(n)]
        num = 1
        while left <= right and top <= bottom:
            ___ i __ xrange(left, right + 1):  # tuning ending condition, be greedy
                result[top][i] = num
                num += 1
            ___ i __ xrange(top + 1, bottom):
                result[i][right] = num
                num += 1

            ___ i __ xrange(right, left, -1):
                result[bottom][i] = num
                num += 1
            ___ i __ xrange(bottom, top, -1):
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        r.. result


class SolutionError:
    ___ generateMatrix(self, n):
        """
        algorithm: array, simulation
        :param n: Integer
        :return: a list of lists of integer
        """
        left = 0
        right = n - 1 # [0, n)
        top = 0
        bottom = n - 1  # [0, n)

        result = [[-1 ___ _ __ xrange(n)] ___ _ __ xrange(n)]
        num = 1
        while left <= right and top <= bottom:
            ___ i __ xrange(left, right):  # tuning ending condition, this will fail in the middle
                result[top][i] = num
                num += 1
            ___ i __ xrange(top, bottom):
                result[i][right] = num
                num += 1

            ___ i __ xrange(right, left, -1):
                result[bottom][i] = num
                num += 1

            ___ i __ xrange(bottom, top, -1):
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        r.. result


__ __name____"__main__":
    result = Solution().generateMatrix(4)
    ___ row __ result:
        print row
