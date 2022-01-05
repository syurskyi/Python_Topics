"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
__author__ = 'Danyang'
c_ Solution:
    ___ getRow  rowIndex):
        """
        iteration.

        Math

        indexing
        use only O(k) extra space
        :param rowIndex: integer
        :return: a list of integers
        """
        __ rowIndex<0:
            r.. N..
        __ rowIndex__0:
            r.. [1]

        current_level = [1, 1]
        ___ row __ x..(2, rowIndex+1):

            # generating next level
            temp = current_level[0]
            ___ col __ x..(1, row): # middle
                summation = current_level[col] + temp
                temp = current_level[col]
                current_level[col] = summation

            current_level.a..(1)

        r.. current_level


__ _____ __ ____
    print Solution().getRow(3)