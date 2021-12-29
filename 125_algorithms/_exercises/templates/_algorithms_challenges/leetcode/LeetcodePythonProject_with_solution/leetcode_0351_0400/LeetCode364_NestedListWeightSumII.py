'''
Created on Mar 28, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    ___ __init__(self, value_ N..
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    ___ isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    ___ add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    ___ setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    ___ getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    ___ getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class Solution(object):
    ___ depthSumInverse(self, nestedList):
        queue = nestedList
        result = 0
        prev = 0
        while queue:
            sumVal = 0
            size = l..(queue)
            ___ _ __ r..(size):
                ni = queue.pop(0)
                __ ni.isInteger():
                    sumVal += ni.getInteger()
                ____:
                    ___ ni0 __ ni.getList():
                        queue.a..(ni0)
            prev += sumVal
            result += prev
        r.. result
