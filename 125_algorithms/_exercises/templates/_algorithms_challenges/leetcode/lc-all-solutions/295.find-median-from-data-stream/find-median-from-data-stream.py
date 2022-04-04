_______ heapq


c_ MedianFinder:
  ___ -
    """
    Initialize your data structure here.
    """
    left    # list
    right    # list
    median = N..

  ___ addNum  num
    """
    Adds a num into the data structure.
    :type num: int
    :rtype: void
    """
    left = left
    right = right
    __ median __ N..
      median = num
      r..

    __ num <= median:
      heapq.heappush(left, -num)
    ____
      heapq.heappush(right, num)

    __ l..(left) > l..(right) + 1:
      top = -heapq.heappop(left)
      heapq.heappush(right, median)
      median = top
    __ l..(right) > l..(left) + 1:
      top = heapq.heappop(right)
      heapq.heappush(left, -median)
      median = top

  ___ findMedian
    """
    Returns the median of current data stream
    :rtype: float
    """
    left, right = left, right
    __ l..(left) __ l..(right
      r.. median
    ____ l..(left) > l..(right
      r.. (median - left[0]) / 2.0
    __ l..(right) > l..(left
      r.. (median + right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
