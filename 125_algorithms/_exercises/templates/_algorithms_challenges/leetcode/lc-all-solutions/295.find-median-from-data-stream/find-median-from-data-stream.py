_______ heapq


class MedianFinder:
  ___ __init__(self):
    """
    Initialize your data structure here.
    """
    self.left    # list
    self.right    # list
    self.median = N..

  ___ addNum(self, num):
    """
    Adds a num into the data structure.
    :type num: int
    :rtype: void
    """
    left = self.left
    right = self.right
    __ self.median __ N..
      self.median = num
      r..

    __ num <= self.median:
      heapq.heappush(left, -num)
    ____:
      heapq.heappush(right, num)

    __ l..(left) > l..(right) + 1:
      top = -heapq.heappop(left)
      heapq.heappush(right, self.median)
      self.median = top
    __ l..(right) > l..(left) + 1:
      top = heapq.heappop(right)
      heapq.heappush(left, -self.median)
      self.median = top

  ___ findMedian(self):
    """
    Returns the median of current data stream
    :rtype: float
    """
    left, right = self.left, self.right
    __ l..(left) __ l..(right):
      r.. self.median
    ____ l..(left) > l..(right):
      r.. (self.median - left[0]) / 2.0
    __ l..(right) > l..(left):
      r.. (self.median + right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
