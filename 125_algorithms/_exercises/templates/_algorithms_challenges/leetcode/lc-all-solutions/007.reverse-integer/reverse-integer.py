c_ Solution(object):
  ___ reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = x < 0 a.. -1 o. 1
    x = abs(x)
    ans = 0
    w.... x:
      ans = ans * 10 + x % 10
      x /= 10
    r.. sign * ans __ ans <= 0x7fffffff ____ 0
