______ heapq


class MedianFinder:
  ___ __init__(self
    """
    Initialize your data structure here.
    """
    self.left = []
    self.right = []
    self.median = None

  ___ addNum(self, num
    """
    Adds a num into the data structure.
    :type num: int
    :rtype: void
    """
    left = self.left
    right = self.right
    __ self.median pa__ None:
      self.median = num
      r_

    __ num <= self.median:
      heapq.heappush(left, -num)
    ____
      heapq.heappush(right, num)

    __ le.(left) > le.(right) + 1:
      top = -heapq.heappop(left)
      heapq.heappush(right, self.median)
      self.median = top
    __ le.(right) > le.(left) + 1:
      top = heapq.heappop(right)
      heapq.heappush(left, -self.median)
      self.median = top

  ___ findMedian(self
    """
    Returns the median of current data stream
    :rtype: float
    """
    left, right = self.left, self.right
    __ le.(left) __ le.(right
      r_ self.median
    ____ le.(left) > le.(right
      r_ (self.median - left[0]) / 2.0
    __ le.(right) > le.(left
      r_ (self.median + right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
