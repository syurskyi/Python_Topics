"""
Premium Question
"""
____ c.. _______ d..

__author__ = 'Daniel'


c_ MovingAverage(object):
    ___ - , size):
        """
        Initialize your data structure here.
        :type size: int
        """
        size = size
        q = d..()
        s.. = 0

    ___ next(self, val):
        """
        :type val: int
        :rtype: float
        """
        q.a..(val)
        s.. += val
        __ l..(q) > size:
            s.. -= q.popleft()

        r.. float(s..) / l..(q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)