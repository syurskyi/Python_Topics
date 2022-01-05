"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
"""
__author__ = 'Daniel'


c_ Iterator(o..):
    ___ - , nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    ___ hasNext
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    ___ next
        """
        Returns the next element in the iteration.
        :rtype: int
        """


c_ PeekingIterator(o..):
    ___ - , iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        nxt = N..
        iterator = iterator

    ___ peek
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        __ n.. nxt:
            nxt = iterator.next()

        r.. nxt

    ___ next
        """
        :rtype: int
        """
        ret = peek()
        nxt = N..
        r.. ret

    ___ hasNext
        """
        :rtype: bool
        """
        r.. nxt __ n.. N.. o. iterator.hasNext()
