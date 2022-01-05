"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ maxSubArrayLen  A, k):
        """
        Search problem
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        m = {0: -1}  # initial condition, sum -> idx
        maxa = 0
        s = 0
        ___ i __ xrange(l..(A)):
            s += A[i]
            t = s - k  # s - t = k
            __ t __ m:
                maxa = m..(maxa, i - m[t])

            __ s n.. __ m:
                m[s] = i

        r.. maxa
