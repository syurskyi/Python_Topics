"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].


[1,1,1,1,1],
[1,1,1,1,1],
[1,2,1,1,1],
[1,3,3,1,1],
[1,4,6,4,1],

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object
    ___ getRow(self, rowIndex
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1 ___ i in range(rowIndex + 1)]
        ___ row in range(rowIndex + 1
            ___ col in range(1, row
                col = row - col
                res[col] += res[col - 1]
        r_ res

s = Solution()
print s.getRow(3)
