class Solution:
    ___ increasingTriplet(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            return False

        a = b = float('inf')

        for x in A:
            __ x <= a:
                a = x
            elif x <= b:
                b = x
            else:
                return True

        return False
