class Solution:
    ___ isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s == t:
            return True
        __ not s or not t or len(s) != len(t):
            return False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:
            __ c not in freq:
                return False

            freq[c] -= 1

        return all(v == 0 for v in freq.values())
