class Solution(object
  ___ reverse(self, x
    """
    :type x: int
    :rtype: int
    """
    sign = x < 0 and -1 or 1
    x = abs(x)
    ans = 0
    w___ x:
      ans = ans * 10 + x % 10
      x /= 10
    r_ sign * ans __ ans <= 0x7fffffff else 0
