from collections ______ deque


class Queue(object
  ___ __init__(self
    """
    initialize your data structure here.
    """
    self.stack1 = deque([])
    self.stack2 = deque([])

  ___ push(self, x
    """
    :type x: int
    :rtype: nothing
    """
    self.stack1.append(x)

  ___ pop(self
    """
    :rtype: nothing
    """
    self.peek()
    self.stack2.pop()

  ___ peek(self
    """
    :rtype: int
    """
    __ not self.stack2:
      w___ self.stack1:
        self.stack2.append(self.stack1.pop())
      r_ self.stack2[-1]
    ____
      r_ self.stack2[-1]

  ___ empty(self
    """
    :rtype: bool
    """
    r_ not self.stack1 and not self.stack2
