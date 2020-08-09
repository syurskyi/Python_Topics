"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object
    ___ __init__(self, value=None
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    ___ isInteger(self
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    ___ add(self, elem
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    ___ setInteger(self, value
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
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

    ___ depthSumInverse(self, nestedList
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        inv_depth = self.height(nestedList)
        self.inverseDepthSum(nestedList, inv_depth)
        r_ self.su.

    ___ height(self, nl
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        __ not nl_lst:
            r_ 1
        __ nl_lst:
            r_ 1 + max(
                map(lambda x: self.height(x.getList()), nl_lst)
            )

    ___ inverseDepthSum(self, nl, inv_depth
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        __ nl_lst:
            map(lambda x: self.inverseDepthSum(x.getList(), inv_depth - 1), nl_lst)
        __ ni_list:
            self.su. += su.(map(lambda x: x.getInteger() * inv_depth, ni_list))


class SolutionError(object
    ___ __init__(self
        self.su. = 0

    ___ depthSumInverse(self, nestedList
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.dfs(nestedList)
        r_ self.su.

    ___ dfs(self, nl
        """
        This dfs use height: the number of edges from to the leaves.
        But the question is supposedly use height but the calculate sum top down; here is bottom up wrongly.
        """
        height = 1

        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        __ nl_lst:
            height = 1 + max(
                map(lambda x: self.dfs(x.getList()), nl_lst)
            )
        __ ni_list:
            self.su. += su.(map(lambda x: x.getInteger() * height, ni_list))

        r_ height
