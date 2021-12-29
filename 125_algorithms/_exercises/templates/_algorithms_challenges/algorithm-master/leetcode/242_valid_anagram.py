class Solution:
    ___ isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s __ t:
            r.. True
        __ n.. s o. n.. t o. l..(s) != l..(t):
            r.. False

        freq = {}

        ___ c __ s:
            freq[c] = freq.get(c, 0) + 1

        ___ c __ t:
            __ c n.. __ freq:
                r.. False

            freq[c] -= 1

        r.. a..(v __ 0 ___ v __ freq.values())
