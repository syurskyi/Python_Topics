"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying
DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
__author__ = 'Daniel'


class Solution:
    ___ findRepeatedDnaSequences(self, s):
        """
        Limited space of possible values --> rewrite hash function

        Rolling hash

        "A": 0 (00)
        "C": 1 (01)
        "G": 2 (10)
        "T": 3 (11)

        :type s: str
        :rtype: list[str]
        """
        __ l..(s) < 10:
            r.. []

        s = map(self.mapping, l..(s))
        h = set()
        # in_ret = set()
        ret = set()
        cur = 0
        ___ i __ xrange(10):
            cur <<= 2
            cur &= 0xFFFFF
            cur += s[i]
        h.add(cur)

        ___ i __ xrange(10, l..(s)):
            cur <<= 2
            cur &= 0xFFFFF  # 10 * 2 = 20 position
            cur += s[i]
            __ cur __ h a.. cur n.. __ ret:
                ret.add(cur)
            ____:
                h.add(cur)

        r.. map(self.decode, ret)

    ___ decode(self, s):
        dic = {
            0: "A",
            1: "C",
            2: "G",
            3: "T"
        }
        ret    # list
        ___ i __ xrange(10):
            ret.a..(dic[s%4])
            s >>= 2

        r.. "".join(reversed(ret))

    ___ mapping(self, a):
        dic = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3,
            }

        r.. dic[a]

__ __name__ __ "__main__":
    ... Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") __ ['CCCCCAAAAA', 'AAAAACCCCC']
