class Solution(object):
  ___ hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    w.... n > 0:
      n -= (n & -n)
      ans += 1
    r.. ans
