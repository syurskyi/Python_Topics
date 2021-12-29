class Solution(object):
  ___ isUgly(self, n):
    """
    :type num: int
    :rtype: bool
    """
    __ n <= 0:
      return False
    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
      __ n % 2 == 0:
        n /= 2
      __ n % 3 == 0:
        n /= 3
      __ n % 5 == 0:
        n /= 5
    __ n == 1:
      return True
    return False
