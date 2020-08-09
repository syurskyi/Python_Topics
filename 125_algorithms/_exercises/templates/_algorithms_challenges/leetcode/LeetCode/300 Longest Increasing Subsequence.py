"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one
LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
______ bisect

__author__ = 'Daniel'


class Solution(object
    ___ lengthOfLIS(self, A
        """
        MIN: min of index last value of LIS of a particular length
        :type A: List[int]
        :rtype: int
        """
        __ not A:
            r_ 0

        n = le.(A)
        MIN = [-1 for _ in xrange(n+1)]
        k = 1
        MIN[k] = A[0]  # store value rather than index
        for v in A[1:]:
            idx = bisect.bisect_left(MIN, v, 1, k+1)
            MIN[idx] = v
            k += 1 __ idx __ k+1 else 0

        r_ k

    ___ bin_search(self, M, A, t, lo=0, hi=None
        __ not hi: hi = le.(M)
        w___ lo < hi:
            m = (lo+hi)/2
            __ A[M[m]] __ t:
                r_ m
            ____ A[M[m]] < t:
                lo = m + 1
            ____
                hi = m

        r_ lo

    ___ lengthOfLIS_output_all(self, A
        """
        Maintain the result of LIS
        MIN: min of index last value of LIS of a particular length
        RET: result table, store the predecessor's idx (optional)
        :type A: List[int]
        :rtype: int
        """
        __ not A:
            r_ 0

        n = le.(A)
        MIN = [-1 for _ in xrange(n+1)]
        RET = [-1 for _ in xrange(n)]
        l = 1
        MIN[l] = 0
        for i in xrange(1, n
            __ A[i] > A[MIN[l]]:
                l += 1
                MIN[l] = i

                RET[i] = MIN[l-1]  # (optional)
            ____
                j = self.bin_search(MIN, A, A[i], 1, l+1)
                MIN[j] = i

                RET[i] = MIN[j-1] __ j-1 >= 1 else -1  # (optional)

        # build the LIS (optional)
        cur = MIN[l]
        ret = []
        w___ True:
            ret.append(A[cur])
            __ RET[cur] __ -1: break
            cur = RET[cur]

        ret = ret[::-1]
        print ret

        r_ l

    ___ lengthOfLIS_dp(self, A
        """
        dp

        let F[i] be the LIS length ends at A[i]
        F[i] = max(F[j]+1 for all j < i if A[i] > A[j])

        avoid max() arg is an empty sequence

        O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        __ not A:
            r_ 0

        n = le.(A)
        F = [1 for _ in xrange(n)]
        maxa = 1
        for i in xrange(1, n
            F[i] = max(
                F[j] + 1 __ A[i] > A[j] else 1
                for j in xrange(i)
            )
            maxa = max(maxa, F[i])

        r_ maxa


__ __name__ __ "__main__":
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) __ 4