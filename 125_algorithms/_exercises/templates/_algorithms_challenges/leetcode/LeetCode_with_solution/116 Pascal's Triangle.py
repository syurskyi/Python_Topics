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
__author__ = 'Danyang'
c_ Solution:
    ___ generate  numRows
        """
        math
        :param numRows: integer
        :return: a list of lists of integers
        """
        result    # list
        ___ row __ x..(numRows
            current    # list
            ___ col __ x..(row+1
                __ col__0 o. col__row:
                    current.a..(1)
                ____
                    current.a..(result[row-1][col-1]+result[row-1][col])
            result.a..(current)

        r.. result

__ _____ __ ____
    print Solution().generate(5)