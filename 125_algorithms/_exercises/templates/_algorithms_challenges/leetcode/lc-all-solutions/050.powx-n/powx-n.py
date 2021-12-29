class Solution(object):
  ___ myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    __ n < 0:
      n = -n
      x = 1 / x
    ans = 1
    while n:
      __ n & 1:
        ans *= x
      x *= x
      n >>= 1
    return ans
