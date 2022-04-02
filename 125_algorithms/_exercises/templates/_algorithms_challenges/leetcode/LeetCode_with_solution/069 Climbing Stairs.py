"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
__author__ = 'Danyang'
c_ Solution:
    ___ climbStairs_save_memory  n
        """
        DP. The transition function should be:
        f(n) = f(n-1) + f(n-2)  n>2;
        or = 1   n=1
        or  = 2   n=2
        :param n: an integer, number of stairs
        :return: an integer, number of different combinations
        """
        f_n_minus_2 = 1  # f(1)
        f_n_minus_1 = 2  # f(2)
        __ n__1: r.. f_n_minus_2
        __ n__2: r.. f_n_minus_1
        fn = 0
        ___ i __ r..(2, n
            fn = f_n_minus_1 +f_n_minus_2
            # for next iteration, n = n+1
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = fn
        r.. fn

    ___ climbStairs  n
        """
        DP. The transition function should be:
        f(n) = f(n-1) + f(n-2)  n>2;
        or = 1   n=1
        or  = 2   n=2
        :param n: an integer, number of stairs
        :return: an integer, number of different combinations
        """
        __ n__1: r.. 1
        __ n__2: r.. 2
        f = [0 ___ _ __ x..(n+1)]
        f[0] = 0
        f[1] = 1
        f[2] = 2
        ___ i __ x..(3, n+1
            f[i] = f[i-1]+f[i-2]
        r.. f[n]


__ _____ __ ____
    print Solution().climbStairs(3)