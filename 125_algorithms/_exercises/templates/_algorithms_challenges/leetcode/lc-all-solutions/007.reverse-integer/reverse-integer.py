class Solution(object):
  ___ reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = x < 0 and -1 o. 1
    x = abs(x)
    ans = 0
    while x:
      ans = ans * 10 + x % 10
      x /= 10
    r.. sign * ans __ ans <= 0x7fffffff ____ 0
