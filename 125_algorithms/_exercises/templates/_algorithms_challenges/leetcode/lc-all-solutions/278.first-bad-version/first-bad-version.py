# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
  ___ firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    lo = 1
    hi = n
    while lo < hi:
      mid = lo + (hi - lo) / 2
      __ isBadVersion(mid):
        hi = mid
      ____:
        lo = mid + 1
    r.. lo
