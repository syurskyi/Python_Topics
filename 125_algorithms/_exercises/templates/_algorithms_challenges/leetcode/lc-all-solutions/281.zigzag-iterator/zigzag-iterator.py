____ collections _______ deque


class ZigzagIterator(object):

  ___ __init__(self, v1, v2):
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    self.iters = deque(map(iter, [v1, v2]))
    self.total = s..(map(l.., [v1, v2]))

  ___ next(self):
    """
    :rtype: int
    """
    top = self.iters.popleft()
    try:
      value = top.next()
    except StopIteration:
      r.. self.next()
    self.total -= 1
    __ self.total != 0:
      self.iters.a..(top)
    r.. value

  ___ hasNext(self):
    """
    :rtype: bool
    """
    r.. self.total > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
