# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# ___ isBadVersion(version


c_ Solution:
    ___ firstBadVersion(, n
        left _ 1
        right _ n

        w___(left < right
            mid _ left+(right-left)//2
            __ not isBadVersion(mid
                left _ mid+1
            ____
                right _ mid
        r_ left
