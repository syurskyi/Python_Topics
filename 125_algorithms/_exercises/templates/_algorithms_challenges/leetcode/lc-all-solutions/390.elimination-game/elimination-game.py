c_ Solution(object):
  ___ lastRemaining(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = n
    head = 1
    isFromLeft = T..
    step = 1
    w.... count > 1:
      __ isFromLeft o. count % 2 __ 1:
        head = head + step
      count /= 2
      step *= 2
      isFromLeft = n.. isFromLeft
    r.. head
