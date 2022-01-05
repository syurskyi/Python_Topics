c_ Solution(o..):
  ___ newInteger  n):
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    k = 1
    w.... n > 0:
      ans += (n % 9) * k
      k *= 10
      n /= 9
    r.. ans
