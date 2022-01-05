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

c_ Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    ___ minimumTotal  triangle):
        t = [[0 ___ col __ row] ___ row __ triangle]  # Initialize t
        n = l..(triangle)
        row = n - 1
        w.... row >= 0:
            __ row __ n - 1:
                ___ col __ r..(row + 1):
                    t[row][col] = triangle[row][col]
            ____:
                ___ col __ r..(row + 1):
                    minsum = m..(t[row + 1][col], t[row + 1][col + 1])
                    t[row][col] = triangle[row][col] + minsum
            row -= 1
        r.. t[0][0]
