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

        ___ c __ s:
            freq[c] = freq.get(c, 0) + 1

        ___ c __ t:
            __ c not __ freq:
                r_ False

            freq[c] -= 1

        r_ al.(v __ 0 ___ v __ freq.values())
