"""
REF: https://discuss.leetcode.com/topic/25720/java-python-o-n-calls-o-1-space-easy-to-understand-solution
"""


class Solution:
    ___ findCelebrity(self, n):
        __ not n:
            return -1

        x = 0

        for i in range(n):
            __ knows(x, i):
                x = i

        for i in range(x):
            __ knows(x, i):
                return -1

        for i in range(n):
            __ not knows(i, x):
                return -1

        return x
