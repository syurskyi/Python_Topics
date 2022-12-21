#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


c.. PeekingIterator o..
    ___ __init__  iterator
        self.iter = iterator
        self.temp = self.iter.next() __ self.iter.hasNext() else None

    ___ peek(self
        r_ self.temp

    ___ next(self
        ret = self.temp
        self.temp = self.iter.next() __ self.iter.hasNext() else None
        r_ ret

    ___ hasNext(self
        r_ self.temp is n.. None
        # return not self.temp


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
