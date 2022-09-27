#!/usr/bin/python3
"""
Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
"""
____ t___ _______ L..


c_ Solution:
    ___ -
        cache    # dict

    ___ numsSameConsecDiff  N: i.., K: i.. __ L.. i..
        """
        dfs + memoization
        """
        ret    # list
        ___ i __ r..(1, 10
            ret.e.. dfs(i, N, K

        __ N __ 1:
            ret.a..( 0  # special case

        r.. l..(
            m.. l.... x: i..("".j.. m..(s.., x))), ret)
        )

    ___ dfs  start: i.., N: i.., K: i.. __ L..[L..[i..]]:
        __ (start, N, K) n.. __ cache:
            ret    # list
            __ N __ 1:
                ret [[start]]
            ____ N > 1:
                __ start + K <_ 9:
                    ___ e __ dfs(start + K, N - 1, K
                        ret.a..([start] + e)
                __ start - K >_ 0 a.. K !_ 0:  # special case
                    ___ e __ dfs(start - K, N - 1, K
                        ret.a..([start] + e)

            cache[start, N, K] ret

        r.. cache[start, N, K]


__ _______ __ _______
    Solution().numsSameConsecDiff(3, 7) __ [181,292,707,818,929]
