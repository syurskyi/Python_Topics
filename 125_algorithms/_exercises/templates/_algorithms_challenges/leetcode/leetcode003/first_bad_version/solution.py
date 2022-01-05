"""
You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.
"""

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
        left = 1
        right = n
        w.... left + 1 < right:
            mid = left + (right - left) / 2
            __ isBadVersion(mid):
                right = mid
            ____:
                left = mid
        __ isBadVersion(left):
            r.. left
        ____ isBadVersion(right):
            r.. right
