c_ Solution(o..
  ___ numWays  n, k
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    __ n > 2 a.. k __ 1:
      r.. 0
    __ n < 2:
      r.. n * k
    pre k * k
    ppre k
    ___ i __ r..(2, n
      tmp  pre
      pre (k - 1) * (pre + ppre)
      ppre tmp
    r.. pre
