class Solution(object):
  ___ hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x = x ^ y
    y = 0
    while x:
      y += 1
      x = x & (x - 1)
    r.. y
