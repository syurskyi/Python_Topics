c_ Solution o..
    # def sortArrayByParity(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: List[int]
    #     """
    #     # Bad idea, O(nlogn)
    #     A.sort(key=lambda x: x % 2)
    #     return A

    # def sortArrayByParity(self, A):
    #     return ([x for x in A if x % 2 == 0] +
    #             [x for x in A if x % 2 == 1])

    ___ sortArrayByParity  A
        # Quit like quick sort or quick selection
        lo, hi = 0, l.. A) - 1
        w.. lo < hi:
            __ A[lo] % 2 > A[hi] % 2:
                A[lo], A[hi] = A[hi], A[lo]
            __ A[lo] % 2 __ 0: lo += 1
            __ A[hi] % 2 __ 1: hi -= 1
        r_ A
