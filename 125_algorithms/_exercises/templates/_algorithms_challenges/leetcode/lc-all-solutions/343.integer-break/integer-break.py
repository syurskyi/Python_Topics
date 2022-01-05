c_ Solution(o..):
  ___ integerBreak  n):
    """
    :type n: int
    :rtype: int
    """
    __ n <= 3:
      r.. n - 1
    __ n % 3 __ 0:
      r.. 3 ** (n / 3)
    __ n % 3 __ 1:
      r.. 3 ** ((n / 3) - 1) * 4
    __ n % 3 __ 2:
      r.. 3 ** (n / 3) * 2
