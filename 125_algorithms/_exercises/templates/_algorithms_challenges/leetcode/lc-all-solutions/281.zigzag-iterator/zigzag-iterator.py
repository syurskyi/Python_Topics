from collections ______ deque


class ZigzagIterator(object

  ___ __init__(self, v1, v2
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    self.iters = deque(map(iter, [v1, v2]))
    self.total = su.(map(le., [v1, v2]))

  ___ next(self
    """
    :rtype: int
    """
    top = self.iters.popleft()
    try:
      value = top.next()
    except StopIteration:
      r_ self.next()
    self.total -= 1
    __ self.total != 0:
      self.iters.append(top)
    r_ value

  ___ hasNext(self
    """
    :rtype: bool
    """
    r_ self.total > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# w___ i.hasNext( v.append(i.next())
