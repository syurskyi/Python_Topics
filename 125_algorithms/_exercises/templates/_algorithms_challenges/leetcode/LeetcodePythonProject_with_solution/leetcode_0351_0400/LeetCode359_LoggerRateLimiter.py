'''
Created on Mar 27, 2017

@author: MT
'''

c_ Logger(object):

    ___ - ):
        """
        Initialize your data structure here.
        """
        hashmap    # dict

    ___ shouldPrintMessage  timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        __ message n.. __ hashmap:
            hashmap[message] = timestamp
            r.. T..
        ____:
            __ timestamp - hashmap[message] >= 10:
                hashmap[message] = timestamp
                r.. T..
            ____:
                r.. F..
    