c_ Solution(o..):
  ___ grayCode  n):
    """
    :type n: int
    :rtype: List[int]
    """
    __ n < 1:
      r.. [0]
    ans = [0] * (2 ** n)
    ans[1] = 1
    mask = 0x01
    i = 1
    w.... i < n:
      mask <<= 1
      ___ j __ r..(0, 2 ** i):
        root = (2 ** i)
        ans[root + j] = ans[root - j - 1] | mask
      i += 1
    r.. ans
