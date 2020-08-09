class Solution(object
  ___ climbStairs(self, n
    """
    :type n: int
    :rtype: int
    """
    __ n <= 1:
      r_ 1
    pre, ppre = 1, 1
    ___ i in range(2, n + 1
      tmp = pre
      pre = ppre + pre
      ppre = tmp
    r_ pre
