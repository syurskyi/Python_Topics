"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is
the total number of rows in the triangle.
"""

class Solution(object
    ___ minimumTotal(self, triangle
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = le.(triangle)
        m = 0
        res = None
        ___ i, row in enumerate(triangle
            m = le.(row)
            __ i > 0:
                ___ j, col in enumerate(row
                    __ 0 < j < m - 1:
                        triangle[i][j] += min(triangle[i - 1][j - 1],
                                              triangle[i - 1][j])
                    ____ j __ 0:
                        triangle[i][j] += triangle[i - 1][j]
                    # j == m - 1
                    ____
                        triangle[i][j] += triangle[i - 1][j - 1]
            __ i __ n - 1:
                ___ col in row:
                    __ res is None:
                        res = col
                    ____
                        res = min(col, res)
        r_ res


a1 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

s = Solution()
print(s.minimumTotal(a1))
