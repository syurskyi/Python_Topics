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
        self.sum = 0

    ___ next(self, val
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.sum += val
        __ le.(self.q) > self.size:
            self.sum -= self.q.popleft()

        r_ float(self.sum) / le.(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)