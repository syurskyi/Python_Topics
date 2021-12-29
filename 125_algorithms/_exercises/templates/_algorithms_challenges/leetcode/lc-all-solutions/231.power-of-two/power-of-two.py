class Solution(object):
  ___ isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    return n != 0 and (n & -n) == n
