"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


c_ NestedInteger(o..
    ___ - , value_ N..
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    ___ isInteger
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    ___ add  elem
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    ___ setInteger  value
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
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


c_ Solution(o..
    ___ - 
        s.. = 0

    ___ depthSumInverse  nestedList
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        inv_depth = height(nestedList)
        inverseDepthSum(nestedList, inv_depth)
        r.. s..

    ___ height  nl
        nl_lst = filter(l.... x: n.. x.isInteger(), nl)
        __ n.. nl_lst:
            r.. 1
        __ nl_lst:
            r.. 1 + m..(
                map(l.... x: height(x.getList()), nl_lst)
            )

    ___ inverseDepthSum  nl, inv_depth
        nl_lst = filter(l.... x: n.. x.isInteger(), nl)
        ni_list = filter(l.... x: x.isInteger(), nl)
        __ nl_lst:
            map(l.... x: inverseDepthSum(x.getList(), inv_depth - 1), nl_lst)
        __ ni_list:
            s.. += s.. m..(l.... x: x.getInteger() * inv_depth, ni_list))


c_ SolutionError(o..
    ___ - 
        s.. = 0

    ___ depthSumInverse  nestedList
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        dfs(nestedList)
        r.. s..

    ___ dfs  nl
        """
        This dfs use height: the number of edges from to the leaves.
        But the question is supposedly use height but the calculate sum top down; here is bottom up wrongly.
        """
        height = 1

        nl_lst = filter(l.... x: n.. x.isInteger(), nl)
        ni_list = filter(l.... x: x.isInteger(), nl)
        __ nl_lst:
            height = 1 + m..(
                map(l.... x: dfs(x.getList()), nl_lst)
            )
        __ ni_list:
            s.. += s.. m..(l.... x: x.getInteger() * height, ni_list))

        r.. height
