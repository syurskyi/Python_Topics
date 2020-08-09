"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
__author__ = 'Danyang'
class Solution:
    ___ climbStairs_save_memory(self, n
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
        __ n__1: r_ f_n_minus_2
        __ n__2: r_ f_n_minus_1
        fn = 0
        for i in range(2, n
            fn = f_n_minus_1 +f_n_minus_2
            # for next iteration, n = n+1
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = fn
        r_ fn

    ___ climbStairs(self, n
        """
        DP. The transition function should be:
        f(n) = f(n-1) + f(n-2)  n>2;
        or = 1   n=1
        or  = 2   n=2
        :param n: an integer, number of stairs
        :return: an integer, number of different combinations
        """
        __ n__1: r_ 1
        __ n__2: r_ 2
        f = [0 for _ in xrange(n+1)]
        f[0] = 0
        f[1] = 1
        f[2] = 2
        for i in xrange(3, n+1
            f[i] = f[i-1]+f[i-2]
        r_ f[n]


__ __name____"__main__":
    print Solution().climbStairs(3)