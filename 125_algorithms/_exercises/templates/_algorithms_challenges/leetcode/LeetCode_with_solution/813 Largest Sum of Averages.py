#!/usr/bin/python3
"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then
our score is the sum of the average of each group. What is the largest score we
can achieve?

Note that our partition must use every number in A, and that scores are not
necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is
9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""
____ t___ _______ List


c_ Solution:
    ___ largestSumOfAverages  A: List[i..], K: i..) __ f__:
        """
        Memoized Backtracking + Prefix sum
        My first hunch is correct
        Complexity O(N^2 * K), mark sum and different way of forming groups
        (inserting dividers)

        calculating each F[l, k] will need O(N) time, thus total O(n^2 k)
        """
        n = l..(A)
        prefix_sum = [0 ___ _ __ r..(n+1)]
        ___ i __ r..(1, n+1
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        F    # dict
        dfs(A, n, prefix_sum, F, K)
        r.. F[n, K]

    ___ dfs  A, l, prefix_sum, F, k
        """
        dfs search divide
        make A[:l] k groups
        """
        __ l < k:
            r.. -f__('inf')

        __ (l, k) n.. __ F:
            __ k __ 1:
                ret = prefix_sum[l] / l
            ____:
                n = l..(A)
                ret = -f__('inf')
                ___ j __ r..(l-1, -1, -1
                    trail = (prefix_sum[l] - prefix_sum[j]) / (l - j)
                    ret = m..(
                        ret,
                        dfs(A, j, prefix_sum, F, k-1) + trail
                    )

            F[l, k] = ret

        r.. F[l, k]

    ___ dfs_error  A, i, prefix_sum, F, k
        """
        inconvenient

        dfs search divide
        make A[:i] 1 group
        make A[i:] k - 1 group
        """
        __ (i, k) n.. __ F:
            ret = 0
            avg = prefix_sum[i] / i
            ret += avg
            ret += m..(
                # error
                dfs(A, j, prefix_sum, F, k - 1)
                ___ j __ r..(i, l..(A))
            )
            F[i, k] = ret

        r.. F[i, k]


__ _______ __ _______
    ... Solution().largestSumOfAverages([9,1,2,3,9], 3) __ 20
