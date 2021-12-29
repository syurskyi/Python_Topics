____ collections _______ deque


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
    self.queue.a..(x)
    ___ _ __ r..(0, l..(self.queue) - 1):
      self.queue.a..(self.queue.popleft())

  ___ pop(self):
    """
    :rtype: nothing
    """
    self.queue.popleft()

  ___ top(self):
    """
    :rtype: int
    """
    r.. self.queue[0]

  ___ empty(self):
    """
    :rtype: bool
    """
    r.. n.. self.queue
