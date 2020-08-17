"""
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
"""
__author__ = 'Daniel'


class PhoneDirectory(object
    ___ __init__(self, maxNumbers
        """
        Pool of numbers
        Two parts:
        1. set
        2. range pointers to save memory
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.released = set()
        self.l = maxNumbers
        self.i = 0

    ___ get(self
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        __ self.released:
            r_ self.released.p..
        __ self.i < self.l:
            ret = self.i
            self.i += 1
            r_ ret

        r_ -1

    ___ check(self, number
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        r_ number in self.released or self.i <= number < self.l

    ___ release(self, number
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        __ self.i <= number < self.l:
            r_

        self.released.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)