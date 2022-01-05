c_ Solution(o..):
  ___ isUgly  n):
    """
    :type num: int
    :rtype: bool
    """
    __ n <= 0:
      r.. F..
    w.... n % 2 __ 0 o. n % 3 __ 0 o. n % 5 __ 0:
      __ n % 2 __ 0:
        n /= 2
      __ n % 3 __ 0:
        n /= 3
      __ n % 5 __ 0:
        n /= 5
    __ n __ 1:
      r.. T..
    r.. F..
