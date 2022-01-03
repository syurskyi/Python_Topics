'''
Created on Mar 20, 2017

@author: MT
'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
c_ NestedInteger(object):
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

c_ Solution(object):
    ___ depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        r.. helper(nestedList, 1)
    
    ___ helper(self, nestedList, level):
        sumVal = 0
        ___ ni __ nestedList:
            __ ni.isInteger():
                sumVal += ni.getInteger()*level
            ____:
                sumVal += helper(ni.getList(), level+1)
        r.. sumVal
    
