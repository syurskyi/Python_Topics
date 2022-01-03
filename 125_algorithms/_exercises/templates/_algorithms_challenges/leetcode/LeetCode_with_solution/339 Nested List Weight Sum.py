"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


c_ NestedInteger(object):
    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    ___ getInteger
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    ___ getList
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


c_ Solution(object):
    ___ - ):
        s.. = 0

    ___ depthSum(self, nestedList):
        """
        NestedInteger is  a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        ___ elt __ nestedList:
            dfs(elt, 1)

        r.. s..

    ___ dfs(self, ni, depth):
        __ ni.isInteger():
            s.. += ni.getInteger() * depth
        ____:
            lst = ni.getList()
            ___ elt __ lst:
                dfs(elt, depth + 1)
