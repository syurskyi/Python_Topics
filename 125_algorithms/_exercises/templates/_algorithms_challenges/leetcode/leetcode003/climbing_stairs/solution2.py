"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""

class Solution(object
    ___ climbStairs(self, n
        """
        :type n: int
        :rtype: int
        """
        t = [0 ___ i in range(n + 1)]
        r_ self.climb(n, t)

    ___ climb(self, n, t
        __ n __ 0:
            r_ 1
        ____ n < 0:
            r_ 0
        ____ t[n] != 0:
            r_ t[n]
        ____
            t[n] = self.climb(n - 1, t) + self.climb(n - 2, t)
            r_ t[n]


s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
