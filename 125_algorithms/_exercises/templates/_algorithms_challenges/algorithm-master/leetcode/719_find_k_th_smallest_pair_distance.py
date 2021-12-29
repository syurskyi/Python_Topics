class Solution:
    ___ smallestDistancePair(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        __ n.. A o. n.. k:
            r.. -1

        A.sort()

        left, right = 0, A[-1] - A[0]
        while left + 1 < right:
            mid = (left + right) // 2
            __ self.check_valid(A, mid, k):
                right = mid
            ____:
                left = mid

        r.. left __ self.check_valid(A, left, k) ____ right

    ___ check_valid(self, A, mid, k):
        """
        valid if there are at least `k` pairs when distance is `mid`
        """
        cnt = left = 0

        ___ right __ r..(l..(A)):
            while A[right] - A[left] > mid:
                left += 1

            cnt += right - left

            __ cnt >= k:
                r.. True

        r.. False
