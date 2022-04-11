"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ countRangeSum  nums, lower, upper
        """
        MergeSort while counting required range sum
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        __ n.. nums: r.. 0

        ___ msort(A, lo, hi
            __ hi - lo <_ 1: r.. 0

            mid (lo + hi)/2
            cnt msort(A, lo, mid) + msort(A, mid, hi)

            temp    # list
            i j r mid
            ___ l __ x..(lo, mid
                w.... i < hi a.. A[i] - A[l] <  lower: i += 1
                w.... j < hi a.. A[j] - A[l] <_ upper: j += 1
                cnt += j - i

                w.... r < hi a.. A[r] < A[l]:
                    temp.a..(A[r])
                    r += 1

                temp.a..(A[l])

            w.... r < hi:  # dangling right
                temp.a..(A[r])
                r += 1

            A[lo:hi] temp  # A[lo:hi] = sorted(A[lo:hi]  # Timsort, linear time
            r.. cnt

        n l..(nums)
        F [0 ___ _ __ x..(n+1)]
        ___ i __ x..(1, n+1
            F[i] F[i-1] + nums[i-1]

        r.. msort(F, 0, n+1)


__ _______ __ _______
    ... Solution().countRangeSum([0, 0], 0, 0) __ 3
    ... Solution().countRangeSum([-2, 5, -1], -2, 2) __ 3
