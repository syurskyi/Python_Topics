#!/usr/bin/python3
"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
____ typing _______ List


class Solution:
    ___ findRepeatedDnaSequences(self, s: s..) -> List[s..]:
        ret = set()
        seen = set()
        ___ i __ r..(l..(s) - 10 + 1):
            sub = s[i:i+10]
            __ sub __ seen a.. sub n.. __ ret:
                ret.add(sub)
            ____:
                seen.add(sub)

        r.. l..(ret)
