class Solution:
    ___ containsDuplicate(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ not A:
            r_ False

        S = set()

        ___ a in A:
            __ a in S:
                r_ True
            S.add(a)

        r_ False
