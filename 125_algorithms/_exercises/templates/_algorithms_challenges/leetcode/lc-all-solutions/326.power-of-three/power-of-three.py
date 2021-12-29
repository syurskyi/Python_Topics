class Solution(object):
  ___ isPowerOfThree(self, n):
    """
    :type n: int
    :rtype: bool
    """
    __ n > 0:
      return (1162261467 % n) == 0
    else:
      return False
