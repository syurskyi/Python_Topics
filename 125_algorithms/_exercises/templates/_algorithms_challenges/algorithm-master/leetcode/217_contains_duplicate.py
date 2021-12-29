class Solution:
    ___ containsDuplicate(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            return False

        S = set()

        for a in A:
            __ a in S:
                return True
            S.add(a)

        return False
