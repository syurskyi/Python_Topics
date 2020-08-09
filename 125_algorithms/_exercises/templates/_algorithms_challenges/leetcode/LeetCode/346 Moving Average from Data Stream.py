"""
Premium Question
"""
from collections ______ deque

__author__ = 'Daniel'


class MovingAverage(object
    ___ __init__(self, size
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = deque()
        self.su. = 0

    ___ next(self, val
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.su. += val
        __ le.(self.q) > self.size:
            self.su. -= self.q.popleft()

        r_ float(self.su.) / le.(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)