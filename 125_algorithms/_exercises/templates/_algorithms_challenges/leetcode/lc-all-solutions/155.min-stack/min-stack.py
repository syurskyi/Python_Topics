c_ MinStack(o..

  ___ -
    """
    initialize your data structure here.
    """
    stack    # list

  ___ push  x
    """
    :type x: int
    :rtype: void
    """
    __ n.. stack:
      stack.a..((x, x))
    ____:
      stack.a..((x, m..(x, stack[-1][-1])))

  ___ pop
    """
    :rtype: void
    """
    stack.pop()

  ___ top
    """
    :rtype: int
    """
    r.. stack[-1][0]

  ___ getMin
    """
    :rtype: int
    """
    r.. stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
