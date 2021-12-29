"""
Premium Question
"""
____ collections _______ deque

__author__ = 'Daniel'


class MovingAverage(object):
    ___ __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = deque()
        self.s.. = 0

    ___ next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.a..(val)
        self.s.. += val
        __ l..(self.q) > self.size:
            self.s.. -= self.q.popleft()

        r.. float(self.s..) / l..(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)