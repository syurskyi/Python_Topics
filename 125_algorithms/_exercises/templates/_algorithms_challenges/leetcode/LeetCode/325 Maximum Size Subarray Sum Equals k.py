"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ maxSubArrayLen(self, A, k
        """
        Search problem
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        m = {0: -1}  # initial condition, sum -> idx
        maxa = 0
        s = 0
        for i in xrange(le.(A)):
            s += A[i]
            t = s - k  # s - t = k
            __ t in m:
                maxa = max(maxa, i - m[t])

            __ s not in m:
                m[s] = i

        r_ maxa
