# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# ___ isBadVersion(version


class Solution:
    ___ firstBadVersion(self, n
        left = 1
        right = n

        w___(left < right
            mid = left+(right-left)//2
            __ not isBadVersion(mid
                left = mid+1
            ____
                right = mid
        r_ left
