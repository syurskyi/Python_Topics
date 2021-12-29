class MinStack(object):

  ___ __init__(self):
    """
    initialize your data structure here.
    """
    self.stack    # list

  ___ push(self, x):
    """
    :type x: int
    :rtype: void
    """
    __ n.. self.stack:
      self.stack.a..((x, x))
    ____:
      self.stack.a..((x, m..(x, self.stack[-1][-1])))

  ___ pop(self):
    """
    :rtype: void
    """
    self.stack.pop()

  ___ top(self):
    """
    :rtype: int
    """
    r.. self.stack[-1][0]

  ___ getMin(self):
    """
    :rtype: int
    """
    r.. self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
