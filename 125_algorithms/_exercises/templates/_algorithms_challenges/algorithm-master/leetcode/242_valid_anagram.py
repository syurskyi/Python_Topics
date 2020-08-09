class Solution:
    ___ isAnagram(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s __ t:
            r_ True
        __ not s or not t or le.(s) != le.(t
            r_ False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:
            __ c not in freq:
                r_ False

            freq[c] -= 1

        r_ all(v __ 0 for v in freq.values())
