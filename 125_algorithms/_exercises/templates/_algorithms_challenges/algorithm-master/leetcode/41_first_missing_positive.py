"""
REF: http://www.cnblogs.com/yuzhangcmu/p/4200096.html
"""


c_ Solution:
    ___ firstMissingPositive  A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, l..(A) - 1

        w.... left <= right:
            """
            for `A[left]`, the index it should be at is `A[left] - 1`
            1. if it is already at `i` => pass
            2. if it out of range or duplicated => let `A[right]` in
            3. if it is legal => swap to let `A[left]` go to `i`
            """
            i = A[left] - 1
            __ i __ left:
                left += 1
            ____ i < 0 o. i > right o. A[i] __ A[left]:
                A[left], A[right] = A[right], A[left]
                # `A[left] = A[right]` is also ok, since no need to visit `A[right]` again
                right -= 1
            ____:
                A[left], A[i] = A[i], A[left]

        r.. left + 1
