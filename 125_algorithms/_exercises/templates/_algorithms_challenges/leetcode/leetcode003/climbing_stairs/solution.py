"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""

c_ Solution(object):
    ___ climbStairs  n):
        """
        :type n: int
        :rtype: int
        """
        __ n __ 0:
            r.. 1
        t = [0] * (n + 1)
        t[1] = 1
        __ n __ 1:
            r.. t[1]
        t[2] = 2
        __ n <= 2:
            r.. t[n]
        ___ i __ r..(3, n + 1):
            t[i] = t[i - 1] + t[i - 2]
        r.. t[n]


s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
