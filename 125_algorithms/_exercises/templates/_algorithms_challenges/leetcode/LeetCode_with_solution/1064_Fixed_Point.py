c_ Solution o..
    # def fixedPoint(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     for index, value in enumerate(A):
    #         # Because if A[i] > i, then i can never be greater than A[i] any more
    #         if index == value:
    #             return index
    #         elif index < value:
    #             return -1

    ___ fixedPoint  A
        l, h = 0, l.. A) - 1
        w.. l <= h:
            mid = (l + h) // 2
            __ A[mid] < mid:
                l = mid + 1
            ____ A[mid] > mid:
                h = mid - 1
            ____
                r_ mid
        r_ -1
