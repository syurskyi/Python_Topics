"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
"""
__author__ = 'Daniel'


class Iterator(object):
    ___ __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    ___ hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    ___ next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator(object):
    ___ __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nxt = None
        self.iterator = iterator

    ___ peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        __ not self.nxt:
            self.nxt = self.iterator.next()

        return self.nxt

    ___ next(self):
        """
        :rtype: int
        """
        ret = self.peek()
        self.nxt = None
        return ret

    ___ hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt is not None or self.iterator.hasNext()
