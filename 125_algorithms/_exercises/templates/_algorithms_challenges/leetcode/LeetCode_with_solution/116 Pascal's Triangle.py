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
class Solution:
    ___ generate(self, numRows):
        """
        math
        :param numRows: integer
        :return: a list of lists of integers
        """
        result = []
        for row in xrange(numRows):
            current = []
            for col in xrange(row+1):
                __ col==0 or col==row:
                    current.append(1)
                else:
                    current.append(result[row-1][col-1]+result[row-1][col])
            result.append(current)

        return result

__ __name__=="__main__":
    print Solution().generate(5)