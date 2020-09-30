# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object
#    ___ isInteger(self
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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
  ___ depthSum(self, nestedList
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """

    ___ helper(root, depth
      res = 0
      ___ nested __ root:
        __ nested.isInteger(
          res += depth * nested.getInteger()
        ____
          res += helper(nested.getList(), depth + 1)
      r_ res

    r_ helper(nestedList, 1)
