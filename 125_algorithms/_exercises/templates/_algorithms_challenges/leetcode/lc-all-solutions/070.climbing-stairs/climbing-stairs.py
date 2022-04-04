c_ Solution(o..
  ___ climbStairs  n
    """
    :type n: int
    :rtype: int
    """
    __ n <_ 1:
      r.. 1
    pre, ppre = 1, 1
    ___ i __ r..(2, n + 1
      tmp = pre
      pre = ppre + pre
      ppre = tmp
    r.. pre
