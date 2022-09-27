# class Logger(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.timestamps = {}

#     def shouldPrintMessage(self, timestamp, message):
#         """
#         Returns true if the message should be printed in the given timestamp, otherwise returns false.
#         If this method returns false, the message will not be printed.
#         The timestamp is in seconds granularity.
#         :type timestamp: int
#         :type message: str
#         :rtype: bool
#         """
#         if timestamp < self.timestamps.get(message, 0):
#             return False
#         self.timestamps[message] = timestamp + 10
#         return True


import heapq


c_ Logger o..

    ___ - ____:
        """
        Initialize your data structure here.
        """
        heap =    # list
        cache  # dict

    ___ shouldPrintMessage  timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        w.. l.. heap):
            __ heap[0][0] <= timestamp:
                temp = heapq.heappop(heap)
                cache.pop(temp[1])
            ____
                break
        __ timestamp < cache.get(message, 0):
            r_ F..
        cache[message] = timestamp + 10
        heapq.heappush(heap, (timestamp + 10, message))
        r_ T..


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
