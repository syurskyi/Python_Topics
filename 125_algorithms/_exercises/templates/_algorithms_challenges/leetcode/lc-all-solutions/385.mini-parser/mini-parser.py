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
  ___ deserialize(self, s
    """
    :type s: str
    :rtype: NestedInteger
    """

    ___ parse(s, i
      __ s[i] __ "[":
        i += 1
        ret = NestedInteger()
        w___ i < le.(s
          __ s[i] __ "]":
            r_ ret, i + 1
          ____ s[i] in "[-0123456789":
            res, i = parse(s, i)
            ret.add(res)
          ____
            i += 1
      ____
        j = i
        w___ j < le.(s) and s[j] in "-0123456789":
          j += 1
        r_ NestedInteger(int(s[i:j])), j

    res, _ = parse(s, 0)
    r_ res
