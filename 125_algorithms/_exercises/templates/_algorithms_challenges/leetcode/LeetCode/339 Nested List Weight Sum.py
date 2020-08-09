"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object
    ___ isInteger(self
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    ___ getInteger(self
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    ___ getList(self
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution(object
    ___ __init__(self
        self.su. = 0

    ___ depthSum(self, nestedList
        """
        NestedInteger is  a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        ___ elt in nestedList:
            self.dfs(elt, 1)

        r_ self.su.

    ___ dfs(self, ni, depth
        __ ni.isInteger(
            self.su. += ni.getInteger() * depth
        ____
            lst = ni.getList()
            ___ elt in lst:
                self.dfs(elt, depth + 1)
