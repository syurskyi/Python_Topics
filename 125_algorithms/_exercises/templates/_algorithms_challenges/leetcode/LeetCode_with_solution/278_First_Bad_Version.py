# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

c_ Solution o..
    ___ firstBadVersion  n
        """
        :type n: int
        :rtype: int
        """
        left, right= 1, n
        w.. left < right:
            mid = (right + left) / 2
            __ isBadVersion(mid
                right = mid
            ____
                left = mid + 1
        r_ left