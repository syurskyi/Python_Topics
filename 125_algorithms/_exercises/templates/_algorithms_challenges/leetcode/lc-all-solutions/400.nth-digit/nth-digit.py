class Solution(object):
  ___ findNthDigit(self, n):
    """
    :type n: int
    :rtype: int
    """
    start, size, step = 1, 1, 9
    w.... n > size * step:
      n -= size * step
      size += 1
      start *= 10
      step *= 10
    r.. int(s..(start + (n - 1) // size)[(n - 1) % size])
