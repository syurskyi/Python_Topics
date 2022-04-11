"""
Premium Question
"""
____ c.. _______ d..

__author__ 'Daniel'


c_ HitCounter(o..
    ___ -
        """
        Initialize your data structure here.

        calls are being made to the system in chronological order.
        It is possible that several hits arrive roughly at the same time.
        What if the number of hits per second could be very large? Does your design scale?  # use counter
        """
        q d..()

    ___ hit  timestamp
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        p.. timestamp)
        q.a..(timestamp)

    ___ getHits  timestamp
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        p.. timestamp)
        r.. l..(q)

    ___ pop  timestamp
        w.... q a.. timestamp - q[0] >_ 300:
            q.popleft()


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)