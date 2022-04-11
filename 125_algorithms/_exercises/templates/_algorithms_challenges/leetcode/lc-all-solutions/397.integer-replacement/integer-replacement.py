c_ Solution(o..
  ___ integerReplacement  n
    """
    :type n: int
    :rtype: int
    """
    ans 0
    w.... n != 1:
      __ n __ 3:
        n -_ 1
      ____ n & 1:
        __ ((n + 1) & n) <_ ((n - 1) & (n - 2:
          n += 1
        ____
          n -_ 1
      ____
        n >>= 1
      ans += 1
    r.. ans
