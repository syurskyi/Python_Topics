'''
Created on Mar 28, 2017

@author: MT
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
c_ NestedInteger(o..):
    ___ - , value_ N..
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        p..

    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        p..

    ___ add  elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        p..

    ___ setInteger  value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        p..

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        p..

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        p..

c_ Solution(o..):
    ___ depthSumInverse  nestedList):
        queue = nestedList
        result = 0
        prev = 0
        w.... queue:
            sumVal = 0
            size = l..(queue)
            ___ _ __ r..(size):
                ni = queue.pop(0)
                __ ni.isInteger
                    sumVal += ni.getInteger()
                ____:
                    ___ ni0 __ ni.getList
                        queue.a..(ni0)
            prev += sumVal
            result += prev
        r.. result
