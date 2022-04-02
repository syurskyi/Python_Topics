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


c_ Solution(o..
    ___ generate  numRows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res    # list
        __ numRows __ 0:
            r.. res
        res.a..([1])
        __ numRows __ 1:
            r.. res
        res.a..([1, 1])
        __ numRows __ 2:
            r.. res
        # n is current row index (starting from 0)
        ___ n __ r..(2, numRows
            cur    # list
            ___ i __ r..(n + 1
                __ i __ 0:
                    cur.a..(1)
                ____ i __ n:
                    cur.a..(1)
                ____:
                    c = res[n - 1][i - 1] + res[n - 1][i]
                    cur.a..(c)
            res.a..(cur)
        r.. res
