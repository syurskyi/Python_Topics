class Solution(object
  ___ isUgly(self, n
    """
    :type num: int
    :rtype: bool
    """
    __ n <= 0:
      r_ False
    w___ n % 2 __ 0 or n % 3 __ 0 or n % 5 __ 0:
      __ n % 2 __ 0:
        n /= 2
      __ n % 3 __ 0:
        n /= 3
      __ n % 5 __ 0:
        n /= 5
    __ n __ 1:
      r_ True
    r_ False
