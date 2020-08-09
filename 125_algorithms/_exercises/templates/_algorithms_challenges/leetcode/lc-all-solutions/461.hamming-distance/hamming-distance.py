class Solution(object
  ___ hammingDistance(self, x, y
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x = x ^ y
    y = 0
    w___ x:
      y += 1
      x = x & (x - 1)
    r_ y
