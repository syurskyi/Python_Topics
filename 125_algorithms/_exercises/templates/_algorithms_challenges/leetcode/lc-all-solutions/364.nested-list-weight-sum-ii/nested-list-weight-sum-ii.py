# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object
#    ___ __init__(self, value=None
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    ___ isInteger(self
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    ___ add(self, elem
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    ___ setInteger(self, value
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    ___ getInteger(self
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    ___ getList(self
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object
  ___ depthSumInverse(self, nestedList
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """

    ___ getDepth(root
      res = 0
      ___ nested in root:
        __ not nested.isInteger(
          res = max(res, getDepth(nested.getList()))
      r_ res + 1

    ___ helper(root, depth, maxDepth
      res = 0
      ___ nested in root:
        __ nested.isInteger(
          res += (maxDepth - depth) * nested.getInteger()
        ____
          res += helper(nested.getList(), depth + 1, maxDepth)
      r_ res

    r_ helper(nestedList, 0, getDepth(nestedList))
