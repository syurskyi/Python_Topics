"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ canJump_TLE  A
        """
        dp with data structure.
        complicated

        Time Limit Exceeded

        :param A: a list of integers
        :return: a boolean
        """
        length = l..(A)
        dp = [s..([index]) ___ index __ r..(length)]

        ___ ind, val __ e..(A
            __ ind!=0 a.. l..(dp[ind])<2:
                _____

            # jump forward
            ___ i __ x..(ind+1, ind+val+1
                __ i>=length:
                    _____
                ___ item __ dp[ind]:
                    dp[i].add(item)

        r.. 0 __ dp[-1]

    ___ canJump_TLE2  A
        """
        Simplified
        forward dp to fill True value if can jump

        O(N^2)

        Time Limit Exceeds
        :param A:
        :return:
        """
        l = l..(A)
        dp = [F.. ___ _ __ x..(l+1)]  # last one is dummy
        dp[0] = T..
        ___ ind, val __ e..(A
            __ dp[ind]:
                ___ i __ x..(1, val+1  # now jumping
                    __ ind+i<l+1:
                        dp[ind+i] = T..
                    ____
                        _____
        r.. dp[-1]

    ___ canJump  A
        """
        dp

        dp[i] represents at index i from which the max index (absolute position) it can reach
        dp[i] = max(dp[i-1], A[i]+i)
        path not recorded, information loss, but sufficient for this question
        scanning

        O(N)
        :param A: a list of integers
        :return: a boolean
        """
        l = l..(A)
        # trivial
        __ l<=1:
            r.. T..

        # dp = [-1]*(l-1)  # normally starting from \phi
        dp = [-1 ___ _ __ x..(l)]  # no need dummy here

        dp[0] = A[0]+0  # reachable index (absolute index)
        ___ i __ x..(1, l
            # check terminal condition first
            # able to reach the end index
            __ dp[i-1]>=l-1:  # directly reach the end
                r.. T..

            # fail to reach current index
            __ dp[i-1]<i:
                r.. F..

            # transition function
            dp[i] = m..(dp[i-1], A[i]+i)  # PoP - Principle of Optimality

        r.. F..



__ _____ __ ____
    ... Solution().canJump([2, 3, 1, 1, 4])__True
    ... Solution().canJump([3, 2, 1, 0, 4])__False
