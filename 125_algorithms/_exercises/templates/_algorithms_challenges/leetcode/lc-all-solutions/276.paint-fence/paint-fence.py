class Solution(object
  ___ numWays(self, n, k
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    __ n > 2 and k __ 1:
      r_ 0
    __ n < 2:
      r_ n * k
    pre = k * k
    ppre = k
    for i in range(2, n
      tmp = pre
      pre = (k - 1) * (pre + ppre)
      ppre = tmp
    r_ pre
