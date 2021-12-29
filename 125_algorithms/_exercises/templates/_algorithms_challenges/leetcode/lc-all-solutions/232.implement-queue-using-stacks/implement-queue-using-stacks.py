____ collections _______ deque


class Queue(object):
  ___ __init__(self):
    """
    initialize your data structure here.
    """
    self.stack1 = deque([])
    self.stack2 = deque([])

  ___ push(self, x):
    """
    :type x: int
    :rtype: nothing
    """
    self.stack1.a..(x)

  ___ pop(self):
    """
    :rtype: nothing
    """
    self.peek()
    self.stack2.pop()

  ___ peek(self):
    """
    :rtype: int
    """
    __ n.. self.stack2:
      while self.stack1:
        self.stack2.a..(self.stack1.pop())
      r.. self.stack2[-1]
    ____:
      r.. self.stack2[-1]

  ___ empty(self):
    """
    :rtype: bool
    """
    r.. n.. self.stack1 and n.. self.stack2
