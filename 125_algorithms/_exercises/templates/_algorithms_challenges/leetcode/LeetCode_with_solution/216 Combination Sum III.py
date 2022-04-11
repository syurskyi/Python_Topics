"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
__author__ 'Daniel'


c_ Solution:
    ___ combinationSum3  k, n
        """
        Backtracking

        :type k: int
        :type n: int
        :rtype: list[list[int]]
        """
        ret    # list
        dfs(k, n, [], ret)
        r.. ret

    ___ dfs  remain_k, remain_n, cur, ret
        __ remain_k __ 0 a.. remain_n __ 0:
            ret.a..(l..(cur
            r..

        # check max and min reach
        __ remain_k * 9 < remain_n o. remain_k * 1 > remain_n:
            r..

        start 1
        __ cur:
            start cur[-1] + 1  # unique
        ___ i __ x..(start, 10
            cur.a..(i)
            dfs(remain_k - 1, remain_n - i, cur, ret)
            cur.p.. )


__ _______ __ _______
    ... Solution().combinationSum3(3, 9) __ [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
