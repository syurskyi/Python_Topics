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

        ___ c in s:
            freq[c] = freq.get(c, 0) + 1

        ___ c in t:
            __ c not in freq:
                r_ False

            freq[c] -= 1

        r_ all(v __ 0 ___ v in freq.values())
