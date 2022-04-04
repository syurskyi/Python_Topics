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


c_ Solution:
    ___ generateMatrix  n
        """
        algorithm: array, simulation
        :param n: Integer
        :return: a list of lists of integer
        """
        left = 0
        right = n - 1 # [0, n)
        top = 0
        bottom = n - 1  # [0, n)

        result = [[-1 ___ _ __ x..(n)] ___ _ __ x..(n)]
        num = 1
        w.... left <_ right a.. top <_ bottom:
            ___ i __ x..(left, right + 1  # tuning ending condition, be greedy
                result[top][i] = num
                num += 1
            ___ i __ x..(top + 1, bottom
                result[i][right] = num
                num += 1

            ___ i __ x..(right, left, -1
                result[bottom][i] = num
                num += 1
            ___ i __ x..(bottom, top, -1
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        r.. result


c_ SolutionError:
    ___ generateMatrix  n
        """
        algorithm: array, simulation
        :param n: Integer
        :return: a list of lists of integer
        """
        left = 0
        right = n - 1 # [0, n)
        top = 0
        bottom = n - 1  # [0, n)

        result = [[-1 ___ _ __ x..(n)] ___ _ __ x..(n)]
        num = 1
        w.... left <_ right a.. top <_ bottom:
            ___ i __ x..(left, right  # tuning ending condition, this will fail in the middle
                result[top][i] = num
                num += 1
            ___ i __ x..(top, bottom
                result[i][right] = num
                num += 1

            ___ i __ x..(right, left, -1
                result[bottom][i] = num
                num += 1

            ___ i __ x..(bottom, top, -1
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        r.. result


__ _____ __ ____
    result = Solution().generateMatrix(4)
    ___ row __ result:
        print row
