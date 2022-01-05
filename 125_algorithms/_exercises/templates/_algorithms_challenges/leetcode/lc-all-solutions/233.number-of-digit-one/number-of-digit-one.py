c_ Solution(o..):
  ___ countDigitOne  n):
    """
    :type n: int
    :rtype: int
    """
    m = 1
    ones = 0
    w.... m <= n:
      r = (n / m) % 10
      __ r > 1:
        ones += m
      ____ r __ 1:
        ones += n % m + 1

      ones += (n / (m * 10)) * m
      m *= 10
    r.. ones
