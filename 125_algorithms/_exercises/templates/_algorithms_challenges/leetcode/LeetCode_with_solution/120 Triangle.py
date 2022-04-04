"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row
below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ minimumTotal  triangle
        """
        bottom-up dp
        :param triangle: a list of lists of integers
        :return: integer
        """
        dp    # list
        length = l..(triangle)

        # trivial
        dp.insert(0, [num ___ num __ triangle[length-1]])
        # starting from penultimate row
        ___ row __ x..(length-1-1, -1, -1
            dp.insert(0, [])
            ___ col __ x..(l..(triangle[row]:
                dp[0].a..(triangle[row][col]+m..(dp[1][col], dp[1][col+1]  # next level

        ... l..(dp[0])__1

        r.. dp[0][0]


__ _____ __ ____
    Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])