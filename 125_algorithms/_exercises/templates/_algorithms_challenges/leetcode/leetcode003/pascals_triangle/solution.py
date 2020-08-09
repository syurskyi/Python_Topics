"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object
    ___ generate(self, numRows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        __ numRows __ 0:
            r_ res
        res.append([1])
        __ numRows __ 1:
            r_ res
        res.append([1, 1])
        __ numRows __ 2:
            r_ res
        # n is current row index (starting from 0)
        for n in range(2, numRows
            cur = []
            for i in range(n + 1
                __ i __ 0:
                    cur.append(1)
                ____ i __ n:
                    cur.append(1)
                ____
                    c = res[n - 1][i - 1] + res[n - 1][i]
                    cur.append(c)
            res.append(cur)
        r_ res
