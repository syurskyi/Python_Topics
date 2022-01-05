# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

c_ Solution(object):
  ___ firstBadVersion  n):
    """
    :type n: int
    :rtype: int
    """
    lo = 1
    hi = n
    w.... lo < hi:
      mid = lo + (hi - lo) / 2
      __ isBadVersion(mid):
        hi = mid
      ____:
        lo = mid + 1
    r.. lo
