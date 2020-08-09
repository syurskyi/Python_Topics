class Solution:
    ___ increasingTriplet(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            r_ False

        a = b = float('inf')

        ___ x in A:
            __ x <= a:
                a = x
            ____ x <= b:
                b = x
            ____
                r_ True

        r_ False
