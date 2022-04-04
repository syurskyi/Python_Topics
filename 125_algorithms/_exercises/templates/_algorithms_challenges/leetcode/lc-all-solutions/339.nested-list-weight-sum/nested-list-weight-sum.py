# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

c_ Solution(o..
  ___ depthSum  nestedList
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """

    ___ helper(root, depth
      res = 0
      ___ nested __ root:
        __ nested.isInteger
          res += depth * nested.getInteger()
        ____
          res += helper(nested.getList(), depth + 1)
      r.. res

    r.. helper(nestedList, 1)
