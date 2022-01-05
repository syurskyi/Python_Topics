"""
Premium question
"""
__author__ = 'Daniel'


c_ Logger(o..):
    ___ - ):
        """
        Initialize your data structure here.
        """
        h    # dict


    ___ shouldPrintMessage  timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        __ message n.. __ h o. timestamp - h[message] >= 10:
            h[message] = timestamp
            r.. T..

        r.. F..


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)