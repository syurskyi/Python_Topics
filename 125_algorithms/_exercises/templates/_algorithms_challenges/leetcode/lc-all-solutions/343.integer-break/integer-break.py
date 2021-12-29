class Solution(object):
  ___ integerBreak(self, n):
    """
    :type n: int
    :rtype: int
    """
    __ n <= 3:
      return n - 1
    __ n % 3 == 0:
      return 3 ** (n / 3)
    __ n % 3 == 1:
      return 3 ** ((n / 3) - 1) * 4
    __ n % 3 == 2:
      return 3 ** (n / 3) * 2
