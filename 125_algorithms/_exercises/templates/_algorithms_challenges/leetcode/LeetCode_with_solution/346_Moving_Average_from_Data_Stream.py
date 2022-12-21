c_ MovingAverage o..

    ___ -  size
        """
        Initialize your data structure here.
        :type size: int
        """
        size = size
        curr_range =    # list
        

    ___ next  val
        """
        :type val: int
        :rtype: float
        """
        __ l.. curr_range) __ size:
            curr_range.pop(0)
        curr_range.append(val)
        r_ s..(curr_range) * 1.0 / l.. curr_range)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

    # def __init__(self, size):
    #     """
    #     Initialize your data structure here.
    #     :type size: int
    #     """
    #     self.next = lambda v, q=collections.deque((), size): q.append(v) or 1.*sum(q) / len(q)