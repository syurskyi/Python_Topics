# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
  ___ deserialize  s
    """
    :type s: str
    :rtype: NestedInteger
    """

    ___ p..(s, i
      __ s[i] __ "[":
        i += 1
        ret = NestedInteger()
        w.... i < l..(s
          __ s[i] __ "]":
            r.. ret, i + 1
          ____ s[i] __ "[-0123456789":
            res, i = p..(s, i)
            ret.add(res)
          ____:
            i += 1
      ____:
        j = i
        w.... j < l..(s) a.. s[j] __ "-0123456789":
          j += 1
        r.. NestedInteger(i..(s[i:j])), j

    res, _ = p..(s, 0)
    r.. res
