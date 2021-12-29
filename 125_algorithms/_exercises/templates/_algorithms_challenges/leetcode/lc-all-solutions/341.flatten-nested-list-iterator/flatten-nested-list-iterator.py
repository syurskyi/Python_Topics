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
____ collections _______ deque


class NestedIterator(object):

  ___ __init__(self, nestedList):
    """
    Initialize your data structure here.
    :type nestedList: List[NestedInteger]
    """
    self.stack = deque(nestedList[::-1])
    self.value = N..

  ___ next(self):
    """
    :rtype: int
    """
    self.hasNext()
    ret = self.value
    self.value = N..
    r.. ret

  ___ hasNext(self):
    """
    :rtype: bool
    """
    __ self.value __ n.. N..
      r.. True

    stack = self.stack
    w.... stack:
      top = stack.pop()
      __ top.isInteger():
        self.value = top.getInteger()
        r.. True
      ____:
        stack.extend(top.getList()[::-1])
    r.. False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
