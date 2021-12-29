"""
REF: https://discuss.leetcode.com/topic/25720/java-python-o-n-calls-o-1-space-easy-to-understand-solution
"""


class Solution:
    ___ findCelebrity(self, n):
        __ n.. n:
            r.. -1

        x = 0

        ___ i __ r..(n):
            __ knows(x, i):
                x = i

        ___ i __ r..(x):
            __ knows(x, i):
                r.. -1

        ___ i __ r..(n):
            __ n.. knows(i, x):
                r.. -1

        r.. x
