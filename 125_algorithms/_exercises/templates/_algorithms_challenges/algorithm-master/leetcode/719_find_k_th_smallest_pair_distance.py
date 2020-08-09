class Solution:
    ___ smallestDistancePair(self, A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        __ not A or not k:
            r_ -1

        A.sort()

        left, right = 0, A[-1] - A[0]
        w___ left + 1 < right:
            mid = (left + right) // 2
            __ self.check_valid(A, mid, k
                right = mid
            ____
                left = mid

        r_ left __ self.check_valid(A, left, k) else right

    ___ check_valid(self, A, mid, k
        """
        valid if there are at least `k` pairs when distance is `mid`
        """
        cnt = left = 0

        ___ right in range(le.(A)):
            w___ A[right] - A[left] > mid:
                left += 1

            cnt += right - left

            __ cnt >= k:
                r_ True

        r_ False
