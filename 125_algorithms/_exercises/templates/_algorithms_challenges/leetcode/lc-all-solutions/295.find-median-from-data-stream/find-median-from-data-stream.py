import heapq


class MedianFinder:
  ___ __init__(self):
    """
    Initialize your data structure here.
    """
    self.left = []
    self.right = []
    self.median = None

  ___ addNum(self, num):
    """
    Adds a num into the data structure.
    :type num: int
    :rtype: void
    """
    left = self.left
    right = self.right
    __ self.median is None:
      self.median = num
      return

    __ num <= self.median:
      heapq.heappush(left, -num)
    else:
      heapq.heappush(right, num)

    __ len(left) > len(right) + 1:
      top = -heapq.heappop(left)
      heapq.heappush(right, self.median)
      self.median = top
    __ len(right) > len(left) + 1:
      top = heapq.heappop(right)
      heapq.heappush(left, -self.median)
      self.median = top

  ___ findMedian(self):
    """
    Returns the median of current data stream
    :rtype: float
    """
    left, right = self.left, self.right
    __ len(left) == len(right):
      return self.median
    elif len(left) > len(right):
      return (self.median - left[0]) / 2.0
    __ len(right) > len(left):
      return (self.median + right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
