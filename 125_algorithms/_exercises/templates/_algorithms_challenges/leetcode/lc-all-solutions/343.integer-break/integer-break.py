class Solution(object
  ___ integerBreak(self, n
    """
    :type n: int
    :rtype: int
    """
    __ n <= 3:
      r_ n - 1
    __ n % 3 __ 0:
      r_ 3 ** (n / 3)
    __ n % 3 __ 1:
      r_ 3 ** ((n / 3) - 1) * 4
    __ n % 3 __ 2:
      r_ 3 ** (n / 3) * 2
