"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""

c_ Solution(o..
    ___ climbStairs  n
        """
        :type n: int
        :rtype: int
        """
        t [0 ___ i __ r..(n + 1)]
        r.. climb(n, t)

    ___ climb  n, t
        __ n __ 0:
            r.. 1
        ____ n < 0:
            r.. 0
        ____ t[n] != 0:
            r.. t[n]
        ____
            t[n] climb(n - 1, t) + climb(n - 2, t)
            r.. t[n]


s Solution()
print(s.climbStairs(0
print(s.climbStairs(1
print(s.climbStairs(2
print(s.climbStairs(3
print(s.climbStairs(4
