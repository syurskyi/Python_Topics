"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one
LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
_______ b__

__author__ 'Daniel'


c_ Solution(o..
    ___ lengthOfLIS  A
        """
        MIN: min of index last value of LIS of a particular length
        :type A: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0

        n l..(A)
        MIN [-1 ___ _ __ x..(n+1)]
        k 1
        MIN[k] A[0]  # store value rather than index
        ___ v __ A 1|
            idx b__.bisect_left(MIN, v, 1, k+1)
            MIN[idx] v
            k += 1 __ idx __ k+1 ____ 0

        r.. k

    ___ bin_search  M, A, t, lo=0, hi_ N..
        __ n.. hi: hi l..(M)
        w.... lo < hi:
            m (lo+hi)/2
            __ A[M[m]] __ t:
                r.. m
            ____ A[M[m]] < t:
                lo m + 1
            ____
                hi m

        r.. lo

    ___ lengthOfLIS_output_all  A
        """
        Maintain the result of LIS
        MIN: min of index last value of LIS of a particular length
        RET: result table, store the predecessor's idx (optional)
        :type A: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0

        n l..(A)
        MIN [-1 ___ _ __ x..(n+1)]
        RET [-1 ___ _ __ x..(n)]
        l 1
        MIN[l] 0
        ___ i __ x..(1, n
            __ A[i] > A[MIN[l]]:
                l += 1
                MIN[l] i

                RET[i] MIN[l-1]  # (optional)
            ____
                j bin_search(MIN, A, A[i], 1, l+1)
                MIN[j] i

                RET[i] MIN[j-1] __ j-1 >_ 1 ____ -1  # (optional)

        # build the LIS (optional)
        cur MIN[l]
        ret    # list
        w... T...
            ret.a..(A[cur])
            __ RET[cur] __ -1: _____
            cur RET[cur]

        ret ret[::-1]
        print ret

        r.. l

    ___ lengthOfLIS_dp  A
        """
        dp

        let F[i] be the LIS length ends at A[i]
        F[i] = max(F[j]+1 for all j < i if A[i] > A[j])

        avoid max() arg is an empty sequence

        O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0

        n l..(A)
        F [1 ___ _ __ x..(n)]
        maxa 1
        ___ i __ x..(1, n
            F[i] m..(
                F[j] + 1 __ A[i] > A[j] ____ 1
                ___ j __ x..(i)
            )
            maxa m..(maxa, F[i])

        r.. maxa


__ _______ __ _______
    ... Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) __ 4