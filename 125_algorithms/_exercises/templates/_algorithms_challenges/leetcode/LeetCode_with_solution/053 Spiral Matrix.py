"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
__author__ = 'Danyang'


class Solution:
    ___ spiralOrder(self, matrix):
        """
              top
               |
        left --+-- right
               |
             bottom

             t
             __
          l |  | r
            |__|
             b

        be careful with the index: be greedy for the first scan
        [[1,2,3],
         [8,9,4],
         [7,6,5]]

        if not greedy, the middle 9 won't be scanned
        [[1,2,3],
         [8,x,4],
         [7,6,5]]

        :param matrix: a list of lists of integers
        :return: a list of integers
        """
        __ n.. matrix o. n.. matrix[0]:
            r.. matrix

        result    # list

        left = 0
        right = l..(matrix[0]) - 1
        top = 0
        bottom = l..(matrix) - 1

        while left <= right and top <= bottom:
            ___ c __ xrange(left, right + 1):
                result.a..(matrix[top][c])
            ___ r __ xrange(top + 1, bottom + 1):
                result.a..(matrix[r][right])
            ___ c __ xrange(right - 1, left - 1, -1):
                __ top < bottom:  # avoid double scanning the first row
                    result.a..(matrix[bottom][c])
            ___ r __ xrange(bottom - 1, top, -1):
                __ left < right:  # avoid double scanning the first column
                    result.a..(matrix[r][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        r.. result

__ __name____"__main__":
    print Solution().spiralOrder([[2, 3]])
