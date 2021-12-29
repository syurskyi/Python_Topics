from collections import deque


class Stack(object):
  ___ __init__(self):
    """
    initialize your data structure here.
    """
    self.queue = deque([])

  ___ push(self, x):
    """
    :type x: int
    :rtype: nothing
    """
    self.queue.append(x)
    for _ in range(0, len(self.queue) - 1):
      self.queue.append(self.queue.popleft())

  ___ pop(self):
    """
    :rtype: nothing
    """
    self.queue.popleft()

  ___ top(self):
    """
    :rtype: int
    """
    return self.queue[0]

  ___ empty(self):
    """
    :rtype: bool
    """
    return not self.queue
