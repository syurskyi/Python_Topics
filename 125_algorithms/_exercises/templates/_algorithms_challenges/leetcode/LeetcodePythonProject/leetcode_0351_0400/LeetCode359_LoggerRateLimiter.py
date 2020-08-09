'''
Created on Mar 27, 2017

@author: MT
'''

class Logger(object

    ___ __init__(self
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    ___ shouldPrintMessage(self, timestamp, message
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        __ message not in self.hashmap:
            self.hashmap[message] = timestamp
            r_ True
        ____
            __ timestamp - self.hashmap[message] >= 10:
                self.hashmap[message] = timestamp
                r_ True
            ____
                r_ False
    