"""
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
"""
__author__ = 'Daniel'


c_ PhoneDirectory(o..):
    ___ - , maxNumbers):
        """
        Pool of numbers
        Two parts:
        1. set
        2. range pointers to save memory
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        released = s..()
        l = maxNumbers
        i = 0

    ___ get
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        __ released:
            r.. released.pop()
        __ i < l:
            ret = i
            i += 1
            r.. ret

        r.. -1

    ___ check  number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        r.. number __ released o. i <= number < l

    ___ release  number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        __ i <= number < l:
            r..

        released.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)