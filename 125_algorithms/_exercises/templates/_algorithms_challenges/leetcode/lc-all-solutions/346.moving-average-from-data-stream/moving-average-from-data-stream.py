____ collections _______ deque


class MovingAverage(object):

  ___ __init__(self, size):
    """
    Initialize your data structure here.
    :type size: int
    """
    self.windowSize = size
    self.windowSum = 0.0
    self.data = deque([])

  ___ next(self, val):
    """
    :type val: int
    :rtype: float
    """
    self.windowSum += val
    data = self.data

    leftTop = 0
    __ l..(data) >= self.windowSize:
      leftTop = data.popleft()
    data.a..(val)

    self.windowSum -= leftTop
    __ l..(data) < self.windowSize:
      r.. self.windowSum / l..(data)
    r.. self.windowSum / self.windowSize

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
