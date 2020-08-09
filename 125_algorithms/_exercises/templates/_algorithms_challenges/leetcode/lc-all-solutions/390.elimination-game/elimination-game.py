class Solution(object
  ___ lastRemaining(self, n
    """
    :type n: int
    :rtype: int
    """
    count = n
    head = 1
    isFromLeft = True
    step = 1
    w___ count > 1:
      __ isFromLeft or count % 2 __ 1:
        head = head + step
      count /= 2
      step *= 2
      isFromLeft = not isFromLeft
    r_ head
