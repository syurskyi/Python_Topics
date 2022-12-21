c_ Solution o..
    # def peakIndexInMountainArray(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     i = 0
    #     while A[i + 1] >= A[i]:
    #         i += 1
    #     return i

    ___ peakIndexInMountainArray  A
        lo, hi = 0, l.. A) - 1
        w.. lo < hi:
            mid = (lo + hi) / 2
            __ A[mid] < A[mid + 1]:
                lo = mid + 1
            ____
                hi = mid
        r_ lo
